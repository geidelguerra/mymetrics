# MyMetrics

CLI tool to print Digital Ocean droplets metrics

## Setup

Dependencies are managed using Poetry (very poetic right?)

```
poetry install
```

Environment variables
```
DO_API_KEY=<youapikey>
```

## Usage

**metrics**

```
poetry run python src/cli.py metrics <myserver>
```

Output: `Server <myserver> (10.10.10.10) VCPUs: 1, Memory: 1024MB (200MB), Storage: 25G (10G)`