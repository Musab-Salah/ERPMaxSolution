var hamburger = document.querySelector(".hamburger");
var wrapper = document.querySelector(".wrapper");
hamburger.addEventListener("click", function () {
  wrapper.classList.toggle("active");
});