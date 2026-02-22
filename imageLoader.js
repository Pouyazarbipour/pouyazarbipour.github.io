// Dynamic Image Loader for Photo Carousel
class ImageLoader {
    constructor() {
        this.images = [];
        this.loadedImages = [];
        this.currentIndex = 0;
    }

    // Discover all images in the assets/images folder
    async discoverImages() {
        const { folder, extensions, namingPattern } = CONFIG.images;
        
        // Try to use PHP endpoint first for better performance
        try {
            const response = await fetch('getImages.php');
            if (response.ok) {
                const data = await response.json();
                if (data.success && data.images.length > 0) {
                    this.images = data.images;
                    console.log('Images discovered via PHP endpoint:', this.images);
                    return this.images;
                }
            }
        } catch (error) {
            console.log('PHP endpoint not available, using fallback method');
        }
        
        // Fallback: use client-side detection
        this.images = await this.generateImageList(folder, extensions, namingPattern);
        
        console.log('Images discovered via fallback method:', this.images);
        return this.images;
    }

    // Generate image list based on naming pattern
    async generateImageList(folder, extensions, pattern) {
        const imageList = [];
        let index = 1;
        
        // Try to find images with the naming pattern
        while (index <= 50) { // Limit to prevent infinite loop
            let found = false;
            
            for (const ext of extensions) {
                const imagePath = `${folder}${pattern}${index}.${ext}`;
                // Check if the image exists by trying to load it
                const exists = await this.imageExists(imagePath);
                if (exists) {
                    imageList.push(imagePath);
                    found = true;
                    break;
                }
            }
            
            if (!found) {
                // If we can't find an image with this index, we've probably reached the end
                break;
            }
            
            index++;
        }
        
        return imageList;
    }

    // Check if an image exists by trying to load it
    imageExists(url) {
        return new Promise((resolve) => {
            const img = new Image();
            img.onload = () => resolve(true);
            img.onerror = () => resolve(false);
            img.src = url;
        });
    }

    // Preload images for better performance
    async preloadImages() {
        const loadPromises = this.images.map(imagePath => {
            return new Promise((resolve, reject) => {
                const img = new Image();
                img.onload = () => {
                    this.loadedImages.push(imagePath);
                    resolve(imagePath);
                };
                img.onerror = () => reject(new Error(`Failed to load: ${imagePath}`));
                img.src = imagePath;
            });
        });

        try {
            await Promise.all(loadPromises);
            console.log('All images preloaded successfully');
        } catch (error) {
            console.warn('Some images failed to load:', error);
        }
    }

    // Get current image
    getCurrentImage() {
        return this.images[this.currentIndex] || CONFIG.images.defaultImage;
    }

    // Get next image
    getNextImage() {
        this.currentIndex = (this.currentIndex + 1) % this.images.length;
        return this.getCurrentImage();
    }

    // Get previous image
    getPrevImage() {
        this.currentIndex = this.currentIndex === 0 ? this.images.length - 1 : this.currentIndex - 1;
        return this.getCurrentImage();
    }

    // Go to specific image
    goToImage(index) {
        if (index >= 0 && index < this.images.length) {
            this.currentIndex = index;
        }
        return this.getCurrentImage();
    }

    // Get total number of images
    getImageCount() {
        return this.images.length;
    }

    // Get current index
    getCurrentIndex() {
        return this.currentIndex;
    }
} 