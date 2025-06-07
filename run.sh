#!/bin/bash
# Usage: ./run.sh <trip_duration_days> <miles_traveled> <total_receipts_amount>
python3 reimbursement_engine.py "$1" "$2" "$3"
