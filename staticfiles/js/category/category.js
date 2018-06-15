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

    $scope.errorRemove = function() {
        $scope.error = null;
    };
});
