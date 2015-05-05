window.onload = function(){
	if ((typeof sessionStorage.getItem("correct") !== 'undefined') && (typeof sessionStorage.getItem("guesses") !== 'undefined')){
		document.getElementById("correct_num").innerHTML = sessionStorage.getItem("correct");
		sessionStorage.removeItem("guesses");
		sessionStorage.removeItem("correct");
	}
};