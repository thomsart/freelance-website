// Nav and arrow effect
let nav = document.querySelector('nav');
let arrow = document.getElementById('arrow');

window.addEventListener('scroll', function(event) {
    let currentPosY = window.scrollY;
    if (currentPosY > 50) {
        // nav.style.visibility = "hidden";
        nav.classList.add('navup');
        arrow.classList.add('arrowdown');
    }else{
        nav.classList.remove('navup');
    }
});

document.addEventListener('mouseover', function(event) {
    let mousePosY = event.clientY;
    if(mousePosY < 100) {
        nav.classList.add('navdown');
    }else if(mousePosY > 650) {
        arrow.classList.add('arrowup');
    }else{
        nav.classList.remove('navdown');
        arrow.classList.remove('arrowup');
    };
});


// Skills
let skills = document.querySelectorAll('.skill');

skills.forEach(skill => {
    skill.addEventListener('click', (e) => {
        e.target.classList.add('active');
        for(let i = 0; i < skills.length; i++) {
            if(skills[i] !== e.target) {
                skills[i].classList.remove('active');
            }
        }
    })
})

// Frames Big projects
function slideTexts (texts) {
    let i = 1;
    texts.forEach(text => {
        setTimeout(function() {
            text.style.transform = "translateX(0px)";
            text.style.transition = "transform 0.5s ease-in-out";
        }, i * 500);
        i++;
    })
}

let bigProjects = document.querySelectorAll('.big-project');
    bigProjects.forEach(project => {
    project.addEventListener('mouseover', function() {
        let texts = project.querySelector('.big-project-corp');
        let text = texts.querySelectorAll('.big-project-text-div');
        slideTexts(text);
    })
})

// Small projects
let smallProject = document.querySelectorAll('article');

smallProject.forEach(card => {
    card.addEventListener("mouseover", () => {
        card.classList.remove('leave')
        card.classList.add('enter')
    })
    card.addEventListener("mouseleave", () => {
        card.classList.remove('enter')
        card.classList.add('leave')
    })
})

// Carrousel process
let nbImgText = document.getElementsByClassName("slide");
nbImgText = (nbImgText.length)/2-1;
let img = document.getElementById('slides-img');
let text = document.getElementById('slides-text');
let textImg = document.createElement('img');
let button = document.getElementById('button-carousel');
let frameWidth = text.clientWidth;
let actualImgPos = 0;
let processNb = document.querySelectorAll('.slide-nb');

let i = 0;
processNb[i].classList.add('revealed');
function displayNum () {
        if (i == 5) {i = -1;}
        i += 1;
        processNb[i].classList.add('revealed');
}

button.addEventListener('click', function(event) {
    actualImgPos = actualImgPos + frameWidth;
    if (actualImgPos > (nbImgText * frameWidth)) {
        actualImgPos = 0;
    }
    img.style.transform = "translateX(-" + actualImgPos.toString() + "px)";
    img.style.transition = "transform 1s ease-in-out";
    text.style.transform = "translateY(-" + actualImgPos.toString() + "px)";
    text.style.transition = "transform 1s ease-in-out";

    processNb[i].classList.remove('revealed');
    setTimeout(displayNum, 1500);
});
