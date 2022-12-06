from pathlib import Path
from ex import process_workbook

# to iterate all spreadsheets in a workbook
path = Path("excelworkbook")
# path.glob()-> returns the generator object
for file in path.glob("*.xlsx"):
    process_workbook(file)

