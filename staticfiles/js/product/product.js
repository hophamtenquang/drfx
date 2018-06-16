app.controller("productCtrl", function($scope, $http, $window) {
    var $list_category_url = "/api/v1/categories/";

    $scope.get_list_categories = function() {
        $http.get($list_category_url).then(
            function (data) {
                $scope.list_categories = data.data;
                $scope.categories = data.data.results;
            }, function (error_data) {
                console.log('error');
            }
        );
    };
    $scope.get_list_categories();

    var $list_factory_url = "/api/v1/factories/";

    $scope.get_list_factories = function() {
        $http.get($list_factory_url).then(
            function (data) {
                $scope.list_factories = data.data;
                $scope.factories = data.data.results;
            }, function (error_data) {
                console.log('error');
            }
        );
    };
    $scope.get_list_factories();

    var $list_product_url = "/api/v1/products/all/";

    $scope.newproduct = {
        'code': null,
        'title': null,
        'key': null,
        'category': null,
        'factory': null,
        'description': null

    }

    $scope.post = function() {
        $scope.error = {
            'code': null
        }
        $scope.validate(function () {
            $http.post($list_product_url, $scope.newproduct).then(
            function (data) {
                $scope.success_create = "Create Success product " + data.data.title;
                $scope.get_list_categories();
                $scope.newCate = null;
            }, function (error_data) {
                $scope.error.create = error_data.data.Exists[0];
                console.log($scope.error.create);
            }
        );
        })
    }


    $scope.validate = function (callback) {
        $scope.error = {};
            if (!$scope.newproduct.code) {
                $scope.error.code = "This field is required.";
            }
            if (!$scope.newproduct.title) {
                $scope.error.title = "This field is required.";
            }
            if (!$scope.newproduct.key) {
                $scope.error.key = "This field is required.";
            }
            if (!$scope.newproduct.category) {
                $scope.error.category = "This field is required.";
            }
            if (!$scope.newproduct.factory) {
                $scope.error.factory = "This field is required.";
            }
            if (!$scope.newproduct.description) {
                $scope.error.description = "This field is required.";
            }
            if (angular.equals({}, $scope.error)) {
                if (typeof callback == 'function') { // make sure the callback is a function
                    callback.call(this); // brings the scope to the callback
                }
            }
    }


    $scope.errorRemove = function() {
        $scope.error = null;
        $scope.success_create = null;
    };
});


app.controller("SearchProductCtrl", function($scope, $http, $window) {
    var $list_products_url = "/api/v1/products/all/";

    $scope.get_list_products = function(url) {
        $http.get(url).then(
            function (data) {
                $scope.products = data.data.results;
                $scope.total_products = data.data.count;
            }, function (error_data) {
                console.log('error');
            }
        );
    };

    $scope.category_filter = '-1';
    $scope.factory_filter = '-1';
    $scope.searchText = '';

    var $list_category_url = "/api/v1/categories/";

    $scope.get_list_categories = function() {
        $http.get($list_category_url).then(
            function (data) {
                $scope.list_categories = data.data;
                $scope.categories = data.data.results;
            }, function (error_data) {
                console.log('error');
            }
        );
    };
    $scope.get_list_categories();

    var $list_factory_url = "/api/v1/factories/";

    $scope.get_list_factories = function() {
        $http.get($list_factory_url).then(
            function (data) {
                $scope.list_factories = data.data;
                $scope.factories = data.data.results;
            }, function (error_data) {
                console.log('error');
            }
        );
    };
    $scope.get_list_factories();

    $scope.validate = function (callback) {
        $scope.error = {};
            if (!$scope.newproduct.code) {
                $scope.error.code = "This field is required.";
            }
            if (!$scope.newproduct.title) {
                $scope.error.title = "This field is required.";
            }
            if (!$scope.newproduct.key) {
                $scope.error.key = "This field is required.";
            }
            if (!$scope.newproduct.category) {
                $scope.error.category = "This field is required.";
            }
            if (!$scope.newproduct.factory) {
                $scope.error.factory = "This field is required.";
            }
            if (!$scope.newproduct.description) {
                $scope.error.description = "This field is required.";
            }
            if (angular.equals({}, $scope.error)) {
                if (typeof callback == 'function') { // make sure the callback is a function
                    callback.call(this); // brings the scope to the callback
                }
            }
    }

    var encodeQueryData =  function encodeQueryData(data) {
       return Object.keys(data).map(function(key) {
            return [key, data[key]].map(encodeURIComponent).join("=");
        }).join("&");
    }

    $scope.buildParams = function() {
        params = {
            'category': $scope.category_filter,
            'factory': $scope.factory_filter,
            'searchText': $scope.searchText
        }
        var params_url = encodeQueryData(params)
        var $url = $list_products_url + '?' + params_url;
        return $url;
    };


    var first_url = $scope.buildParams();
    $scope.get_list_products(first_url);

    $scope.log = function() {
      console.log($scope.category_filter, $scope.factory_filter);
      var url = $scope.buildParams();
      $scope.get_list_products(url);
    };

    $scope.errorRemove = function() {
        $scope.error = null;
        $scope.success_create = null;
    };

    $scope.get_current_produtct = function(id) {
        var url = "/api/v1/products/product/" + id +"/"
        $http.get(url).then(
            function (data) {
                $scope.current_product = data.data;
            }, function (error_data) {
                console.log('error');
            }
        );
    }

    $scope.view_product = function (current_index) {
        $scope.current_product_id = $scope.products[current_index]['id'];
        $scope.get_current_produtct($scope.current_product_id);
        document.getElementById("openModal").click();
    }

    $scope.delete_product = function(id) {
        var url = "/api/v1/products/product/" + id +"/"
        $http.delete(url).then(
            function (data) {
               var aaaurl = $scope.buildParams();
                $scope.get_list_products(aaaurl);
            }, function (error_data) {
                console.log('error');
            }
        );
    }

    $scope.del_product = function (current_index) {
        var r = confirm("Are you sure want to delete!");
        if (r == true) {
            current_product_id = $scope.products[current_index]['id'];
            $scope.delete_product(current_product_id);
        }
    }

    $scope.update_product = function() {
        var url = "/api/v1/products/product/" + $scope.current_product_id +"/"
        $http.put(url, $scope.current_product).then(
            function (data) {
                document.getElementById("closeModal").click();
               var aaaurl = $scope.buildParams();
                $scope.get_list_products(aaaurl);
                $scope.get_current_produtct($scope.current_product_id);
            }, function (error_data) {
                console.log('error');
            }
        );
    }

});
