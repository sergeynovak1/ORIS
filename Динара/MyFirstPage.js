function checkPassword() {
    const username1 = document.getElementById("username");
    const usernameEntered = username1.value;
    if (usernameEntered.length < 2){
        alert('gf')
        username1.style.borderColor = 'red';
    }
}




// const loginForm = document.getElementById("login-form");
// const loginButton = document.getElementById("login-button");
// const loginErrorMsg = document.getElementsByClassName("password-form-field");

// loginButton.addEventListener("click", (e) => {
//     e.preventDefault();
//     const password = loginForm.password.value;
//     const username = loginForm.username.value;
//     const phone = loginForm.phone.value;
//     const email = loginForm.email.value;
//     const birth = loginForm.birth.value;
//     const login = loginForm.login.value;
//     let flag = 0;
//     let res = '';

//     if (username.length < 6) {
//         alert('ghjk')}
    //     location.reload();
    //     loginForm.login.style.borderColor = "red";1
    // }
    
    // if (!((phone.length === 11 && phone[0] === '8') || (phone.length === 12 && phone.slice(0, 1) === '+'))) {
    //     if (res.length ===0) {
    //         res = "Неверный номер телефона";
    //     }
    //     else {
    //         res += " и " + "Неверный номер телефона";
    //     }
    //     loginForm.phone.style.borderColor = "red";
    //     flag = 1;
    // } else {
    //     loginForm.phone.style.borderColor = "blue";
    //     flag = 0;
    // }
    // if (!(email.includes('@') && email.includes('.', indexOf('@')) && email.length < 5)) {
    //     if (res.length ===0) {
    //         res = "Неверный email";
    //     }
    //     else {
    //         res += " и " + "Неверный email";
    //     }
    //     loginForm.email.style.borderColor = "red";
    //     flag = 1;
    // } else {
    //     loginForm.email.style.borderColor = "blue";
    //     flag = 0;
    // }
    // if (flag === 0) {
    //     if (res.length === 0) {
    //         res = "Регистрация прошла успешно."
    //     }
    //     location.reload();
    // }
    // alert(res);
    // })

// function checkNumber() {
//     let phone = document.getElementById("phoneBox");
//     let phoneEntered = phone.value;
//     if (phoneEntered.lenght > 3) {
//         return true;
//     }
//     else{
//         text.style = "border: 1px solid red;"
//         return false
//     }
    
// }

// let inputs = document.querySelector('input[data-rule]');

// for (let input of inputs) {
//     input.addEventListener('blur', function() {
//         let rule = this.dataset.rule;
//         let value = this.value;
//         let check;

//         switch (rule) {
//             case 'username' :
//                 check = /password.style = "border: 1px solid red;"/.test(value);
//             break;
//         }
//         if (check) {
//             this.classList.add('valid');
//         }
//         else{
//             this.classList.add('invalid');
//         }

//     })
// }