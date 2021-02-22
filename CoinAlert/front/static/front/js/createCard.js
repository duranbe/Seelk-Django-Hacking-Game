function createValueAlertCard(data){
 	var newCard = document.createElement("div");
	newCard.className = 'card';
	if(data['when_alert']=='Above'){
		var word = 'above'
	}else{
		var word = 'below'
	}

	if(data['is_activated']){
		var is_checked = 'checked'
	}else{
		var is_checked = ''
	}

	newCard.innerHTML = `
	<div class="card-title">
		<h2> ${data['title']}</h2>  <h5><button class='btn bg-white' id=${data['id']} onClick="deleteAlert(this.id,'value')"><i class="material-icons">delete</i></button></h5>
	</div>
	<p>${data['base_asset']} is ${word} ${Number(data['coin_value']).toLocaleString()} ${data['quote_asset']}<p>
	<div>
		<input type="checkbox" class="regular-checkbox" id="scales" name="scales" ${is_checked}>
		<label>Enabled</label>
	</div>`
 	return(newCard)
 }

function createTimeAlertCard(data){
 	var newCard = document.createElement("div");
	newCard.className = 'card';
	if(data['when_alert']=='Above'){
		var word = 'above'
	}else{
		var word = 'below'
	}

	if(data['is_activated']){
		var is_checked = 'checked'
	}else{
		var is_checked = ''
	}
	newCard.innerHTML = `
	<div class="card-title">
		<h2> ${data['title']}</h2>  <h5><button class='btn bg-white' id=${data['id']} onClick="deleteAlert(this.id,'time')"><i class="material-icons">delete</i></button></h5>
	</div>
	<p>${data['base_asset']} is ${word} ${Number(data['percentage']).toLocaleString()} % ${data['quote_asset']} during the last ${data['time_delta']}<p>
	<div>
		<input type="checkbox" class="regular-checkbox" id="scales" name="scales" ${is_checked}>
		  <label>Enabled</label>
	</div>`
 	return(newCard)
}

function CreateValueAlertCardForm(){
 	const elem = document.getElementById('form-card-container');
 	var newCard = document.createElement("div");
	newCard.className = 'card';
	newCard.innerHTML = `
		<div class="card-title"><h2>Create Value Alert</h2></div>
		<form id="ValueAlertForm">		
			<div>
				<label for="email">Title</label>
			</div>
			<div>
				<input type="text"  size="20" name="title" required>
			</div>
			<div>
				<label for="base_asset">Base Asset</label>
			</div>
			<div>
		    	<input type="text"  name="base_asset" minlength="3" size="10" maxlength="3" required>
		    </div>
		    <div>
				<label for="quote_asset">Quote Asset</label>
			</div>
			<div>
		    	<input type="text" name="quote_asset" minlength="3" size="10" maxlength="3" required>
		    </div>
		    <div>
				<label for="value">Coin Value</label>
			</div>
			<div>
		    	<input type="number"  name="coin_value"  required>
		    </div>
		    <div>
		    	<label for="when">When to trigger</label>
		    </div>
		    <div>
				<select name="when" required>
				    <option value="">--Please choose an option--</option>
				    <option value="ABV">Above</option>
				    <option value="BLW">Below</option>

				</select>
			</div>
		</form>
		<button id="ValueSubmit" onClick="createAlert('value')">Submit</button>`
	elem.append(newCard)
}

function CreateTimeAlertCardForm(){
	const elem = document.getElementById('form-card-container');	
 	var newCard = document.createElement("div");
	newCard.className = 'card';
	newCard.innerHTML = `
		<div class="card-title"><h2>Create Time Alert</h2></div>
		<form id="TimeAlertForm">		
			<div>
				<label for="email">Title</label>
			</div>
			<div>
				<input type="text" size="20" name="title" required>
			</div>
			<div>
				<label for="base_asset">Base Asset</label>
			</div>
			<div>
		    	<input type="text"  name="base_asset" minlength="3" size="10" maxlength="3" required>
		    </div>
		    <div>
				<label for="quote_asset">Quote Asset</label>
			</div>
			<div>
		    	<input type="text"  name="quote_asset" minlength="3" size="10" maxlength="3" required>
		    </div>
		    <div>
				<label for="percentage">Percentage</label>
			</div>
			<div>
		    	<input type="number" name="percentage"  required>
		    </div>
		    <div>
				<label for="time_delta">Time Delta</label>
			</div>
			<div>
		    	<input type="text"  name="time_delta" placeholder="00:00:00:00" required>
		    </div>
		    <div>
		    	<label for="when">When to trigger</label>
		    </div>
		    <div>
				<select name="when">
				    <option value="">--Please choose an option--</option>
				    <option value="ABV">Above</option>
				    <option value="BLW">Below</option>
				</select>
			</div>
		    <button id="TimeSubmit" onClick="createAlert('time')">Send</button>
		</form>`
		elem.append(newCard)
}
function createAlert(AlertType){
		console.log(AlertType)
		if(AlertType == 'value'){
			var Form = document.getElementById('ValueAlertForm');
		}else{
			var Form = document.getElementById('TimeAlertForm');
		}
			
		var formData = new FormData(Form);
		const xhr = new XMLHttpRequest();
		xhr.responseType = "json";
		xhr.open('POST','HTTP://'+window.location.host +'/api/alerts/'+AlertType);
		xhr.setRequestHeader('X-CSRF-Token', csrftoken)
		xhr.setRequestHeader('Authorization','Token '+auth_token)
		xhr.onload = function(){ 
			var response = xhr.response;
		}
		xhr.send(formData);
}