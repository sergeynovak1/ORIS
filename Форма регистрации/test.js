const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-button");
const loginErrorMsg = document.getElementsByClassName("password-form-field");

loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    const password1 = loginForm.password1.value;
    const password2 = loginForm.password2.value;
    const username = loginForm.username.value;
    const phone = loginForm.phone.value;
    const email = loginForm.email.value;
    let kik = 0;
    let res = '';

    if (username.length < 6) {
        if (res.length ===0) {
            res = "Логин слишком короткий";
        } else {
            res += ", " + "Логин слишком короткий"
        }
        loginForm.username.style.borderColor = "red";
    } else {
        loginForm.username.style.borderColor = "blue";
    }
    if (password1.length < 6) {
        if (res.length ===0) {
            res = "Пароль слишком короткий";
        } else {
            res += ", " + "Пароль слишком короткий"
        }
        loginForm.password1.style.borderColor = "red";
    } else {
        loginForm.password1.style.borderColor = "blue";
        kik = 1
    }
    if (kik > 0) {
        if (password1 !== password2) {
            if (res.length ===0) {
                res = "Пароли не совпадают";
            } else {
                res += ", " + "Пароли не совпадают"
            }
            for (let i = 0; i < loginErrorMsg.length; i++) {
                loginErrorMsg[i].style.borderColor = "red";
            }
        } else { for (let i = 0; i < loginErrorMsg.length; i++) {
            loginErrorMsg[i].style.borderColor = "blue";
        }
    }}


    if (!((phone.length === 11 && phone[0] === '8') || (phone.length === 12 && phone.slice(0, 1) === '+'))) {
        if (res.length ===0) {
            res = "Неверный номер телефона";
        } else {
            res += ", " + "Неверный номер телефона";
        }
        loginForm.phone.style.borderColor = "red";
    } else {
        loginForm.phone.style.borderColor = "blue";
    }
    if (!(email.includes('@') && email.length > 5)) {
        if (res.length ===0) {
            res = "Неверный email";
        } else {
            res += ", " + "Неверный email";
        }
        loginForm.email.style.borderColor = "red";
    } else {
        loginForm.email.style.borderColor = "blue";
    }
    if (res.length === 0) {
        alert("Успешная регистрация")
        location.reload();
    } else {
        alert(res);
    }
    })

