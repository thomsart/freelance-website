let form = document.getElementById("contactForm");
let email = document.getElementById("emailValue");
let job = document.getElementById("jobValue");

form.addEventListener("submit", function(e) {


    email.classList.remove('empty');
    job.classList.remove('empty');

    if (email.value == "") {
        email.classList.add('empty');
    }
    if (job.value == "") {
        job.classList.add('empty');
    }
    if (email.value != "" && job.value != "") {
        form.setAttribute("method", "post");
        form.setAttribute("action", "/contact");
    }
})