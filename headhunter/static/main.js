window.addEventListener('load', function() {
    let reg_button = $('#register_button');
    let log_button = $('#login_button');
    let register = $('#registerModal');
    let login = $('#loginModal');
    // let form = $('.modal-content');
    reg_button.on('click', function() {
        register[0].style.display = "block";
    });
    log_button.on('click', function() {
        login[0].style.display = "block";
    });
    });

let registerModal = document.getElementById('registerModal')
let closeRegister = document.getElementById('modalRegisterClose')
closeRegister.onclick = function() {
    registerModal.style.display = "none";
  }

let loginModal = document.getElementById('loginModal')
let closeLogin = document.getElementById('closeLogin')
closeLogin.onclick = function() {
    loginModal.style.display = "none";
  }
//         let label = $('.form-label');
//         let mb = $('.mb-3');
//         let btn = $('.btn');
//
//         for(let i=1; i < 7; i++) {
//                 label[i].style.display = "none";
//                 mb[i].style.display = "none";
//             }
//         btn[0].style.display = "none";
//
//         let category_button = $('<input type="submit" class="btn btn-primary btn-sm" id="add-other-fields" value="Выбрать">')
//         form.append(category_button)
//
//         category_button = $('#add-other-fields')
//         category_button.on('click', function(evt) {
//             for(let i=1; i < 7; i++) {
//                 label[i].style.display = "block";
//                 mb[i].style.display = "block";
//             }
//             label[0].style.display = "none";
//                 mb[0].style.display = "none";
//             btn[0].style.display = "block";
//             category_button[0].style.display = "none";
//
//             categ = $('#id_user_category');
//             option = $("select option:selected").val();
//
//             if (option == 'employer'){
//                 $('[for="id_username"]').text('Название компании');
//             }
//         });
//     });
// });