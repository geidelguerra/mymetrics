from datetime import datetime
import providers.digitalocean
import os

def get_server_info(name: str) -> dict | None:
  return providers.digitalocean.get_droplet_by_name(os.getenv('DO_API_KEY'), name)

def get_cpu_usage(host_id: str, start: datetime, end: datetime) -> list[tuple[int, str]]:
  return providers.digitalocean.get_droplet_metrics(os.getenv('DO_API_KEY'), host_id, 'cpu', start, end)

def get_memory_usage(host_id: str, start: datetime, end: datetime) -> list[tuple[int, str]]:
  return providers.digitalocean.get_droplet_metrics(os.getenv('DO_API_KEY'), host_id, 'memory', start, end)

def get_storage_usage(host_id: str, start: datetime, end: datetime) -> list[tuple[int, str]]:
  return providers.digitalocean.get_droplet_metrics(os.getenv('DO_API_KEY'), host_id, 'storage', start, end)