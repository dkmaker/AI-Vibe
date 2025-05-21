---
description: Rules for web development demos in the 03-cline examples
globs: ["examples/03-cline/**/*.html", "examples/03-cline/**/*.js", "examples/03-cline/**/*.css"]
tags: ["web-demo", "organization", "best-practices"]
---

# Web Demo Output Organization

When creating web-related files (HTML, CSS, JavaScript) for the examples/03-cline directory:

## Directory Structure

1. **ALWAYS** place these files in the `examples/03-cline/web/` subdirectory
2. **ALWAYS** use the following structure:
   - HTML files in the root of the web directory
   - CSS files in a `css` subdirectory
   - JavaScript files in a `js` subdirectory (unless embedded in HTML)

## Code Quality Standards

1. **ALWAYS** include appropriate comments and documentation in the code:
   - File headers explaining the purpose
   - Function/method documentation
   - Complex logic explanations
2. **ALWAYS** follow these HTML best practices:
   - Use semantic HTML elements
   - Include proper meta tags
   - Ensure accessibility features
3. **ALWAYS** follow these CSS best practices:
   - Use consistent naming conventions
   - Organize properties logically
   - Minimize specificity issues
4. **ALWAYS** follow these JavaScript best practices:
   - Use modern ES6+ syntax where appropriate
   - Avoid global variables
   - Handle errors appropriately

## Rationale

This organization ensures:
- Consistent project structure
- Improved maintainability
- Separation of concerns
- Better code readability
- Easier navigation for developers

By following these rules, all web demos will maintain a professional standard and demonstrate best practices in web development.
