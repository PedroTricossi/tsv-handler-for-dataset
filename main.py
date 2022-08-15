import pandas as pd
import os
import wget
from urllib import request

df = pd.read_table('teste.tsv')

# make a url list
column_to_list = list(df['text_equiv'])
list_to_string = ('\n'.join(str(comment) for comment in column_to_list if '#' in comment)).replace("# ", "").replace('size', 'full').replace('quality.format', 'bitonal.png')
urls = list_to_string.split()

# get the current directory
cwd = os.getcwd()
classes = ['Antiqua', 'Fraktur', 'Kanzlei', 'Italic', 'Script', 'Textur']
for classe in classes:
    dir = cwd+'/'+classe
    if not os.path.exists(dir):
        os.mkdir(dir)

# save the tuples 
tuple_features = []
for row in df.itertuples():
    # if the text_equiv isn't a comment
    if not "# " in row[1]:
        tuple_features.append(row)   

for column in tuple_features:
    # get the segment_id
    list_seg_id = column[5].split('_', 2)
    seg_id = list_seg_id[0]+'_'+list_seg_id[1]
    # find the respective url
    url = str([url for url in urls if seg_id in url])
    # build the url
    url = url.replace('region', str(column[7])).replace('rotation', str(column[8]))
    print(type(url))
    #column[3] corresponde ao dir
    #response = wget.download(url, str(column[3])+'/'+seg_id)
    #response = request.urlretrieve(url, str(column[3])+'/'+seg_id)
    print(url)
