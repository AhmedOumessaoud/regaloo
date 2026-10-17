from pathlib import Path
from playwright.sync_api import sync_playwright
p=Path('regaloo-menu').resolve()
with sync_playwright() as pw:
 b=pw.chromium.launch(executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe',headless=True)
 page=b.new_page(viewport={'width':390,'height':844})
 errors=[]
 page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto((p/'index.html').as_uri())
 assert page.locator('.product-button').count()==60
 page.locator('.product-button').first.click(click_count=2)
 page.locator('#cart-toggle').click()
 assert page.locator('#cart-total').inner_text()=='30 dh'
 page.get_by_role('button',name='Retirer un Salade Salade Marocaine',exact=True).click()
 assert page.locator('#cart-total').inner_text()=='15 dh'
 page.locator('#customer-name').fill('Test client')
 page.locator('#customer-address').fill('Casablanca, adresse test')
 page.locator('#order-notes').fill('Sans oignons & sauce à part')
 page.evaluate("document.querySelector('#order-form').addEventListener('submit', e=>e.preventDefault())")
 page.locator('#checkout').click()
 message=page.locator('#whatsapp-message').input_value()
 assert '1 × Salade — Salade Marocaine : 15 dh' in message
 assert 'Total produits : 15 dh' in message
 assert 'Sans oignons & sauce à part' in message
 assert page.locator('#order-form').get_attribute('action')=='https://wa.me/212787142624'
 page.locator('#delivery-mode').select_option(label='À emporter')
 assert not page.locator('#customer-address').is_visible()
 page.locator('#clear-cart').click()
 assert page.locator('#checkout').is_disabled()
 page.locator('#close-cart').click()
 for width in [320,375,390,430,1280]:
  page.set_viewport_size({'width':width,'height':844})
  assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
 page.set_viewport_size({'width':390,'height':844})
 page.screenshot(path=str(p/'preview-390.png'),full_page=True)
 assert not errors,errors
 print('PASS: 60 products; add/decrease/clear; totals; delivery/pickup; WhatsApp message and number; empty checkout; responsive widths; no JS errors. No message sent.')
 b.close()
