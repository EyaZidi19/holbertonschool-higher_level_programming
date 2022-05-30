// JavaScript script that fetches and lists the title for all movies by using the URL
jQuery.get("https://swapi-api.hbtn.io/api/films/?format=json", function(data) { 
	$('UL#list_movies').append(...data.results.map(movie => `<li>${movie.title}</li>`));
});
