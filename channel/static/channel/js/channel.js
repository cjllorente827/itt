currentChannel = 0;
(function($){

	//http status codes
	var HTTP_OK = "success",
		HTTP_NOT_MODIFIED = "notmodified";

	var POLL_INTERVAL = 3000; //3 second poll time

	var messageTextArea,
		messageSendButton;

	function createMessage(){
		var text = messageTextArea.val();
		if(text == "") return;

		$.ajax({
			method : "POST",
			url : "/c/api/message",
			contentType: "application/json",
			data: JSON.stringify({
				"channelId" : currentChannel,
				"messageBody": text
			}),
			success : function(response, status, xhr) {
				messageList.html(response);
				messageTextArea.val('');
			},
			error : function(xhr, status, error){
				console.error(status + ' '  + error);
			} 
		});
	}

	function pollMessages(){
		if(!currentChannel){
			return;
		}
		$.ajax({
			method : "GET",
			url : "http://localhost:8001/c/api/channel/"+currentChannel+"/messages/"+(Date.now()-POLL_INTERVAL),
			success : function(response, status, xhr) {
				console.debug(status);
				if(status == HTTP_OK){
					redrawMessageList(response);
				}
			},
			error : function(xhr, status, error){
				console.error(status + ' '  + error);
			} 
		});
	}

	$(function() {
		messageTextArea 	= $('#messageTextArea');
		messageSendButton 	= $('#messageSendButton');
		messageList 		= $('#messageList');
		messageSendButton.click(createMessage);

		setInterval(pollMessages, POLL_INTERVAL);
	})
})(jQuery);
