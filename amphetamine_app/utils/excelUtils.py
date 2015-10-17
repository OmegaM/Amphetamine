#!/Users/Omega/pythonVenv/venv/bin python
# -*- coding:utf-8 -*-


"""
    Amphetamine.app

    Create on 15/10/17 10:24 By OmegaMiao

    excelUtils.py
"""


import xlwt


class ExcelSheet(object):

    def __init__(self, sheet_name, col_width, font_name):
        self.sheet_name = sheet_name
        self.excel = xlwt.Workbook(encoding='utf-8')
        self.sheet = self.excel.add_sheet(sheet_name, cell_overwrite_ok=True)
        self.sheet.col(0).width = col_width
        self.style = xlwt.XFStyle()
        self.font = xlwt.Font()
        self.font.name = font_name
        self.style.font = self.font

    def get_excel_object(self):
        return self.excel

    def write_to_sheet(self, row, col, content, style=None):
        if not style:
            self.sheet.write(row, col, content, self.style)
        else:
            self.sheet.write(row, col, content, style)
