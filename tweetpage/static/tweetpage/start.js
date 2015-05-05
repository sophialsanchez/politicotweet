window.onload = function(){
	if (typeof sessionStorage.getItem("correct") !== 'undefined' && typeof sessionStorage.getItem("guesses") == 'undefined'){
		sessionStorage.removeItem("guesses");
		sessionStorage.removeItem("correct");
	}
};