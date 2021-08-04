// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal, it is i important to handle each event individually
var btn1 = document.getElementById("myBtn1");
var btn2 = document.getElementById("myBtn2");
var btn3 = document.getElementById("myBtn3");
var btn4 = document.getElementById("myBtn4");
var btn5 = document.getElementById("myBtn5");
var btn6 = document.getElementById("myBtn6");
var btn7 = document.getElementById("myBtn7");
var btn8 = document.getElementById("myBtn8");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal
// always checking if the element is clicked, it is import to handle each event individually

btn1.addEventListener("click", () => {
    modal.style.display = "block";
});
btn2.addEventListener("click", () => {
    modal.style.display = "block";
});
btn3.addEventListener("click", () => {
    modal.style.display = "block";
});
btn4.addEventListener("click", () => {
    modal.style.display = "block";
});
btn5.addEventListener("click", () => {
    modal.style.display = "block";
});
btn6.addEventListener("click", () => {
    modal.style.display = "block";
});
btn7.addEventListener("click", () => {
    modal.style.display = "block";
});
btn8.addEventListener("click", () => {
    modal.style.display = "block";
});


// When the user clicks on <span> (x), close the modal
span.onclick = function() {
        modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
        if (event.target === modal) {
        modal.style.display = "none";
    }
}
