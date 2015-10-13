/**
 * Created by Omega on 15/10/13.
 */


/**
 * Created by OmegaMiao on 2015/9/30 0030 16:00.
 */


$(document).ready(function () {

    var exportTestSuiteButton = $("a[name='exportTestSuiteButton']");

    exportTestSuiteButton.bind("click", function () {

        var obj;
        var tr = $(this).parent().parent();
        var tds = tr.children("td");
        $(tds).each(function () {
            if ($(this).attr("name") == "parent") {
                obj.parent = $(this).text();
                //console.log("parent is : " + parent);
            }
            else if ($(this).attr("name") == "child"){
                obj.child = $(this).text();
                //console.log("child is : " + child);
            }
        });

        $.get('/export_testsuite_xls', {"parent": obj.parent, "child": obj.child});
        return false;
    });




});
