"""
PDF Generator for Catholic Diocese of Tombura-Yambio Information Request Form
Generates a professional PDF document from the Markdown form
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

def create_pdf():
    """Create the PDF information request form"""
    
    # Output file path
    output_path = r"C:\Users\DBTECH AFRICA\Desktop\St Yambio Catholic Website\INFORMATION-REQUEST-FORM.pdf"
    
    # Create PDF with A4 size
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=18
    )
    
    # Container for story elements
    story = []
    
    # Styles
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=18,
        textColor=colors.darkblue,
        spaceAfter=30,
        alignment=TA_CENTER
    )
    
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.darkgreen,
        spaceAfter=20,
        alignment=TA_CENTER
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading3'],
        fontSize=12,
        textColor=colors.darkblue,
        spaceAfter=12,
        spaceBefore=20
    )
    
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=12,
        leading=14
    )
    
    bold_style = ParagraphStyle(
        'CustomBold',
        parent=styles['Normal'],
        fontSize=10,
        fontName='Helvetica-Bold',
        spaceAfter=12
    )
    
    # Title Page
    story.append(Paragraph("INFORMATION REQUEST FORM", title_style))
    story.append(Spacer(0, 0.2*inch))
    story.append(Paragraph("Catholic Diocese of Tombura-Yambio", subtitle_style))
    story.append(Paragraph("Website Restructuring Project", subtitle_style))
    story.append(Spacer(0, 0.5*inch))
    
    # Header information
    header_data = [
        ["Date:", "October 7, 2026"],
        ["To:", "Bishop Eduardo Hiiboro Kussala and Diocesan Curia"],
        ["From:", "Website Redesign Team"],
        ["Purpose:", "Gather required information for website redesign and content migration"]
    ]
    
    header_table = Table(header_data, colWidths=[1.5*inch, 4*inch])
    header_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(header_table)
    story.append(Spacer(0, 0.3*inch))
    
    # Instructions
    story.append(Paragraph("INSTRUCTIONS", heading_style))
    instructions = """
    This document contains all the information needed from the Catholic Diocese of Tombura-Yambio to proceed with the website redesign project. Please review each section carefully and provide the requested information.
    
    <b>Timeline:</b> Please complete this form within 4 weeks of receipt.
    <b>Contact:</b> [Project Manager Contact Information]
    <b>Questions:</b> Please contact the project team for clarification on any items.
    """
    story.append(Paragraph(instructions, normal_style))
    story.append(PageBreak())
    
    # Section 1: Critical Verifications
    story.append(Paragraph("SECTION 1: CRITICAL VERIFICATIONS", heading_style))
    story.append(Paragraph("(REQUIRED BEFORE DEVELOPMENT)", bold_style))
    story.append(Spacer(0, 0.1*inch))
    
    # 1.1 Geographic Jurisdiction
    story.append(Paragraph("1.1 Geographic Jurisdiction", heading_style))
    
    geo_text = """
    <b>Current Website States:</b>
    "The jurisdiction of the diocese covers 7 Counties of former Western Equatoria State, namely, Maridi, Ibba, Yambio, Nzara, Ezo, Tombura and Nagero."
    """
    story.append(Paragraph(geo_text, normal_style))
    story.append(Spacer(0, 0.1*inch))
    
    geo_questions = [
        ["Question", "Response"],
        ["Is the reference to 'former Western Equatoria State' still accurate?", ""],
        ["What is the current official administrative structure?", ""],
        ["Are the 7 counties still correct?", ""],
        ["Have any counties been added, removed, or renamed?", ""],
        ["What is the correct way to reference the region now?", ""],
        ["Has the diocesan jurisdiction changed in any way?", ""],
        ["Additional Information:", ""],
        ["", ""],
        ["", ""],
    ]
    
    geo_table = Table(geo_questions, colWidths=[3.5*inch, 2*inch])
    geo_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(geo_table)
    story.append(Spacer(0, 0.2*inch))
    
    # 1.2 Parish Count
    story.append(Paragraph("1.2 Parish Count", heading_style))
    
    parish_text = """
    <b>Inconsistency Found:</b>
    • English version: "Ecclesiastically, the diocese comprises of Thirty Five (35) parishes"
    • Italian version: "Ecclesiasticamente, la diocesi comprende ventisette parrocchie" (27 parishes)
    • French version: "Sur le plan ecclésiastique, le diocèse comprend vingt-sept paroisses" (27 parishes)
    """
    story.append(Paragraph(parish_text, normal_style))
    story.append(Spacer(0, 1*inch))
    
    parish_questions = [
        ["Question", "Response"],
        ["What is the ACTUAL current number of parishes?", ""],
        ["Why do Italian and French versions show 27 parishes?", ""],
        ["Have new parishes been created since the translations were made?", ""],
        ["Are all 35 parishes listed in the English version still active?", ""],
        ["Have any parishes been closed or merged?", ""],
        ["Please provide the current complete list of all parishes:", ""],
        ["", ""],
        ["", ""],
    ]
    
    parish_table = Table(parish_questions, colWidths=[3.5*inch, 2*inch])
    parish_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(parish_table)
    story.append(Spacer(0, 0.2*inch))
    
    # 1.3 Deanery Count
    story.append(Paragraph("1.3 Deanery Count and Structure", heading_style))
    
    deanery_text = """
    <b>Inconsistency Found:</b>
    • English version: Lists 6 deaneries with specific names
    • Italian version: "raggruppate in quattro decanati" (4 deaneries)
    • French version: "regroupées en quatre doyennés" (4 deaneries)
    """
    story.append(Paragraph(deanery_text, normal_style))
    story.append(Spacer(0, 0.1*inch))
    
    deanery_questions = [
        ["Question", "Response"],
        ["Are there 6 deaneries or 4?", ""],
        ["What are the CORRECT names of all deaneries?", ""],
        ["Have deanery boundaries changed?", ""],
        ["Which structure is current?", ""],
        ["Please list all deaneries with their official names:", ""],
        ["1. ", ""],
        ["2. ", ""],
        ["3. ", ""],
        ["4. ", ""],
        ["5. ", ""],
        ["6. ", ""],
    ]
    
    deanery_table = Table(deanery_questions, colWidths=[3.5*inch, 2*inch])
    deanery_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(deanery_table)
    story.append(Spacer(0, 0.2*inch))
    
    # 1.4 Population Statistics
    story.append(Paragraph("1.4 Catholic Population Statistics", heading_style))
    
    pop_text = """
    <b>Current Website States:</b>
    "The current population of Catholics is over 1,000,000, constituting over 60% of the total population."
    """
    story.append(Paragraph(pop_text, normal_style))
    story.append(Spacer(0, 0.1*inch))
    
    pop_questions = [
        ["Question", "Response"],
        ["Are these statistics current?", ""],
        ["When were they last updated?", ""],
        ["What is the source of these statistics?", ""],
        ["Are more recent statistics available?", ""],
        ["If updated, what are the current numbers?", ""],
    ]
    
    pop_table = Table(pop_questions, colWidths=[3.5*inch, 2*inch])
    pop_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(pop_table)
    story.append(Spacer(0, 0.2*inch))
    
    pop_sub = """
    <b>Updated Statistics (if available):</b>
    • Total Catholic population: _________________
    • Percentage of total population: _________________
    • Date of statistics: _________________
    • Source: _________________
    """
    story.append(Paragraph(pop_sub, normal_style))
    story.append(PageBreak())
    
    # 1.5 Bishop Information
    story.append(Paragraph("1.5 Bishop Information", heading_style))
    
    bishop_text = """
    <b>Current Status:</b> Bishop only mentioned on homepage with limited information. No dedicated biography page.
    """
    story.append(Paragraph(bishop_text, normal_style))
    story.append(Spacer(0, 0.1*inch))
    
    # Personal Information
    story.append(Paragraph("<b>Personal Information:</b>", bold_style))
    bishop_personal = [
        ["Full Name:", "Barani Eduardo Hiiboro Kussala"],
        ["Title:", "Bishop of Catholic Diocese of Tombura-Yambio"],
        ["Date of Birth:", ""],
        ["Place of Birth:", ""],
        ["Date of Ordination:", ""],
        ["Date of Episcopal Ordination:", ""],
        ["Date of Installation as Bishop:", ""],
    ]
    
    bishop_personal_table = Table(bishop_personal, colWidths=[2*inch, 3.5*inch])
    bishop_personal_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(bishop_personal_table)
    story.append(Spacer(0, 0.1*inch))
    
    # Biography
    story.append(Paragraph("<b>Biography:</b>", bold_style))
    story.append(Paragraph("Please provide a complete biography (200-500 words):", normal_style))
    
    bio_lines = [
        [""],
        [""],
        [""],
        [""],
        [""],
        [""],
        [""],
        [""],
        [""],
        [""],
    ]
    
    bio_table = Table(bio_lines, colWidths=[5.5*inch])
    bio_table.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('TOPPADDING', (0, 0), (-1, -1), 12),
        ('ROW_HEIGHT', (0, 0), (-1, -1), 24),
    ]))
    story.append(bio_table)
    story.append(Spacer(0, 0.1*inch))
    
    # Recent Activities
    story.append(Paragraph("<b>Recent Activities and Initiatives:</b>", bold_style))
    story.append(Paragraph("List major activities, pastoral letters, or initiatives from the past 2 years:", normal_style))
    
    activities = [
        ["1. ", ""],
        ["2. ", ""],
        ["3. ", ""],
        ["4. ", ""],
        ["5. ", ""],
    ]
    
    activities_table = Table(activities, colWidths=[0.5*inch, 5*inch])
    activities_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(activities_table)
    story.append(Spacer(0, 0.1*inch))
    
    # Photos
    story.append(Paragraph("<b>Photos:</b>", bold_style))
    story.append(Paragraph("Please provide:", normal_style))
    photo_checklist = [
        ["□", "Official portrait photo (high resolution)"],
        ["□", "3-5 recent activity photos"],
        ["□", "Historical photos if available"],
    ]
    
    photo_table = Table(photo_checklist, colWidths=[0.3*inch, 5.2*inch])
    photo_table.setStyle(TableStyle([
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(photo_table)
    story.append(Spacer(0, 0.1*inch))
    
    # Contact Information
    story.append(Paragraph("<b>Contact Information:</b>", bold_style))
    bishop_contact = [
        ["Bishop's Office Phone:", ""],
        ["Bishop's Office Email:", ""],
        ["Bishop's Secretary Name:", ""],
        ["Bishop's Secretary Contact:", ""],
    ]
    
    bishop_contact_table = Table(bishop_contact, colWidths=[2.5*inch, 3*inch])
    bishop_contact_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(bishop_contact_table)
    story.append(PageBreak())
    
    # 1.6 Priest Assignments
    story.append(Paragraph("1.6 Priest Assignments", heading_style))
    
    priest_text = """
    <b>Current Status:</b> Deanery pages list priests, but assignments may have changed.
    <b>Verification Needed for Each Deanery:</b>
    """
    story.append(Paragraph(priest_text, normal_style))
    story.append(Spacer(0, 0.1*inch))
    
    # Deanery priest tables
    deaneries = [
        "Our Lady Queen of South Sudan Western Deanery",
        "Holy Spirit Mid-West Deanery",
        "Holy Cross Central West Deanery",
        "All Saints Central Deanery",
        "Resurrection Mid-East Deanery",
        "Corpus Christi Eastern Deanery"
    ]
    
    current_names = [
        "Rev. Fr. Mark Kumbonyaki",
        "Fr. Luke Yugue",
        "Fr. Anthony Bangoye",
        "Fr. Elias Juma",
        "Fr. Babu Kashiore",
        "Fr. Venencio Zukpa"
    ]
    
    for i, (deanery, current) in enumerate(zip(deaneries, current_names)):
        story.append(Paragraph(f"{deanery}", bold_style))
        
        deanery_data = [
            ["Position", "Current Name on Website", "Current Actual Name", "Status"],
            ["Episcopal Vicar", current, "", "□ Still same  □ Changed"],
            ["If changed, new name:", "", "", ""],
        ]
        
        deanery_table = Table(deanery_data, colWidths=[1.5*inch, 2*inch, 2*inch, 1.5*inch])
        deanery_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 8),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ]))
        story.append(deanery_table)
        story.append(Spacer(0, 0.1*inch))
    
    story.append(Paragraph("<b>Parish Priest Assignments:</b>", bold_style))
    story.append(Paragraph("Please provide an updated list of all parish priests:", normal_style))
    
    parish_header = ["Parish", "Deanery", "Current Priest on Website", "Current Actual Priest"]
    parish_priest_data = [parish_header]
    for _ in range(35):  # 35 parishes
        parish_priest_data.append(["", "", "", ""])
    
    parish_priest_table = Table(parish_priest_data, colWidths=[1.5*inch, 1.5*inch, 1.5*inch, 1.5*inch])
    parish_priest_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 7),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(parish_priest_table)
    story.append(PageBreak())
    
    # 1.7 Contact Information
    story.append(Paragraph("1.7 Contact Information", heading_style))
    
    contact_text = """
    <b>Current Website Lists:</b>
    
    <b>Head Office (Yambio):</b>
    • Address: Wilson St, Yambio, South Sudan
    • Phone: (+211) 913 410 880, (+211) 915 021 709
    • Email: mail2cdty@cdty.org
    
    <b>Kampala Office:</b>
    • Address: Plot 7979 Block 246, Muyenga, Uganda
    • Phone: (+256) 779869165
    • Email: muyenga@cdty.org
    
    <b>Nairobi Office:</b>
    • Email: nairobi@cdty.org (no address or phone listed)
    
    <b>Juba Office:</b>
    • Email: juba@cdty.org (no address or phone listed)
    """
    story.append(Paragraph(contact_text, normal_style))
    story.append(Spacer(0, 0.1*inch))
    
    contact_header = ["Office", "Phone - Current", "Phone - Correct", "Address - Current", "Address - Correct", "Email - Current", "Email - Correct", "Office Hours"]
    contact_data = [contact_header]
    
    offices = [
        ("Yambio", "(+211) 913 410 880, (+211) 915 021 709", "", "Wilson St, Yambio, South Sudan", "", "mail2cdty@cdty.org", ""),
        ("Kampala", "(+256) 779869165", "", "Plot 7979 Block 246, Muyenga, Uganda", "", "muyenga@cdty.org", ""),
        ("Nairobi", "Not listed", "", "Not listed", "", "nairobi@cdty.org", ""),
        ("Juba", "Not listed", "", "Not listed", "", "juba@cdty.org", ""),
    ]
    
    for office in offices:
        contact_data.append(list(office))
    
    contact_table = Table(contact_data, colWidths=[0.8*inch, 1.2*inch, 0.8*inch, 1.2*inch, 0.8*inch, 1.2*inch, 0.8*inch, 0.8*inch])
    contact_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 7),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(contact_table)
    story.append(Spacer(0, 0.2*inch))
    
    story.append(Paragraph("<b>Additional Offices:</b>", bold_style))
    story.append(Paragraph("Are there any other offices not listed? □ Yes  □ No", normal_style))
    story.append(Paragraph("If yes, please provide details:", normal_style))
    
    additional_office = [["", ""]]
    additional_table = Table(additional_office, colWidths=[5.5*inch])
    additional_table.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('TOPPADDING', (0, 0), (-1, -1), 12),
        ('ROW_HEIGHT', (0, 0), (-1, -1), 36),
    ]))
    story.append(additional_table)
    story.append(Spacer(0, 0.1*inch))
    
    # Social Media
    story.append(Paragraph("<b>Social Media:</b>", bold_style))
    story.append(Paragraph("Please provide all official social media accounts:", normal_style))
    
    social_media = [
        ["Facebook:", ""],
        ["YouTube:", ""],
        ["Instagram:", ""],
        ["Twitter/X:", ""],
        ["Other:", ""],
    ]
    
    social_table = Table(social_media, colWidths=[1.5*inch, 4*inch])
    social_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(social_table)
    story.append(PageBreak())
    
    # Section 2: High Priority
    story.append(Paragraph("SECTION 2: HIGH PRIORITY VERIFICATIONS", heading_style))
    story.append(Spacer(0, 0.1*inch))
    
    # 2.1 Staff Directory
    story.append(Paragraph("2.1 Staff Directory (Curia)", heading_style))
    
    staff_text = """
    <b>Current Status:</b> 28+ staff members listed on Curia page.
    """
    story.append(Paragraph(staff_text, normal_style))
    story.append(Spacer(0, 0.1*inch))
    
    staff_questions = [
        ["Question", "Response"],
        ["Are all listed staff still with the Diocese?", ""],
        ["Are there new staff not listed?", ""],
        ["Have roles changed?", ""],
        ["Should all staff be publicly listed?", ""],
        ["Should contact details be included for staff?", ""],
    ]
    
    staff_table = Table(staff_questions, colWidths=[3.5*inch, 2*inch])
    staff_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(staff_table)
    story.append(Spacer(0, 0.1*inch))
    
    story.append(Paragraph("<b>Updated Staff Directory:</b>", bold_style))
    story.append(Paragraph("Please provide current staff list:", normal_style))
    
    staff_header = ["Name", "Title/Role", "Department", "Email", "Phone"]
    staff_data = [staff_header]
    for _ in range(30):  # 30 staff
        staff_data.append(["", "", "", "", ""])
    
    staff_list_table = Table(staff_data, colWidths=[1.5*inch, 1.5*inch, 1*inch, 1*inch, 0.8*inch])
    staff_list_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 7),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(staff_list_table)
    story.append(PageBreak())
    
    # Note about remaining sections
    story.append(Paragraph("NOTE:", heading_style))
    note_text = """
    Due to the extensive nature of this information request form, this PDF contains the most critical sections (Section 1 and Section 2) in fillable format.
    
    For the complete information request including all sections (Sections 3-7), please refer to the accompanying Markdown document:
    
    <b>INFORMATION-REQUEST-DIACSESE.md</b>
    
    This document contains:
    • Section 3: Medium Priority Verifications
    • Section 4: Missing Information Requests
    • Section 5: Additional Information
    • Section 6: Approval and Sign-off
    • Section 7: Contact Information
    • Appendix: Document Checklist
    
    Please complete both this PDF form (for critical sections) and the Markdown document (for all sections).
    """
    story.append(Paragraph(note_text, normal_style))
    story.append(Spacer(0, 0.5*inch))
    
    # Approval section
    story.append(Paragraph("SECTION 6: APPROVAL AND SIGN-OFF", heading_style))
    story.append(Spacer(0, 0.1*inch))
    
    story.append(Paragraph("6.1 Information Accuracy", bold_style))
    story.append(Paragraph("I certify that the information provided in this form is accurate to the best of my knowledge.", normal_style))
    story.append(Spacer(0, 0.2*inch))
    
    approval_data = [
        ["Name:", ""],
        ["Title:", ""],
        ["Signature:", ""],
        ["Date:", ""],
    ]
    
    approval_table = Table(approval_data, colWidths=[1.5*inch, 4*inch])
    approval_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ('TOPPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(approval_table)
    story.append(Spacer(0, 0.3*inch))
    
    story.append(Paragraph("6.2 Diocesan Approval", bold_style))
    story.append(Paragraph("This information request has been reviewed and approved by:", normal_style))
    story.append(Spacer(0, 0.2*inch))
    
    story.append(Paragraph("Bishop Eduardo Hiiboro Kussala", normal_style))
    story.append(Paragraph("Signature: ______________________________", normal_style))
    story.append(Paragraph("Date: ______________________________", normal_style))
    story.append(Spacer(0, 0.2*inch))
    
    story.append(Paragraph("Vicar General", normal_style))
    story.append(Paragraph("Name: ______________________________", normal_style))
    story.append(Paragraph("Signature: ______________________________", normal_style))
    story.append(Paragraph("Date: ______________________________", normal_style))
    story.append(Spacer(0, 0.2*inch))
    
    story.append(Paragraph("Curia Secretary", normal_style))
    story.append(Paragraph("Name: ______________________________", normal_style))
    story.append(Paragraph("Signature: ______________________________", normal_style))
    story.append(Paragraph("Date: ______________________________", normal_style))
    
    # Build PDF
    doc.build(story)
    
    print(f"PDF generated successfully: {output_path}")
    return output_path

if __name__ == "__main__":
    try:
        pdf_path = create_pdf()
        print(f"\nPDF created at: {pdf_path}")
        print(f"File size: {os.path.getsize(pdf_path) / 1024:.2f} KB")
    except Exception as e:
        print(f"Error creating PDF: {e}")
        import traceback
        traceback.print_exc()
