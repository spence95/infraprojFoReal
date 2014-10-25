$(function(){
	if(document.URL == 'localhost:8000'){ 
		document.URL = 'localhost:8000/homepage';
	}
	if(document.URL == 'http://mysite-env-u2fnrdew65.elasticbeanstalk.com'){
		document.URL = 'http://mysite-env-u2fnrdew65.elasticbeanstalk.com/homepage')
	}
})