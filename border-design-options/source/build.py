from pathlib import Path
import shutil,json

root=Path(__file__).resolve().parents[1]
project=root.parents[1]
base=project/'content/achilles-elongation-v2'
for d in ['assets','exports','qa']:(root/d).mkdir(parents=True,exist_ok=True)
shutil.copyfile(base/'assets/NotoSansKR-VF.ttf',root/'assets/NotoSansKR-VF.ttf')
shutil.copyfile(base/'assets/OFL.txt',root/'assets/OFL.txt')
css=(base/'source/cards.css').read_text(encoding='utf-8')
css+='\n.border-decoration{position:absolute;inset:0;width:1080px;height:1350px;pointer-events:none;z-index:0;} .card>*:not(.border-decoration){position:relative;z-index:1;}\n'
(root/'source/cards.css').write_text(css,encoding='utf-8')
body=(base/'source/03.html').read_text(encoding='utf-8')
variants=[
('B01','얇은 라운드 프레임','전체 외곽을 2px 회청색 선으로 정리. 가장 차분한 기본형.', '<rect x="34" y="34" width="1012" height="1282" rx="28" fill="none" stroke="#d0dce5" stroke-width="2"/>'),
('B02','네 모서리 포인트','모서리에만 짧은 선. 전체 테두리보다 개방적인 인상.', '<g fill="none" stroke="#c5d8e6" stroke-width="3" stroke-linecap="round"><path d="M36 118V56Q36 36 56 36H118"/><path d="M962 36H1024Q1044 36 1044 56V118"/><path d="M36 1232V1294Q36 1314 56 1314H118"/><path d="M962 1314H1024Q1044 1314 1044 1294V1232"/></g>'),
('B03','상하 열린 프레임','상단·하단만 얇게 연결하고 가운데를 살짝 비워 답답함을 줄임.', '<g fill="none" stroke="#d0dce5" stroke-width="2.5" stroke-linecap="round"><path d="M36 100V58Q36 36 58 36H446M634 36H1022Q1044 36 1044 58V100"/><path d="M36 1250V1292Q36 1314 58 1314H446M634 1314H1022Q1044 1314 1044 1292V1250"/></g><path d="M518 36H562M518 1314H562" stroke="#b8d0e2" stroke-width="3" stroke-linecap="round"/>'),
('B04','이중 헤어라인','두 개의 아주 얇은 선. 종이 액자 같은 정돈된 인상.', '<rect x="29" y="29" width="1022" height="1292" rx="18" fill="none" stroke="#d5dfe6" stroke-width="1.5"/><rect x="41" y="41" width="998" height="1268" rx="12" fill="none" stroke="#e6edf2" stroke-width="1.5"/>'),
('B05','부드러운 페일 블루 테두리','연한 블루 띠와 가는 윤곽. 가장 부드럽게 카드의 가장자리를 감쌈.', '<rect x="33" y="33" width="1014" height="1284" rx="42" fill="none" stroke="#edf4f8" stroke-width="12"/><rect x="33" y="33" width="1014" height="1284" rx="42" fill="none" stroke="#d4e2ec" stroke-width="1.5"/>'),
]
for key,name,desc,svg in variants:
    art=f'<svg class="border-decoration" viewBox="0 0 1080 1350" aria-hidden="true">{svg}</svg>'
    html=body.replace('<article class="card card--function">','<article class="card card--function">'+art)
    html=html.replace('<title>아킬레스건 길어짐 카드 3</title>',f'<title>{key} {name}</title>')
    (root/f'source/{key}.html').write_text(html,encoding='utf-8')
(root/'options.json').write_text(json.dumps([{'id':v[0],'name':v[1],'description':v[2]} for v in variants],ensure_ascii=False,indent=2),encoding='utf-8')
print('5 independent border variants built from the same centered card.')
