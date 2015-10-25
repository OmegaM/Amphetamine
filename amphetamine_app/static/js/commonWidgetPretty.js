/**
 * Created by Omega on 15/10/17.
 */


$(document).ready(function () {
    var collapseTestcase = $('#collapseTestCase');

    collapseTestcase.on('hidden.bs.collapse', function () {
        //console.log($("#chevronSpan").attr("class"));
        $("#chevronSpan").attr("class", "glyphicon glyphicon-chevron-down");
    });

    collapseTestcase.on('shown.bs.collapse', function () {
        //console.log($("#chevronSpan").attr("class"));
        $("#chevronSpan").attr("class", "glyphicon glyphicon-chevron-up");
    });


});