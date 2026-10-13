from pathlib import Path
import shutil,json

root=Path(__file__).resolve().parents[1]
project=root.parents[1]
base=project/'content/achilles-elongation-v2'
for d in ['assets','exports','qa']:(root/d).mkdir(parents=True,exist_ok=True)
for name in ['NotoSansKR-VF.ttf','OFL.txt']:shutil.copyfile(base/'assets'/name,root/'assets'/name)
css=(base/'source/cards.css').read_text(encoding='utf-8')
css+='\n.border-decoration{position:absolute;inset:0;width:1080px;height:1350px;pointer-events:none;z-index:0;} .card>*:not(.border-decoration){position:relative;z-index:1;}\n'
(root/'source/cards.css').write_text(css,encoding='utf-8')
body=(base/'source/03.html').read_text(encoding='utf-8')

variants=[
('C01','블루 그라데이션','기존 페일 블루를 조금 더 풍부하게: 색 농도가 달라지는 띠와 부드러운 이중 윤곽.', '''<defs><linearGradient id="tone" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#e3eff8"/><stop offset=".45" stop-color="#f5f9fc"/><stop offset="1" stop-color="#daeaf5"/></linearGradient></defs><rect x="34" y="34" width="1012" height="1282" rx="46" fill="none" stroke="url(#tone)" stroke-width="22"/><rect x="34" y="34" width="1012" height="1282" rx="46" fill="none" stroke="#cbdfea" stroke-width="1.5"/><rect x="48" y="48" width="984" height="1254" rx="34" fill="none" stroke="#edf4f9" stroke-width="1.5"/><path d="M482 34H598M482 1316H598" stroke="#b5d3e7" stroke-width="5" stroke-linecap="round"/>'''),
('C02','겹친 코너 곡선','페일 블루 프레임에 대각선 두 모서리만 곡선을 겹쳐 작은 포인트.', '''<rect x="34" y="34" width="1012" height="1282" rx="46" fill="none" stroke="#e9f3f9" stroke-width="18"/><rect x="34" y="34" width="1012" height="1282" rx="46" fill="none" stroke="#d0e2ee" stroke-width="1.5"/><g fill="none" stroke-linecap="round"><path d="M34 162V82Q34 34 82 34H162" stroke="#c2dcee" stroke-width="5"/><path d="M50 148V88Q50 50 88 50H148" stroke="#e1edf6" stroke-width="5"/><path d="M918 1316H998Q1046 1316 1046 1268V1188" stroke="#c2dcee" stroke-width="5"/><path d="M932 1300H992Q1030 1300 1030 1262V1202" stroke="#e1edf6" stroke-width="5"/></g><circle cx="170" cy="34" r="3" fill="#c2dcee"/><circle cx="910" cy="1316" r="3" fill="#c2dcee"/>'''),
('C03','스포츠 코너','두 모서리를 사선으로 정리하고 작은 사선 두 개를 더한 가벼운 스포츠 인상.', '''<path d="M84 34H1000L1046 80V1268Q1046 1316 998 1316H80L34 1270V82Q34 34 84 34Z" fill="none" stroke="#e9f3f9" stroke-width="18" stroke-linejoin="round"/><path d="M84 34H1000L1046 80V1268Q1046 1316 998 1316H80L34 1270V82Q34 34 84 34Z" fill="none" stroke="#cbdfea" stroke-width="1.5" stroke-linejoin="round"/><g stroke="#c0d9ea" stroke-width="3" stroke-linecap="round"><path d="M984 34L1046 96M967 34L1046 113M34 1237L113 1316M34 1254L96 1316"/></g>'''),
('C04','유려한 곡선','옆선을 부드럽게 휘게 하고 반대편에 가는 곡선을 더한 가장 유기적인 시안.', '''<path d="M93 34H987Q1046 34 1046 94V370C1046 484 1029 526 1038 656C1048 790 1046 879 1046 986V1257Q1046 1316 987 1316H93Q34 1316 34 1257V978C34 862 51 815 42 682C32 549 34 471 34 365V94Q34 34 93 34Z" fill="none" stroke="#e7f1f8" stroke-width="19"/><path d="M93 34H987Q1046 34 1046 94V370C1046 484 1029 526 1038 656C1048 790 1046 879 1046 986V1257Q1046 1316 987 1316H93Q34 1316 34 1257V978C34 862 51 815 42 682C32 549 34 471 34 365V94Q34 34 93 34Z" fill="none" stroke="#c8ddeb" stroke-width="1.5"/><path d="M52 410C52 522 65 563 55 694M1028 938C1028 826 1015 784 1025 654" stroke="#d8e8f3" stroke-width="2" fill="none" stroke-linecap="round"/>'''),
('C05','페이퍼 프레임','넓은 페일 블루 띠와 규칙적인 작은 점. 은은한 종이 가장자리 느낌.', '''<rect x="34" y="34" width="1012" height="1282" rx="42" fill="none" stroke="#e9f3f9" stroke-width="26"/><rect x="47" y="47" width="986" height="1256" rx="30" fill="none" stroke="#d1e3ef" stroke-width="1.5"/><g fill="none" stroke="#b9d4e7" stroke-width="2.5" stroke-linecap="round" stroke-dasharray=".1 15"><path d="M100 34H980M100 1316H980M34 100V1250M1046 100V1250"/></g>'''),
]
for key,name,desc,svg in variants:
    html=body.replace('<article class="card card--function">','<article class="card card--function"><svg class="border-decoration" viewBox="0 0 1080 1350" aria-hidden="true">'+svg+'</svg>')
    html=html.replace('<title>아킬레스건 길어짐 카드 3</title>',f'<title>{key} {name}</title>')
    (root/f'source/{key}.html').write_text(html,encoding='utf-8')
(root/'options.json').write_text(json.dumps([{'id':v[0],'name':v[1],'description':v[2]} for v in variants],ensure_ascii=False,indent=2),encoding='utf-8')
render=(project/'content/border-design-options/source/render.cjs').read_text(encoding='utf-8')
for i in range(1,6):render=render.replace(f'B{i:02}',f'C{i:02}')
(root/'source/render.cjs').write_text(render,encoding='utf-8')
print('Five refined designs based on B05: same centered text, independent decorative SVG layer.')
