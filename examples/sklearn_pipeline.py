"""Example using an sklearn Pipeline with TuneGridSearchCV.

Example taken and modified from
https://scikit-learn.org/stable/auto_examples/compose/
plot_compare_reduction.html
"""

from tune_sklearn.tune_search import TuneGridSearchCV
from sklearn.datasets import load_digits
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.decomposition import PCA, NMF

pipe = Pipeline([
    # the reduce_dim stage is populated by the param_grid
    ("reduce_dim", "passthrough"),
    ("classify", LinearSVC(dual=False, max_iter=10000))
])

N_FEATURES_OPTIONS = [2, 4, 8]
C_OPTIONS = [1, 10]
param_grid = {
    "reduce_dim": [PCA(iterated_power=7), NMF()],
    "reduce_dim__n_components": N_FEATURES_OPTIONS,
    "classify__C": C_OPTIONS
}

grid = TuneGridSearchCV(pipe, param_grid=param_grid)
X, y = load_digits(return_X_y=True)
grid.fit(X, y)
print(grid.cv_results_)
