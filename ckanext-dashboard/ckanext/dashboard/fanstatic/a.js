// Enable JavaScript's strict mode. Strict mode catches some common
// programming errors and throws exceptions, prevents some unsafe actions from
// being taken, and disables some confusing and bad JavaScript features.
"use strict";

ckan.module('a', function ($) {
    return{
         initialize: function () {
		function escapeRegExp(str) {
                        return str.replace(/([.*+?^=!:${}()|\[\]\/\\])/g, "\\$1");
                        };
          	function replaceAll(str, find, replace) {
                        return str.replace(new RegExp(escapeRegExp(find), 'g'), replace);
                        }
         
	}
    };
});