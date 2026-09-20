"""Regenerate offline-compatible website data after editing data/venues.csv."""
from pathlib import Path
import csv,json
root=Path(__file__).resolve().parent
with (root/'data/venues.csv').open(newline='') as f: rows=list(csv.DictReader(f))
for row in rows:
 for key in ['capacity','transit_distance_m','parking_spaces']: row[key]=int(row[key])
 row['capacity_configuration']='Seated' if 'seated' in row['notes'].lower() else 'Other / unspecified'
(root/'data/venues-data.js').write_text('// Generated from venues.csv by build_data.py; do not edit directly.\nwindow.venueData = '+json.dumps(rows,ensure_ascii=False,indent=2)+';\n')
