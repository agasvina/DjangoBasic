angular.module('todoList', [])
  .component('todoList', {
  templateUrl:'/api/templates/todo-list.html',
  controller: ['$scope', '$http', '$cookies','$location', function($scope, $http, $cookies, $location) {    
    var todoListUrl = "/api/todo/"

    var tokenExists = $cookies.get("token")

    $scope.todo = {};
    $scope.newTodo = {}

    $scope.getTodo = function() {
      var requestConfig = {
        method : "GET",
        url: todoListUrl,
        headers: {
          "Authorization": "JWT " + $cookies.get("token")
        }
      }

      var requestAction = $http(requestConfig)
      requestAction.success(function(r_data, r_status, r_headers, r_config){
        $scope.todos = r_data

      })
      requestAction.error(function(r_data, r_status, r_headers, r_config){
      })
    }

    $scope.doSave = function(todo){
      var requestConfig = {
        method : "PUT",
        url: todo.url+"edit/",
        headers: {
          "Authorization": "JWT " + $cookies.get("token")
        },
        data : {
          "todo": todo.todo,
          "completed": todo.completed
        }
      }

      var requestAction = $http(requestConfig)
      requestAction.success(function(r_data, r_status, r_headers, r_config){
        console.log(r_data)

      })
      requestAction.error(function(r_data, r_status, r_headers, r_config){
      })
    }


    $scope.doCreate = function(){
      $scope.verifyToken()
      var requestConfig = {
        method : "POST",
        url: todoListUrl+"create/",
        headers: {
          "Authorization": "JWT " + $cookies.get("token")
        },
        data : {
          "todo": $scope.newTodo.todo,
          "category": $scope.newTodo.category
        }
      }

      var requestAction = $http(requestConfig)
      requestAction.success(function(r_data, r_status, r_headers, r_config){
        $scope.getTodo()
      })
      requestAction.error(function(r_data, r_status, r_headers, r_config){
      })
    }

    $scope.doDelete = function(todo){
      console.log(todo)
      var requestConfig = {
        method : "DELETE",
        url: todo.url+"delete/",
        headers: {
          "Authorization": "JWT " + $cookies.get("token")
        }
      }

      var requestAction = $http(requestConfig)
      requestAction.success(function(r_data, r_status, r_headers, r_config){
          var index = $scope.todos.indexOf(todo);
          $scope.todos.splice(index, 1);   
      })
      requestAction.error(function(r_data, r_status, r_headers, r_config){
      })
    }

    $scope.verifyToken = function() {
      var url = "/api-token-verify/"
      var requestConfig = {
        method : "POST",
        url: url,
        data: {
          "token": $cookies.get("token")
        }
      }
      var requestAction = $http(requestConfig)
      requestAction.success(function(r_data, r_status, r_headers, r_config){
         //TOKEN FINE
      })
      requestAction.error(function(r_data, r_status, r_headers, r_config){
        $location.path("/login")
      })
    }


    if(tokenExists) {
      $scope.getTodo()
    }

  }],
});
