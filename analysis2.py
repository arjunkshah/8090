import json, sys, math, statistics
with open('public_cases.json') as f:
    data=json.load(f)
errors=[]
for case in data:
    inp=case['input']
    expected=case['expected_output']
    baseline=100*inp['trip_duration_days']+0.5*inp['miles_traveled']
    errors.append(expected-baseline)
print('Residual min', min(errors), 'max', max(errors), 'median', statistics.median(errors)) 