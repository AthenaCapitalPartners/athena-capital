from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle

def create_capability_statement():
    output_path = "/Users/Nila/Desktop/cm-mcp-server/website/capability-statement.pdf"
    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter  # 612 x 792

    # Colors
    navy = HexColor("#0A192F")
    gold = HexColor("#C5A059")
    dark_gray = HexColor("#2d2d2d")
    medium_gray = HexColor("#555555")
    light_bg = HexColor("#F5EDD8")
    white = HexColor("#ffffff")

    margin = 40
    content_width = width - 2 * margin

    # === TOP HEADER BAR ===
    c.setFillColor(navy)
    c.rect(0, height - 105, width, 105, fill=True, stroke=False)

    # Gold accent line at bottom of header
    c.setStrokeColor(gold)
    c.setLineWidth(2.5)
    c.line(0, height - 105, width, height - 105)

    # Company name
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 20)
    c.drawString(margin, height - 40, "ATHENA CAPITAL PARTNERS LLC")

    # Gold accent line under name
    c.setStrokeColor(gold)
    c.setLineWidth(1.5)
    c.line(margin, height - 50, margin + 265, height - 50)

    # Tagline
    c.setFont("Helvetica", 9)
    c.setFillColor(HexColor("#cccccc"))
    c.drawString(margin, height - 65, "Micro-Purchase Office Supply & Professional Services | Southern Nevada")

    # IDs row
    c.setFont("Helvetica", 8)
    c.setFillColor(HexColor("#aaaaaa"))
    c.drawString(margin, height - 80, "CAGE: 1NGH5   |   UEI: F1VPSS7P7DM6   |   SAM.gov Active")

    # Right side badges
    c.setFillColor(gold)
    c.setFont("Helvetica-Bold", 9)
    c.drawRightString(width - margin, height - 38, "WOMAN-OWNED SMALL BUSINESS")
    c.setFont("Helvetica", 8)
    c.setFillColor(white)
    c.drawRightString(width - margin, height - 52, "NAICS: 541611 | 459540")
    c.drawRightString(width - margin, height - 66, "PSC: 7510 | R706 | R410 | R412")
    c.drawRightString(width - margin, height - 80, "GPC Accepted | EFT Accepted")

    # === CAPABILITY STATEMENT TITLE ===
    y = height - 128
    c.setFillColor(navy)
    c.setFont("Helvetica-Bold", 13)
    c.drawCentredString(width / 2, y, "CAPABILITY STATEMENT")

    # Gold line under title
    c.setStrokeColor(gold)
    c.setLineWidth(1.5)
    c.line(margin, y - 8, width - margin, y - 8)

    # === ABOUT US SECTION ===
    y = y - 28
    c.setFillColor(navy)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(margin, y, "ABOUT US")
    c.setStrokeColor(gold)
    c.setLineWidth(1)
    c.line(margin, y - 3, margin + 58, y - 3)

    y -= 16
    about_text = (
        "Athena Capital Partners LLC is a Woman-Owned Small Business (WOSB) based in Las Vegas, Nevada, "
        "specializing in micro-purchase fulfillment and last-mile desktop delivery of office supplies, imaging "
        "consumables, and professional services to federal agencies throughout Southern Nevada. We are SAM.gov "
        "registered, FAR-compliant, and strategically located to provide same-day and next-day emergency "
        "fulfillment for Nellis AFB, VA Southern Nevada, and other federal installations in the region."
    )
    style = ParagraphStyle('about', fontName='Helvetica', fontSize=8.5, leading=12, textColor=dark_gray)
    p = Paragraph(about_text, style)
    pw, ph = p.wrap(content_width, 100)
    p.drawOn(c, margin, y - ph)
    y = y - ph - 14

    # === TWO COLUMN LAYOUT ===
    col1_x = margin
    col2_x = width / 2 + 10
    col_width = content_width / 2 - 10

    # === LEFT COLUMN: CORE COMPETENCIES ===
    left_y = y

    c.setFillColor(navy)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(col1_x, left_y, "CORE COMPETENCIES")
    c.setStrokeColor(gold)
    c.line(col1_x, left_y - 3, col1_x + 138, left_y - 3)

    left_y -= 18

    competencies = [
        ("Imaging Supplies",
         "OEM high-yield toner & ink cartridges\n(HP, Brother, Lexmark) for federal printers"),
        ("Office & Stationery Supplies",
         "Paper, writing instruments, folders,\nadmin essentials — no minimum order"),
        ("Breakroom Consumables",
         "Coffee, snacks, janitorial & facility\nitems for high-traffic federal offices"),
        ("Administrative Support",
         "Virtual assistance, data entry,\nscheduling & document management"),
        ("Writing, Editing & Translation",
         "Technical writing, proofreading,\nmultilingual translation services"),
        ("Graphic Design & Printing",
         "Branding, marketing collateral,\npresentations & print fulfillment"),
    ]

    for title, desc in competencies:
        c.setFillColor(gold)
        c.circle(col1_x + 5, left_y - 2, 3, fill=True, stroke=False)
        c.setFillColor(navy)
        c.setFont("Helvetica-Bold", 8.5)
        c.drawString(col1_x + 14, left_y, title)
        left_y -= 12
        c.setFillColor(medium_gray)
        c.setFont("Helvetica", 7.5)
        for line in desc.split('\n'):
            c.drawString(col1_x + 14, left_y, line)
            left_y -= 10
        left_y -= 6

    # === RIGHT COLUMN ===
    right_y = y

    # DIFFERENTIATORS
    c.setFillColor(navy)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(col2_x, right_y, "DIFFERENTIATORS")
    c.setStrokeColor(gold)
    c.line(col2_x, right_y - 3, col2_x + 120, right_y - 3)

    right_y -= 18

    box_height = 122
    c.setFillColor(light_bg)
    c.roundRect(col2_x, right_y - box_height + 10, col_width, box_height, 5, fill=True, stroke=False)

    differentiators = [
        ("Desktop Delivery", "Bypass loading docks — delivered\ndirectly to your administrative desk"),
        ("Same/Next-Day Fulfillment", "Emergency supply runs for Nellis\nAFB & VA Southern Nevada"),
        ("WOSB Set-Aside Eligible", "Qualifies for WOSB & small\nbusiness set-aside contracts"),
        ("GPC & MPT Ready", "Sub-$10,000 orders via Govt\nPurchase Card — no contract needed"),
    ]

    diff_y = right_y - 4
    for title, desc in differentiators:
        c.setFillColor(gold)
        c.setFont("Helvetica-Bold", 8.5)
        c.drawString(col2_x + 10, diff_y, "\u2713  " + title)
        diff_y -= 11
        c.setFillColor(medium_gray)
        c.setFont("Helvetica", 7.5)
        for line in desc.split('\n'):
            c.drawString(col2_x + 20, diff_y, line)
            diff_y -= 9
        diff_y -= 4

    right_y = diff_y - 12

    # NAICS CODES
    c.setFillColor(navy)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(col2_x, right_y, "NAICS CODES")
    c.setStrokeColor(gold)
    c.line(col2_x, right_y - 3, col2_x + 88, right_y - 3)

    right_y -= 16
    naics = [
        ("541611", "Admin Management Consulting"),
        ("459540", "Office Supplies & Stationery Retailers"),
    ]
    for code, desc in naics:
        c.setFillColor(navy)
        c.setFont("Helvetica-Bold", 8.5)
        c.drawString(col2_x, right_y, code)
        c.setFillColor(medium_gray)
        c.setFont("Helvetica", 7.5)
        c.drawString(col2_x + 44, right_y, desc)
        right_y -= 13

    right_y -= 8

    # PSC CODES
    c.setFillColor(navy)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(col2_x, right_y, "PSC CODES")
    c.setStrokeColor(gold)
    c.line(col2_x, right_y - 3, col2_x + 72, right_y - 3)

    right_y -= 16
    psc = [
        ("7510", "Office Supplies"),
        ("R706", "Administrative Support Services"),
        ("R410", "Technical Writing"),
        ("R412", "Translation & Interpreting"),
    ]
    for code, desc in psc:
        c.setFillColor(navy)
        c.setFont("Helvetica-Bold", 8.5)
        c.drawString(col2_x, right_y, code)
        c.setFillColor(medium_gray)
        c.setFont("Helvetica", 7.5)
        c.drawString(col2_x + 38, right_y, desc)
        right_y -= 13

    right_y -= 8

    # PAST PERFORMANCE
    c.setFillColor(navy)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(col2_x, right_y, "PAST PERFORMANCE")
    c.setStrokeColor(gold)
    c.line(col2_x, right_y - 3, col2_x + 130, right_y - 3)

    right_y -= 16
    c.setFillColor(medium_gray)
    c.setFont("Helvetica", 8)
    c.drawString(col2_x, right_y, "Available upon request.")
    c.drawString(col2_x, right_y - 12, "Contact us for references & project details.")

    # === BOTTOM CONTACT BAR ===
    bar_height = 52
    c.setFillColor(navy)
    c.rect(0, 0, width, bar_height, fill=True, stroke=False)

    c.setStrokeColor(gold)
    c.setLineWidth(2)
    c.line(0, bar_height, width, bar_height)

    # Contact items
    contacts = [
        ("WEB",      "athenacapitalnv.com",        margin),
        ("EMAIL",    "janani@athenacapitalnv.com",  margin + 145),
        ("PHONE",    "(702) 301-9535",              margin + 320),
        ("LOCATION", "Las Vegas, Nevada",           margin + 450),
    ]

    c.setFillColor(white)
    for label, value, x in contacts:
        c.setFont("Helvetica-Bold", 7.5)
        c.setFillColor(gold)
        c.drawString(x, 32, label)
        c.setFont("Helvetica", 8)
        c.setFillColor(white)
        c.drawString(x, 16, value)

    c.save()
    print(f"PDF created: {output_path}")

create_capability_statement()
