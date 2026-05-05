document.addEventListener("DOMContentLoaded", function() {
    
    // Array of the images you generated
    const bgImages = [
        'media/bg_spirograph/random_30.png',
        'media/bg_spirograph/random_31.png',
        'media/bg_spirograph/random_32.png',
        'media/bg_spirograph/random_33.png',
        'media/bg_spirograph/random_34.png',
        'media/bg_spirograph/random_35.png',
        'media/bg_spirograph/random_36.png',
        'media/bg_spirograph/random_37.png',
        'media/bg_spirograph/random_38.png',
        'media/bg_spirograph/random_39.png'
    ];

    const topLayer = document.getElementById('bg-layer-top');
    const bottomLayer = document.getElementById('bg-layer-bottom');
    
    let currentIndex = 0;
    const holdDuration = 6000; 
    const fadeDuration = 4000; 

    function cycleBackground() {
        let nextIndex = (currentIndex + 1) % bgImages.length;
        topLayer.classList.add('fade-out');

        setTimeout(function() {
            topLayer.src = bgImages[nextIndex];
            topLayer.classList.remove('fade-out');
            
            let upcomingIndex = (nextIndex + 1) % bgImages.length;
            bottomLayer.src = bgImages[upcomingIndex];
            
            currentIndex = nextIndex;

        }, fadeDuration);
    }

    setInterval(cycleBackground, holdDuration);
});