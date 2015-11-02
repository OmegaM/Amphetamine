/**
 * Created by OmegaMiao on 2015/11/2 0002 11:43.
 */



function validCheckboxIsChecked() {
    var inputCheckboxArray = $("input[name='isRun']");
    var runTestCaseButton = $("#runTestCaseButton");
    var checkedArray = [];
    $(inputCheckboxArray).each(function () {
        if ($(this).prop("checked") == true) {
            checkedArray.push($(this));
        }
    });
    if (checkedArray.length > 0) {
        runTestCaseButton.attr('class', 'btn btn-info btn-lg');
    } else {
        runTestCaseButton.attr('class', 'btn btn-info btn-lg disabled');
    }
    return false;
}