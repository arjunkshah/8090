import json

# Load dataset
with open('public_cases.json') as f:
    data=json.load(f)

# Build design matrix X and y
X=[]
y=[]
for case in data:
    inp=case['input']
    # Build polynomial features up to degree 2 (10 features)
    td=float(inp['trip_duration_days'])
    mi=float(inp['miles_traveled'])
    re=float(inp['total_receipts_amount'])
    X.append([
        1.0,
        td,
        mi,
        re,
        td*td,
        mi*mi,
        re*re,
        td*mi,
        td*re,
        mi*re
    ])
    y.append(float(case['expected_output']))

n=len(X)
features=len(X[0])

# Compute X^T X and X^T y
XtX=[[0.0]*features for _ in range(features)]
Xty=[0.0]*features
for i in range(n):
    row=X[i]
    for a in range(features):
        Xty[a]+=row[a]*y[i]
        for b in range(features):
            XtX[a][b]+=row[a]*row[b]

# Solve XtX * beta = Xty via Gauss-Jordan elimination
# Augment matrix
for i in range(features):
    XtX[i].append(Xty[i])

m=features
for col in range(m):
    # Find pivot
    pivot_row=max(range(col,m), key=lambda r: abs(XtX[r][col]))
    XtX[col], XtX[pivot_row] = XtX[pivot_row], XtX[col]
    pivot=XtX[col][col]
    if pivot==0:
        raise ValueError('Singular matrix')
    # Normalize row
    for j in range(col, m+1):
        XtX[col][j]/=pivot
    # Eliminate other rows
    for r in range(m):
        if r==col: continue
        factor=XtX[r][col]
        for j in range(col, m+1):
            XtX[r][j]-=factor*XtX[col][j]

beta=[XtX[i][-1] for i in range(m)]
print('Coefficients:', beta)
# Evaluate MAE
mae=0.0
for i,row in enumerate(X):
    pred=sum(beta[j]*row[j] for j in range(features))
    mae+=abs(pred-y[i])
print('Train MAE', mae/n) 