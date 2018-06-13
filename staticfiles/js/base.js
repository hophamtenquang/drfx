var app = angular.module("ProductManager", []);

app.config(['$qProvider', function ($qProvider) {
    $qProvider.errorOnUnhandledRejections(false);
}]);

app.config(function ($interpolateProvider, $httpProvider) {
  $interpolateProvider.startSymbol('{$');
  $interpolateProvider.endSymbol('$}');
});
