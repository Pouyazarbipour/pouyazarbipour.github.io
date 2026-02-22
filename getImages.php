<?php
// PHP script to discover images in the assets/images folder
// This can be used as an API endpoint for better image discovery

header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');

$config = [
    'folder' => 'assets/images/',
    'extensions' => ['jpeg', 'jpg', 'png', 'webp'],
    'namingPattern' => 'img'
];

$images = [];
$folder = $config['folder'];

if (is_dir($folder)) {
    $files = scandir($folder);
    
    foreach ($files as $file) {
        if ($file === '.' || $file === '..') continue;
        
        $pathInfo = pathinfo($file);
        $extension = strtolower($pathInfo['extension']);
        
        // Check if file matches our naming pattern and has valid extension
        if (in_array($extension, $config['extensions']) && 
            strpos($pathInfo['filename'], $config['namingPattern']) === 0) {
            
            $images[] = $folder . $file;
        }
    }
    
    // Sort images by name to ensure proper order
    sort($images);
}

echo json_encode([
    'success' => true,
    'images' => $images,
    'count' => count($images)
]);
?> 