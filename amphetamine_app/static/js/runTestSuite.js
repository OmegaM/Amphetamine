/**
 * Created by Omega on 15/10/16.
 */


$(document).ready(function () {
    var inputCheckboxs = $("input[name='isRun']");
    var parentArray = new Array();
    var childArray = new Array();
    var testSuiteObject = Object();
    $("#runTestSuiteButton").bind('click', function () {
        //console.log(inputCheckboxs);
        $(inputCheckboxs).each(function () {

            if ($(this).attr("name") == 'isRun' && $(this).prop("checked") == true){
                console.log("hint");
                var tr = $(this).parent().parent("tr[name='testSuiteTr']");
                //console.log(tr);
                $(tr.children("td")).each(function () {
                    if ($(this).attr("name") == 'parent'){
                        parentArray.push($(this).text());
                    } else if ($(this).attr("name") == 'child'){
                        childArray.push($(this).text());
                    }
                });
            }
        });
        //console.log(parentArray);
        //console.log(childArray);
        testSuiteObject.parentArrays = parentArray;
        testSuiteObject.childArrays = childArray;
        console.log(testSuiteObject.parentArrays);
        console.log(testSuiteObject.childArrays);

        //$.post('/run_testsuite', JSON.stringify({testSuite: testSuiteObject}), function (results){
        //
        //});

        //ajax
        $.ajax({
            type: 'POST',
            url: '/run_testsuite',
            data: JSON.stringify({testSuite: testSuiteObject}),
            contentType: 'application/json;charset=UTF-8'
        });

        //下面清空数组以完成初始化
        parentArray.length = 0;
        childArray.length = 0;
        return false;
    });
});