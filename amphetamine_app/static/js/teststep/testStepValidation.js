/**
 * Created by Omega on 15/10/1.
 */


$(document).ready(function () {
    $("#addTestStepForm").bootstrapValidator({
        message: 'This value is not valid',
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            pageName: {
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
            pageObjectName: {
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
            step: {
                validators: {
                    notEmpty: {
                        message: '必填项'
                    },
                    Integer: {
                        message: '必须为整数'
                    }
                }
            },
            stepDescription: {
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
            byExpression: {
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
            testData: {
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
            testExpectValue: {
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
            officalData: {
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
            officalExpectValue: {
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