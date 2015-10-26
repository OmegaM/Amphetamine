/**
 * Created by Omega on 15/10/26.
 */

$(document).ready(function () {
    function getTree() {
        var defaultData = [
            {
                text: 'Root',
                href: '#parent1',
                tags: ['4'],
                nodes: [{
                    text: '用例维护',
                    href: '#child1',
                    tags: ['2'],
                    nodes: [
                        {
                            text: 'WEB用例维护',
                            id: 'web',
                            href: '#web1',
                            tags: ['0']
                        },
                        {
                            text: 'IOS用例维护',
                            href: '#grandchild2',
                            tags: ['0']
                        },
                        {
                            text: 'Android用例维护',
                            href: '#grandchild2',
                            tags: ['0']
                        }
                    ]
                },
                    {
                        text: '用例查看',
                        href: '#child1',
                        tags: ['2'],
                        nodes: [
                            {
                                text: 'WEB用例查看',
                                href: 'http://www.baidu.com',
                                tags: ['0']
                            },
                            {
                                text: 'IOS用例查看',
                                href: '#grandchild2',
                                tags: ['0']
                            },
                            {
                                text: 'Android用例查看',
                                href: '#grandchild2',
                                tags: ['0']
                            }
                        ]
                    }

                ]
            }
        ];
        return defaultData;
    }

    var frame = $("#myiframe");
    $('#tree').treeview({
        showBorder: false,
        data: getTree(),
        onNodeSelected: function (event, node) {
            alert(node.id);
            if (node.id == 'web') {
                $.get('/show_testcases', function (data) {
                    frame.append(data);
                });
            }
        }
    });


});


