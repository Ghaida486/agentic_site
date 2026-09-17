from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

OUT = 'VenueFit_Boston_Data_and_Methodology_Note.docx'
doc = Document()
sec = doc.sections[0]
sec.top_margin = Inches(.58); sec.bottom_margin = Inches(.55)
sec.left_margin = Inches(.7); sec.right_margin = Inches(.7)
styles = doc.styles
styles['Normal'].font.name = 'Aptos'; styles['Normal'].font.size = Pt(9.5)
styles['Normal'].font.color.rgb = RGBColor(35, 54, 51)
styles['Normal'].paragraph_format.space_after = Pt(4)
for name, size in [('Title', 21), ('Heading 1', 12)]:
    st = styles[name]; st.font.name = 'Aptos Display'; st.font.size = Pt(size); st.font.bold = True; st.font.color.rgb = RGBColor(0,0,0)
    st.paragraph_format.space_before = Pt(8); st.paragraph_format.space_after = Pt(3)

title = doc.add_paragraph('VenueFit Boston Data and Methodology Note', style='Title')
title.alignment = WD_ALIGN_PARAGRAPH.LEFT
p = doc.add_paragraph('Purpose: a public-data decision tool for Boston university, nonprofit, and community event teams choosing a venue shortlist.')
p.runs[0].bold = True

def heading(text): doc.add_paragraph(text, style='Heading 1')
def para(text): doc.add_paragraph(text)

heading('Decision question')
para('Which venue should an event team shortlist when it needs to fit an expected audience while keeping access to rapid transit practical? The site lets users adjust expected attendance, indoor or outdoor preference, season, and a straight-line transit-distance tolerance. It returns a ranked shortlist and shows the comparison evidence.')

heading('Dataset and collection')
para('The CSV contains eight Boston venues. Capacity, setting, operating season, parking statement, and venue details were transcribed on 17 September 2026 from venue-owner pages or City of Boston public project material. Each row includes the exact capacity and details source URLs. The venue list is a purposeful comparison sample, not a census of Boston event spaces. No personal data was collected.')

table = doc.add_table(rows=1, cols=3)
table.alignment = WD_TABLE_ALIGNMENT.CENTER
table.style = 'Table Grid'
headers = ['Field', 'Unit or definition', 'Source method']
for i, text in enumerate(headers):
    cell = table.rows[0].cells[i]; cell.text = text; cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
    tcPr = cell._tc.get_or_add_tcPr(); shade = OxmlElement('w:shd'); shade.set(qn('w:fill'),'183F3B'); tcPr.append(shade)
    for run in cell.paragraphs[0].runs: run.font.bold=True; run.font.color.rgb=RGBColor(255,255,255); run.font.size=Pt(8.5)
rows = [
 ('capacity', 'Maximum people in cited configuration', 'Official venue or public project material'),
 ('setting and season', 'Indoor or outdoor; year-round or summer', 'Venue information pages'),
 ('transit distance', 'Approximate straight-line meters to listed stop', 'Venue location + MBTA GTFS stop framework'),
 ('planner score', '0–100 transparent fit score', 'Site calculation; not a measured outcome'),
]
for a,b,c in rows:
    cells=table.add_row().cells
    for i,t in enumerate([a,b,c]):
        cells[i].text=t; cells[i].vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
        for run in cells[i].paragraphs[0].runs: run.font.size=Pt(8.2)

heading('Analysis and recommendations')
para('The tool compares a capacity ladder, a capacity-versus-transit-distance chart, and a venue table. The displayed score gives 60 points for capacity fit, up to 30 for transit proximity, and 10 for a preferred setting. For a 2,000–3,500 person indoor event, Roadrunner and Wang Theatre are strong first checks because both meet the size range and lie within 500 meters of rapid transit. Leader Bank Pavilion suits summer events that require 5,000 seats, but its longer transit walk and outdoor exposure should remain explicit planning risks. Jordan Hall and Shubert Theatre provide right-sized choices for 1,000–1,500 seated events.')

heading('Uncertainty and limits')
para('Capacity depends on layout, production, seating, and fire-code approval. The transit measure is a straight-line proxy, not walking distance, travel time, service frequency, or accessibility. The data excludes availability, rental quotes, actual ticket demand, satisfaction, neighborhood impacts, weather, and accessibility details. The findings support a first shortlist only. Teams should confirm configuration, availability, accessibility, routes, and costs directly with each venue before booking.')

heading('Sources and reproducibility')
para('Primary venue pages include Agganis Arena, Roadrunner, Boch Center, Leader Bank Pavilion, Citizens House of Blues Boston, and New England Conservatory. MGM Music Hall capacity comes from the City of Boston project presentation. Transit-data context uses MBTA GTFS documentation. Full links, source dates, definitions, and row notes appear in data/venues.csv and on the Site Sources and definitions section.')

doc.save(OUT)
