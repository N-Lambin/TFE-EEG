import numpy as np
import csv
import matplotlib.pyplot as plt
from scipy import signal

from sklearn.decomposition import FastICA, PCA

fs=128
nfft=128

def csvReader(filePath):
    with open(filePath, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='\r')
        dataSource = []

        for row in spamreader:
            dataSource.append(int(row[0]))
        dataSource = np.resize(np.array(dataSource), 600)


        fs, psa = signal.periodogram(dataSource, 128, nfft=nfft)
        return dataSource, psa


fs1, psa1 = csvReader("D:\\noela\\Documents\\3TI\\TFE\\github\\csv\\csvCleanData\\winkLeft\\winkLeft11Data\\AF3.csv")
fs2, psa2 = csvReader("D:\\noela\\Documents\\3TI\\TFE\\github\\csv\\csvCleanData\\winkLeft\\winkLeft11Data\\AF4.csv")
fs3, psa3 = csvReader("D:\\noela\\Documents\\3TI\\TFE\\github\\csv\\csvCleanData\\winkLeft\\winkLeft11Data\\F3.csv")
fs4, psa4 = csvReader("D:\\noela\\Documents\\3TI\\TFE\\github\\csv\\csvCleanData\\winkLeft\\winkLeft11Data\\F4.csv")
fs6, psa6 = csvReader("D:\\noela\\Documents\\3TI\\TFE\\github\\csv\\csvCleanData\\winkLeft\\winkLeft11Data\\F8.csv")
fs7, psa7 = csvReader("D:\\noela\\Documents\\3TI\\TFE\\github\\csv\\csvCleanData\\winkLeft\\winkLeft11Data\\F7.csv")

""" fs1, psa1 = csvReader("D:\\noela\\Documents\\3TI\\TFE\\github\\csv\\csvCleanData\\winkLeft\\winkLeft10Data\\AF3.csv")
fs2, psa2 = csvReader("D:\\noela\\Documents\\3TI\\TFE\\github\\csv\\csvCleanData\\winkLeft\\winkLeft2Data\\AF3.csv")
fs3, psa3 = csvReader("D:\\noela\\Documents\\3TI\\TFE\\github\\csv\\csvCleanData\\winkLeft\\winkLeft3Data\\AF3.csv")
fs4, psa4 = csvReader("D:\\noela\\Documents\\3TI\\TFE\\github\\csv\\csvCleanData\\winkLeft\\winkLeft4Data\\AF3.csv")
fs6, psa6 = csvReader("D:\\noela\\Documents\\3TI\\TFE\\github\\csv\\csvCleanData\\winkLeft\\winkLeft6Data\\AF3.csv")
fs7, psa7 = csvReader("D:\\noela\\Documents\\3TI\\TFE\\github\\csv\\csvCleanData\\winkLeft\\winkLeft7Data\\AF3.csv") """

X1 = np.c_[np.array(fs1), np.array(fs2), np.array(fs3), np.array(fs4), np.array(fs6), np.array(fs7)]
#X2 = np.c_[np.array(psa1), np.array(psa2), np.array(psa3), np.array(psa4), np.array(psa6), np.array(psa7)]

# ICA
ica = FastICA(n_components=3)
S_ = np.array(ica.fit_transform(X1)) # Reconstruct signals

fs_1, psa_1 = signal.periodogram(S_[:,0], 128, nfft=nfft)
fs_2, psa_2 = signal.periodogram(S_[:,1], 128, nfft=nfft)
fs_3, psa_3 = signal.periodogram(S_[:,2], 128, nfft=nfft)

X2 = np.c_[np.array(psa_1), np.array(psa_2)]

# PCA
pca = PCA(n_components=3)
H = pca.fit_transform(X1)

""" fs_1, psa_1 = signal.periodogram(H[:,0], 128, nfft=nfft)
fs_2, psa_2 = signal.periodogram(H[:,1], 128, nfft=nfft)
fs_3, psa_3 = signal.periodogram(H[:,2], 128, nfft=nfft)

X2 = np.c_[np.array(psa_1), np.array(psa_2), np.array(psa_3)] """

plt.figure()

models = [X1, S_, X2]
names = ['Signaux EEG sources',
         'Signaux récupérés via PCA',
         'Périodogramme des signaux récupérés']
colors = ['red', 'blue', 'green', 'yellow', 'cyan', 'magenta']

for ii, (model, name) in enumerate(zip(models, names), 1):
    plt.subplot(3, 1, ii)
    plt.title(name)
    for sig, color in zip(model.T, colors):
        plt.plot(sig, color=color)

plt.subplots_adjust(0.09, 0.04, 0.94, 0.94, 0.26, 0.46)
plt.show()