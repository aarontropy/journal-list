var JLApp = angular.module("JournalList", ['ngCookies', 'restangular'])
    .config(function ($interpolateProvider, RestangularProvider) {
        $interpolateProvider.startSymbol("{[{");
        $interpolateProvider.endSymbol("}]}");

        RestangularProvider.setBaseUrl('/api');
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


JLApp.controller('JLCtrl', function($scope, $http, Restangular) {
    var baseItems = Restangular.all('items');
    // var JListDailyInfo = $resource('/api/d/?d=:date');
    // var JListItem = $resource('api/items/:id', {id: '@id'}, {
    //     get: { method: 'GET' },
    //     save: { method: 'POST' },
    //     update: {method: 'PUT', isArray: false},
    //     create: { method: 'POST' },
    //     destroy: { method: 'DELETE' },
    //     delete: { method: 'DELETE' }
    // });
    // var JListCategory = $resource('api/categories/:id', {id:'@id'});

    $scope.current_date = new moment();
    $scope.JLItems = [];
    $scope.message = "Yo";



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
        Restangular.all('d').getList({d: $scope.current_date.format('YYYYMMDD')}).then(function(catItems) {
            $scope.JLItems = catItems;
        });
    };

    $scope.editItem = function(catIndex, itemIndex) {
        var item = $scope.JLItems[catIndex].items[itemIndex];
        console.log(item);
        baseItems.one(item.id).patch(item);
    };

    $scope.addItem = function(cat) {
        console.log(cat);
        console.log($scope.newItem);
    };

    $scope.addCategory = function() {
        // var cat = JListCategory.get({search: $scope.new_category}, function() {
        //     console.log(cat);
        // });
    };


    // Now get the first set of items
    $scope.getItems();
});

