# REGALOO digital menu

Open `index.html` in any modern browser. No installation, network access, dependencies, or build is required.

Menu names and prices are editable directly in `index.html`. The mobile stylesheet is `menu.css`. `identity.css` restores the established artwork and desktop styles. All artwork is local in `assets/`.

Mobile uses one column with 48px add buttons, readable names and prices, and an always-visible cart bar. Desktop preserves the original layout with two or three columns depending on screen width. Buttons display “✓ Ajouté” after addition. Customers can change quantities, remove items, and review totals in the accessible cart dialog.

`script.js` opens `https://wa.me/212725240109` with the complete order encoded using `encodeURIComponent`, including the customer's name, delivery address or pickup choice, and optional notes. The customer sends the message in WhatsApp. Delivery fees require confirmation by the restaurant. A connection is needed to open WhatsApp; the menu itself works offline.

The current artwork consists of AI-generated recreations inspired by the supplied menu, optimized to transparent WebP (except the opaque wood background), and code-drawn SVG decorations. The master PNG files remain outside the website folder.
