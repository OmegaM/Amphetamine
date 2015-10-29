/**
 * Created by Omega on 15/10/1.
 */


$(document).ready(function () {
    $("#addTestCaseForm").bootstrapValidator({
        message: 'This value is not valid',
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            platform: {
                validators: {
                    notEmpty: {
                        message: '必填项'
                    },
                    stringLength: {
                        min: 1,
                        max: 30,
                        message: '超过字符限制'
                    }
                }
            },
            caseDescription: {
                validators: {
                    notEmpty: {
                        message: '必填项'
                    },
                    stringLength: {
                        min: 1,
                        max: 255,
                        message: '超过字符限制'
                    }
                }
            },
            testSet: {
                validators: {
                    notEmpty: {
                        message: '必填项'
                    },
                    stringLength: {
                        min: 1,
                        max: 30,
                        message: '超过字符限制'
                    }
                }
            },
            projectId: {
                validators: {
                    notEmpty: {
                        message: '必填项'
                    },
                    stringLength: {
                        min: 1,
                        max: 30,
                        message: '超过字符限制'
                    }
                }
            },
            projectName: {
                validators: {
                    notEmpty: {
                        message: '必填项'
                    },
                    stringLength: {
                        min: 1,
                        max: 30,
                        message: '超过字符限制'
                    }
                }

            }
        }
    });
});