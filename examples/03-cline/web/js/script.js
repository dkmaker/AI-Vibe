/**
 * script.js
 * JavaScript for the Cline Demo Example 2
 * This file is placed in the js subdirectory as specified in the .clinerules
 */

// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Get references to the elements
    const greetingElement = document.getElementById('greeting');
    const changeButton = document.getElementById('changeButton');
    
    // Add click event listener to the button
    changeButton.addEventListener('click', function() {
        // Change the greeting text when the button is clicked
        greetingElement.textContent = 'Hello, World!';
        
        // Optional: Add some animation or style change
        greetingElement.style.color = '#4CAF50';
        
        // Log to console for demonstration
        console.log('Greeting changed to: Hello, World!');
    });
    
    // Log that the script has loaded
    console.log('Script loaded successfully!');
});
