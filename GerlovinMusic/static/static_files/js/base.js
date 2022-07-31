let player_btn = document.getElementById('player_btn');
let player_btn_parent = document.getElementById('player_btn_block');
let header = document.getElementById('header');
let navbar_brand = document.getElementsByClassName('navbar-toggler')[0];
let player_btn_bool = false;
let simple_text = document.querySelector(".simple-text")


function text_decor_height() {
    let text_decoration = document.getElementsByClassName('text_background')[0].childNodes;
    let summa_height = document.querySelector('.container-height').scrollHeight + document.querySelector('.footer').scrollHeight;
    let screenHeight = $(window).height()
    
    if (summa_height  > screenHeight){
        document.querySelector('.footer').style.position = 'static';   
    }
    else{
        document.querySelector('.footer').style.position = 'absolute';
    }
    
    text_decoration.forEach(element => {
        try {
            element.style.height = document.getElementsByTagName('body')[0].scrollHeight + "px";
        }
        catch {
            //pass
        }
    });
}

if (typeof document.getElementsByClassName('text_background')[0] !== "undefined") {
    text_decor_height();
    window.addEventListener('resize', text_decor_height);
}




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

    if ($(window).width() < 992 && typeof simple_text != "undefined"){
        $(simple_text).detach().appendTo(document.querySelector('.our_history'));
    }
    else if($(window).width() > 992 && typeof simple_text != "undefined"){
        $(simple_text).detach().appendTo(document.querySelector('.simple_text_zone'));
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