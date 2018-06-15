app.controller("categoryCtrl", function($scope, $http, $window) {
    var $list_category_url = "/api/v1/categories/";

    $scope.get_list_categories = function() {
        $http.get($list_category_url).then(
            function (data) {
                $scope.list_categories = data.data;
                $scope.categories = data.data.results;
                $scope.total_categories = data.data.count;
            }, function (error_data) {
                console.log('error');
            }
        );
    };
    $scope.get_list_categories();

    $scope.post = function() {
        $scope.error = {
            'create': null
        }
        $http.post($list_category_url, $scope.newcate).then(
            function (data) {
                $scope.success_create = "Create Success category " + data.title;
                $scope.get_list_categories();
            }, function (error_data) {
                $scope.error.create = error_data.data.Exists[0];
                console.log($scope.error.create);
            }
        );
    }

    $scope.errorRemove = function() {

    }

    $scope.errorRemove = function() {
        $scope.error = null;
        $scope.success_create = null;
    };
});
