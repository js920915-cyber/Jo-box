from pathlib import Path
import zipfile
from PIL import Image

root=Path(__file__).resolve().parents[1]
for id in ['B01','B02','B03','B04','B05']:
    with Image.open(root/'exports'/f'{id}.png') as im:assert im.size==(1080,1350)
with zipfile.ZipFile(root/'border-design-options.zip','w',zipfile.ZIP_DEFLATED) as z:
    for folder in ['assets','exports','source']:
        for p in (root/folder).iterdir():
            if p.is_file():z.write(p,str(Path('border-design-options')/p.relative_to(root)))
    for name in ['README.md','QA_REPORT.md','options.json']:
        z.write(root/name,str(Path('border-design-options')/name))
print('5 PNGs + editable SVG/HTML/CSS sources packaged.')
