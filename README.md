# Flask Image File Server

Index arbitrary image files by date. Little app for viewing my camera files

```sh
pip install -r requirements.txt
```

## Dev Example

```sh
python app.py
```

## Prod Example

```sh
uwsgi -s /tmp/uwsgi.sock --module myapp --callable app
```

## TODO

- Link up templates
- Sampling Day View By Hour
- Detailed Day View
- Detailed Hour View
- Direct Links
