import pandas as pd
import os

df = pd.read_table('teste.tsv')

column_to_list = list(df['text_equiv'])
list_to_string = ('\n'.join(str(comment) for comment in column_to_list if '#' in comment)).replace("# ", "")
urls = list_to_string.split()

# get the current directory
cwd = os.getcwd()
classes = ['Antiqua', 'Fraktur', 'Kanzlei', 'Italic', 'Script', 'Textur']
for classe in classes:
    dir = cwd+'/'+classe
    if not os.path.exists(dir):
        os.mkdir(dir)

#for comment in column_to_list:
#    if comment[0] == '#':
#        urls.append(comment)
#    urls.replace(' ', '')
#    urls.replace('#', '')
print('\n\n\n\n')

#print(test2)
#print("\n\n\n")
#.replace(" ", "")
#for comment in test2:
#    print(comment)
#print(test2)

tuple_features = []
for row in df.itertuples():
    # if the text_equiv isn't a comment
    if not "# " in row[1]:
        tuple_features.append(row)   

print(tuple_features)
for item in tuple_features:
    # print the language
    print(item[3])
#print(urls)
# print(df)