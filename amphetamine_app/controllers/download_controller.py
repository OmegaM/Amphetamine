#!/Users/Omega/pythonVenv/venv/bin python
# -*- coding:utf-8 -*-


"""
    Amphetamine.app

    Create on 15/10/13 21:21 By OmegaMiao

    download_controller.py
"""


import xlwt
import StringIO
from flask import jsonify, request, make_response
from sqlalchemy.sql import and_
from .. import amphetamine_app, logger, db
from ..models.mian_model import Amphetamine as Amp


@amphetamine_app.route('/export_testsuite_xls', methods=['GET'])
def export_testsuite_xls():
    wb=xlwt.Workbook()
    wb.encoding='UTF-8'
    ws=wb.add_sheet('1')
    ws.write(0, 0, u'序号')
    ws.write(0,1, u'用例描述')
    ws.write(0,2, u'父项')
    ws.write(0, 3, u'子项')
    ws.write(0, 4, u'步骤')
    ws.write(0, 5, u'期望值')
    sio=StringIO.StringIO()

    if request.method == 'GET':
        parent = request.args.get('parent')
        child = request.args.get('child')
        try:
            testsuite_list = db.session.query(
                Amp.element_desc, Amp.parent_desc, Amp.child_desc, Amp.step, Amp.element_value).\
                filter(and_(Amp.parent == parent, Amp.child == child)).order_by(Amp.step).all()
            for index, item in enumerate(testsuite_list):
                # testsuite_dict[index] = item.element_desc
                ws.write(index +1, 0, index+1)
                ws.write(index + 1, 1, item.element_desc)
                ws.write(index + 1, 2, item.parent_desc)
                ws.write(index + 1, 3, item.child_desc)
                ws.write(index + 1, 4, item.step)
                ws.write(index + 1, 5, item.element_value)

            wb.save(sio)
            resp = make_response(sio.getvalue())
            resp.headers['Content-type'] = 'application/vnd.ms-excel'
            resp.headers['Transfer-Encoding'] = 'chucked'
            resp.headers['Content-Disposition'] = 'attachment;filename="export.xls"'
            return resp
        except Exception, e:
            logger.error("export excel has an error : " + e.message)
            return jsonify({"errorMessage": e.message})
