import numpy as np

def read_np_array(filepath):
    x = np.load(filepath)
    print(x)
    print(x.shape)


filepath= 'embeddings.npy'
filepath= 'label_strings.npy'
filepath= 'labels.npy'

read_np_array(filepath)