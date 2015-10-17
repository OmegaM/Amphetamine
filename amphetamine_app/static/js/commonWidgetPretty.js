/**
 * Created by Omega on 15/10/17.
 */


$(document).ready(function () {

    $('#collapseTestCase').on('hidden.bs.collapse', function () {
        console.log($("#chevronSpan").attr("class"));
        $("#chevronSpan").attr("class", "glyphicon glyphicon-chevron-down");
    });

    $('#collapseTestCase').on('shown.bs.collapse', function () {
        console.log($("#chevronSpan").attr("class"));
        $("#chevronSpan").attr("class", "glyphicon glyphicon-chevron-up");
    });


});