function anim() {
	var t= setTimeout(function(){
		$("#01").css({"visibility":"visible"}).addClass("flipInX");
	},0);
	var t= setTimeout(function(){
		$("#02").css({"visibility":"visible"}).addClass("flipInX");
	},150);
	var t= setTimeout(function(){
		$("#03").css({"visibility":"visible"}).addClass("flipInX");
	},300);
}

function rd(r) {
 	location.href=r;
}

