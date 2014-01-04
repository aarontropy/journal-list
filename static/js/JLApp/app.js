var JLApp = angular.module("JournalList", ['ngCookies', 'restangular'])
    .config(function ($interpolateProvider, RestangularProvider) {
        $interpolateProvider.startSymbol("{[{");
        $interpolateProvider.endSymbol("}]}");

        RestangularProvider.setBaseUrl('/api');
        RestangularProvider.setRequestSuffix('/');
});


JLApp.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);


// Awesome directive shamelessly stolen from the similarly awesome EpokK
// https://gist.github.com/EpokK
JLApp.directive('ngEnter', function () {
    return function (scope, element, attrs) {
        element.bind("keydown keypress", function (event) {
            if(event.which === 13) {
                scope.$apply(function (){
                    scope.$eval(attrs.ngEnter);
                });

                event.preventDefault();
            }
        });
    };
});


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

    $scope.changeDate = function(increment) {
        $scope.current_date.add('d', increment);
        $scope.getItems();
    };

    $scope.getItems = function() {
        Restangular.all('d/').getList({d: $scope.current_date.format('YYYYMMDD')}).then(function(catItems) {
            $scope.JLItems = catItems;
        });
    };

    $scope.editItem = function(catIndex, itemIndex) {
        var item = $scope.JLItems[catIndex].items[itemIndex];
        Restangular.one('items', item.id).get().then(function(ret) {
            ret.item_text = item.item_text;
            ret.put();
        })
    };

    $scope.addItem = function(cat) {
        if (cat.newItem !== undefined && cat.newItem != '') {
            var newItem = {
                item_text: cat.newItem, 
                category: cat.url, 
                pub_date: $scope.current_date.format("YYYY-MM-DD")
            };
            baseItems.post(newItem);
            $scope.getItems();
        }
    };

    $scope.addCategory = function() {
        // var cat = JListCategory.get({search: $scope.new_category}, function() {
        //     console.log(cat);
        // });
    };


    // Now get the first set of items
    $scope.getItems();
});

