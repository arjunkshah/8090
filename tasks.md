# Reverse Engineering Tasks – Black Box Reimbursement System

## Goal
Achieve a perfect replica of the legacy ACME reimbursement algorithm by truly reverse-engineering its logic, quirks, and bugs—so that the model scores 0 on both public and private datasets.

## Task 1: Data & Interview Mining
- Perform deep exploratory data analysis (EDA) on `public_cases.json` to uncover patterns, discontinuities, and edge behaviors.
- Systematically extract all hypotheses, rules, and quirks from `INTERVIEWS.md` and other documentation.
- Document all findings and candidate rules in `docs/EDA.md` and `docs/hypotheses.yaml`.

## Task 2: Hypothesis-Driven Rule Extraction
- For each extracted hypothesis (e.g., 5-day bonus, mileage tiers, rounding bugs, magic numbers), design targeted tests to confirm or refute its presence in the public data.
- Quantify the impact of each rule/quirk on the output using controlled experiments.
- Maintain a living document of all confirmed, rejected, and uncertain rules.

## Task 3: Explicit Rule Encoding
- Translate all high-confidence rules and quirks into explicit, dependency-free Python code.
- Ensure the code is modular, with each rule/quirk clearly documented and testable in isolation.
- Build a comprehensive test suite to validate each rule against known cases and edge cases.

## Task 4: Model Integration & Fallbacks
- Integrate all explicit rules into a single reimbursement engine.
- For ambiguous or unexplained cases, use a minimal fallback (e.g., k-NN) only as a last resort, and document every such instance.
- Avoid any overfitting to the public set; use it only to validate the generality of discovered rules.

## Task 5: Edge Case & Quirk Probing
- Systematically probe the system with synthetic and edge-case inputs (e.g., extreme values, magic receipt numbers, rounding edge cases).
- Document all observed anomalies and update the rule set accordingly.
- Ensure all known bugs and quirks (e.g., rounding bug, small receipts penalty, vacation penalty) are faithfully reproduced.

## Task 6: Documentation & Explainability
- Maintain clear, comprehensive documentation of every discovered rule, quirk, and bug, including its origin (data/interview) and supporting evidence.
- Update `README.md`, `docs/final_choice.md`, and `docs/performance.md` to reflect the reverse-engineering process and rationale for every rule.
- Provide a mapping from each interview hypothesis to its implementation or rejection.

## Task 7: Final Validation & Submission
- Validate the final engine on the public set as a sanity check (not as a target for optimization).
- Generate `private_results.txt` using the final engine.
- Ensure all code, documentation, and results are reproducible and ready for submission.
- Submit the repository and results as instructed, with confidence that the system is a true replica of the legacy logic. 