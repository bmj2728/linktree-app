# Linktree App

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Docker Image](https://img.shields.io/docker/pulls/bmj2728/linktree-app.svg)](https://hub.docker.com/r/bmj2728/linktree-app)
[![GitHub Container Registry](https://img.shields.io/badge/GHCR-linktree--app-blue)](https://github.com/bmj2728/linktree-app/pkgs/container/linktree-app)

A self-hosted, customizable link management page similar to Linktree. Create your own personalized landing page with organized links, custom themes, and section headings - all configurable through simple YAML files.

![Linktree App Screenshot](https://via.placeholder.com/800x400?text=Linktree+App+Screenshot)

## Overview

This application provides a clean, customizable single-page website to organize and showcase all your important links. Perfect for social media profiles, portfolios, or any scenario where you need to share multiple links from one location.

### Why Use This?

- **Self-hosted**: Full control over your data and appearance
- **No subscription fees**: Unlike commercial alternatives
- **Customizable**: Multiple themes and easy configuration
- **Docker ready**: Easy deployment across any platform
- **Section organization**: Group links by purpose or category
- **Responsive design**: Looks great on any device

## Features

- **Simple Python Flask server** serving a single page
- **Content configurable via YAML files**
- **Card-like design** for links with icon support
- **Section headings** for organizing links
- **Link descriptions** for additional context
- **Multiple theme options** including Brian Jipson inspired theme
- **Simple theme configuration** without requiring CSS knowledge
- **Custom template support**
- **Docker support** with runtime configuration injection
- **Volume mapping** for config, custom themes, and avatar image

## Quick Start

### Using Docker Compose (Recommended)

1. Clone this repository:
   ```bash
   git clone https://github.com/bmj2728/linktree-app.git
   cd linktree-app
   ```

2. Edit the configuration file in `config/config.yaml` with your information and links

3. Replace `config/avatar.png` with your profile image

4. Run with Docker Compose:
   ```bash
   docker-compose up -d
   ```

5. Access your Linktree page at `http://localhost:5000`

### Using Pre-built Docker Images

Pull and run from Docker Hub:
```bash
docker pull bmj2728/linktree-app:latest
docker run -p 5000:5000 -v /path/to/your/config:/config -v /path/to/your/custom/templates:/templates/custom bmj2728/linktree-app:latest
```

Or from GitHub Container Registry:
```bash
docker pull ghcr.io/bmj2728/linktree-app:latest
docker run -p 5000:5000 -v /path/to/your/config:/config -v /path/to/your/custom/templates:/templates/custom ghcr.io/bmj2728/linktree-app:latest
```

## Project Structure

```
linktree-app/
├── app/
│   ├── app.py              # Main Flask application
│   └── requirements.txt    # Python dependencies
├── config/
│   ├── avatar.png          # User avatar image
│   └── config.yaml         # Main configuration file
├── templates/
│   ├── default/            # Default theme templates
│   │   ├── default_theme_config.yaml
│   │   ├── dark_theme_config.yaml
│   │   ├── minimal_theme_config.yaml
│   │   └── brianjipson_theme_config.yaml
│   └── custom/             # Custom theme templates
│       ├── example_theme_config.yaml  # Example custom template
│       └── README.md       # Documentation for custom templates
├── Dockerfile              # Docker image definition
├── docker-compose.yml      # Docker Compose configuration
└── LICENSE                 # MIT License
```

## Configuration

Edit `config/config.yaml` to customize your linktree page:
- Basic information (title, name, description)
- Theme selection
- Links with icons, sections, and descriptions
- Additional settings

Example configuration:
```yaml
# Basic Information
title: "My Linktree"
name: "John Doe"
description: "Web Developer & Designer"

# Theme Configuration
theme: "brianjipson"  # Using the Brian Jipson inspired theme

# Links with sections
links:
  - title: "Portfolio Website"
    url: "https://example.com/portfolio"
    icon: "fas fa-globe"
    section: "My Projects"
    description: "Check out my latest web development work"
  
  - title: "GitHub"
    url: "https://github.com/johndoe"
    icon: "fab fa-github"
    section: "My Projects"
    description: "View my open source contributions"
```

## Available Themes

The application comes with several pre-configured themes:

| Theme | Description |
|-------|-------------|
| **default** | Clean, minimal design with blue links |
| **dark** | Dark mode theme with light text |
| **minimal** | Ultra-minimalist design with subtle styling |
| **brianjipson** | Dark navy theme with colored card borders, section headings, and descriptions (inspired by linktree.brianjipson.com) |

### Theme Customization

Themes are configured using simple YAML files that don't require any CSS knowledge. You can customize:

- Background and text colors
- Link card styling (colors, borders, shadows)
- Avatar styling
- Container styling
- Animation effects
- Section headings
- Card colors for borders

See `templates/custom/README.md` for detailed instructions on creating custom themes.

## Section Headings

The Brian Jipson inspired theme supports section headings to organize your links. Simply add a `section` property to your links in the config.yaml file:

```yaml
links:
  - title: "GitHub"
    url: "https://github.com/username"
    icon: "fab fa-github"
    section: "My Projects"
    description: "View my open source contributions"
```

## Link Descriptions

You can add descriptions to your links to provide additional context:

```yaml
links:
  - title: "Portfolio"
    url: "https://example.com/portfolio"
    icon: "fas fa-globe"
    description: "Check out my latest web development work"
```

## Docker Deployment Options

### Build and Deploy Locally

1. Build the Docker image:
   ```bash
   docker build -t linktree-app:latest .
   ```

2. Run the container:
   ```bash
   docker run -p 5000:5000 -v $(pwd)/config:/config -v $(pwd)/templates/custom:/templates/custom linktree-app:latest
   ```

### Push to Docker Hub and GitHub Container Registry

1. Build with both tags:
   ```bash
   docker build -t bmj2728/linktree-app:latest -t ghcr.io/bmj2728/linktree-app:latest .
   ```

2. Push to Docker Hub:
   ```bash
   docker push bmj2728/linktree-app:latest
   ```

3. Push to GitHub Container Registry:
   ```bash
   docker push ghcr.io/bmj2728/linktree-app:latest
   ```

## Making Changes

To update your linktree page:
1. Edit the configuration files or themes
2. Restart the container to apply changes:
   ```bash
   docker-compose restart
   ```

No rebuilding of the application or Docker image is required for configuration changes.

## Icon Support

The application supports Font Awesome icons. You can specify icons for each link in your config.yaml file:

```yaml
links:
  - title: "GitHub"
    url: "https://github.com/username"
    icon: "fab fa-github"
```

Visit [Font Awesome](https://fontawesome.com/icons) to browse available icons.

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `CONFIG_PATH` | Path to the configuration file | `/config/config.yaml` |
| `TEMPLATES_PATH` | Path to the templates directory | `/templates` |
| `AVATAR_PATH` | Path to the avatar image | `/config/avatar.png` |

## Contributing

Contributions are welcome! Feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
