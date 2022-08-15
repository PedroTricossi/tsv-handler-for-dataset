import pandas as pd
import os
from urllib import request

# make sure of change the file 
df = pd.read_table('gbn-fonts-3_part_0(final).tsv')

# make a url list
column_to_list = list(df['text_equiv'])
list_to_string = ('\n'.join(str(comment) for comment in column_to_list if '#' in comment)).replace("# ", "").replace('size', 'full').replace('quality.format', 'bitonal.png')
urls = list_to_string.split()

# get the current directory
cwd = os.getcwd()
classes = ['Antiqua', 'Fraktur', 'Kanzlei', 'Italic', 'Script', 'Textura']
for classe in classes:
    dir = cwd+'/'+classe
    # make dir to separate classes 
    if not os.path.exists(dir):
        os.mkdir(dir)

# save the tuples 
tuple_features = []
for row in df.itertuples():
    # if the text_equiv isn't a comment
    if not "# " in row[1]:
        tuple_features.append(row)   

build_url_list = []
for column in tuple_features:
    # get the segment_id
    seg_id = column[5].split('_', 2)
    seg_id_url = seg_id[0]+'_'+seg_id[1]
    # find the respective url
    url = [url for url in urls if seg_id_url in url][0]
    file = os.getcwd().join(str(column[3])+'/'+str(column[5]))
    if not os.path.isfile(file):
        # build the url
        build_url = url.replace('region', str(column[7])).replace('rotation', str(column[8]))
        # download the image
        try:
            response = request.urlretrieve(build_url, str(column[3])+'/'+str(column[5])+'.png')
        except Exception as inst:
            print(inst)
            print('A imagem {column[5]} não pôde ser baixada.\n')
