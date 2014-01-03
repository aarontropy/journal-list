var JLApp = angular.module("JournalList", ['ngCookies', 'ngResource'], function ($interpolateProvider) {
    $interpolateProvider.startSymbol("{[{");
    $interpolateProvider.endSymbol("}]}");
});


JLApp.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

// $JLItem = JLApp.factory('JLItem', ['$resource', function($resource) {
//     return $resource('api/items/:id/', {}, {
//         get: { method: 'GET' },
//         save: { method: 'PUT' },
//         create: { method: 'POST' },
//         destroy: { method: 'DELETE' },
//         delete: { method: 'DELETE' }
//     });
// }]);


JLApp.controller('JLCtrl', function($scope, $http, $resource) {
    var JListCategory = $resource('/api/d/?d=:date');
    var JListItem = $resource('api/items/:id', {id: '@id'}, {
        get: { method: 'GET' },
        save: { method: 'POST' },
        update: {method: 'PUT', isArray: false},
        create: { method: 'POST' },
        destroy: { method: 'DELETE' },
        delete: { method: 'DELETE' }
    });

    $scope.message = "Yo";
    $scope.current_date = new moment();

    $scope.JLItems = [];


    $scope.getDateString = function() {
        return $scope.current_date.format('MMMM Do YYYY');
    };

    $scope.increaseDate = function() {
        $scope.current_date.add('d', 1);
        $scope.getItems();
    };

    $scope.decreaseDate = function() {
        $scope.current_date.subtract('d', 1);
        $scope.getItems();
    };

    $scope.getItems = function() {
        var items = JListCategory.query({date: $scope.current_date.format('YYYYMMDD')}, function() {
            $scope.JLItems = items;
        })

        // $http.get('/api/d/' + year + '/' + month + '/' + day + '/').
        //     success(function(data, status, headers, config) {
        //         $scope.JLItems = data;
        //     }).
        //     error(function(data, status, headers, congfig) {
        //         console.log("ERRR");
        //         console.log(data);
        //     });
    }

    $scope.test = function(catIndex, itemIndex) {
        var editedItem = new JListItem($scope.JLItems[catIndex].items[itemIndex]);
        editedItem.$update();
        console.log($scope.JLItems[catIndex].items[itemIndex]);
    }


    // Now get the first set of items
    $scope.getItems();
});

