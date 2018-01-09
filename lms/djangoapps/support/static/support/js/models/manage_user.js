(function(define) {
    'use strict';
    define(['backbone', 'underscore'], function(Backbone, _) {
        return Backbone.Model.extend({

                initialize: function(options) {
                    this.user = options.user || '';
                    this.baseUrl = options.baseUrl;
                },

                url: function() {
                    return this.baseUrl + this.user;
                },
                disableAccount: function () {
                return $.ajax({
                    url: this.url(),
                    type: 'POST',
                    contentType: 'application/json',
                    data: JSON.stringify({
                        reason: this.get('username')
                    })
                });
                }

        });
    });
}).call(this, define || RequireJS.define);
