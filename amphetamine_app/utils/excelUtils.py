#!/Users/Omega/pythonVenv/venv/bin python
# -*- coding:utf-8 -*-


"""
    Amphetamine.app

    Create on 15/10/17 10:24 By OmegaMiao

    excelUtils.py
"""


import xlwt


class Excel(object):

    def __init__(self):
        self.excel = xlwt.Workbook(encoding='utf-8')
        self.__sheet = None

    def create_sheet(self, sheet_name, col_width):
        self.__sheet = self.excel.add_sheet(sheet_name, cell_overwrite_ok=True)
        self.__sheet.col(0).width = col_width

        return self.__sheet

    def save(self, filename_or_stream):
        self.excel.save(filename_or_stream)


class Style(object):

    def __init__(self, font_name, is_bold=False):
        self.__style = xlwt.XFStyle()
        self.__font = xlwt.Font()
        self.__font.name = font_name
        self.__font.bold = is_bold
        self.__style.font = self.__font

    def create_style(self):
        return self.__style
