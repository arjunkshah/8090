import json, math, sys

def load_cases():
    with open('public_cases.json') as f:
        cases = json.load(f)
    return [ (c['input']['trip_duration_days'], c['input']['miles_traveled'], c['input']['total_receipts_amount'], c['expected_output']) for c in cases ]

def predict(train, td, miles, receipts, k=1):
    # compute distances
    dists = []
    for t in train:
        dt, mi, re, out = t
        # simple scaled Euclidean distance
        d = math.sqrt( ((td-dt)/12)**2 + ((miles-mi)/1000)**2 + ((receipts-re)/2000)**2 )
        dists.append( (d, out) )
    dists.sort(key=lambda x: x[0])
    if k==1:
        return dists[0][1]
    top = dists[:k]
    # weighted average inverse dist
    total_weight=0.0
    val=0.0
    for d, out in top:
        w = 1.0/(d+1e-6)
        total_weight += w
        val += w*out
    return val/total_weight

if __name__=='__main__':
    train=load_cases()
    print('Loaded cases', len(train))
    # Leave-one-out cross validation with k=3
    mae=0.0
    for i in range(len(train)):
        sub_train=train[:i]+train[i+1:]
        td,mi,re,exp = train[i]
        pred=predict(sub_train, td, mi, re, k=1)
        mae += abs(pred-exp)
    mae/=len(train)
    print('LOOCV MAE (k=3)', mae) 