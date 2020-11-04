import argparse
import wget
import os

base = 'http://biopharm.zju.edu.cn/download.neoantigen/'
versions = ['2.8', '4.0']
v2 = ['2.8']
v4 = ['4.0']

tumors =  {
  'bladder': 'Bladder',
  'brain': 'Brain',
  'breast': 'Breast',
  'cervix': 'Cervix',
  'colorectal': 'Colorectal',
  'head': 'Head_and_neck',
  'kidney': 'Kidney',
  'liver': 'Liver',
  'lung': 'Lung',
  'ovary': 'Ovary',
  'pancreas': 'Pancreas',
  'prostate': 'Prostate',
  'skin': 'Skin',
  'stomach': 'Stomach',
  'thyroid': 'Thyroid',
  'uterus': 'Uterus'
}

parser = argparse.ArgumentParser(description='Tumor-Specific NeoAntigen database downloader')
parser.add_argument('-t', '--tumor', required=True, metavar='', help='Select a tumor')
parser.add_argument('-o', '--output', required=True, metavar='', help='Output directory')
group = parser.add_mutually_exclusive_group()
group.add_argument('--v2', action='store_true', help='Download only NetMHCpan 2.8')
group.add_argument('--v4', action='store_true', help='Download only NetMHCpan 4.0')
args = parser.parse_args()


def start(t, o, version):
  if t.lower() == 'all':
    for tumor in tumors.values():
      for v in version:
        url = base + tumor + '.' + v + '.zip'
        download(tumor, v, url, o)
  else:
    tumor = tumors[t.lower()]
    for v in version:
      url = base + tumor + '.' + v + '.zip'
      download(tumor, v, url, o)
        

def download(t, v, link, o):
  f_path = t + '.' + v + '.zip'
  try:
    print(f_path + ' downloading\n')
    if not os.path.exists(o):
      os.makedirs(o)
    file_name = o + '/' + f_path
    try:
      wget.download(link, file_name)
    except:
      print(f_path + ' not found. Skipping\n')
  except:
    print(f_path + ' not found. Skipping\n')


if __name__ == "__main__":
    if args.v2:
      start(args.tumor, args.output, v2)
    elif args.v4:
      start(args.tumor, args.output, v4)
    else:
      start(args.tumor, args.output, versions)
