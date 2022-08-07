let player = document.querySelector('#player');
let player_overlay = document.querySelector('#player_overlay');
let previous = document.querySelector('#pre');
let play = document.querySelector('#play');
let play_img = document.querySelector('#play_img');
let next = document.querySelector('#next');
let title = document.querySelector('#title');
let recent_volume = document.querySelector('#volume');
let volume_btn = document.querySelector('#volume_btn');
let volume_img_page = document.querySelectorAll('.volume_img_page');
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
let playing_song_img;
let slider_position = 0.00001;

let player_opened = true;
let timer;
let opacity_now = 0;
let volume_show = 90;
let autoplay = 1;
let index_no = 0;
let Playing_song = false;

let track = document.createElement('audio');
let All_song = JSON.parse(localStorage.getItem('json'));

let sliders = document.getElementsByClassName('duration_slider_page');



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


function fetchAudioFile(callaudio) {
	var requestObj = new Request(callaudio.src, {
		method: 'GET',
		headers: {
			'Accept-Ranges': '1000000000'
		},
		referrerPolicy: 'no-referrer'
	});

	fetch(requestObj).then(function (response) {
		return response;
	}).then(async function (outcome) {
		const blob = await outcome.blob();
		const url = window.URL.createObjectURL(blob);
		callaudio.src = url;
	});
};


function load_track(index_no) {

	clearInterval(timer);
	slider.value = 0;
	Array.from(sliders).forEach(element => {
		element.value = 0;
	});
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

	fetchAudioFile(track);

	track.load();

	timer = setInterval(range_slider, 1000);
}

function check_playing_img_song() {
	playing_song_img = document.querySelectorAll('.playing_song_img');
	active_items = document.querySelectorAll('.active_song_items');

	if (playing_song_img !== null) {
		Array.from(playing_song_img).forEach(element => {
			element.src = String(element.src).replace("pause", "play");
			element.classList.remove('playing_song_img');
		})
	
	}

	if (active_items !== null) {
		active_items.forEach(element => {
			element.classList.remove('active_song_items');
		})
	}
}

function mute_sound() {
	if (track.volume == 0) {
		recent_volume.value = 80;
		volume_show.innerHTML = recent_volume.value;
		track.volume = recent_volume.value / 100;
		volume_img.src = String(volume_img.src).replace("silent", "sound");
		volume_img_page.forEach(element => {
			element.src = String(element.src).replace("silent", "sound");
		});
	}
	else {
		track.volume = 0;
		volume.value = 0;
		volume_show.innerHTML = 0;
		recent_volume.setAttribute('value', '0')
		volume_img.src = String(volume_img.src).replace("sound", "silent");
		volume_img_page.forEach(element => {
			element.src = String(element.src).replace("sound", "silent");
		});
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
	if (slider_position !== 0.00001){
		track.currentTime = slider_position;
		slider_position = 0.00001;
	}
	track.oncanplay = function () {
		track.play();
	}	

	Playing_song = true;
	play_img.src = String(play_img.src).replace("play", "pause");
	check_playing_img_song();
	now_playing = "song_" + (index_no + 1);
	slider_now_playing = "slider_song_" + (index_no + 1);
	volume_now_playing = "volume_song_" + (index_no + 1);
	now_playing = document.querySelectorAll('img[name=' + now_playing + ']');

	playing_song_slider = document.querySelector('input[name=' + slider_now_playing + ']');
	playing_song_volume = document.querySelector('button[name=' + volume_now_playing + ']');
	try {
		Array.from(now_playing).forEach(element => {
			element.src = String(element.src).replace("play", "pause");
			element.classList.add("playing_song_img");
		}); 
		now_playing.id = "playing_song_img";
	}
	catch {
		pass
	}
	try {
		playing_song_slider.classList.add('active_song_items');
		playing_song_volume.classList.add('active_song_items');
	}
	catch {
		//pass
	}
	track.play();
}

function pausesong() {
	track.pause();
	Playing_song = false;
	play_img.src = String(play_img.src).replace("pause", "play");
	check_playing_img_song();
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
		index_no = All_song.length - 1;
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

function change_duration(elem) {
	slider_position = track.duration * (elem.value / 100);
	if (Playing_song == true){
		track.currentTime = slider_position;
	}
	
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
		if (Playing_song == true){
			slider.value = position;
		}
		Array.from(sliders).forEach(element => {
			element.value = position;
		});
	}
	// function will run when the song is over
	if (track.ended) {
		play_img.src = String(play_img.src).replace("pause", "play");
		if (autoplay == 1) {
			next_song();
		}
	}
	
	
}

function song_opener(elem) {
	playing_song_img = document.querySelectorAll('.playing_song_img');
	if (Playing_song == true && playing_song_img !== null && playing_song_img[0].getAttribute("name") == elem.getAttribute("name")) {
		pausesong();
	}
	else {
		index_no = Number(realId(elem.getAttribute("name").replace("song_", ""))) - 1;
		if (player_opened == false) {
			player_open();
		}
		load_track(index_no);
		playsong();
	}
}

function realId(id){
	song = All_song.filter(function(el){
		return el.id === id;
	})
	index = song[0].index;
	return index
}


player_open();

player_btn.onclick = player_open;

load_track(index_no);

