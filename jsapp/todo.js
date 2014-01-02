function TodoCtrl($scope) {

    $scope.todos = [
        {text: 'Learn AngualrJS', done:false},
        {text: 'Build an app', done:false}
    ];


    $scope.getTotalTodos = function() {
        return $scope.todos.length;
    };

    $scope.addTodo = function() {
        $scope.todos.push({text:$scope.formTodoText, don:false })
        $scope.formTodoText = '';
    };

}