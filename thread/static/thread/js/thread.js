
(function($){

	//http status codes
	var 	HTTP_OK = "success",
		HTTP_NOT_MODIFIED = "notmodified";

	var POLL_INTERVAL = 3000; //3 second poll time

	var 	messageTextArea,
		messageSendButton,
		threadId;

	function createMessage(){
		var text = messageTextArea.val()
		if(text == "") return;

		$.ajax({
			method : "POST",
			url : "api/message",
			contentType: "application/json",
			data: JSON.stringify({
				"threadId" : threadId,
				"messageBody": text
			}),
			success : function(response, status, xhr) {
				redrawMessageList(response);
			},
			error : function(xhr, status, error){
				console.error(status + ' '  + error);
			} 
		});
	}

	function redrawMessageList(messageData){
		messageList.html(messageData);
	}

	function pollMessages(){
		$.ajax({
			method : "GET",
			url : "api/thread/"+threadId+"/messages/"+(Date.now()-POLL_INTERVAL),
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
		threadId 		= $('#threadId').val();
		messageTextArea 	= $('#messageTextArea');
		messageSendButton 	= $('#messageSendButton');
		messageList 		= $('#messageList');
		messageSendButton.click(createMessage);

		//setInterval(pollMessages, POLL_INTERVAL);
	})
})(jQuery);
