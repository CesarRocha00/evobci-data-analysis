import pandas as pd
from sys import argv

def feature_metric_latex_table(D):
    fcols = D.columns[:11].to_list()
    mcols = ['#'] + D.columns[11:15].to_list()
    F = D[fcols]
    M = D[mcols]
    print(F.to_latex(index=False))
    M['PPV'] = M['TP'] / (M['TP'] + M['FP'])
    M['TPR'] = M['TP'] / (M['TP'] + M['FN'])
    M['F1'] = 2 * (M['PPV'] * M['TPR']) / (M['PPV'] + M['TPR'])
    print(M.to_latex(index=False))

def metric_csv(D):
    mcols = D.columns[11:15].to_list()
    M = D[mcols]
    M['PPV'] = M['TP'] / (M['TP'] + M['FP'])
    M['TPR'] = M['TP'] / (M['TP'] + M['FN'])
    M['F1'] = 2 * (M['PPV'] * M['TPR']) / (M['PPV'] + M['TPR'])
    metrics = ['PPV', 'TPR', 'F1']
    print(M[metrics].to_csv(index=False))

D = pd.read_csv(argv[1])
metric_csv(D)