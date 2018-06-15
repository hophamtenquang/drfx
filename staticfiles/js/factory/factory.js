app.controller("factoryCtrl", function($scope, $http, $window) {
    var $list_factory_url = "/api/v1/factories/";

    $scope.get_list_factories = function() {
        $http.get($list_factory_url).then(
            function (data) {
                $scope.list_factories = data.data;
                $scope.factories = data.data.results;
                $scope.total_factories = data.data.count;
            }, function (error_data) {
                console.log('error');
            }
        );
    };
    $scope.get_list_factories();

    $scope.post = function() {
        $scope.error = {
            'create': null
        }
        $http.post($list_factory_url, $scope.newcate).then(
            function (data) {
                $scope.success_create = "Create Success factory " + data.data.title;
                $scope.get_list_factories();
                $scope.newCate = null;
            }, function (error_data) {
                $scope.error = error_data.data;
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
