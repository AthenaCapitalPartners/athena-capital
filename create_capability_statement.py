from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle

def create_capability_statement():
    output_path = "/Users/Nila/Desktop/cm-mcp-server/website/capability-statement.pdf"
    c = canvas.Canvas(output_path, pagesize=letter)
    W, H = letter  # 612 x 792

    # ── Palette ────────────────────────────────────────────────────────────
    navy      = HexColor("#0A192F")
    navy_mid  = HexColor("#0D2240")
    gold      = HexColor("#C5A059")
    gold_lt   = HexColor("#E8D5A3")
    off_white = HexColor("#F7F4EF")
    white_c   = HexColor("#FFFFFF")
    mid_txt   = HexColor("#3A3A4A")
    muted_txt = HexColor("#666677")
    sidebar_hi= HexColor("#D4D8E8")
    divider   = HexColor("#1E3A5F")

    # ── Layout constants ───────────────────────────────────────────────────
    SB_W   = 210          # sidebar width
    MX     = SB_W + 18    # main content left edge
    MW     = W - MX - 16  # main content width  (~368)
    SM     = 15           # sidebar inner margin
    MM     = 14           # main inner margin

    # ══════════════════════════════════════════════════════════════════════
    # SIDEBAR BACKGROUND + ACCENTS
    # ══════════════════════════════════════════════════════════════════════
    c.setFillColor(navy)
    c.rect(0, 0, SB_W, H, fill=True, stroke=False)

    # Gold top cap
    c.setFillColor(gold)
    c.rect(0, H - 9, SB_W, 9, fill=True, stroke=False)

    # Gold right edge
    c.setStrokeColor(gold)
    c.setLineWidth(1.5)
    c.line(SB_W, 0, SB_W, H)

    # ══════════════════════════════════════════════════════════════════════
    # SIDEBAR — COMPANY NAME & BADGE
    # ══════════════════════════════════════════════════════════════════════
    y = H - 32
    c.setFillColor(gold)
    c.setFont("Helvetica-Bold", 23)
    c.drawString(SM, y, "ATHENA")

    y -= 22
    c.setFillColor(white_c)
    c.setFont("Helvetica-Bold", 10.5)
    c.drawString(SM, y, "CAPITAL PARTNERS LLC")

    y -= 10
    c.setStrokeColor(gold)
    c.setLineWidth(1)
    c.line(SM, y, SB_W - SM, y)

    y -= 11
    c.setFillColor(sidebar_hi)
    c.setFont("Helvetica", 7)
    c.drawString(SM, y, "Professional Services  ·  Federal Contractor")

    y -= 10
    c.drawString(SM, y, "Las Vegas, Nevada  ·  WOSB Certified")

    # WOSB pill badge
    y -= 18
    bw = SB_W - 2 * SM
    c.setFillColor(gold)
    c.roundRect(SM, y - 5, bw, 17, 4, fill=True, stroke=False)
    c.setFillColor(navy)
    c.setFont("Helvetica-Bold", 7.5)
    c.drawCentredString(SB_W / 2, y + 3, "WOMAN-OWNED SMALL BUSINESS")

    y -= 22
    c.setStrokeColor(divider)
    c.setLineWidth(0.5)
    c.line(SM, y, SB_W - SM, y)

    # ── Helper: sidebar section block ──────────────────────────────────────
    def sb_section(title, rows, sy, label_w=52):
        c.setFillColor(gold)
        c.setFont("Helvetica-Bold", 8)
        c.drawString(SM, sy, title)
        sy -= 3
        c.setStrokeColor(gold)
        c.setLineWidth(0.6)
        c.line(SM, sy, SB_W - SM, sy)
        sy -= 11

        for row in rows:
            if isinstance(row, tuple):
                lbl, val = row
                c.setFillColor(gold_lt)
                c.setFont("Helvetica-Bold", 7.5)
                c.drawString(SM, sy, lbl)
                c.setFillColor(sidebar_hi)
                c.setFont("Helvetica", 7.5)
                c.drawString(SM + label_w, sy, val)
            else:
                c.setFillColor(gold)
                c.circle(SM + 4, sy - 1, 2.2, fill=True, stroke=False)
                c.setFillColor(sidebar_hi)
                c.setFont("Helvetica", 7.5)
                c.drawString(SM + 12, sy, row)
            sy -= 13
        return sy - 5

    y = sb_section("REGISTRATIONS & IDs", [
        ("SAM.gov", "Active"),
        ("CAGE",    "1NGH5"),
        ("UEI",     "F1VPSS7P7DM6"),
        ("State",   "Nevada LLC"),
    ], y - 10)

    y = sb_section("NAICS CODES", [
        ("541611", "Admin Mgmt Consulting"),
        ("459540", "Office Supplies & Stationery"),
    ], y, label_w=44)

    y = sb_section("PSC CODES", [
        ("7510", "Office Supplies"),
        ("R706", "Admin Support Services"),
        ("R410", "Technical Writing"),
        ("R412", "Translation & Interpreting"),
    ], y, label_w=38)

    y = sb_section("CERTIFICATIONS", [
        "SAM.gov Registered",
        "WOSB Certified",
        "GPC / Micro-Purchase Ready",
        "FAR Compliant",
        "EFT Accepted",
    ], y)

    # ── Sidebar bottom contact block ───────────────────────────────────────
    c.setStrokeColor(divider)
    c.setLineWidth(0.5)
    c.line(SM, 120, SB_W - SM, 120)

    c.setFillColor(gold)
    c.setFont("Helvetica-Bold", 8)
    c.drawString(SM, 108, "CONTACT US")

    contacts = [
        ("Web",      "athenacapitalnv.com"),
        ("Email",    "janani@athenacapitalnv.com"),
        ("Phone",    "(702) 301-9535"),
        ("Location", "Las Vegas, Nevada"),
        ("SAM.gov",  "Search 'Athena Capital Partners'"),
    ]
    cy = 95
    for lbl, val in contacts:
        c.setFillColor(gold_lt)
        c.setFont("Helvetica-Bold", 6.5)
        c.drawString(SM, cy, lbl + ":")
        c.setFillColor(sidebar_hi)
        c.setFont("Helvetica", 7)
        c.drawString(SM + 38, cy, val)
        cy -= 11

    # ══════════════════════════════════════════════════════════════════════
    # MAIN CONTENT AREA
    # ══════════════════════════════════════════════════════════════════════
    c.setFillColor(white_c)
    c.rect(SB_W + 1, 0, W - SB_W - 1, H, fill=True, stroke=False)

    # Gold top cap (matches sidebar)
    c.setFillColor(gold)
    c.rect(SB_W + 1, H - 9, W - SB_W - 1, 9, fill=True, stroke=False)

    # ── Title ──────────────────────────────────────────────────────────────
    y = H - 31
    c.setFillColor(navy)
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(MX + MW / 2, y, "CAPABILITY STATEMENT")

    y -= 8
    c.setStrokeColor(gold)
    c.setLineWidth(1.5)
    c.line(MX, y, MX + MW, y)

    # ── Helper: main section header ────────────────────────────────────────
    def section_hdr(title, sy):
        c.setFillColor(navy)
        c.setFont("Helvetica-Bold", 9)
        c.drawString(MX + MM, sy, title)
        sy -= 4
        c.setStrokeColor(gold)
        c.setLineWidth(0.7)
        c.line(MX + MM, sy, MX + MW, sy)
        return sy - 11

    # ── ABOUT US ───────────────────────────────────────────────────────────
    y -= 16
    y = section_hdr("ABOUT US", y)

    about = (
        "Athena Capital Partners LLC is a Woman-Owned Small Business (WOSB) "
        "headquartered in Las Vegas, Nevada, delivering professional services and "
        "micro-purchase supply fulfillment to U.S. federal agencies. SAM.gov "
        "registered and FAR-compliant, we specialize in desktop delivery of office "
        "supplies, imaging consumables, and administrative support — with same-day "
        "and next-day emergency fulfillment capacity for federal installations "
        "throughout Southern Nevada."
    )
    style_body = ParagraphStyle(
        "body", fontName="Helvetica", fontSize=8.5, leading=13, textColor=mid_txt
    )
    p = Paragraph(about, style_body)
    _, ph = p.wrap(MW - 2 * MM, 200)
    y -= ph
    p.drawOn(c, MX + MM, y)
    y -= 18

    # ── CORE COMPETENCIES ──────────────────────────────────────────────────
    y = section_hdr("CORE COMPETENCIES", y)

    competencies = [
        ("Imaging Supplies",
         "OEM high-yield toner & ink cartridges (HP, Brother, Lexmark) "
         "for federal office printers."),
        ("Office & Stationery",
         "Paper, writing instruments, folders, and admin essentials "
         "with no minimum order requirement."),
        ("Breakroom & Facility",
         "Coffee, snacks, janitorial and facility consumables for "
         "high-traffic federal offices."),
        ("Administrative Support",
         "Virtual assistance, data entry, scheduling coordination, "
         "and document management."),
        ("Writing & Translation",
         "Technical writing, policy documents, proofreading, "
         "and multilingual translation services."),
        ("Graphic Design & Print",
         "Branding, marketing collateral, presentations, "
         "and full print fulfillment."),
    ]

    cols     = 2
    card_gap = 8
    card_w   = (MW - 2 * MM - card_gap) / 2
    card_h   = 52
    row_gap  = 7
    style_card = ParagraphStyle(
        "card", fontName="Helvetica", fontSize=7.2, leading=10, textColor=muted_txt
    )

    grid_top = y
    for i, (title, desc) in enumerate(competencies):
        col = i % cols
        row = i // cols
        cx  = MX + MM + col * (card_w + card_gap)
        cy  = grid_top - row * (card_h + row_gap)

        # Card fill
        c.setFillColor(off_white)
        c.roundRect(cx, cy - card_h, card_w, card_h, 5, fill=True, stroke=False)

        # Gold left accent bar
        c.setFillColor(gold)
        c.roundRect(cx, cy - card_h, 4, card_h, 2, fill=True, stroke=False)

        # Card title
        c.setFillColor(navy)
        c.setFont("Helvetica-Bold", 8)
        c.drawString(cx + 12, cy - 13, title)

        # Card body
        p2 = Paragraph(desc, style_card)
        _, ph2 = p2.wrap(card_w - 18, 35)
        p2.drawOn(c, cx + 12, cy - 14 - ph2 - 2)

    num_rows = -(-len(competencies) // cols)   # ceiling div
    y = grid_top - num_rows * (card_h + row_gap) - 16

    # ── DIFFERENTIATORS ────────────────────────────────────────────────────
    y = section_hdr("DIFFERENTIATORS", y)

    differentiators = [
        ("Desktop Delivery",
         "Bypass loading docks — delivered directly to your administrative desk."),
        ("Same / Next-Day Fulfillment",
         "Emergency supply runs for Nellis AFB, VA Southern Nevada, "
         "and nearby federal sites."),
        ("WOSB Set-Aside Eligible",
         "Qualifies for WOSB and small business set-aside contract vehicles."),
        ("GPC & Micro-Purchase Ready",
         "Sub-$10,000 orders via Government Purchase Card — "
         "no solicitation required."),
    ]

    diff_cols  = 2
    diff_gap   = 8
    diff_w     = (MW - 2 * MM - diff_gap) / 2
    diff_h     = 42
    diff_style = ParagraphStyle(
        "diff", fontName="Helvetica", fontSize=7.2, leading=10, textColor=muted_txt
    )

    diff_top = y
    for i, (title, desc) in enumerate(differentiators):
        col = i % diff_cols
        row = i // diff_cols
        cx  = MX + MM + col * (diff_w + diff_gap)
        cy  = diff_top - row * (diff_h + 6)

        c.setFillColor(off_white)
        c.roundRect(cx, cy - diff_h, diff_w, diff_h, 5, fill=True, stroke=False)

        # Gold checkmark circle
        c.setFillColor(gold)
        c.circle(cx + 11, cy - 12, 7, fill=True, stroke=False)
        c.setFillColor(navy)
        c.setFont("Helvetica-Bold", 9)
        c.drawCentredString(cx + 11, cy - 16, "v")

        c.setFillColor(navy)
        c.setFont("Helvetica-Bold", 7.5)
        c.drawString(cx + 24, cy - 10, title)

        p3 = Paragraph(desc, diff_style)
        _, ph3 = p3.wrap(diff_w - 28, 28)
        p3.drawOn(c, cx + 24, cy - 12 - ph3 - 1)

    diff_rows = -(-len(differentiators) // diff_cols)
    y = diff_top - diff_rows * (diff_h + 6) - 16

    # ── ORDERING PROCESS ───────────────────────────────────────────────────
    y = section_hdr("ORDERING PROCESS", y)

    steps = [
        ("01", "Contact Us",       "Submit your requirement by email or phone — we respond same business day."),
        ("02", "Receive a Quote",  "Get a detailed quote within 24 hours with pricing and delivery timeline."),
        ("03", "Fast Delivery",    "We fulfill and deliver on time, every time. GPC accepted at checkout."),
    ]

    step_cols = 3
    step_gap  = 8
    step_w    = (MW - 2 * MM - step_gap * (step_cols - 1)) / step_cols
    step_h    = 62

    for i, (num, title, desc) in enumerate(steps):
        cx = MX + MM + i * (step_w + step_gap)
        cy = y

        c.setFillColor(off_white)
        c.roundRect(cx, cy - step_h, step_w, step_h, 5, fill=True, stroke=False)

        # Number badge
        badge_r = 11
        c.setFillColor(navy)
        c.circle(cx + badge_r + 4, cy - badge_r - 5, badge_r, fill=True, stroke=False)
        c.setFillColor(gold)
        c.setFont("Helvetica-Bold", 9)
        c.drawCentredString(cx + badge_r + 4, cy - badge_r - 9, num)

        c.setFillColor(navy)
        c.setFont("Helvetica-Bold", 7.5)
        c.drawString(cx + 8, cy - 32, title)

        s = ParagraphStyle(
            "step", fontName="Helvetica", fontSize=7, leading=9.5, textColor=muted_txt
        )
        p4 = Paragraph(desc, s)
        _, ph4 = p4.wrap(step_w - 14, 30)
        p4.drawOn(c, cx + 8, cy - 34 - ph4)

    y -= step_h + 16

    # ── PAST PERFORMANCE ───────────────────────────────────────────────────
    y = section_hdr("PAST PERFORMANCE", y)

    c.setFillColor(off_white)
    c.roundRect(MX + MM, y - 26, MW - 2 * MM, 28, 4, fill=True, stroke=False)
    c.setStrokeColor(gold)
    c.setLineWidth(0.5)
    c.roundRect(MX + MM, y - 26, MW - 2 * MM, 28, 4, fill=False, stroke=True)
    c.setFillColor(muted_txt)
    c.setFont("Helvetica", 8)
    c.drawString(MX + MM + 10, y - 10,
                 "References and project details available upon request.")
    c.setFont("Helvetica-Oblique", 7.5)
    c.drawString(MX + MM + 10, y - 22,
                 "Contact quotes@athenacapitalnv.com for a tailored proposal.")
    y -= 26

    # ── BOTTOM BANNER (main area) ──────────────────────────────────────────
    banner_h = 46
    c.setFillColor(navy)
    c.rect(SB_W + 1, 0, W - SB_W - 1, banner_h, fill=True, stroke=False)
    c.setStrokeColor(gold)
    c.setLineWidth(1.5)
    c.line(SB_W + 1, banner_h, W, banner_h)

    tags = [
        ("GPC Accepted",     MX + MM),
        ("EFT Accepted",     MX + MM + 95),
        ("FAR Compliant",    MX + MM + 185),
        ("SAM.gov Active",   MX + MM + 278),
    ]
    for label, tx in tags:
        c.setFillColor(gold)
        c.circle(tx + 5, banner_h / 2 + 2, 3, fill=True, stroke=False)
        c.setFillColor(white_c)
        c.setFont("Helvetica-Bold", 7.5)
        c.drawString(tx + 13, banner_h / 2 - 1, label)

    c.save()
    print(f"PDF saved: {output_path}")

create_capability_statement()
