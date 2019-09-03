let f_name=document.getElementById("f_name");
let l_name=document.getElementById("l_name");
let email=document.getElementById("email");
let pass=document.getElementById("pass");
let sign_up=document.getElementById("signup");

sign_up.onclick=function(e){
    if (f_name.value==''){
        f_name.focus();
        f_name.style.border='1px solid red';
        e.preventDefault();
    }

    if (l_name.value==''){
        l_name.focus();
        l_name.style.border='1px solid red';
        e.preventDefault();
    }

    if (email.value==''){
        email.focus();
        email.style.border='1px solid red';
        e.preventDefault();
    }

    if (pass.value==''){
        pass.focus();
        pass.style.border='1px solid red';
        e.preventDefault();
    }
}

let username=document.getElementById("username");
let log_pwd=document.getElementById("log_pwd");
let login=document.getElementById("login");

login.onclick=function(e){
    if(log_pwd.value==''){
        log_pwd.focus();
        log_pwd.style.border='1px solid red';
        e.preventDefault();
    }

    if(username.value==''){
        username.focus();
        username.style.border='1px solid red';
        e.preventDefault();
    }
}