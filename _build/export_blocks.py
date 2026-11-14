# pptx(260730) 안의 원본 그림을 블록별로 따로 꺼낸다. 겹쳐 놓은 슬라이드 구성 대신 웹에서 한 장씩 보여 주려고.
# 쓰는 법: pptx를 풀어 둔 폴더(X)와 내보낼 폴더(assets/blocks)를 준다. python3 export_blocks.py <풀어 둔 pptx 폴더> <my_page/assets/blocks>
import sys, json
from lxml import etree
from PIL import Image, ImageFilter
ns={'p':'http://schemas.openxmlformats.org/presentationml/2006/main','a':'http://schemas.openxmlformats.org/drawingml/2006/main','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
X, OUT = sys.argv[1], sys.argv[2]
# 그림별 자르기·회전(pptx 설정 그대로)
info={}
for i in range(3,11):
    rels=etree.parse(f'{X}/ppt/slides/_rels/slide{i}.xml.rels'); rm={r.get('Id'):r.get('Target') for r in rels.getroot()}
    for pic in etree.parse(f'{X}/ppt/slides/slide{i}.xml').iter('{%s}pic'%ns['p']):
        f=rm[pic.find('.//a:blip',ns).get('{%s}embed'%ns['r'])].split('/')[-1]
        src=pic.find('.//a:srcRect',ns); x=pic.find('.//a:xfrm',ns)
        info[f.split('.')[0]]=(f, dict(src.attrib) if src is not None else {}, x.get('rot'))
# 가릴 곳(원본 화소 좌표): 학생 이름, KC 코드 칸
BLUR={'image19':[(222,38,258,182)],
      'image25':[(238,68,384,86),(260,92,290,183)],
      'image17':[(1212,53,1544,102)], 'image18':[(1204,51,1541,99)]}
ROWS={
 'enuma_aidt':[[11,8],[9,10]], 'todo':[[12,13]],
 'wj_aidt56':[[17,18]], 'wj_aidt34':[[14,15],[16]],
 'defense':[[19,20]], 'allbaek':[[21,22]],
 'kmap':[[23,24]], 'terraforming':[[27,28],[25,26]],
 'stem':[[29,30]], 'prime':[[32,31],[33,34]],
 'gumjeong':[[37,38],[39]], 'ai_reco':[[35,36]],
 'homerun':[[45,50,44],[48,46,47],[43,42,41]], 'ice_ops':[[40,49]],
 'sae_content':[[54,55,64],[51,52,53],[56,57,58]], 'sae_field':[[59,60,61],[62,63]],
}
MAXW=1200
meta={}
for blk,rows in ROWS.items():
    mrows=[]; n=0
    for row in rows:
        mr=[]
        for k in row:
            f,src,rot=info[f'image{k}']
            im=Image.open(f'{X}/ppt/media/{f}').convert('RGB')
            for box in BLUR.get(f'image{k}',[]):
                reg=im.crop(box).filter(ImageFilter.GaussianBlur(6)); im.paste(reg,box[:2])
            if src:
                W,H=im.size; g=lambda s:int(src.get(s,0))/100000
                im=im.crop((round(W*g('l')),round(H*g('t')),round(W*(1-g('r'))),round(H*(1-g('b')))))
            if rot=='10800000': im=im.rotate(180)
            if im.width>MAXW: im=im.resize((MAXW,round(im.height*MAXW/im.width)),Image.LANCZOS)
            n+=1; name=f'{blk}_{n}.jpg'
            im.save(f'{OUT}/{name}',quality=86,optimize=True)
            mr.append((name,im.width,im.height))
        mrows.append(mr)
    meta[blk]=mrows
json.dump(meta,open('blocks_meta.json','w'),ensure_ascii=False,indent=0)  # gallery_data.py를 만들 재료
print(sum(len(r) for v in meta.values() for r in v),'장')
