let player_btn = document.getElementById('player_btn');
let player_btn_parent = document.getElementById('player_btn_block');
let header = document.getElementById('header');
let navbar_brand = document.getElementsByClassName('navbar-toggler')[0];
let player_btn_bool = false;


function CheckSize() {
    if ($(window).width() > 576 && player_btn_bool == true) {
        player_btn_parent.appendChild(player_btn);
        navbar_brand.removeEventListener('click', toggler_clicked);
        player_btn_bool = false;
    }
    else if ($(window).width() < 576 && player_btn_bool == false) {
        header.insertBefore(player_btn, navbar_brand);
        navbar_brand.addEventListener('click', toggler_clicked);

        player_btn_bool = true;
    }
}

function toggler_clicked() {
    if (navbar_brand.classList[1] !== "collapsed") {
        player_btn.style.display = "none";

    }
    else {
        player_btn.style.display = "flex";
    }

}

CheckSize();
$(window).resize(CheckSize);