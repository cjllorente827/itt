
(function($){

	var messageTextArea,
		messageSendButton,
		csrfToken,
		threadId;

	function sendMessage(){
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
				refresh(response);
			},
			error : function(xhr, status, error){
				console.error(status + ' '  + error);
			} 
		});
	}

	function refresh(messageData){
		messageList.html(messageData);
	}

	$(function() {
		threadId 			= $('#threadId').val();
		messageTextArea 	= $('#message');
		messageSendButton 	= $('#messageSend');
		messageList 		= $('#messageList');
		messageSendButton.click(sendMessage);
	})
})(jQuery);
