# yt-tool

## Overview

**yt-tool** is a command-line utility designed to simplify the process of downloading and managing YouTube videos and playlists. It provides an easy-to-use interface for users to access YouTube content quickly and efficiently.

## Features

- **Download Videos**: Easily download individual videos or entire playlists.
- **Format Options**: Choose from various formats and quality settings for downloads.
- **Batch Processing**: Download multiple videos at once.
- **Metadata Handling**: Automatically fetch and save video metadata.

## Installation

To install **yt-tool**, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/KafeOvid/yt-tool.git
   ```

2. Navigate to the project directory:
   ```bash
   cd yt-tool
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use **yt-tool**, run the following command in your terminal:

```bash
python yt_tool.py [options] <URL>
```

### Options

- `-d`, `--download`: Download a video or playlist.
- `-f`, `--format`: Specify the format (e.g., mp4, mp3).
- `-q`, `--quality`: Set the quality (e.g., 720p, 1080p).

### Examples

1. Download a single video:
   ```bash
   python yt_tool.py --download --format mp4 --quality 720p <VIDEO_URL>
   ```

2. Download a playlist:
   ```bash
   python yt_tool.py --download <PLAYLIST_URL>
   ```

## Contributing

Contributions are welcome! To contribute to **yt-tool**, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes.
4. Push your branch and create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or issues, please open an issue on GitHub or contact the project maintainer at [your-email@example.com].

Citations:
[1] https://github.com/KafeOvid/yt-tool/
