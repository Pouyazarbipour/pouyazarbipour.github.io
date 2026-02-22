// Simple test to see if JavaScript is running
console.log('Script.js loaded!');

// Multi-line Typing Animation
class MultiLineTypeWriter {
    constructor() {
        this.lines = [
            { id: 'typing-text-1', text: 'hydrology by training,', delay: 1000 },
            { id: 'typing-text-2', text: 'statistics by passion,', delay: 3000 },
            { id: 'typing-text-3', text: 'coding by practice.', delay: 5000 }
        ];
        this.currentLineIndex = 0;
        this.currentCharIndex = 0;
        this.isDeleting = false;
        this.waitTime = 2000;
        this.completedLines = [];
        this.stopped = false;
        this.startTyping();
    }

    // Improved helper to remove any cursor span
    removeCursor(str) {
        return str.replace(/<span[^>]*class=["']cursor["'][^>]*>\|<\/span>/g, '');
    }

    // Get a variable typing speed for a more human feel
    getTypingSpeed(char) {
        // Base random speed between 40ms and 180ms
        let speed = 40 + Math.random() * 140;
        // Add a longer pause after spaces, commas, and periods
        if (char === ' ' || char === ',' || char === '.' || char === '-') {
            speed += 100 + Math.random() * 120;
        }
        return speed;
    }

    startTyping() {
        setTimeout(() => {
            this.typeLine();
        }, this.lines[0].delay);
    }

    typeLine() {
        if (this.stopped) return;
        // Remove cursor from all lines before typing
        this.lines.forEach(line => {
            const el = document.getElementById(line.id);
            if (el) el.innerHTML = this.removeCursor(el.innerHTML);
        });

        const currentLine = this.lines[this.currentLineIndex];
        const element = document.getElementById(currentLine.id);
        if (!element) return;

        let typeSpeed;

        if (this.isDeleting) {
            let text = currentLine.text.substring(0, this.currentCharIndex - 1);
            element.innerHTML = this.removeCursor(text) + '<span class="cursor">|</span>';
            this.currentCharIndex--;
            typeSpeed = 60; // Deleting is always fast
        } else {
            let text = currentLine.text.substring(0, this.currentCharIndex + 1);
            if (this.currentCharIndex < currentLine.text.length) {
                // Always show cursor while typing
                element.innerHTML = this.removeCursor(text) + '<span class="cursor">|</span>';
                // Variable speed for each character
                typeSpeed = this.getTypingSpeed(currentLine.text[this.currentCharIndex]);
            } else {
                // No cursor after finished
                element.textContent = text;
                typeSpeed = 500; // Pause before next line
            }
            this.currentCharIndex++;
        }

        if (!this.isDeleting && this.currentCharIndex === currentLine.text.length) {
            this.completedLines.push(this.currentLineIndex);
            this.isDeleting = false;
            this.currentLineIndex = (this.currentLineIndex + 1);
            this.currentCharIndex = 0;
            // Stop after the last line is typed
            if (this.completedLines.length === this.lines.length) {
                this.stopped = true;
                return;
            }
        }

        setTimeout(() => {
            this.typeLine();
        }, typeSpeed);
    }
}

// Story Embed Toggle
class StoryEmbed {
    constructor() {
        this.toggleBtn = document.getElementById('toggle-embed');
        this.closeBtn = document.getElementById('close-embed');
        this.embedContainer = document.getElementById('story-embed');
        
        this.init();
    }
    
    init() {
        if (this.toggleBtn) {
            this.toggleBtn.addEventListener('click', () => this.showEmbed());
        }
        
        if (this.closeBtn) {
            this.closeBtn.addEventListener('click', () => this.hideEmbed());
        }
        
        // Close embed when clicking outside
        document.addEventListener('click', (e) => {
            if (this.embedContainer && this.embedContainer.style.display !== 'none') {
                if (!this.embedContainer.contains(e.target) && !this.toggleBtn.contains(e.target)) {
                    this.hideEmbed();
                }
            }
        });
        
        // Close embed with Escape key
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && this.embedContainer && this.embedContainer.style.display !== 'none') {
                this.hideEmbed();
            }
        });
    }
    
    showEmbed() {
        if (this.embedContainer) {
            this.embedContainer.style.display = 'block';
            this.toggleBtn.innerHTML = '<i class="fas fa-compress"></i> Hide Embedded Story';
            this.toggleBtn.classList.remove('btn-secondary');
            this.toggleBtn.classList.add('btn-primary');
            
            // Smooth scroll to embed
            this.embedContainer.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    }
    
    hideEmbed() {
        if (this.embedContainer) {
            this.embedContainer.style.display = 'none';
            this.toggleBtn.innerHTML = '<i class="fas fa-expand"></i> Show Embedded Story';
            this.toggleBtn.classList.remove('btn-primary');
            this.toggleBtn.classList.add('btn-secondary');
        }
    }
}

// Initialize typing animation when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM loaded, initializing components...');
    
    // Initialize multi-line typing animation
    new MultiLineTypeWriter();
    
    // Initialize story embed
    new StoryEmbed();
    
    // Remove PhotoCarousel initialization and related code

    // Load and render about.md as markdown in the About section
    fetch('about.md')
      .then(response => response.text())
      .then(text => {
        if (marked && typeof marked.parse === 'function') {
          document.getElementById('about-container').innerHTML = marked.parse(text);
        } else {
          document.getElementById('about-container').textContent = text;
        }
      })
      .catch(err => {
        console.error("Error loading about.md:", err);
      });
      
    console.log('About.md loaded, now setting up EmailJS...');
      
    // EMAILJS SETUP - Add this here
    console.log('=== EMAILJS SETUP STARTING ===');
    console.log('Setting up EmailJS...');
    console.log('EmailJS available:', typeof emailjs);
    console.log('EmailJS object:', emailjs);
    
    // Check if EmailJS is loaded
    if (typeof emailjs === 'undefined') {
        console.error('EmailJS is not loaded!');
        return;
    }
    
    // Initialize EmailJS
    emailjs.init("6l6wMbqUhp1iOrsu2");
    console.log('EmailJS initialized');
    
    const contactForm = document.getElementById('contact-form');
    console.log('Contact form found:', contactForm);
    
    if (contactForm) {
        // Add both form submit and button click listeners
        contactForm.addEventListener('submit', handleFormSubmit);
        
        // Also add a direct click listener to the submit button as backup
        const submitButton = contactForm.querySelector('button[type="submit"]');
        if (submitButton) {
            submitButton.addEventListener('click', function(e) {
                console.log('Submit button clicked!');
                // Don't prevent default here, let the form submit event handle it
            });
        }
        
        console.log('Contact form event listener added');
    } else {
        console.error('Contact form not found!');
    }
});

function handleFormSubmit(e) {
    e.preventDefault();
    console.log('Form submitted!');
    
    // Get form data
    const name = this.querySelector('input[name="user_name"]').value;
    const email = this.querySelector('input[name="user_email"]').value;
    const message = this.querySelector('textarea[name="message"]').value;
    
    console.log('Form data:', { name, email, message });
    
    // Simple validation
    if (!name || !email || !message) {
        alert('Please fill in all fields');
        return;
    }
    
    // Show loading state
    const submitButton = this.querySelector('button[type="submit"]');
    const originalText = submitButton.textContent;
    submitButton.textContent = 'Sending...';
    submitButton.disabled = true;
    
    // Prepare template parameters
    const templateParams = {
        to_name: 'Matt Hatami',
        from_name: name,
        from_email: email,
        message: message,
        reply_to: email
    };
    
    // Send email using EmailJS
    console.log('Sending email with params:', templateParams);
    console.log('EmailJS object:', emailjs);
    console.log('Service ID: service_xi6qi1j');
    console.log('Template ID: template_vjd6iil');
    
    emailjs.send('service_xi6qi1j', 'template_vjd6iil', templateParams)
        .then(function(response) {
            console.log('=== EMAILJS SUCCESS ===');
            console.log('SUCCESS!', response.status, response.text);
            alert('Thank you for your message! I\'ll get back to you soon.');
            this.reset();
        }.bind(this), function(error) {
            console.log('=== EMAILJS FAILED ===');
            console.log('FAILED...', error);
            console.log('Error details:', {
                status: error.status,
                text: error.text,
                user: error.user
            });
            alert('Sorry, there was an error sending your message. Error: ' + error.text + '. Please try again or contact me directly at HatamiMatt@gmail.com');
        })
        .finally(function() {
            // Reset button state
            submitButton.textContent = originalText;
            submitButton.disabled = false;
        });
}

// Typing Animation (keeping for backward compatibility)
class TypeWriter {
    constructor(txtElement, words, wait = 3000) {
        this.txtElement = txtElement;
        this.words = words;
        this.txt = '';
        this.wordIndex = 0;
        this.wait = parseInt(wait, 10);
        this.type();
        this.isDeleting = false;
    }

    type() {
        // Current word
        const current = this.wordIndex % this.words.length;
        const fullTxt = this.words[current];

        // Check if deleting
        if (this.isDeleting) {
            // Remove char
            this.txt = fullTxt.substring(0, this.txt.length - 1);
        } else {
            // Add char
            this.txt = fullTxt.substring(0, this.txt.length + 1);
        }

        // Insert txt into element
        this.txtElement.innerHTML = `<span class="txt">${this.txt}</span>`;

        // Initial Type Speed
        let typeSpeed = 100;

        if (this.isDeleting) {
            typeSpeed /= 2;
        }

        // If word is complete
        if (!this.isDeleting && this.txt === fullTxt) {
            // Make pause at end
            typeSpeed = this.wait;
            // Set delete to true
            this.isDeleting = true;
        } else if (this.isDeleting && this.txt === '') {
            this.isDeleting = false;
            // Move to next word
            this.wordIndex++;
            // Pause before start typing
            typeSpeed = 500;
        }

        setTimeout(() => this.type(), typeSpeed);
    }
}

// Mobile Navigation
const hamburger = document.querySelector('.hamburger');
const navMenu = document.querySelector('.nav-menu');

hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('active');
    navMenu.classList.toggle('active');
});

// Close mobile menu when clicking on a link
document.querySelectorAll('.nav-link').forEach(n => n.addEventListener('click', () => {
    hamburger.classList.remove('active');
    navMenu.classList.remove('active');
}));

// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Intersection Observer for fade-in animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
        }
    });
}, observerOptions);

// Observe all sections for fade-in animation
document.addEventListener('DOMContentLoaded', () => {
    const sections = document.querySelectorAll('section');
    sections.forEach(section => {
        section.classList.add('fade-in');
        observer.observe(section);
    });
});

// Simple test to see if JavaScript is running
console.log('Script.js loaded!');

// Add loading animation
window.addEventListener('load', () => {
    document.body.classList.add('loading');
});

// Parallax effect for hero section
window.addEventListener('scroll', () => {
    const scrolled = window.pageYOffset;
    const hero = document.querySelector('.hero');
    if (hero) {
        const rate = scrolled * -0.5;
        hero.style.transform = `translateY(${rate}px)`;
    }
});

// Add hover effects to work cards
document.addEventListener('DOMContentLoaded', () => {
    const workCards = document.querySelectorAll('.work-card');
    workCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px) scale(1.02)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });
});

// Add click effects to buttons
document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(button => {
        button.addEventListener('click', function(e) {
            // Create ripple effect
            const ripple = document.createElement('span');
            const rect = this.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            const x = e.clientX - rect.left - size / 2;
            const y = e.clientY - rect.top - size / 2;
            
            ripple.style.width = ripple.style.height = size + 'px';
            ripple.style.left = x + 'px';
            ripple.style.top = y + 'px';
            ripple.classList.add('ripple');
            
            this.appendChild(ripple);
            
            setTimeout(() => {
                ripple.remove();
            }, 600);
        });
    });
});

// Add CSS for ripple effect
const style = document.createElement('style');
style.textContent = `
    .btn {
        position: relative;
        overflow: hidden;
    }
    
    .ripple {
        position: absolute;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.3);
        transform: scale(0);
        animation: ripple-animation 0.6s linear;
        pointer-events: none;
    }
    
    @keyframes ripple-animation {
        to {
            transform: scale(4);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// Add scroll progress indicator
document.addEventListener('DOMContentLoaded', () => {
    const progressBar = document.createElement('div');
    progressBar.className = 'scroll-progress';
    progressBar.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 0%;
        height: 3px;
        background: linear-gradient(45deg, #2563eb, #7c3aed);
        z-index: 1001;
        transition: width 0.1s ease;
    `;
    document.body.appendChild(progressBar);
    
    window.addEventListener('scroll', () => {
        const scrolled = (window.scrollY / (document.documentElement.scrollHeight - window.innerHeight)) * 100;
        progressBar.style.width = scrolled + '%';
    });
});

// Add keyboard navigation support
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        // Close mobile menu if open
        hamburger.classList.remove('active');
        navMenu.classList.remove('active');
    }
});

// Add touch support for mobile
let touchStartY = 0;
let touchEndY = 0;

document.addEventListener('touchstart', (e) => {
    touchStartY = e.changedTouches[0].screenY;
});

document.addEventListener('touchend', (e) => {
    touchEndY = e.changedTouches[0].screenY;
    handleSwipe();
});

function handleSwipe() {
    const swipeThreshold = 50;
    const diff = touchStartY - touchEndY;
    
    if (Math.abs(diff) > swipeThreshold) {
        if (diff > 0) {
            // Swipe up - could be used for navigation
            console.log('Swipe up detected');
        } else {
            // Swipe down - could be used for navigation
            console.log('Swipe down detected');
        }
    }
} 

// Add scroll event to toggle .scrolled class on navbar
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    const hero = document.querySelector('.hero');
    if (!navbar || !hero) return;
    const heroRect = hero.getBoundingClientRect();
    if (heroRect.bottom <= 80) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
}); 

// Scroll down arrow button functionality
const scrollDownArrow = document.getElementById('scroll-down-arrow');
if (scrollDownArrow) {
    scrollDownArrow.addEventListener('click', function() {
        const nextSection = document.getElementById('about');
        if (nextSection) {
            nextSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });
} 

// Work Filter System
document.addEventListener('DOMContentLoaded', function() {
    const filterBtns = document.querySelectorAll('.filter-btn');
    const workCards = document.querySelectorAll('.work-card');
    
    filterBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            // Remove active class from all buttons
            filterBtns.forEach(b => b.classList.remove('active'));
            // Add active class to clicked button
            this.classList.add('active');
            
            const filterValue = this.getAttribute('data-filter');
            
            workCards.forEach(card => {
                const cardCategories = card.getAttribute('data-category').split(' ');
                
                if (filterValue === 'all' || cardCategories.includes(filterValue)) {
                    card.classList.remove('hidden');
                } else {
                    card.classList.add('hidden');
                }
            });
        });
    });
}); 