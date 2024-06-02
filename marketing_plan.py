from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle


def create_business_overview_section(data):
    story = []
    styles = getSampleStyleSheet()

    # Business Overview Title
    title_style = styles['Title']
    story.append(Paragraph("Business Overview", title_style))
    story.append(Spacer(1, 12))

    # Business Details
    details = [
        ("Name", data['business_overview']['name']),
        ("Industry", data['business_overview']['industry']),
        ("Company Size", data['business_overview']['company_size'])
    ]

    table_data = [[key, value] for key, value in details]

    # Table Style
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])

    table = Table(table_data, colWidths=[150, 350])
    table.setStyle(table_style)

    story.append(table)
    story.append(Spacer(1, 12))

    return story


def create_company_objectives_section(data):
    story = []
    styles = getSampleStyleSheet()

    # Company Objectives Title
    title_style = styles['Title']
    story.append(Paragraph("Company Objectives", title_style))
    story.append(Spacer(1, 12))

    # Objectives List
    for objective in data['company_objectives']:
        story.append(Paragraph(f"- {objective}", styles['Normal']))
        story.append(Spacer(1, 6))

    return story


def create_social_media_strategy_section(data):
    story = []
    styles = getSampleStyleSheet()

    # Social Media Strategy Title
    title_style = styles['Title']
    story.append(Paragraph("Social Media Strategy", title_style))
    story.append(Spacer(1, 12))

    # Strategy Details
    for platform, strategy in data['social_media_strategy'].items():
        story.append(Paragraph(f"Platform: {platform}", styles['Heading2']))
        story.append(Spacer(1, 6))
        story.append(Paragraph(f"Frequency: {strategy['frequency']}", styles['Normal']))
        story.append(Spacer(1, 6))
        story.append(Paragraph(f"Content Types: {', '.join(strategy['content_types'])}", styles['Normal']))
        story.append(Spacer(1, 12))

    return story


def create_budget_section(data):
    story = []
    styles = getSampleStyleSheet()

    # Budget Title
    title_style = styles['Title']
    story.append(Paragraph("Budget", title_style))
    story.append(Spacer(1, 12))

    # Budget Details
    budget_data = [
        ["Category", "Amount"],
        ["Advertising", f"${data['budget']['advertising']}"],
        ["Content Creation", f"${data['budget']['content_creation']}"],
        ["Software", f"${data['budget']['software']}"],
        ["Miscellaneous", f"${data['budget']['miscellaneous']}"]
    ]

    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])

    table = Table(budget_data, colWidths=[150, 350])
    table.setStyle(table_style)

    story.append(table)
    story.append(Spacer(1, 12))

    return story


def create_pdf(data, filename):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    story = []

    # Add sections
    story.extend(create_business_overview_section(data))
    story.extend(create_company_objectives_section(data))
    story.extend(create_social_media_strategy_section(data))
    story.extend(create_budget_section(data))

    # Build PDF
    doc.build(story)


def main():
    # Example data
    data = {
        "business_overview": {
            "name": "ABC Corp",
            "industry": "Technology",
            "company_size": "200 employees"
        },
        "company_objectives": [
            "Increase market share by 10%",
            "Launch 3 new products",
            "Improve customer satisfaction"
        ],
        "social_media_strategy": {
            "Facebook": {
                "frequency": "Daily",
                "content_types": ["Posts", "Stories", "Ads"]
            },
            "Twitter": {
                "frequency": "Twice daily",
                "content_types": ["Tweets", "Retweets"]
            },
            "Instagram": {
                "frequency": "Daily",
                "content_types": ["Posts", "Stories", "Reels"]
            }
        },
        "budget": {
            "advertising": 5000,
            "content_creation": 2000,
            "software": 1000,
            "miscellaneous": 500
        }
    }

    # Create the PDF
    create_pdf(data, "marketing_plan.pdf")


if __name__ == "__main__":
    main()
