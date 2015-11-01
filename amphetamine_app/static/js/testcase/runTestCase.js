/**
 * Created by Omega on 15/10/16.
 */


$(document).ready(function () {
    var inputCheckboxs = $("input[name='isRun']");
    var testCaseArray = new Array();

    $("#runTestCaseButton").bind('click', function () {
        //console.log(inputCheckboxs);
        $(inputCheckboxs).each(function () {

            if ($(this).attr("name") == 'isRun' && $(this).prop("checked") == true) {
                //console.log("hint");
                //下面由于添加了checkbox的父级标签label所以使用三个parent找到testSuiteTr
                var tr = $(this).parent().parent().parent("tr[class='testCaseTr']");
                //console.log(tr);
                $(tr.children("td")).each(function () {
                    if ($(this).attr("class") == 'testCaseId') {
                        console.log($(this).text());
                        testCaseArray.push($(this).text());
                    }
                });
            }
        });


        $.ajax({
            type: 'POST',
            url: '/run_testcase',
            data: JSON.stringify({runTestCaseArray: testCaseArray}),
            contentType: 'application/json;charset=UTF-8'
        });
        console.log(testCaseArray);
        //下面清空数组以完成初始化
        testCaseArray.length = 0;
        return false;
    });
});