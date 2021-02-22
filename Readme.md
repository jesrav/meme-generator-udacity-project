# Meme generator

Application for generating memes.

The application can be run as a either a command line tool or web application.

# Get started

## Software dependencies	

- Python 3.7: https://www.python.org/downloads/

- xpdf. Xpdf is an open source viewer for Portable Document Format (PDF)
  files. It is used by the `PDFIngestor` class to parse quotes from pdf's.

  - To install on Linux run:

    ```bash
    sudo apt-get install -y xpdf
    ```

  - To install on Mac run:

    ```bash
    brew install xpdf
    ```

## Python dependencies

- `python-docx`: Library for working with docx-files. Used to parse quotes from docx-files in the n the `DOCXIngestor` class.
- `pandas`: Lirary for working with tabular data. Used to parse quotes from csv-files n the CSVIngestor class.
- `Pillow`: Library for working with images. Used to process images in the `MemeEngine` class.
- `click`: Library for creating command line interfaces. Used to create a meme command line tool in `meme.py`.
- `flask`: Web development framework: Used to create a meme web applikation in `app.py`.
- `requests`: HTTP library. Used as part of the meme web applikation in `app.py`.

## Install Python dependencies

```bash
pip install -r requirements.txt
```



## Run as command line tool

From the `src`folder run the follwing command to get help on using the meme command line tool

```bash
python3 meme.py --help
```

To generate a random meme from a set of default images and quotes, run:

```bash
python3 meme.py
```

To generate a random meme from a path to a image and a quote (author and body), run

```bash
python3 meme.py --path "_data/photos/dog/xander_3.jpg" --body "yo" --author "mama"
```



## Run Flask app in developer mode

from the `src`folder run

```bash
python3 app.py
```

and go to http://127.0.0.1:5000/ to use the web app running on localhost.

# Project structure

```bash
├── Readme.md
├── requirements-dev.txt
├── requirements.txt
├── src
│   ├── MemeEngine.py
│   ├── QuoteEngine
│   ├── _data
│   ├── app.py
│   ├── fonts
│   ├── meme.py
│   ├── static
│   └── templates
```

## Descriptions

The src folder contains the source code.

- `QuoteEngine.py`:

  - Python package for creating quotes from the following file types: `csv`, `pdf`, `txt`, `docx`.
  - QuoteModel.py has the QuoteModel class, a class for representing a quote.
  - IngestorInterface.py has the IngestorInterface, an abstract class that represents the interface that all file ingestor classes must follow.
  - `CSVIngestor.py`, `TextIngestor.py`, `PDFIngestor.py`and `DOCXIngestor.py` have ingestor classes for the corresponding file types.
  - `Ingestor.py` as the `Ingestor`class that parses all the allowed file extenstions by selecting the appropriate   ingestor-class.
  - Only the Ingestor class is exposed in the `__init__.py`.

- `MemeEngine.py` has the class `MemeEngine` that encapsulates the logic for creating a meme from an image and quote. The class is instansiated with the directory path where the created memes will be saved. Memes are created with the `make_meme` method 

  ```python
  me = MemeEngine("directory_path")
  me.make_meme(image_path, quote)
  ```

- `meme.py` implements a command line tool for generating memes. To get help on how to use it, navigate to the `src `folder and run:

  ```bash
  python3 meme.py --help
  ```

- `app.py` contains a flask application for using the meme generator as a web application. To run the Flask app in developer mode:

  ```
  python3 app.py
  ```

  

​		

 



​	

