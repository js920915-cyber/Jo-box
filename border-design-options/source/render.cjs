const fs=require('fs'),path=require('path'),{pathToFileURL}=require('url');
const deps='C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules';
const {chromium}=require(path.join(deps,'playwright')),sharp=require(path.join(deps,'sharp'));
(async()=>{
const root=path.resolve(__dirname,'..');
const browser=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});
const page=await browser.newPage({viewport:{width:1080,height:1350},deviceScaleFactor:1});
const checks=[];
for(const id of ['B01','B02','B03','B04','B05']){
 await page.goto(pathToFileURL(path.join(__dirname,id+'.html')).href);await page.evaluate(()=>document.fonts.ready);
 const check=await page.evaluate(()=>{
  const errors=[];
  for(const e of document.querySelectorAll('.card h1,.card p,.card strong')){
   const b=e.getBoundingClientRect();if(b.bottom>1252||b.left<88||b.right>992)errors.push('Text bounds: '+e.className);
   if(getComputedStyle(e).textAlign!=='center')errors.push('Text alignment');
  }
  return {errors,text:document.querySelector('.card').innerText};
 });if(check.errors.length)throw Error(id+check.errors.join(','));
 const dest=path.join(root,'exports',id+'.png');await page.locator('.card').screenshot({path:dest});
 const m=await sharp(dest).metadata();if(m.width!==1080||m.height!==1350)throw Error('Size');
 await sharp(dest).resize(360,450).png().toFile(path.join(root,'qa',id+'-mobile.png'));
 checks.push({id,...check});
}
if(new Set(checks.map(c=>c.text)).size!==1)throw Error('Variant text differs');
fs.writeFileSync(path.join(root,'qa/layout-check.json'),JSON.stringify(checks,null,2));
await browser.close();console.log('PASS: 5 border PNGs, identical text, centered typography, safe margins.');
})();
