var guesses = 3;
var correct = 0;


window.onload = function(){
	if (typeof sessionStorage.getItem("guesses") == 'undefined' || !sessionStorage.getItem("guesses")){
		sessionStorage.setItem("guesses", guesses);
		sessionStorage.setItem("correct", correct);
	}
	document.getElementById("correct_num").innerHTML = sessionStorage.getItem("correct");
	document.getElementById("guesses_num").innerHTML = sessionStorage.getItem("guesses");
};


// tests if the user matched the politician to the tweet, increments stats, and presents a new tweet or the ranking page
function test_match(name_choice){
	tweet_div = document.getElementsByClassName('twitter-tweet')[0]
	if(name_choice === tweet_div.id){
		// give the tweet and choice green border and display "Correct"!
		matched_divs = document.getElementsByName(name_choice)
		change_div_colors_and_text(matched_divs, "#66FF33", "Correct!"); 
		// increment the correct choice by 1 and refresh the page
		sessionStorage.setItem("correct", Number(sessionStorage.getItem("correct")) + 1);
		location.reload();
	}
	else{
		// give the tweet and wrong choice red border and display "Wrong!"
		unmatched_divs = [document.getElementsByName(name_choice)[0], tweet_div]
		change_div_colors_and_text(unmatched_divs, "red", "Wrong!");
		// if user has run out of guesses, redirect to their ranking page
		if (sessionStorage.getItem("guesses") < 2){
			correct = sessionStorage.getItem("correct");
			if (correct < 2){
				ranking("clueless");
			}
			else if (correct < 4){
				ranking("active-voter");
			}
			else if (correct < 5){
				ranking("intern");
			}
			else if (correct < 6){
				ranking("senator");
			}
			else if (correct < 8){
				ranking("vice-president");
			}
			else{
				ranking("president");
			}	
		}
		else{
		// decrement the incorrect choice by 1 and refresh the page
			sessionStorage.setItem("guesses", sessionStorage.getItem("guesses") - 1);
			location.reload();
		}
	}
}


// Changes the tweet and chosen politician div border color and adds text
function change_div_colors_and_text(lst, border_color, text){
	match_text = document.getElementById("match_outcome");
	var clickable_politicians = document.getElementsByClassName('politician');
	// prevents user from clicking on other politicians while next page is loading
	for (var i=0; i < clickable_politicians.length; i++){
   		clickable_politicians[i].onclick = function() {
     	return false;
   		}
   	}
   	// change div border colors
	for (var i=0;i<lst.length;i++){
		lst[i].style.borderColor=border_color;
		lst[i].style.borderWidth="3px";
	};
	match_text.innerHTML = text;
	match_text.style.color = border_color;
}


// Redirects to the specified ranking page
function ranking(rank){
	ranking_str = "/politicotweet/" + rank + "/";			
	return window.location.assign(ranking_str);
}
