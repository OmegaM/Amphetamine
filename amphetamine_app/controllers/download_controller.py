#!/Users/Omega/pythonVenv/venv/bin python
# -*- coding:utf-8 -*-


"""
    Amphetamine.app

    Create on 15/10/13 21:21 By OmegaMiao

    download_controller.py
"""

import StringIO
from flask import jsonify, request, make_response
from sqlalchemy.sql import and_
from .. import amphetamine_app, logger, db
from ..models.mian_model import Amphetamine as Amp
from ..utils.excelUtils import ExcelSheet


@amphetamine_app.route('/export_testsuite_xls', methods=['GET'])
def export_testsuite_xls():

    sio = StringIO.StringIO()

    excel_sheet = ExcelSheet('testsuite', 1200, 'Times')
    excel = excel_sheet.get_excel()

    excel_sheet.write_to_sheet(0, 0, u'序号')
    excel_sheet.write_to_sheet(0, 1, u'用例描述')
    excel_sheet.write_to_sheet(0, 2, u'父项')
    excel_sheet.write_to_sheet(0, 3, u'子项')
    excel_sheet.write_to_sheet(0, 4, u'步骤')
    excel_sheet.write_to_sheet(0, 5, u'期望值')

    if request.method == 'GET':
        parent = request.args.get('parent')
        child = request.args.get('child')
        try:
            testsuite_list = db.session.query(
                Amp.element_desc, Amp.parent_desc, Amp.child_desc, Amp.step, Amp.element_value). \
                filter(and_(Amp.parent == parent, Amp.child == child)).order_by(Amp.step).all()
            for index, item in enumerate(testsuite_list):
                index += 1
                excel_sheet.write_to_sheet(index, 0, index)
                excel_sheet.write_to_sheet(index, 1, item.element_desc)
                excel_sheet.write_to_sheet(index, 2, item.parent_desc)
                excel_sheet.write_to_sheet(index, 3, item.child_desc)
                excel_sheet.write_to_sheet(index, 4, item.step)
                excel_sheet.write_to_sheet(index, 5, item.element_value)

            excel.save(sio)
            resp = make_response(sio.getvalue())
            resp.headers['Content-type'] = 'application/vnd.ms-excel'
            resp.headers['Transfer-Encoding'] = 'chucked'
            resp.headers['Content-Disposition'] = 'attachment;filename="TestSuite.xls"'
            return resp
        except Exception, e:
            logger.error("export excel has an error : " + e.message)
            return jsonify({"errorMessage": e.message})
