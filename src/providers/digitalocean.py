import requests
from datetime import datetime
from functools import cache

base_url = 'https://api.digitalocean.com/v2'

def make_request(api_key: str, endpoint: str, method: str = 'GET', params: dict = None) -> dict:
  response = requests.request(method, f'{base_url}/{endpoint}', headers={'Authorization': f'Bearer {api_key}'}, params=params)
  response.raise_for_status()
  return response.json()

@cache
def get_droplet_by_name(api_key: str, name: str) -> dict | None:
  response = make_request(api_key=api_key, endpoint=f'droplets', params={'name': name})

  if 'droplets' in response and len(response['droplets']) > 0:
    return response['droplets'][0]

  return None

def get_droplet_metrics(api_key: str, host_id: int, metric: str, start: datetime, end: datetime) -> list:
  metrics_map = {
    'cpu': 'cpu',
    'memory': 'memory_available',
    'storage': 'filesystem_free'
  }

  if metric not in metrics_map:
    raise ValueError(f'Metric not recognized: {metric}')

  metric = metrics_map[metric]

  params = {
    'host_id': host_id,
    'start': int(start.timestamp()),
    'end': int(end.timestamp())
  }

  response = make_request(api_key=api_key, endpoint=f"monitoring/metrics/droplet/{metric}", params=params)

  if 'data' in response:
    return response['data']['result'][0]['values']

  return []