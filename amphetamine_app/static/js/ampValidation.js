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
            element_desc: {
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
            element_key: {
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
            element_value: {
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
            step: {
                validators: {
                    notEmpty: {
                        message: '必填项'
                    },
                    integer: {
                        message: '非整数'
                    }
                }
            },
            child_desc: {
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
            parent_desc: {
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
            row: {
                validators: {
                    notEmpty: {
                        message: '必填项'
                    },
                    integer: {
                        message: '非整数'
                    }
                }
            }
        }
    });
});