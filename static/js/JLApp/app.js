var JLApp = angular.module("JournalList", [], function ($interpolateProvider) {
        $interpolateProvider.startSymbol("{[{");
        $interpolateProvider.endSymbol("}]}");
    }
);


JLApp.controller('JLCtrl', function($scope, $http) {
    $scope.message = "Yo";
    $scope.current_date = new Date();

    $scope.JLItems = [];


    $scope.getDateString = function() {
        return $scope.current_date.toDateString();
    };

    $scope.increaseDate = function() {
        $scope.current_date = new Date($scope.current_date.getTime() + (24*60*60*1000));
        $scope.getItems();
    };

    $scope.decreaseDate = function() {
        $scope.current_date = new Date($scope.current_date.getTime() - (24*60*60*1000));    
        $scope.getItems();
    };

    $scope.getItems = function() {
        var year = $scope.current_date.getFullYear();
        var month = $scope.current_date.getMonth() + 1;
        var day = $scope.current_date.getDate();

        $http.get('/api/d/' + year + '/' + month + '/' + day + '/').
            success(function(data, status, headers, config) {
                $scope.JLItems = data;
            }).
            error(function(data, status, headers, congfig) {
                console.log("ERRR");
                console.log(data);
            });
    }


    // Now get the first set of items
    $scope.getItems();
})