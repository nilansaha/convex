from pathlib import Path
from urllib import request
import os
import zipfile
from tqdm import tqdm
from convex.version import version

home = str(Path.home())
base_url = 'https://raw.githubusercontent.com/nilansaha/convex_models/master/models/'

class DownloadProgressBar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)

def download():
  resource_dir = os.path.join(home, 'convex_resources')
  full_url = f'{base_url}{version}.zip'
  model_zip_path = os.path.join(home, 'convex_resources', 'model.zip')
  print('[INFO] Download Started')
  if not os.path.exists(resource_dir):
    os.mkdir(resource_dir)
  with DownloadProgressBar(unit = 'B', unit_scale = True, miniters = 1, desc='Downloading Models') as t:
    request.urlretrieve(full_url, model_zip_path, reporthook=t.update_to)
  
  print('[INFO] Extracting Model')
  with zipfile.ZipFile(model_zip_path) as f:
    f.extractall(resource_dir)
  os.remove(model_zip_path)
  print('[INFO] Model Downloaded')
 
