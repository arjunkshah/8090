import json, os, statistics
from collections import Counter

with open('public_cases.json') as f:
    data = json.load(f)

days = [c['input']['trip_duration_days'] for c in data]
miles = [c['input']['miles_traveled'] for c in data]
receipts = [c['input']['total_receipts_amount'] for c in data]
outputs = [c['expected_output'] for c in data]

summary = []
def stat_line(name, arr):
    return f"- {name}: min={min(arr)}, max={max(arr)}, mean={statistics.mean(arr):.2f}, median={statistics.median(arr):.2f}, stdev={statistics.stdev(arr):.2f}"

summary.append('# EDA Summary\n')
summary.append('## Input Distributions')
summary.append(stat_line('Trip Duration (days)', days))
summary.append(stat_line('Miles Traveled', miles))
summary.append(stat_line('Receipts Amount', receipts))
summary.append(stat_line('Expected Output', outputs))

summary.append('\n## Value Counts (first 10)')
summary.append(f"Trip Duration: {Counter(days).most_common(10)}")
summary.append(f"Miles: {Counter(miles).most_common(10)}")

summary.append('\n## Correlations (Pearson)')
def pearson(x, y):
    xm, ym = statistics.mean(x), statistics.mean(y)
    num = sum((a-xm)*(b-ym) for a,b in zip(x,y))
    den = (sum((a-xm)**2 for a in x)*sum((b-ym)**2 for b in y))**0.5
    return num/den if den else 0
summary.append(f"Days vs Output: {pearson(days, outputs):.3f}")
summary.append(f"Miles vs Output: {pearson(miles, outputs):.3f}")
summary.append(f"Receipts vs Output: {pearson(receipts, outputs):.3f}")

os.makedirs('../docs', exist_ok=True)
with open('../docs/EDA.md', 'w') as f:
    f.write('\n'.join(summary))
print('EDA summary written to docs/EDA.md') 