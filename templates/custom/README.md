# Custom Templates Guide

This document explains how to create and use custom templates for the Linktree application.

## Overview

Custom templates allow you to personalize the appearance of your Linktree page beyond the default themes. Templates are defined in YAML files and use a simple configuration format that doesn't require any CSS knowledge.

## Creating a Custom Template

1. Create a new YAML file in the `/templates/custom/` directory
2. Name your file with a descriptive name (e.g., `mytheme_theme_config.yaml`)
3. Define your template using the format shown below

## Template Format

```yaml
# Basic colors
background_color: "#f0f4f8"
container_background: "rgba(255, 255, 255, 0.9)"
text_color: "#2d3748"
description_color: "#4a5568"

# Link styling
link_style:
  background_color: "#4299e1"
  text_color: "#ffffff"
  border_radius: "10px"
  border: "none"
  shadow: true
  hover:
    transform: true
    background_color: "#3182ce"
    shadow_increase: true

# Card styling
card_style:
  padding: "16px 20px"
  margin_bottom: "14px"
  display_icon: true
  icon_position: "left"

# Avatar styling
avatar_style:
  size: "130px"
  border: "4px solid #fff"
  shadow: true

# Container styling
container_style:
  max_width: "600px"
  padding: "35px 25px"
  border_radius: "15px"
  shadow: true
  backdrop_filter: true

# Animation
animations:
  link_hover: true
  page_load: true
```

## Configuration Options

### Basic Colors
- `background_color`: Page background color
- `container_background`: Main container background color
- `text_color`: Main text color
- `description_color`: Description text color

### Link Styling
- `link_style.background_color`: Background color of link cards
- `link_style.text_color`: Text color of links
- `link_style.border_radius`: Rounded corners of link cards
- `link_style.border`: Border style for link cards
- `link_style.shadow`: Whether to add shadow to link cards
- `link_style.hover.transform`: Whether links move up slightly on hover
- `link_style.hover.background_color`: Background color change on hover
- `link_style.hover.shadow_increase`: Whether shadow increases on hover

### Card Styling
- `card_style.padding`: Internal padding of link cards
- `card_style.margin_bottom`: Space between link cards
- `card_style.display_icon`: Whether to show icons in link cards
- `card_style.icon_position`: Position of icons (left or right)

### Avatar Styling
- `avatar_style.size`: Size of the avatar image
- `avatar_style.border`: Border style for avatar
- `avatar_style.shadow`: Whether to add shadow to avatar

### Container Styling
- `container_style.max_width`: Maximum width of the main container
- `container_style.padding`: Internal padding of the main container
- `container_style.border_radius`: Rounded corners of the main container
- `container_style.shadow`: Whether to add shadow to the main container
- `container_style.backdrop_filter`: Whether to add blur effect behind container

### Animation
- `animations.link_hover`: Whether to animate links on hover
- `animations.page_load`: Whether to add fade-in animations on page load

## Using Your Custom Template

To use your custom template, update your `config.yaml` file and set the `theme` property to the name of your template file (without the _theme_config.yaml extension):

```yaml
# In config.yaml
theme: "mytheme"  # Will use /templates/custom/mytheme_theme_config.yaml
```

The application will automatically look for your template in the custom templates directory.

## Example

See the included `example_theme_config.yaml` in the custom templates directory for a complete example of a custom template.

## Tips

- Use color picker tools to find hex color codes
- Test your template with different content lengths
- Consider enabling icons for a more professional look
- Use animations sparingly for the best user experience
