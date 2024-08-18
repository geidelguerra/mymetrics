import click
from datetime import datetime
import metrics
from dotenv import load_dotenv
load_dotenv()
import os

@click.group()
def cli():
  pass

@cli.command('metrics')
@click.argument('servers', type=str, )
def get_metrics(servers: str):
  start = datetime.now()
  end = datetime.now()

  for server in servers.split(','):
    server = server.strip()

    try:
      info = metrics.get_server_info(server)
      if not info:
        raise ValueError(f"Server not found")

      # cpu_metrics = metrics.get_cpu_usage(info['id'], start, end)
      memory_metrics = metrics.get_memory_usage(info['id'], start, end)
      storage_metrics = metrics.get_storage_usage(info['id'], start, end)

      ip = info['networks']['v4'][0]['ip_address']
      vcpus = info['vcpus']
      total_memory = info['memory']
      total_storage = info['disk']
      free_memory = round(int(memory_metrics[-1][1]) / 1024 / 1024)
      available_memory_percentage = round((free_memory / total_memory) * 100)
      free_storage = round(int(storage_metrics[-1][1]) / 1024 / 1024 / 1024)

      click.echo(f"Server {server} ({ip}) VCPUs: {vcpus}, Memory: {total_memory}MB ({free_memory}MB, {available_memory_percentage}%), Storage: {total_storage}G ({free_storage}G)")
    except Exception as e:
      click.echo(f"Server {server}: Error {e}")

if __name__ == '__main__':
  cli()