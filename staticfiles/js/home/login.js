app.controller("loginCtrl", function($scope, $http, $window) {
    var $login_url = "/api/v1/rest-auth/login/";
    var $home_url = '/home'
    $scope.login = function() {
      $scope.login_data = {
          'username': $scope.username,
          'password': $scope.pass
      };
      $http.post($login_url, $scope.login_data).then(function (data) {
          // TODO
          $window.location.href = $home_url;
      }), (function (error_data) {
          $scope.error = error_data.non_field_errors;
      });
    };
});
