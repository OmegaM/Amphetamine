/**
 * Created by OmegaMiao on 2015/9/30 0030 16:00.
 */


function updateTestCase(obj) {
    var aArray = {};
    var tr = $(obj).parent().parent();
    var tds = tr.children("td");
    $(tds).each(function (index) {
        if (!$(this).find("a").length > 0) {
            aArray[index] = $(this).text();
        }
    });
    //console.log(aArray);
    var testCaseObj = $.parseJSON('{' +
        '"id": "' + aArray[0] + '",' +
        '"element_desc": "' + aArray[1] + '", ' +
        '"element_key": "' + aArray[3] + '", ' +
        '"element_value": "' + aArray[4] + '", ' +
        '"step": "' + aArray[6] + '", ' +
        '"child": "' + aArray[7] + '", ' +
        '"child_desc": "' + aArray[8] + '", ' +
        '"parent": "' + aArray[9] + '", ' +
        '"parent_desc": "' + aArray[10] + '", ' +
        '"row": "' + aArray[11] + '"' +
        '}');
    //console.log(testCaseObj);
    $.post('/update_test_case', testCaseObj, function (results) {
        console.log(results.messages);

        var flashDivBegin = '<div class="alert alert-success alert-dismissible fade in">' +
            '<button type="button" class="close" data-dismiss="alert">&times;</button>';

        var flashDivEnd = '</div>';

        if (results.status == "success"){
            $("#flash_message").append(
            flashDivBegin +
            results.messages + flashDivEnd);
        } else {
            $("#flash_message").append(
            flashDivBegin +
            results.messages + flashDivEnd);
        }
    });
    return false;
}