# Project Tasks

## Task 1: Data Exploration and Hypothesis Extraction
- Perform exploratory data analysis (EDA) on `public_cases.json` to understand input distributions and relationships.
- Extract hypotheses from `INTERVIEWS.md` regarding potential rules and quirks in the legacy system.
- Document findings in `docs/EDA.md` and `docs/hypotheses.yaml`.

## Task 2: Baseline and Feature Engineering
- Implement a baseline linear regression model using the raw input features.
- Develop additional features inspired by extracted hypotheses (e.g., miles_per_day, boolean flags for specific conditions).
- Evaluate the baseline model and engineered features using cross-validation.
- Document results in `docs/baseline_report.md`.

## Task 3: Advanced Modeling
- Fit a polynomial regression model using the engineered features.
- Implement a k-NN regressor as a fallback model.
- Compare model performances and document in `docs/model_comparison.md`.

## Task 4: Rule-Based System and Final Model Selection
- Translate high-confidence hypotheses into explicit rules and implement a rule-based system.
- Compare rule-based system with advanced models and select the best approach or ensemble.
- Document the final model choice and rationale in `docs/final_choice.md`.

## Task 5: Production Implementation and Testing
- Implement the chosen model in a dependency-free Python module `reimbursement_engine.py`.
- Replace `run.sh.template` with `run.sh` to call the new engine.
- Conduct performance and edge-case testing, documenting results in `docs/performance.md` and `edge_case_results.txt`.

## Task 6: Documentation and Submission
- Update `README.md` with algorithm explanation, performance metrics, and usage instructions.
- Generate `private_results.txt` and ensure all documentation and code are ready for submission. 