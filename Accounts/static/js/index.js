var count = 0
document.querySelector(".myButton").addEventListener("mouseover",
function() {
    var messageDiv = document.querySelector(".message");
    messageDiv.innerHTML = `Ljlfkb yjdt gjdsljvktyyz ${count}`;
    messageDiv.style.color = "red";
    count += 1;
})