// Configuration file for the personal blog
const CONFIG = {
    // Image settings
    images: {
        folder: 'assets/images/',
        extensions: ['jpeg', 'jpg', 'png', 'webp'],
        namingPattern: 'img', // Images should be named: img1.jpeg, img2.jpeg, etc.
        defaultImage: 'img1.jpeg'
    },
    
    // Carousel settings
    carousel: {
        transitionDuration: 800, // milliseconds
        autoAdvance: false, // Set to true if you want auto-advance later
        autoAdvanceInterval: 8000 // milliseconds
    },
    
    // Typing animation settings
    typing: {
        typeSpeed: 100,
        deleteSpeed: 50,
        waitTime: 2000
    }
};

// Export for use in other files
if (typeof module !== 'undefined' && module.exports) {
    module.exports = CONFIG;
} 