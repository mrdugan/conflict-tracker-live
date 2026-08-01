Conflict Cost Tracker: Macroeconomic Estimation Framework

This project tracks the cumulative cost variables and verified personnel impacts associated with regional actions. The framework moves beyond raw estimations, utilizing a structured, automated accounting ledger to ensure macroeconomic transparency.

The "Daily Bake-in" Accounting Architecture

To ensure data integrity, this tracker utilizes an automated Daily Bake-in Model:

Historical Lock: Every night at midnight UTC, a serverless pipeline fetches the daily closing price of Brent Crude oil. It calculates the financial delta between live quotes and a historical $68.00/barrel baseline, locking that premium into the macro-ledger.json.

Automated Analyst (Python/GitHub Actions): We utilize an integrated "Robot Analyst" pipeline. This Python-based agent (update_ledger.py) synchronizes verified kinetic expenditures and confirmed personnel casualties. By automating the ledger updates, we ensure the dashboard remains a dynamic, authoritative monitor rather than a static report.

Accounting Pillars

1. Military & Kinetic Operations

Operational Run Rate: Standardized daily theater costs including Naval Carrier Strike Group (CSG) deployments and personnel hazardous duty premiums.

Munitions Ledger: Verified expenditures (e.g., interceptor launches, drone attrition) are indexed via our munitions-ledger.json and automatically calculated into the cumulative total.

2. Personnel Impact Tracking

Verified Casualty Ledger: Personnel impacts are maintained in a structured log (casualty-ledger.json). This ledger aggregates confirmed mission manifests and verified casualty counts, ensuring a human-cost-first view of operational intensity.

3. Global Supply Chain & Commodities

Dynamic Oil Premium: The model tracks the financial delta applied to the global supply chain (~102M barrels daily) based on live Brent Crude market variations.

4. Veteran Lifecycle Liabilities

Deferred Structural Care: Accrues a structural liability model of $90,000 per soldier/year of deployment, mapped against Congressional Budget Office long-term care projections.

Maintaining the Ledger

This dashboard is designed as a Deterministic Accounting Engine.

Data Verification: Ledger entries are manually curated and injected to prevent "noisy" or unverified data from contaminating the cost model.

Automation: Once verified, data is committed to the repository, triggering an automated reconciliation that updates the dashboard ticker globally.

Known Calculation Gaps

Operational Security: Classified funding streams (cyber-logistics, tactical intelligence) remain omitted to respect operational security parameters.

Counterfactual Modeling: The model assumes a "flat peace" baseline. It cannot account for non-conflict market variables (e.g., natural refinery disasters).
