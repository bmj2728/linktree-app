import os
import yaml
from flask import Flask, render_template_string, send_from_directory
import logging
import random

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Configuration paths for local testing
CONFIG_PATH = os.environ.get('CONFIG_PATH', os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config/config.yaml'))
TEMPLATES_PATH = os.environ.get('TEMPLATES_PATH', os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates'))
DEFAULT_TEMPLATES_PATH = os.path.join(TEMPLATES_PATH, 'default')
CUSTOM_TEMPLATES_PATH = os.path.join(TEMPLATES_PATH, 'custom')
AVATAR_PATH = os.environ.get('AVATAR_PATH', os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config/avatar.png'))

def load_yaml_file(file_path):
    """Load and parse a YAML file."""
    try:
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    except Exception as e:
        logger.error(f"Error loading YAML file {file_path}: {e}")
        return {}

def load_config():
    """Load the configuration from the YAML file."""
    return load_yaml_file(CONFIG_PATH)

def load_theme_config(theme_name):
    """Load the theme configuration based on the theme name."""
    # First check custom templates
    custom_theme_path = os.path.join(CUSTOM_TEMPLATES_PATH, f"{theme_name}_theme_config.yaml")
    if os.path.exists(custom_theme_path):
        return load_yaml_file(custom_theme_path)
    
    # Then check default templates
    default_theme_path = os.path.join(DEFAULT_TEMPLATES_PATH, f"{theme_name}_theme_config.yaml")
    if os.path.exists(default_theme_path):
        return load_yaml_file(default_theme_path)
    
    # Fallback to default theme
    logger.warning(f"Theme {theme_name} not found, using default theme")
    return load_yaml_file(os.path.join(DEFAULT_TEMPLATES_PATH, "default_theme_config.yaml"))

def generate_css_from_theme(theme_config):
    """Generate CSS from theme configuration."""
    # Get card colors for borders
    card_colors = theme_config.get('card_colors', ['#0077cc'])
    
    css = f"""
    * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        font-family: 'Arial', sans-serif;
    }}
    
    body {{
        background-color: {theme_config.get('background_color', '#f5f5f5')};
        color: {theme_config.get('text_color', '#333')};
        line-height: 1.6;
        padding: 20px;
        min-height: 100vh;
    }}
    
    .container {{
        max-width: {theme_config.get('container_style', {}).get('max_width', '600px')};
        margin: 0 auto;
        padding: {theme_config.get('container_style', {}).get('padding', '30px 20px')};
        background-color: {theme_config.get('container_background', '#fff')};
        border-radius: {theme_config.get('container_style', {}).get('border_radius', '10px')};
        {f"box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);" if theme_config.get('container_style', {}).get('shadow', True) else ""}
        text-align: center;
        {f"backdrop-filter: blur(5px);" if theme_config.get('container_style', {}).get('backdrop_filter', False) else ""}
    }}
    
    .profile {{
        margin-bottom: 30px;
    }}
    
    .avatar {{
        width: {theme_config.get('avatar_style', {}).get('size', '120px')};
        height: {theme_config.get('avatar_style', {}).get('size', '120px')};
        border-radius: 50%;
        object-fit: cover;
        margin-bottom: 15px;
        {f"border: {theme_config.get('avatar_style', {}).get('border', '3px solid #fff')};" if theme_config.get('avatar_style', {}).get('border', '') else ""}
        {f"box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);" if theme_config.get('avatar_style', {}).get('shadow', True) else ""}
    }}
    
    h1 {{
        font-size: 24px;
        margin-bottom: 10px;
        color: {theme_config.get('text_color', '#333')};
    }}
    
    p {{
        color: {theme_config.get('description_color', '#666')};
        margin-bottom: 20px;
    }}
    
    .section-heading {{
        font-size: {theme_config.get('section_style', {}).get('font_size', '24px')};
        margin-top: {theme_config.get('section_style', {}).get('margin_top', '40px')};
        margin-bottom: {theme_config.get('section_style', {}).get('margin_bottom', '20px')};
        text-align: {theme_config.get('section_style', {}).get('text_align', 'center')};
        color: {theme_config.get('section_heading_color', theme_config.get('text_color', '#333'))};
        {f"display: none;" if not theme_config.get('section_style', {}).get('display', True) else ""}
    }}
    
    .links {{
        display: flex;
        flex-direction: column;
        gap: {theme_config.get('card_style', {}).get('margin_bottom', '12px')};
    }}
    
    .link-item {{
        display: flex;
        align-items: center;
        padding: {theme_config.get('card_style', {}).get('padding', '14px 20px')};
        background-color: {theme_config.get('link_style', {}).get('background_color', '#0077cc')};
        color: {theme_config.get('link_style', {}).get('text_color', 'white')};
        text-decoration: none;
        border-radius: {theme_config.get('link_style', {}).get('border_radius', '8px')};
        font-weight: 500;
        transition: all 0.2s ease;
        position: relative;
        overflow: hidden;
        text-align: left;
    }}
    
    .link-icon-container {{
        display: flex;
        align-items: center;
        justify-content: center;
        margin-right: 15px;
        {f"display: none;" if not theme_config.get('card_style', {}).get('display_icon', False) else ""}
    }}
    
    .link-icon {{
        font-size: {theme_config.get('card_style', {}).get('icon_size', '18px')};
        color: {theme_config.get('card_style', {}).get('icon_color', 'inherit')};
    }}
    
    .link-content {{
        flex: 1;
    }}
    
    .link-title {{
        font-size: {theme_config.get('card_style', {}).get('title_size', '16px')};
        margin-bottom: 4px;
        color: {theme_config.get('link_style', {}).get('text_color', 'white')};
    }}
    
    .link-description {{
        font-size: {theme_config.get('card_style', {}).get('description_size', '14px')};
        color: {theme_config.get('link_style', {}).get('description_color', 'rgba(255,255,255,0.8)')};
        {f"display: none;" if not theme_config.get('card_style', {}).get('display_description', True) else ""}
    }}
    
    .external-link-icon {{
        position: absolute;
        top: 50%;
        right: 15px;
        transform: translateY(-50%);
        font-size: 14px;
        opacity: 0.7;
        {f"display: none;" if not theme_config.get('card_style', {}).get('external_link_icon', False) else ""}
    }}
    """
    
    # Add card color styles
    for i, color in enumerate(card_colors):
        css += f"""
        .link-item:nth-child({i + 1}n) {{
            border-color: {color};
        }}
        """
    
    # Add hover styles
    css += f"""
    .link-item:hover {{
        {f"background-color: {theme_config.get('link_style', {}).get('hover', {}).get('background_color', '#005fa3')};" if theme_config.get('link_style', {}).get('hover', {}).get('background_color', '') else ""}
        {f"transform: translateY(-2px);" if theme_config.get('link_style', {}).get('hover', {}).get('transform', True) else ""}
        {f"box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);" if theme_config.get('link_style', {}).get('hover', {}).get('shadow_increase', True) and theme_config.get('link_style', {}).get('shadow', True) else ""}
    }}
    """
    
    # Add responsive styles
    css += """
    @media (max-width: 480px) {
        .container {
            padding: 20px 15px;
        }
        
        .avatar {
            width: calc(var(--avatar-size, 120px) * 0.8);
            height: calc(var(--avatar-size, 120px) * 0.8);
        }
        
        .link-title {
            font-size: 16px;
        }
        
        .link-description {
            font-size: 12px;
        }
    }
    """
    
    # Add animations if enabled
    if theme_config.get('animations', {}).get('link_hover', False):
        css += """
        .link-item {
            transition: all 0.3s ease;
        }
        """
    
    if theme_config.get('animations', {}).get('page_load', False):
        css += """
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .container {
            animation: fadeIn 0.8s ease-out;
        }
        
        .section-heading {
            animation: fadeIn 0.5s ease-out forwards;
            animation-delay: 0.2s;
            opacity: 0;
        }
        
        .link-item {
            animation: fadeIn 0.5s ease-out forwards;
            opacity: 0;
        }
        
        .link-item:nth-child(1) { animation-delay: 0.1s; }
        .link-item:nth-child(2) { animation-delay: 0.2s; }
        .link-item:nth-child(3) { animation-delay: 0.3s; }
        .link-item:nth-child(4) { animation-delay: 0.4s; }
        .link-item:nth-child(5) { animation-delay: 0.5s; }
        .link-item:nth-child(6) { animation-delay: 0.6s; }
        .link-item:nth-child(7) { animation-delay: 0.7s; }
        .link-item:nth-child(8) { animation-delay: 0.8s; }
        .link-item:nth-child(9) { animation-delay: 0.9s; }
        .link-item:nth-child(10) { animation-delay: 1.0s; }
        """
    
    # Add footer styles
    css += """
    .footer {
        margin-top: 40px;
        font-size: 12px;
        color: rgba(255, 255, 255, 0.5);
        text-align: center;
    }
    """
    
    return css

def render_page(config, theme_config):
    """Render the page using the configuration and theme."""
    try:
        # Generate CSS from theme configuration
        css_styles = generate_css_from_theme(theme_config)
        
        # Get card colors for borders
        card_colors = theme_config.get('card_colors', ['#0077cc'])
        
        # Build HTML content
        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{config.get('title', 'Linktree')}</title>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
            <style>
                {css_styles}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="profile">
                    <img src="/avatar" alt="{config.get('name', 'User')}" class="avatar">
                    <h1>{config.get('name', 'User')}</h1>
                    <p>{config.get('description', '')}</p>
                </div>
        """
        
        # Group links by section
        sections = {}
        for link in config.get('links', []):
            section = link.get('section', 'default')
            if section not in sections:
                sections[section] = []
            sections[section].append(link)
        
        # Add links by section
        for section_name, section_links in sections.items():
            if section_name != 'default':
                html_content += f"""
                <h2 class="section-heading">{section_name}</h2>
                """
            
            html_content += """
                <div class="links">
            """
            
            # Add links with icons and descriptions
            for i, link in enumerate(section_links):
                icon = link.get('icon', 'fas fa-link')
                description = link.get('description', '')
                color_index = i % len(card_colors)
                border_color = card_colors[color_index]
                
                html_content += f"""
                    <a href="{link.get('url', '#')}" class="link-item" target="_blank" style="border-left: 4px solid {border_color};">
                        <div class="link-icon-container">
                            <i class="{icon} link-icon"></i>
                        </div>
                        <div class="link-content">
                            <div class="link-title">{link.get('title', 'Link')}</div>
                            {f'<div class="link-description">{description}</div>' if description else ''}
                        </div>
                        <i class="fas fa-external-link-alt external-link-icon"></i>
                    </a>
                """
            
            html_content += """
                </div>
            """
        
        # Add footer
        html_content += """
                <div class="footer">
                    © 2025 Self-hosted Linktree Alternative
                </div>
            </div>
        </body>
        </html>
        """
        
        return html_content
    except Exception as e:
        logger.error(f"Error rendering page: {e}")
        return f"<h1>Error rendering page</h1><p>{str(e)}</p>"

@app.route('/')
def index():
    """Serve the main page."""
    config = load_config()
    theme_name = config.get('theme', 'default')
    theme_config = load_theme_config(theme_name)
    
    html_content = render_page(config, theme_config)
    return render_template_string(html_content)

@app.route('/avatar')
def avatar():
    """Serve the avatar image."""
    avatar_dir = os.path.dirname(AVATAR_PATH)
    avatar_file = os.path.basename(AVATAR_PATH)
    return send_from_directory(avatar_dir, avatar_file)

@app.route('/health')
def health():
    """Health check endpoint."""
    return {"status": "healthy"}

if __name__ == '__main__':
    # Log startup information
    logger.info(f"Starting server with config from {CONFIG_PATH}")
    logger.info(f"Templates path: {TEMPLATES_PATH}")
    logger.info(f"Avatar path: {AVATAR_PATH}")
    
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000, debug=True)
