/**
 * Created by OmegaMiao on 2015/9/30 0030 16:00.
 */


function updateTestCase(obj) {

    var testCaseObject = Object();
    //找到绑定了点击事件的按钮的td标签的父级元素的父级元素tr
    //为表格的一行
    var tr = $(obj).parent().parent();
    var tds = tr.children("td");
    $(tds).each(function () {
        //过滤掉td子元素中含有a标签和没有name属性的标签
        //this相当于each中的每一项的标签元素
        if (!$(this).find("a").length > 0 && $(this).attr("name")) {
            //取td的name属性的值作为testCaseObject的键,Html的内容作为其值
            testCaseObject[$(this).attr("name")] = $(this).text();
        }
    });

    //console.log(testCaseObject);

    $.post('/update_testcase', testCaseObject, function (results) {
        //console.log(results.messages);
        //警告框HTML代码
        var flashDivSuccessBegin = '<div class="alert alert-success alert-dismissible fade in">' +
            '<button type="button" class="close" data-dismiss="alert">&times;</button>';
        var flashDivFailBegin = '<div class="alert alert-danger alert-dismissible fade in">' +
            '<button type="button" class="close" data-dismiss="alert">&times;</button>';
        var flashDivEnd = '</div>';
        //警告框div对象
        var flashMessageObj = $("#flash_message");

        if (results.status == "success") {
            flashMessageObj.append(
                flashDivSuccessBegin +
                results.messages + flashDivEnd);
        } else {
            flashMessageObj.append(
                flashDivFailBegin +
                results.messages + flashDivEnd);
        }
    });
    return false;
}
