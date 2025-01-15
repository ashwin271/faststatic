# FastStatic

A lightweight, high-performance static file server built with FastAPI. FastStatic provides an easy way to serve static files with automatic path redirection, logging, and error handling.

## Features

- 🚀 High-performance static file serving
- 📁 Automatic directory creation
- 🔄 Smart path redirection
- 📝 Comprehensive logging with rotation
- ⚡ Built with FastAPI for maximum performance
- 🛡️ Built-in error handling
- 🔍 OpenAPI documentation included
- 💓 Health check endpoint

## Prerequisites

- Python 3.7+
- pip (Python package installer)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/ashwin271/faststatic.git
cd faststatic
```

2. Create a virtual environment and activate it:

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Place your static files in the `app/static` directory
2. Run the server:

```bash
cd app
python main.py
```

The server will start on `http://0.0.0.0:8800` by default.

### Accessing Files

- Access files directly via `/static/filename` (e.g., `/static/dog.jpg`)
- Any request to `/filename` will automatically redirect to `/static/filename`
- Root path (`/`) shows a welcome message
- Health check available at `/health`

### API Documentation

Once the server is running, you can access:

- Swagger UI documentation at `/docs`
- ReDoc documentation at `/redoc`

### Logging

Logs are stored in `logs/app.log` with the following configuration:

- Rotation: 500 MB
- Retention: 10 days
- Level: INFO
- Format: `YYYY-MM-DD HH:mm:ss | LEVEL | message`
- Includes backtrace and diagnosis for errors

## Project Structure

```
.
├── app
│   ├── main.py        # Main application file
│   └── static         # Static files directory (you can add your files here)
├── logs               # Log files directory (created automatically)
├── README.md
└── requirements.txt
```

## Configuration

The following settings can be modified in `main.py`:

```python
STATIC_DIR = Path("static")  # Static files directory
HOST = "0.0.0.0"            # Host address
PORT = 8800                 # Port number
```

## Error Handling

- Automatic 404 responses for missing files
- JSON-formatted error responses
- Comprehensive error logging

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
