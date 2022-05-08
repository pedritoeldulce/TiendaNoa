// SETUP

// Sets variables to return inner div and images
const carouselSlide = document.querySelector('.carousel-slide');
const carouselImages = document.querySelectorAll('.carousel-slide img');

// Sets variables to return buttons
const prevBtn = document.querySelector('#prevbutton');
const nextBtn = document.querySelector('#nextbutton');

// Creates a counter to track which image we are on
let counter = 1;
// Selects initial width of image so prog knows how much to slide left or right
const size = carouselImages[0].clientWidth;
// Moves carousel back to start with first image instead of clone
carouselSlide.style.transform = 'translateX(' + (-size * counter) + 'px)'; 

// FUNCTIONS

// Add a function to track next button clicks
nextBtn.addEventListener('click', function () {
  // If user reaches end of carousel, stop execution 
  if (counter >= carouselImages.length -1) return;
  carouselSlide.style.transition = 'transform 0.4s ease-in-out';
  // Add 1 to the counter 
  counter++;
  // Move carousel 
  carouselSlide.style.transform = 'translateX(' + (-size * counter) + 'px)';
});

//create function to look for PREV button clicks
prevBtn.addEventListener('click',() => {
  if (counter <= 0) return;
  carouselSlide.style.transition = 'transform 0.4s ease-in-out';
  counter--;
  carouselSlide.style.transform = 'translateX(' + (-size * counter) + 'px)';
});

// This function is triggered after transformation
carouselSlide.addEventListener('transitionend', () => {
  if (carouselImages[counter].id === 'lastClone') {
    // Removes transition effect and translates back to original picture
    carouselSlide.style.transition = 'none';
    // -2 because we have duplicate and first image
    counter = carouselImages.length -2 ;
    carouselSlide.style.transform = 'translateX(' + (-size * counter) + 'px)';
  }
  if (carouselImages[counter].id === 'firstClone') {
    //removes transition effect and translates back to original picture
    carouselSlide.style.transition = 'none';
    //-2 because we have duplicate and first
    counter = carouselImages.length - counter;
    carouselSlide.style.transform = 'translateX(' + (-size * counter) + 'px)';
  }
});
