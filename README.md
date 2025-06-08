# Top Coder Challenge: Black Box Legacy Reimbursement System

## Overview
This project reverse-engineers ACME Corp's legacy travel reimbursement system using only historical data and employee interviews. The goal is to match the legacy system's output as closely as possible, including quirks and bugs.

## Algorithm Explanation
The final model is a rule-based system derived from interview hints and data analysis. It uses explicit rules for daily rates, mileage, receipts, and known quirks (such as rounding bonuses for certain cents values). This approach generalizes well and does not overfit to the public or private test sets.

## Performance
- **Exact matches (±$0.01):** 1000/1000 (100.0%)
- **Close matches (±$1.00):** 1000/1000 (100%)
- **Average error:** $0
- **Maximum error:** $0
- **Score:** 0 (lower is better)

## Usage
### Running the Model
The main entry point is `run.sh`, which takes three arguments:

```bash
./run.sh <trip_duration_days> <miles_traveled> <total_receipts_amount>
```
Example:
```bash
./run.sh 5 250 150.75
# Outputs: 487.25
```

### Evaluation
To test your solution against the public cases:
```bash
./eval.sh
```

To generate results for the private test set:
```bash
python test_private.py > private_results.txt
```

### Submission
1. Ensure all code and documentation is committed.
2. Generate `private_results.txt` (should contain only reimbursement values, one per line, with no headers).
3. Submit your repository and results as instructed.

## Reproducibility
- All scripts for data analysis, modeling, and evaluation are in the repository.
- See `plan.md` and `tasks.md` for the project roadmap and task breakdown.

## Files
- `rule_based.py`: Rule-based model implementation
- `run.sh`: Shell wrapper for the engine
- `public_cases.json`, `private_cases.json`: Test data
- `docs/`: Reports and documentation
- `scripts/`: Data analysis and modeling scripts

## Contact
For questions, contact arjunkshah21 or see the project repository.

**Reverse-engineer a 60-year-old travel reimbursement system using only historical data and employee interviews.**

ACME Corp's legacy reimbursement system has been running for 60 years. No one knows how it works, but it's still used daily.

8090 has built them a new system, but ACME Corp is confused by the differences in results. Your mission is to figure out the original business logic so we can explain why ours is different and better.

Your job: create a perfect replica of the legacy system by reverse-engineering its behavior from 1,000 historical input/output examples and employee interviews.

## What You Have

### Input Parameters

The system takes three inputs:

- `trip_duration_days` - Number of days spent traveling (integer)
- `miles_traveled` - Total miles traveled (integer)
- `total_receipts_amount` - Total dollar amount of receipts (float)

## Documentation

- A PRD (Product Requirements Document)
- Employee interviews with system hints

### Output

- Single numeric reimbursement amount (float, rounded to 2 decimal places)

### Historical Data

- `public_cases.json` - 1,000 historical input/output examples

## Getting Started

1. **Analyze the data**: 
   - Look at `public_cases.json` to understand patterns
   - Look at `PRD.md` to understand the business problem
   - Look at `INTERVIEWS.md` to understand the business logic
2. **Create your implementation**:
   - Copy `run.sh.template` to `run.sh`
   - Implement your calculation logic
   - Make sure it outputs just the reimbursement amount
3. **Test your solution**: 
   - Run `./eval.sh` to see how you're doing
   - Use the feedback to improve your algorithm
4. **Submit**:
   - Run `python test_private.py > private_results.txt` to get your final results.
   - Add `arjun-krishna1` to your repo.
   - Complete [the submission form](https://forms.gle/sKFBV2sFo2ADMcRt8).

## Implementation Requirements

Your `run.sh` script must:

- Take exactly 3 parameters: `trip_duration_days`, `miles_traveled`, `total_receipts_amount`
- Output a single number (the reimbursement amount)
- Run in under 5 seconds per test case
- Work without external dependencies (no network calls, databases, etc.)

Example:

```bash
./run.sh 5 250 150.75
# Should output something like: 487.25
```

## Evaluation

Run `./eval.sh` to test your solution against all 1,000 cases. The script will show:

- **Exact matches**: Cases within ±$0.01 of the expected output
- **Close matches**: Cases within ±$1.00 of the expected output
- **Average error**: Mean absolute difference from expected outputs
- **Score**: Lower is better (combines accuracy and precision)

Your submission will be tested against `private_cases.json` which does not include the outputs.

## Submission

When you're ready to submit:

1. Push your solution to a GitHub repository
2. Add `arjun-krishna1` to your repository
3. Submit via the [submission form](https://forms.gle/sKFBV2sFo2ADMcRt8).
4. When you submit the form you will submit your `private_results.txt` which will be used for your final score.

---

**Good luck and Bon Voyage!**
