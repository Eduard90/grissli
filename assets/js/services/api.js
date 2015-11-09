app.factory('API', function($http, $q){

	var basePath = '/chat/api/';

	function makeRequest(verb, uri, data){
		var defer = $q.defer();
		verb = verb.toLowerCase();

		var httpArgs = [basePath + uri];
		if (verb.match(/post|put/)){
			httpArgs.push( data );
		}

		$http[verb].apply(null, httpArgs)
		.success(function(data, status){
			defer.resolve(data);
			// $rootScope.$$phase || $rootScope.$apply();
		})
		.error(function(data, status){
			defer.reject({data: data, status: status});
		});

		return defer.promise;
	}

	return {
		get: function( uri ){
			return makeRequest( 'get', uri );
		}
		,post: function( uri, data ){
			return makeRequest( 'post', uri, data );
		}
		,put: function( uri, data ){
			return makeRequest( 'put', uri, data );
		}
		,delete: function( uri ){
			return makeRequest( 'delete', uri );
		}
	};
});