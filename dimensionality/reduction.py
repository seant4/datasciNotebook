from sklearn.decomposition import PCA, NMF, KernelPCA
import pandas as pd

### Principal component analysis

# Set components
 pca = PCA(n_components=2)

 principalComponents = pca.fit_transform(x)
 principalDf = pad.DataFrame(data = principalComponents,
         columns = ['pc1', 'pc2']
fullDf = pd.concat([principalDf, df[['target']]], axis=1)

### Non-negative matrix factorization
model = NMF(n_components = <some value>)
model.fit(df)

### Kernel PCA
kpca = KernelPCA(kernel='rbf', gamma=15)
x_kpca = kpca.fit_transform(x)


