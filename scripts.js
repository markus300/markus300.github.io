let index = 0;

function showSlide(n) {
    const slides = document.getElementsByClassName("slide");
    if (n >= slides.length) index = 0;
    if (n < 0) index = slides.length - 1;
    for (let i = 0; i < slides.length; i++) {
        slides[i].style.transform = `translateX(${-index * 100}%)`;
    }
}

function nextSlide() {
    index++;
    showSlide(index);
}

function prevSlide() {
    index--;
    showSlide(index);
}