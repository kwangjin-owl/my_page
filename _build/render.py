# PDF 만들기: python3 render.py <my_page 폴더>  (playwright, 크롬, Pretendard 글꼴이 깔려 있어야 함). index.html·print.html은 build.py로 먼저 만든다
import sys
from playwright.sync_api import sync_playwright
root=sys.argv[1]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome')
    pg=b.new_page(viewport={'width':1320,'height':900})
    pg.goto(f'file://{root}/print.html'); pg.wait_for_timeout(1200)
    over=pg.evaluate('''()=>{const r=[];document.querySelectorAll('.pg').forEach((P,i)=>{
      P.querySelectorAll('.txt,.mp,.pg,.core').forEach(el=>{ if(el.scrollHeight>el.clientHeight+1||el.scrollWidth>el.clientWidth+1) r.push([i+1,el.className,el.scrollHeight,el.clientHeight]);});
      const fam=getComputedStyle(P).fontFamily; if(i==0) r.push(['font',fam]);});
      return r;}''')
    print(over)
    pg.pdf(path=f'{root}/docs/portfolio.pdf', prefer_css_page_size=True, print_background=True)
    b.close()
