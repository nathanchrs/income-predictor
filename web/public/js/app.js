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

      },       
      methods: {         
      	getData: function() {   
      		var arr = [];
      		for(x in this._data) {
      			if(this[x] == null) {
      				arr.push("?");
      			} else {
      				arr.push(this[x]);
      			}
      		}
      		return arr
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