var app = new Vue({
	  el: '#app',
	  data: {
	    age: null,
	    workclass: "?",
	    fnlwgt: null,
	    education: "?",
	    education_num: null,
	    marital_status: "?",
	    occupation: "?",
	    relationship: "?",
	    race: "?",
	    sex: "?",
	    capital_gain: null,
	    capital_loss: null,
	    hours_per_week: null,
	    native_country: "?",
	   	view_data: {loading: false, result: ""}
      },       
      methods: {         
      	getData: function() {   
      		var arr = [];
      		for(x in this._data) {
      			if(x != "view_data"){
	      			if(this[x] == null) {
	      				arr.push("?");
	      			} else {
	      				arr.push(this[x]);
	      			}
	      		}
      		}
      		return arr
      	},

      	postData: function() {
      		smoothScroll("#result");
      		this.view_data.loading = true;
      		dataSend = JSON.stringify(this.getData());
      		$.ajax({
			    url        : "predict",
			    dataType   : 'json',
			    contentType: 'application/json; charset=UTF-8', // This is the money shot
			    data       : dataSend,
			    type       : 'POST',
			    complete   : function(response){
			    	if(response.readyState === 4) {
			    		app.view_data.result = response.responseText;
			    		app.view_data.loading = false;
			    	}
			    } // etc
			});
	  	}
	  }
})

$(document).ready(function(){
  // Add smooth scrolling to all links
  $("a").on('click', function(event) {

    // Make sure this.hash has a value before overriding default behavior
    if (this.hash !== "") {
      // Prevent default anchor click behavior
      event.preventDefault();
      smoothScroll(this.hash)
     
    } // End if
  });
});


function smoothScroll(to) {
	 // Store hash
      var hash = to;

      // Using jQuery's animate() method to add smooth page scroll
      // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 800, function(){
   
        // Add hash (#) to URL when done scrolling (default click behavior)
        window.location.hash = hash;
      });
}