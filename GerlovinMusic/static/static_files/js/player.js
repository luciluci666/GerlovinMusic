let player = document.querySelector('#player');
let player_overlay = document.querySelector('#player_overlay');
let previous = document.querySelector('#pre');
let play = document.querySelector('#play');
let play_img = document.querySelector('#play_img');
let next = document.querySelector('#next');
let title = document.querySelector('#title');
let recent_volume = document.querySelector('#volume');
let volume_btn = document.querySelector('#volume_btn');
let volume_img = document.querySelector('#volume_img');
let slider = document.querySelector('#duration_slider');
let show_duration = document.querySelector('#show_duration');
let track_image = document.querySelector('#track_image');
let auto_play = document.querySelector('#auto');
let present = document.querySelector('#present');
let total = document.querySelector('#total');
let artist = document.querySelector('#artist');
let navbar_toggler = document.querySelector('.navbar-toggler')
let default_image = track_image.src;

let player_opened = true;
let timer;
let opacity_now = 0;
let volume_show = 90;
let autoplay = 1;
let index_no = 0;
let Playing_song = false;

let track = document.createElement('audio');
let All_song = JSON.parse(localStorage.getItem('json'));

function click_listner() {
	player_open();
}
function player_open() {
	if (player_opened == false) {
		player.style = 'display:block !important;';
		player_opened = true;
		player_overlay.addEventListener('click', click_listner);
		navbar_toggler.addEventListener('click', click_listner);
	}
	else {
		player.style = 'display:none !important;';
		player_opened = false;
		player_overlay.removeEventListener('click', click_listner);
		navbar_toggler.removeEventListener('click', click_listner);
	}
}

player_open();

player_btn.onclick = player_open;

function load_track(index_no) {
	clearInterval(timer);
	slider.value = 0;
	song = All_song[index_no];

	track.src = song.path;
	title.innerHTML = song.name;
	if (song.poster !== "") {
		track_image.src = song.poster;
	}
	else {
		track_image.src = default_image;
	}
	artist.innerHTML = "Sergei Gerlovin";
	track.load();

	timer = setInterval(range_slider, 1000);

}

load_track(index_no);

function mute_sound() {
	if (track.volume == 0) {
		recent_volume.value = 80;
		volume_show.innerHTML = recent_volume.value;
		track.volume = recent_volume.value / 100;
		volume_img.src = String(volume_img.src).replace("silent", "sound");;
	}
	else {
		track.volume = 0;
		volume.value = 0;
		volume_show.innerHTML = 0;
		recent_volume.setAttribute('value', '0')
		volume_img.src = String(volume_img.src).replace("sound", "silent");
	}
}

function justplay() {
	if (Playing_song == false) {
		playsong();

	} else {
		pausesong();
	}
}

function playsong() {
	track.play();
	Playing_song = true;
	play_img.src = String(play_img.src).replace("play", "pause");
}

function pausesong() {
	track.pause();
	Playing_song = false;
	play_img.src = String(play_img.src).replace("pause", "play");
}

function next_song() {
	if (index_no < All_song.length - 1) {
		index_no += 1;
		load_track(index_no);
		playsong();

	} else {
		index_no = 0;
		load_track(index_no);
		playsong();
	}
}

function previous_song() {
	if (index_no > 0) {
		index_no -= 1;
		load_track(index_no);
		playsong();

	} else {
		index_no = All_song.length;
		load_track(index_no);
		playsong();
	}
}

function opacity() {
	opacity_now += 0.02;
	recent_volume.style["opacity"] = opacity_now;
	if (opacity_now >= 1) {
		clearInterval(myInterval);
		opacity_now = 0;
	}
}

function volume_open() {
	recent_volume.style["display"] = "block";
	myInterval = setInterval(opacity, 1);

}
function volume_close() {
	recent_volume.style["display"] = "none";
	recent_volume.style["opacity"] = 0;
	clearInterval(myInterval);
	opacity_now = 0;
}

function volume_change() {
	volume_show.innerHTML = recent_volume.value;
	track.volume = recent_volume.value / 100;
	if (track.volume > 0) {
		volume_img.src = String(volume_img.src).replace("silent", "sound");;
	}
	else {
		volume_img.src = String(volume_img.src).replace("sound", "silent");
	}
}

function change_duration() {
	slider_position = track.duration * (slider.value / 100);
	track.currentTime = slider_position;
}

function autoplay_switch() {
	if (autoplay == 1) {
		autoplay = 0;
	} else {
		autoplay = 1;
	}
}

function range_slider() {
	let position = 0;

	// update slider position
	if (!isNaN(track.duration)) {
		position = track.currentTime * (100 / track.duration);
		slider.value = position;

	}
	// function will run when the song is over
	if (track.ended) {
		play_img.src = String(play_img.src).replace("pause", "play");
		if (autoplay == 1) {
			index_no += 1;
			load_track(index_no);
			playsong();
		}
	}
}





