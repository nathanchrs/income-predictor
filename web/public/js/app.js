var app = new Vue({
	  el: '#app',
	  data: {
	    age: "?",
	    workclass: "?",
	    fnlwgt: "?",
	    education: "?",
	    education_num: "?",
	    marital_status: "?",
	    occupation: "?",
	    relationship: "?",
	    race: "?",
	    sex: "?",
	    capital_gain: "?",
	    capital_loss: "?",
	    hours_per_week: "?",
	    native_country: "?",

      },       
      methods: {         
      	getData: function() {             
      		return [this.age, this.workclass, this.fnlwgt, this.education, this.education_num,
      				this.marital_status, this.occupation, this.relationship, this.race, this.sex, this.capital_gain, 
      				this.capital_loss, this.hours_per_week, this.native_country]         
      	},

      	postData: function() {
      		$('.ui.basic.modal').modal('show')
      		dataSend = JSON.stringify(this.getData());
      		console.log(dataSend);
      		$.ajax({
			    url        : "predict",
			    dataType   : 'json',
			    contentType: 'application/json; charset=UTF-8', // This is the money shot
			    data       : dataSend,
			    type       : 'POST',
			    complete   : function (data) {
			    	console.log(data)
			    } // etc
			});
	  	}
	  }
})