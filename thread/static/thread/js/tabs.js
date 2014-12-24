(function($){

	var main;

	function openTab(threadId){
		$.ajax({
			method : "GET",
			url : "/t/api/thread/"+threadId,
			contentType: "application/json",
			success : function(response, status, xhr) {
				main.html(response);
			},
			error : function(xhr, status, error){
				console.error(status + ' '  + error);
			} 
		});
	}

	$(function() {
		main = $('#main');

		var channels 	= $('#channelsList > p > a');
		for(var c in channels){
			if(channels[c].id){
				channels[c].onclick = function(){
					openTab(this.id.replace('channel_', ''));
				};
			}
		}
	})
})(jQuery);