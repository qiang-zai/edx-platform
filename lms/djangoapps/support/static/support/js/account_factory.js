(function(define) {
    'use strict';

    define([
        'underscore',
        'support/js/views/enrollment'
    ], function(_, EnrollmentView) {
        return function(options) {
            options = _.extend({el: '.user-account-content'}, options);
            console.log(options);
            return new EnrollmentView(options).render();
        };
    });
}).call(this, define || RequireJS.define);