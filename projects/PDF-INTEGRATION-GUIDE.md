# PDF Integration Guide for Project Pages

This guide explains how to embed PDF reports directly into your project pages.

## Quick Setup

### 1. Add PDF Files
Place your PDF reports in the `assets/reports/` directory:
```
assets/
├── reports/
│   ├── coastal-vulnerability-report.pdf
│   ├── shallow-landslide-report.pdf
│   ├── garfanana-valley-report.pdf
│   └── transfer-learning-report.pdf
```

### 2. Add PDF Viewer Styles
Add these CSS styles to your project page's `<style>` section:

```css
/* PDF Viewer Styles */
.pdf-viewer-container {
    margin: 3rem 0;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    background: white;
}

.pdf-viewer-header {
    background: linear-gradient(45deg, #2563eb, #7c3aed);
    color: white;
    padding: 1rem 1.5rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.pdf-viewer-header h3 {
    margin: 0;
    font-size: 1.2rem;
    font-weight: 600;
}

.pdf-download-btn {
    background: rgba(255, 255, 255, 0.2);
    color: white;
    border: 1px solid rgba(255, 255, 255, 0.3);
    padding: 0.5rem 1rem;
    border-radius: 6px;
    text-decoration: none;
    font-size: 0.9rem;
    transition: all 0.3s ease;
}

.pdf-download-btn:hover {
    background: rgba(255, 255, 255, 0.3);
    transform: translateY(-1px);
    color: white;
}

.pdf-embed {
    width: 100%;
    height: 600px;
    border: none;
}

/* Mobile responsive */
@media (max-width: 768px) {
    .pdf-embed {
        height: 400px;
    }
    
    .pdf-viewer-header {
        flex-direction: column;
        gap: 1rem;
        text-align: center;
    }
}
```

### 3. Add PDF Viewer Component
Insert this HTML component where you want the PDF to appear:

```html
<!-- PDF Viewer Component -->
<div class="pdf-viewer-container">
    <div class="pdf-viewer-header">
        <h3><i class="fas fa-file-pdf"></i> Project Report Title</h3>
        <a href="../assets/reports/your-report.pdf" class="pdf-download-btn" download>
            <i class="fas fa-download"></i> Download PDF
        </a>
    </div>
    <iframe 
        src="../assets/reports/your-report.pdf#toolbar=1&navpanes=1&scrollbar=1" 
        class="pdf-embed"
        title="Project Report PDF">
    </iframe>
</div>
```

## Examples for Each Project

### Coastal Vulnerability Dashboard
```html
<div class="pdf-viewer-container">
    <div class="pdf-viewer-header">
        <h3><i class="fas fa-file-pdf"></i> Coastal Vulnerability Assessment Report</h3>
        <a href="../assets/reports/coastal-vulnerability-report.pdf" class="pdf-download-btn" download>
            <i class="fas fa-download"></i> Download PDF
        </a>
    </div>
    <iframe 
        src="../assets/reports/coastal-vulnerability-report.pdf#toolbar=1&navpanes=1&scrollbar=1" 
        class="pdf-embed"
        title="Coastal Vulnerability Assessment Report PDF">
    </iframe>
</div>
```

### Shallow Landslide Risk Assessment
```html
<div class="pdf-viewer-container">
    <div class="pdf-viewer-header">
        <h3><i class="fas fa-file-pdf"></i> Shallow Landslide Risk Assessment Report</h3>
        <a href="../assets/reports/shallow-landslide-report.pdf" class="pdf-download-btn" download>
            <i class="fas fa-download"></i> Download PDF
        </a>
    </div>
    <iframe 
        src="../assets/reports/shallow-landslide-report.pdf#toolbar=1&navpanes=1&scrollbar=1" 
        class="pdf-embed"
        title="Shallow Landslide Risk Assessment Report PDF">
    </iframe>
</div>
```

### Garfanana Valley Risk Assessment
```html
<div class="pdf-viewer-container">
    <div class="pdf-viewer-header">
        <h3><i class="fas fa-file-pdf"></i> Garfanana Valley Risk Assessment Report</h3>
        <a href="../assets/reports/garfanana-valley-report.pdf" class="pdf-download-btn" download>
            <i class="fas fa-download"></i> Download PDF
        </a>
    </div>
    <iframe 
        src="../assets/reports/garfanana-valley-report.pdf#toolbar=1&navpanes=1&scrollbar=1" 
        class="pdf-embed"
        title="Garfanana Valley Risk Assessment Report PDF">
    </iframe>
</div>
```

### Transfer Learning in Remote Sensing
```html
<div class="pdf-viewer-container">
    <div class="pdf-viewer-header">
        <h3><i class="fas fa-file-pdf"></i> Transfer Learning Research Report</h3>
        <a href="../assets/reports/transfer-learning-report.pdf" class="pdf-download-btn" download>
            <i class="fas fa-download"></i> Download PDF
        </a>
    </div>
    <iframe 
        src="../assets/reports/transfer-learning-report.pdf#toolbar=1&navpanes=1&scrollbar=1" 
        class="pdf-embed"
        title="Transfer Learning Research Report PDF">
    </iframe>
</div>
```

## Features

### PDF Viewer Features
- **Embedded viewing**: PDFs display directly in the browser
- **Download button**: Users can download the PDF file
- **Responsive design**: Works on desktop and mobile devices
- **Professional styling**: Matches your portfolio design
- **Toolbar controls**: Users can zoom, search, and navigate the PDF

### Browser Compatibility
- **Chrome/Edge**: Full support with toolbar
- **Firefox**: Full support with toolbar
- **Safari**: Full support with toolbar
- **Mobile browsers**: Responsive design with touch controls

## Customization Options

### Change PDF Height
Modify the `.pdf-embed` height in CSS:
```css
.pdf-embed {
    height: 800px; /* Make it taller */
}
```

### Change Header Colors
Modify the gradient in `.pdf-viewer-header`:
```css
.pdf-viewer-header {
    background: linear-gradient(45deg, #059669, #7c3aed); /* Green to purple */
}
```

### Add Multiple PDFs
You can add multiple PDF viewers on the same page:
```html
<!-- First PDF -->
<div class="pdf-viewer-container">
    <!-- PDF content -->
</div>

<!-- Second PDF -->
<div class="pdf-viewer-container">
    <!-- PDF content -->
</div>
```

## Troubleshooting

### PDF Not Loading
1. Check file path is correct
2. Ensure PDF file exists in `assets/reports/`
3. Verify file permissions
4. Check browser console for errors

### PDF Loading Slowly
1. Optimize PDF file size
2. Consider using PDF compression
3. Use CDN hosting for large files

### Mobile Issues
1. Ensure responsive CSS is included
2. Test on different mobile devices
3. Check touch controls work properly

## Best Practices

1. **File naming**: Use descriptive, lowercase names with hyphens
2. **File size**: Keep PDFs under 10MB for better loading
3. **Accessibility**: Include proper titles and alt text
4. **Backup links**: Keep external links as fallbacks
5. **Testing**: Test on multiple browsers and devices 