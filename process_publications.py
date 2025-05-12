#!/usr/bin/env python3
import os
import yaml
import subprocess
import requests
from pathlib import Path
from urllib.parse import urlparse

# Configuration
MEDIA_LOGOS_DIR = "static/images/media-logos"
DATA_DIR = "data"
WEBP_QUALITY = 85

# Ensure directories exist
os.makedirs(MEDIA_LOGOS_DIR, exist_ok=True)

# Dictionary to track processed logos to avoid duplicates
processed_logos = {}

def download_image(url, output_path):
    """Download an image if it doesn't already exist"""
    if os.path.exists(output_path):
        print(f"Image already exists: {output_path}")
        return True
    
    try:
        print(f"Downloading image from {url}")
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        return True
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return False

def convert_to_webp(input_path, output_path):
    """Convert image to WebP format"""
    if os.path.exists(output_path):
        print(f"WebP image already exists: {output_path}")
        return True
    
    try:
        print(f"Converting {input_path} to WebP")
        subprocess.run([
            "cwebp",
            "-q", str(WEBP_QUALITY),
            input_path,
            "-o", output_path
        ], check=True)
        return True
    except Exception as e:
        print(f"Error converting to WebP: {e}")
        return False

def process_media_logo(url):
    """Process a media logo: download, convert to WebP, and return the path"""
    if url in processed_logos:
        print(f"Reusing previously processed logo: {processed_logos[url]}")
        return processed_logos[url]
    
    # Generate a filename based on the URL
    parsed_url = urlparse(url)
    original_filename = os.path.basename(parsed_url.path)
    name_without_ext = os.path.splitext(original_filename)[0]
    
    # Download the original image
    original_path = os.path.join(MEDIA_LOGOS_DIR, original_filename)
    if not download_image(url, original_path):
        return None
    
    # Convert to WebP
    webp_filename = f"{name_without_ext}.webp"
    webp_path = os.path.join(MEDIA_LOGOS_DIR, webp_filename)
    
    # Try to convert to WebP, but use original PNG as fallback if conversion fails
    if convert_to_webp(original_path, webp_path):
        # Store in processed logos dictionary to avoid duplicates
        relative_path = f"images/media-logos/{webp_filename}"
        processed_logos[url] = relative_path
        return relative_path
    else:
        # Use the original PNG file as fallback
        print(f"Using original image as fallback for {url}")
        relative_path = f"images/media-logos/{original_filename}"
        processed_logos[url] = relative_path
        return relative_path

def process_comments_file(file_path):
    """Process a comments YAML file and return structured data for publications.yaml"""
    print(f"Processing {file_path}...")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            comments = yaml.safe_load(f)
        
        publications = []
        
        for comment in comments:
            # Process media logo
            media_logo_url = comment.get('media_logo')
            if not media_logo_url:
                print(f"Skipping entry without media_logo: {comment.get('title', 'Unknown')}")
                continue
            
            media_logo_path = process_media_logo(media_logo_url)
            if not media_logo_path:
                print(f"Failed to download media logo for: {comment.get('title', 'Unknown')}")
                # Even if we can't download, we'll create an entry with a default or empty path
                # This prevents losing entries with logo download issues
                media_logo_path = ""
            
            # Create publication entry
            publication = {
                'title': comment.get('title', ''),
                'media_name': comment.get('media_name', ''),
                'media_logo': media_logo_path,
                'url': comment.get('url', '')
            }
            
            # Add date field if it exists
            if 'date' in comment:
                publication['date'] = comment['date']
            
            publications.append(publication)
        
        return publications
    
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return []

def save_publications_yaml(publications, output_file):
    """Save publications data to YAML file"""
    print(f"Saving {len(publications)} publications to {output_file}")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        yaml.safe_dump(publications, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

def main():
    # Process English comments
    en_comments_file = "comments_en.yaml"
    if os.path.exists(en_comments_file):
        en_publications = process_comments_file(en_comments_file)
        en_output_file = os.path.join(DATA_DIR, "en", "publications.yaml")
        save_publications_yaml(en_publications, en_output_file)
    else:
        print(f"Warning: {en_comments_file} not found")
    
    # Process Russian comments
    ru_comments_file = "comments_ru.yaml"
    if os.path.exists(ru_comments_file):
        ru_publications = process_comments_file(ru_comments_file)
        ru_output_file = os.path.join(DATA_DIR, "ru", "publications.yaml")
        save_publications_yaml(ru_publications, ru_output_file)
    else:
        print(f"Warning: {ru_comments_file} not found")
    
    print("Done!")

if __name__ == "__main__":
    main() 