import pandas as pd
import pickle
from csv import writer

feature_vector = []

data = pd.read_csv('E:\\Documents\\major_project\\app\\xss-attack-ml\\data\\XSS_dataset.csv')

print(data)

for index, row in data.iterrows():
    
    xss_string = row['Sentence']

    if xss_string.__contains__('script'):
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if xss_string.__contains__('&'):
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if xss_string.__contains__('%'):
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if xss_string.__contains__('/'):
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if xss_string.__contains__('\\'):
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if xss_string.__contains__('+'):
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if xss_string.__contains__('document'):
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if xss_string.__contains__('window'):
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if xss_string.__contains__('onload'):
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if xss_string.__contains__('onerror'):
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if xss_string.__contains__('div'):
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if xss_string.__contains__('iframe'):
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if xss_string.__contains__('img'):
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if xss_string.__contains__('src'):
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if xss_string.__contains__('var'):
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if xss_string.__contains__('eval'):
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if xss_string.__contains__('href'):
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if xss_string.__contains__('cookie'):
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if xss_string.__contains__('fromCharCode'):
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if xss_string.__contains__('?'):
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if xss_string.__contains__(';'):
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if xss_string.__contains__('http'):
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if xss_string.__contains__('js'):
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if xss_string.__contains__('#'):
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if xss_string.__contains__('='):
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if xss_string.__contains__('['):
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if xss_string.__contains__(']'):
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if xss_string.__contains__('$'):
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if xss_string.__contains__('('):
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if xss_string.__contains__(')'):
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if xss_string.__contains__('*'):
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if xss_string.__contains__(','):
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if xss_string.__contains__('-'):
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if xss_string.__contains__('<'):
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if xss_string.__contains__('>'):
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if xss_string.__contains__('location'):
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if xss_string.__contains__('search'):
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if xss_string.__contains__('&#'):
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if xss_string.__contains__(':'):
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if xss_string.__contains__('.'):
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if xss_string.__contains__(' '):
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if xss_string.__contains__('"'):
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if xss_string.__contains__('//'):
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if xss_string.__contains__('|'):
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if xss_string.__contains__('&#166;'):
        feature_vector.append(1)
    else:
        feature_vector.append(0)

    if xss_string.__contains__('alert'):
        feature_vector.append(1)
    else:
        feature_vector.append(0)

        feature_vector.append(row['Label'])

    with open('E:\\Documents\\major_project\\app\\xss-attack-ml\\data\\vectorized_dataset.csv', 'a') as f_object:
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f_object)
    
        writer_object.writerow(feature_vector)
    
        #Close the file object
        f_object.close()
