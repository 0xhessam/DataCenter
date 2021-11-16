javascript: pswd={
"192.168.X.X":"PASSWORD",
"192.168.X.X":"PASSWORD"};
document.getElementById("appFrame").contentWindow.document.getElementById("usernameInput").value="Administrator";
document.getElementById("appFrame").contentWindow.document.getElementById("passwordInput").value=pswd[document.URL.slice(document.URL.indexOf("//")+2,-1)];
document.getElementById("appFrame").contentWindow.document.getElementById("ID_LOGON").click();

#For One password You can Use This: 

javascript: 
document.getElementById("appFrame").contentWindow.document.getElementById("usernameInput").value="Administrator";
document.getElementById("appFrame").contentWindow.document.getElementById("passwordInput").value="adminpassword";
document.getElementById("appFrame").contentWindow.document.getElementById("ID_LOGON").click();
