# Project Pages Guide

This folder contains individual project pages for Matt Hatami's portfolio.

## How to Add a New Project

### 1. Create a New Project Page
1. Copy `project-template.html` and rename it to `your-project-name.html`
2. Replace all placeholder text (marked with CAPS) with your actual content
3. Update the title, meta information, and content

### 2. Update the Main Portfolio
1. Go to `../index.html`
2. Find the Work section
3. Add a new work card with:
   - Appropriate `data-category` attribute for filtering
   - Link to your new project page
   - Correct tags and description

### 3. Template Structure

#### Required Fields to Replace:
- `PROJECT_TITLE` - The main title of your project
- `PROJECT_SUBTITLE` - A brief subtitle
- `PROJECT_CATEGORY` - One of: GIS, Remote Sensing, Coding
- `TECHNOLOGIES_USED` - Technologies, tools, languages used
- `PROJECT_DURATION` - How long the project took
- `YOUR_ROLE` - Your role in the project
- `PROJECT_MAIN_HEADING` - Main content heading
- `PROJECT_DESCRIPTION` - Detailed project description
- `PROJECT_LINK` - Link to live demo or external resource

#### Optional Sections:
- Key Features (bullet points)
- Methodology
- Results
- Additional Information

### 4. File Naming Convention
Use kebab-case for file names:
- `coastal-vulnerability-dashboard.html`
- `webgis-shelter-planning.html`
- `landslide-risk-assessment.html`

### 5. Categories for Filtering
Add appropriate `data-category` attributes to work cards:
- `gis` - GIS projects
- `remote-sensing` - Remote sensing projects
- `coding` - Programming/coding projects
- Multiple categories: `"gis remote-sensing"` (space-separated)

### 6. Styling
The template includes:
- Responsive design
- Back navigation to main portfolio
- Consistent styling with main site
- Project meta information box
- Call-to-action buttons

## Example Project Structure

```html
<!-- In index.html work card -->
<div class="work-card" data-category="gis">
    <div class="work-image">
        <i class="fas fa-chart-line"></i>
    </div>
    <div class="work-content">
        <h3>Your Project Title</h3>
        <p>Brief project description</p>
        <div class="work-tags">
            <span class="tag">Technology 1</span>
            <span class="tag">Technology 2</span>
        </div>
        <a href="projects/your-project-name.html" class="work-link">View Project</a>
    </div>
</div>
```

## Tips
- Keep project descriptions concise but informative
- Use consistent formatting and styling
- Include relevant links to live demos or external resources
- Add appropriate icons for each project type
- Test all links before publishing 