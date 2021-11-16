javascript: pswd={
"192.168.X.X:"PASSWORD",
"192.168.X.X":"PASSWORD"};
document.getElementById("appFrame").contentWindow.document.getElementById("username").value="Administrator";
document.getElementById("appFrame").contentWindow.document.getElementById("password").value=pswd[document.URL.slice(document.URL.indexOf("//")+2,-1)];
document.getElementById("appFrame").contentWindow.document.getElementById("login-form__submit").click();


#For One password You can Use This: 

javascript: 
document.getElementById("appFrame").contentWindow.document.getElementById("username").value="Administrator";
document.getElementById("appFrame").contentWindow.document.getElementById("password").value="adminpassword";
document.getElementById("appFrame").contentWindow.document.getElementById("login-form__submit").click();
