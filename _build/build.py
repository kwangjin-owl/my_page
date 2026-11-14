# index.html(웹 첫 화면)과 print.html(인쇄본)을 portfolio_data.py 하나에서 만든다.
# 쓰는 법: python3 build.py <my_page 폴더> <build 번호>
import sys, html
from portfolio_data import BASE, COMPANIES, BLOCKS, PAGES, NOW_MAIN, NOW_MP

ROOT, BUILD = sys.argv[1], sys.argv[2]
E = html.escape

# ── 경로(옛 깃허브 02를 실명으로) ──────────────────────────────
PATH = [
 dict(yr="2016 — 2017", w=31, mo="1년 4개월", role="체험 교육 콘텐츠 기획", org="㈜새로운교육 · 콘텐츠 개발팀 · 연구원",
      body='전공과 무관한 코딩과 피지컬 컴퓨팅까지 다루며 체험형 콘텐츠 약 40개를 다시 만들고, 그것을 초·중등 학생 앞에서 강의했습니다. 만든 사람이 곧 가르치는 사람이라 어디서 막히는지가 그 자리에서 보였고, 보고 고치는 일을 반복하면서 <span class="node-mark">배우는 사람의 입장에서 먼저 생각하는 습관</span>이 생겼습니다.'),
 dict(yr="2017 — 2021", w=100, mo="4년 3개월", role="학습 플랫폼 콘텐츠 기획 · 운영", org="㈜아이스크림에듀 · 콘텐츠 기획실 수학팀 · 대리",
      body='초등 전 학년 콘텐츠를 개념부터 평가까지 이어지는 흐름으로 구성하고, 문제은행에 문항을 쌓으며 운영했습니다. 이때 <span class="node-mark">메타데이터 항목을 나중에 분석할 수 있을 만큼 잘게 나눠 두는 일</span>이 따로 필요하다는 것을 알게 됐습니다. 쌓인 뒤에 다시 나누는 건 훨씬 어렵기 때문입니다. 국정 교과서였던 때라 학습 순서가 하나였고, 매년 나오는 수시개정 내용만 대조해 이미 만든 콘텐츠를 고쳐 나가면 됐습니다.'),
 dict(yr="2021 — 2025", w=86, mo="3년 8개월", role="AI 디지털교과서 · 지식맵 설계", org="㈜웅진씽크빅 · 학습개발실 / AI디지털교과서개발실 · 책임연구원",
      body='같은 회사에서 학습 플랫폼 콘텐츠를 맡다가 교과서 개발로 옮겼습니다. 평가 데이터에서 난이도와 정답률이 어긋나는 지점을 찾아 문항을 교체했고, 학습 내용 자체가 어려운 영역은 보완 콘텐츠로 새로 기획했습니다. 매번 개별로 고치는 대신 개념을 선후행으로 엮어 두려고 <span class="node-mark">초등 전 과정 수학 지식 개념맵</span>을 설계한 것도 이 시기입니다.'),
 dict(yr="2025", w=16, mo="8개월", role="특수교육 AI 디지털교과서 커리큘럼", org="㈜에누마코리아 · 개발2본부 · 수학 커리큘럼 디자이너",
      body='특수교육 대상 학습자를 맡으면서 <span class="node-mark">접근성과 인지 부담이 커리큘럼을 정하는 기준</span>이 됐습니다. 이미 정리되어 있던 표준분류체계도 그대로는 쓸 수 없어 제품 구조에 맞게 다시 묶었습니다. 필요한 도구는 만들어 쓰면서, 그렇게 번 시간을 출시 전 전수 점검에 썼습니다.'),
 dict(yr="2026.05 — 06", w=5, mo="2개월", role="신규 학습 서비스 기획", org="㈜퍼스트해빗 · 서비스 기획팀 · PM",
      body='여러 과목과 수준을 아우르는 신규 학습 서비스의 오픈 베타 준비에 참여했습니다. 시험마다 문항 형태가 달라 화면이 제각각이었는데, <span class="node-mark">학습 모듈을 콘텐츠 형식이 아니라 학습 목적과 실행 흐름 기준으로 다시 정의</span>하니 공통으로 묶였습니다. 콘텐츠팀과 서비스 기획팀이 서로 다른 말로 같은 것을 가리키던 부분도 함께 맞췄습니다.'),
 dict(yr="NEXT", w=40, mo="진행 중", role="AI 프로덕트 매니저", org="멀티캠퍼스 AI.M 1기 · AI 프로덕트 매니저 트랙", nxt=True,
      body='Python과 웹·API 기초에서 시작해 LLM 활용, 서비스 기획과 출시 전략으로 이어지는 920시간 과정을 밟고 있습니다. 그동안 필요할 때마다 익혀 쓴 것들을 순서를 갖춰 정리하고, 검수와 데이터 관리 경험을 제품 환경에서 어떻게 쓸지 찾는 것이 목표입니다.'),
]
BRIDGE = [
 ("초등 전 과정 지식 개념맵을 선후행 관계로 설계", "제품이 다룰 대상을 데이터 구조로 정의"),
 ("정답률·난이도 데이터를 분석해 문항을 교체·보완", "무엇을 볼지 정하고, 고친 뒤 다시 확인"),
 ("콘텐츠팀과 서비스 기획팀 사이 요구사항 정리·조율", "요구사항을 개발이 바로 받을 수 있는 단위로 분해"),
 ("출시 전 전수 검수와 수정·보완 대조표 기반 개정 운영", "어디까지 되면 내보낼지 기준을 먼저 합의"),
 ("반복되는 제작·검수 업무를 AI 도구로 자동화", "AI에 맡길 일과 사람이 맡을 일을 나누기"),
]
# 상세 페이지가 있는 쪽의 웹 대표 그림
DETAIL_THUMB = {"projects/ai-work-tools.html":"assets/tools/generator.jpg",
                "projects/fraction-planet.html":"assets/fraction/hero.jpg",
                "projects/knowledge-map.html":"assets/kmap/unit_tree.jpg"}

def bullets(b, cls="bl"):
    out=[f'<ul class="{cls}">']
    for lv,t in b['b']:
        out.append(f'<li class="lv{lv}">{E(t)}</li>')
    out.append('</ul>')
    return "\n".join(out)

# ── 웹: 회사 쪽 항목 ─────────────────────────────────────────
def web_item(pg, n):
    det = pg.get('detail')
    first = BLOCKS[pg['blocks'][0]]
    thumb = DETAIL_THUMB[det[0]] if det else "assets/slides/"+first['img']
    heads=[]; bodies=[]
    for k in pg['blocks']:
        b=BLOCKS[k]
        heads.append(f'''<div class="it-row"><h3>{E(b['title'])}</h3><span class="it-pd">{E(b['period'])}</span>
          <p class="it-res">{E(b['result'])}</p></div>''')
        lim = f'<p class="it-lim">한계: {E(b["limit"])}</p>' if b.get('limit') else ''
        bodies.append(f'''<div class="it-blk"><div class="it-blk-txt"><h4>{E(b['title'])}</h4>{bullets(b)}{lim}</div>
          <figure class="it-blk-img"><img src="assets/slides/{b['img']}" alt="" loading="lazy" /></figure></div>''')
    note = f'<p class="it-note">{E(pg["note"])}</p>' if pg.get('note') else ''
    more = f'<a class="btn" href="{det[0]}">자세히 보기 · {E(det[1])} →</a>' if det else ''
    return f'''
    <article class="item{' has-detail' if det else ''}" id="p{n}">
      <a class="it-thumb" href="{det[0] if det else '#p'+str(n)}"><img src="{thumb}" alt="" loading="lazy" /></a>
      <div class="it-main">
        {''.join(heads)}
        <div class="it-act">{more}<span class="it-pdf">PDF {n}쪽</span></div>
        <details class="it-more"><summary>쪽 내용 펼치기</summary>{''.join(bodies)}{note}</details>
      </div>
    </article>'''

def web_company():
    out=[]; cur=None; n=3
    for pg in PAGES:
        if pg['co']!=cur:
            if cur: out.append('</div>')
            cur=pg['co']; name,per=COMPANIES[cur]
            out.append(f'<div class="co"><div class="co-head"><h3>{E(name)}</h3><span>{E(per)}</span></div>')
        out.append(web_item(pg,n)); n+=1
    out.append('</div>')
    return "\n".join(out)

def card(c, feature=False):
    return f'''
    <a class="card" href="{c['href']}">
      <div class="card-img"><img src="{c['img']}" alt="" loading="lazy" /></div>
      <div class="card-body">
        <div class="card-meta"><span class="card-kind">{E(c['kind'])}</span><span>{E(c['period'])}</span></div>
        <h2>{E(c['title'])}</h2>
        <p class="card-line">{E(c['line'])}</p>
        <p class="card-result">{E(c['result'])}</p>
      </div>
    </a>'''

def path_html():
    nodes=[]
    for p in PATH:
        bar = f'<span class="node-bar dash" style="width:{p["w"]}%"></span>' if p.get('nxt') else f'<span class="node-bar" style="width:{p["w"]}%"></span>'
        nodes.append(f'''
      <div class="node{' next' if p.get('nxt') else ''}">
        <span class="node-yr">{p['yr']}</span>
        <div class="node-span">{bar}<span class="node-mo">{p['mo']}</span></div>
        <h3 class="node-role">{p['role']}</h3>
        <span class="node-org">{p['org']}</span>
        <p class="node-body">{p['body']}</p>
      </div>''')
    return "".join(nodes)

def bridge_html():
    rows="".join(f'''
      <div class="bridge-row"><div class="bridge-from">{E(a)}</div><div class="bridge-arrow">→</div><div class="bridge-to">{E(b)}</div></div>''' for a,b in BRIDGE)
    return rows

HEAD = '''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>김광진 | 포트폴리오</title>
<meta name="description" content="학습 서비스의 콘텐츠를 기획하고 커리큘럼·메타데이터·지식맵을 설계해 온 10년. 지금은 AI를 활용해 웹 서비스를 기획하고 만들어 보고 있습니다." />
<meta property="og:title" content="김광진 | 포트폴리오" />
<meta property="og:description" content="학습 서비스의 콘텐츠를 기획하고 커리큘럼·메타데이터·지식맵을 설계해 온 10년. 지금은 AI를 활용해 웹 서비스를 기획하고 만들어 보고 있습니다." />
<meta property="og:type" content="website" />
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css" />
<link rel="stylesheet" href="assets/site.css" />
</head>'''

index = f'''{HEAD}
<body>

<div class="topbar">
  <div class="shell topbar-in">
    <a class="mark-name" href="index.html">김광진<span>.</span></a>
    <nav class="topnav" aria-label="섹션 이동"><a href="#path">경로</a><a href="#work">회사</a><a href="#now">지금</a></nav>
    <div class="topbar-contact"><a href="mailto:kwangjin.owl@gmail.com">kwangjin.owl@gmail.com</a> · <a href="docs/portfolio.pdf">PDF</a></div>
  </div>
</div>

<main class="shell">
  <header class="intro">
    <span class="eyebrow">Portfolio</span>
    <h1>학습 콘텐츠와 구조를<br />함께 설계해 온 10년 차 기획자</h1>
    <p>10년 동안 학습 서비스의 콘텐츠를 기획하고, 그 콘텐츠를 서비스 안에서 찾고 추천할 수 있도록 커리큘럼·메타데이터·지식맵을 설계했습니다. 지금은 AI를 활용해 웹 서비스를 기획하고 만들어 보고 있습니다.</p>
    <div class="intro-act"><a class="btn ghost" href="docs/portfolio.pdf">PDF로 받기 <small>11쪽</small></a></div>
  </header>

  <section class="group" id="path">
    <div class="group-head">
      <span class="eyebrow">Path · 2016–2026</span>
      <h2>콘텐츠를 만들다가, 콘텐츠가 놓이는 구조를 만들게 됐습니다.</h2>
      <p>교재와 문항에서 시작해 메타데이터와 문제은행, 지식 개념맵, 학습 서비스의 모듈 구조로 이어졌습니다. 2025년에 두 번 겪은 사업 종료는 AI 디지털교과서 정책이 바뀌며 관련 조직이 개편된 일과 겹칩니다.</p>
    </div>
    <div class="tree">{path_html()}
    </div>
  </section>

  <section class="group" id="bridge">
    <div class="group-head">
      <span class="eyebrow">Bridge</span>
      <h2>버리려는 것이 아니라, 그 위에 더하려는 것입니다.</h2>
      <p>왼쪽은 10년 동안 실제로 해 온 일이고, 오른쪽은 그 일이 제품을 만드는 자리에서 어떤 일과 통하는지 적은 것입니다.</p>
    </div>
    <div class="bridge">
      <div class="bridge-head"><span>해 온 일</span><span></span><span>통하는 일</span></div>{bridge_html()}
    </div>
  </section>

  <section class="group" id="work">
    <div class="group-head">
      <span class="eyebrow">Work · 2016–2025</span>
      <h2>회사에서: 콘텐츠와 그 구조</h2>
      <p>PDF 3~10쪽과 같은 내용입니다. 화면과 과정을 더 보여 드릴 수 있는 것은 「자세히 보기」로 이어집니다.</p>
    </div>
{web_company()}
  </section>

  <section class="group" id="now">
    <div class="group-head">
      <span class="eyebrow">Now · 2026</span>
      <h2>지금: AI로 기획하고 직접 만든 것</h2>
      <p>회사를 나온 뒤 기획부터 배포까지 직접 해 본 작업입니다. 개인 작업 하나와 부트캠프 미니 프로젝트 넷입니다. PDF 11쪽에 같은 목록이 있습니다.</p>
    </div>
    <div class="cards feature">{card(NOW_MAIN)}
    </div>
    <div class="cards pair">{''.join(card(c) for c in NOW_MP)}
    </div>
  </section>

  <section class="closing">
    <span class="eyebrow">Closing</span>
    <h2>만드는 쪽과 굴리는 쪽, 양쪽을 아는 자리에서 일하고 싶습니다.</h2>
    <p>콘텐츠를 잘 만드는 일과, 그 콘텐츠가 서비스 위에서 제대로 동작하게 하는 일은 서로 다른 일이었습니다. 10년 동안 그 사이에 있었습니다.</p>
    <p>학습이나 콘텐츠가 제품의 중심에 있는 곳에서, 콘텐츠와 서비스 양쪽을 아는 사람이 필요한 자리를 찾고 있습니다. 콘텐츠를 만들어 본 사람이 기획하는 자리에 있으면, 실제로 만들 수 있는 형태로 정할 수 있다고 생각합니다.</p>
    <div class="end-link" style="border-top:0;margin-top:26px;padding-top:0">
      <a class="btn" href="mailto:kwangjin.owl@gmail.com">메일 보내기</a>
      <a class="btn ghost" href="docs/portfolio.pdf">PDF로 받기</a>
      <a class="btn ghost" href="https://github.com/kwangjin-owl" target="_blank" rel="noopener">GitHub</a>
    </div>
  </section>
</main>

<div class="shell">
  <footer>
    <span class="code">김광진 · 포트폴리오</span>
    <span class="code">updated 2026.11</span>
    <span class="code">build {BUILD}</span>
  </footer>
</div>

</body>
</html>
'''
open(f"{ROOT}/index.html","w",encoding="utf-8").write(index)

# ── 인쇄본 ───────────────────────────────────────────────
def p_block(k):
    b=BLOCKS[k]
    lim = f'<p class="lim">한계: {E(b["limit"])}</p>' if b.get('limit') else ''
    return f'''
    <section class="blk">
      <div class="txt">
        <div class="bh"><h2>{E(b['title'])}</h2><span class="pd">{E(b['period'])}</span></div>
        {bullets(b)}
        <p class="res">성과: {E(b['result'])}</p>{lim}
      </div>
      <figure class="pic"><img src="assets/slides/{b['img']}" alt="" /></figure>
    </section>'''

TOTAL = 3 + len(PAGES)
pages=[]
pages.append(f'''
<div class="pg cover">
  <div class="cv-l">
    <span class="cv-eb">PORTFOLIO</span>
    <h1>학습 콘텐츠와 구조를<br />함께 설계해 온<br /><em>10년 차</em> 기획자</h1>
    <div class="cv-name">김광진</div>
    <div class="cv-ct">kwangjin.owl@gmail.com<br /><a href="{BASE}">kwangjin-owl.github.io/my_page</a></div>
  </div>
  <div class="cv-r">
    <p class="cv-sub">커리큘럼·문항 설계부터 지식맵과<br />학습 데이터 분석까지</p>
    <div class="cv-tags"><span># 디지털 교과서</span><span># 학습 플랫폼</span><span># 학습 앱</span><span># 학습 데이터</span><span># AI 활용</span></div>
    <p class="cv-web">화면과 과정은 웹에서 더 볼 수 있습니다<br /><a href="{BASE}">{BASE.replace('https://','')}</a></p>
  </div>
  <span class="pn">1/{TOTAL}</span>
</div>''')
CORE = [
 ("01","메타데이터·지식맵 설계",["커리큘럼·학습 차시·문항의 위계 설계 및 메타데이터 관리","선후행 관계로 연결한 초등 전 과정 수학 지식 개념맵 구축","교육과정 표준체계 분류 구성 및 학습 콘텐츠 코드 부여"]),
 ("02","콘텐츠 기획",["국정·검정 커리큘럼 기반 디지털 콘텐츠 기획 및 개발","애니메이션·인터랙티브·게임·강의·문항 등 다양한 형태의 콘텐츠 기획","국내외 학습 제품을 정기적으로 분석해 콘텐츠 방향과 개선점 도출","콘텐츠가 서비스 구조에 맞게 구현되도록 개발·디자인 조직과 조율"]),
 ("03","품질 관리",["원고·업로드·태블릿 검증·배포 단계별 콘텐츠 검수 수행","출시 전후 검수를 통한 콘텐츠 오류 점검 및 품질 개선","외주 디자인·개발 산출물 기준 정의 및 수정 요청 관리"]),
 ("04","데이터·AI 활용",["학습 데이터 분석 기반 콘텐츠 개선","반복 작업을 줄이는 제작·검수 도구 제작","AI 도구를 활용한 콘텐츠 제작·검수 효율화"]),
]
cores="".join(f'''<div class="core c{n}"><h2><span>{n}</span>{E(t)}</h2><ul>{''.join(f'<li>{E(x)}</li>' for x in xs)}</ul></div>''' for n,t,xs in CORE)
pages.append(f'''
<div class="pg">
  <div class="core-head"><span class="eb">CORE COMPETENCY</span><h1>4대 핵심역량</h1></div>
  <div class="cores">{cores}</div>
  <p class="core-foot">2026년 신규 학습 서비스 기획을 거쳐, 지금은 AI 프로덕트 매니저 과정을 밟고 있습니다.</p>
  <span class="pn">2/{TOTAL}</span>
</div>''')
for i,pg in enumerate(PAGES, start=3):
    name,per = COMPANIES[pg['co']]
    det = pg.get('detail')
    dl = f'<a class="more" href="{BASE}{det[0]}">자세히 보기 → {E(det[1])}<small>{(BASE+det[0]).replace("https://","")}</small></a>' if det else ''
    note = f'<p class="note">{E(pg["note"])}</p>' if pg.get('note') else ''
    pages.append(f'''
<div class="pg">
  <header class="ph"><h1>{E(name)}</h1><span class="per">{E(per)}</span>{dl}</header>
  <div class="blks">{''.join(p_block(k) for k in pg['blocks'])}</div>
  {note}<span class="pn">{i}/{TOTAL}</span>
</div>''')
mp="".join(f'''
    <a class="mp" href="{BASE}{c['href']}">
      <div class="mp-img"><img src="{c['img']}" alt="" /></div>
      <span class="mp-kind">{E(c['kind'])} · {E(c['period'])}</span>
      <h3>{E(c['title'])}</h3>
      <p>{E(c['result'])}</p>
      <span class="mp-more">자세히 보기 →</span>
    </a>''' for c in NOW_MP)
pages.append(f'''
<div class="pg">
  <header class="ph"><h1>2026 · AI로 기획하고 만든 것</h1><span class="per">개인 작업과 멀티캠퍼스 AI 프로덕트 매니저 트랙 미니 프로젝트</span></header>
  <section class="blk now">
    <div class="txt">
      <div class="bh"><h2>AI 메뉴판 편집기</h2><span class="pd">26.08~26.11</span></div>
      <ul class="bl">
        <li class="lv1">{E(NOW_MAIN['line'])}</li>
        <li class="lv1">사장님이 가게에서 써 보며 불편하다고 한 것을 두 달 동안 하나씩 고침</li>
        <li class="lv1">AI가 읽은 메뉴를 사진 옆에 나란히 보여 주고, 사장님이 확인한 뒤에 메뉴판이 만들어지게 함</li>
        <li class="lv1">기획과 확인을 맡고 코드는 Claude Code가 작성</li>
      </ul>
      <p class="res">성과: 9월 7일부터 지인 요리주점에서 인쇄해 사용</p>
      <a class="more inl" href="{BASE}projects/menu.html">자세히 보기 → 메뉴판 편집기</a>
    </div>
    <figure class="pic"><img src="{NOW_MAIN['img']}" alt="" /></figure>
  </section>
  <div class="mps">{mp}
  </div>
  <span class="pn">{TOTAL}/{TOTAL}</span>
</div>''')

PRINT_CSS = open(f"{ROOT}/assets/print.css",encoding="utf-8").read() if False else None
printhtml = f'''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=1280" />
<title>김광진 포트폴리오 (인쇄본)</title>
<meta name="robots" content="noindex" />
<link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css" />
<link rel="stylesheet" href="assets/print.css" />
</head>
<body>
<!-- index.html과 같은 데이터에서 만든 인쇄본. 브라우저 인쇄 → PDF로 저장(여백 없음, 배경 그래픽 켬). build {BUILD} -->
{''.join(pages)}
</body>
</html>
'''
open(f"{ROOT}/print.html","w",encoding="utf-8").write(printhtml)
print("ok", TOTAL, "쪽")
