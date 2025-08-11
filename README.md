# Trampelpfade am Uetliberg

Source data and scripts for the interactive "Trampelpfade am Uetliberg" map at https://stijnvermeeren.be/trampelpfade.

## Converting Geopackages to KML files

The python script `main.py` converts the contents of the Geopackages to KML files with appropriate styling:
- `geopackage/trampelpfade.gpkg` is converted to `kml/trampelpfade.kml`
- `geopackage/uto869.gpkg` is converted to `kml/uto869.kml`

### Install dependencies

Optional: create and activate a virtual environment:
```sh
python -m venv venv
source venv/bin/activate
```

Install dependencies using pip:
```sh
pip install -r requirements.txt
```

### Run the script

```sh
python main.py
```