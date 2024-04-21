let form = document.getElementById("commentForm");
let name_ = document.getElementById("nameValue");
let company = document.getElementById("companyValue");
let comment = document.getElementById("commentValue");

form.addEventListener("submit", function(e) {

    name_.classList.remove('empty');
    company.classList.remove('empty');
    comment.classList.remove('empty');

    if (name_.value == "") {
        e.preventDefault();
        name_.classList.add('empty');
    }
    if (company.value == "") {
        e.preventDefault();
        company.classList.add('empty');
    }
    if (comment.value == "") {
        e.preventDefault();
        comment.classList.add('empty');
    }
    if (name_.value != "" && company.value != "" && comment.value != "") {
        form.setAttribute("action", "/comment");
    }
})