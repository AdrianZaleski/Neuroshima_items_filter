console.log("It is working");

const list = document.querySelectorAll(".navbar_list");

function activeLink() {
    list.forEach(item => item.classList.remove("active"));
    this.classList.add("active");
}

list.forEach(item => item.addEventListener("click", activeLink));
