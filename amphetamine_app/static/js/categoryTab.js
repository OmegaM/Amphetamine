/**
 * Created by Omega on 15/10/24.
 */


$(document).ready(function () {
    var currentTab = $("div[name='currentTab']");
    var aLinkTab = $("a[name='aLinkTab']");
    //var clickme = $("#clickme");
    //var clickText = '<span id="clickText">clickText</span>'
    aLinkTab.bind('click', function () {
        //console.log($(this).attr('href'));
        var queryString = $(this).attr('href');
        currentTab.attr('id', queryString.substring(1));
        console.log(currentTab.attr('id'));
        //console.log(queryString.substring(1, 4));
        //$.get('/show_testcase_by_category/' + queryString.substring(1), function () {
        //
        //});
        //aLinkTab.attr('href', '/show_testcase_by_category/' + queryString.substring(1));
        //aLinkTab.trigger("click");
        //console.log(clickme);
        //console.log($(this).parent().attr('class'));
        //console.log('ending');
        //aLinkTab.parent().attr('class', 'active');
        //clickme.append(clickText);
        //$('#clickText').click();
    });
});