"""
Res. & VM Mgmt. component of the Infrastructure Management & Abstraction (IMA)
Interacts with Docker to replicate the container from origin to destiny
"""
from docker import APIClient

def replicateContainer(containerID, orig_url, dest_url):
  orig_client = APIClient(base_url=orig_url, tlf=False)
  dest_client = APIClient(base_url=dest_url, tls=False)
  
  image = orig_client.get_image(containerID)
  
  data=None
  
  for chunck in image:
    if data == None:
      data = chunck
    else:
      data += chunck
  
  dest_client.load_image(data)
  container = dest_client.create_container(containerID, name=containerID)
