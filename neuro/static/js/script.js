let ikona = localStorage.getItem("navbat_list");

if (ikona == null) {
    active("home");
} else {
    active(ikona);
}

let navbar_list = document.getElementsByClassName("navbar_list");

for (var i = 0; navbar_list.length > i; i++) {
    navbar_list[i].addEventListener("click", function () {
        let mode = this.dataset.mode;
        console.log(this.dataset);
        console.log("Option clicked: ", mode);
        setNavSelector(mode);
    });
}

function setNavSelector(mode) {
    console.log("Klikłem", mode);
    active(mode);
}

function active(mode) {
    document.getElementById(mode).classList.add("active");
    localStorage.setItem("navbat_list", mode);
}
