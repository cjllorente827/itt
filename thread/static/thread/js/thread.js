
(function($){

	var messageTextArea,
		messageSendButton,
		csrfToken,
		threadId;

	function sendMessage(){
		$.ajax({
			method : "POST",
			url : threadId + "/message",
			contentType: "application/json",
			data: JSON.stringify({
				"messageBody": messageTextArea.val()
			}),
			success : function(response, status, xhr) {
				console.debug("Success");
			}
		});
	}

	$(function() {
		threadId 			= $('#threadId').val();
		messageTextArea 	= $('#message');
		messageSendButton 	= $('#messageSend');
		messageSendButton.click(sendMessage);
	})
})(jQuery);
