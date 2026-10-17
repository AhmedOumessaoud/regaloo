from pathlib import Path
from playwright.sync_api import sync_playwright
import json
p=Path('regaloo-menu').resolve()
with sync_playwright() as pw:
    browser=pw.chromium.launch(executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe',headless=True)
    page=browser.new_page(device_scale_factor=1)
    results=[]
    for width in [320,375,390,430,1280]:
        page.set_viewport_size({'width':width,'height':900})
        page.goto((p/'index.html').as_uri())
        page.wait_for_load_state('networkidle')
        result=page.evaluate('''() => ({width:innerWidth,scrollWidth:document.documentElement.scrollWidth,categories:document.querySelectorAll('section.category').length,items:document.querySelectorAll('li').length,brokenImages:[...document.images].filter(i=>!i.complete||i.naturalWidth===0).map(i=>i.src),phone:document.querySelector('footer a').getAttribute('href'),overflowingRows:[...document.querySelectorAll('li')].filter(e=>e.scrollWidth>e.clientWidth+1).map(e=>e.innerText)})''')
        results.append(result)
        if width==390:page.screenshot(path=str(p/'preview-390.png'),full_page=True)
    browser.close()
print(json.dumps(results,indent=2))
(p/'verification.json').write_text(json.dumps(results,indent=2))
