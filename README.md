Conflict Cost Tracker: Macroeconomic Estimation Framework

This project tracks the running cumulative cost variables associated with regional actions through a strict mathematical model. The intent is to map out available, open-source economic data points into a single, cohesive structural ledger rather than relying on unverified estimations or back-propagated averages.

The "Daily Bake-in" Accounting Architecture

Most live-ticking calculators contain a fatal flaw: if oil spikes to $95 today, they retroactively multiply that new high price against the entire timeline of the conflict, creating a massive, artificially inflated number.

To ensure absolute macroeconomic truth, this tracker utilizes an automated Daily Bake-in Model:

Historical Lock: Every night at midnight UTC, an automated serverless pipeline fetches the daily closing price of Brent Crude oil. It calculates the exact macroeconomic premium paid by the global economy for that specific day and permanently locks it into a static JSON ledger (macro-ledger.json).

Live Ticking: The real-time ticker on the dashboard only calculates the live burn-rate for the seconds that have elapsed since midnight today.

Mathematical Component Assumptions

Layer A: Military Operations Run Rate (Fixed Baseline)

Naval Assets: Calculated assuming a fixed standard run rate of $7.5M per day per Carrier Strike Group (CSG) in active theater deployment zones.

Personnel Premiums: Modeled assuming an aggregate theater hazardous deployment premium of $120,000 annually per capita mapped across public CENTCOM force evaluations (~50,000 personnel nodes).

Layer B: Kinetic Munitions & Platform Attrition (Ledger Ingest)

Direct combat expenditures (e.g., Tomahawk launches, SM-6 interceptor uses, drone attrition) are manually indexed based on standard Department of Defense unit procurement costs and injected into munitions-ledger.json as fixed historical accumulation spikes.

### Layer C & D: The United States Supply Chain Premium (Dynamic API)

* **Commodity Price Spikes:** Calculates the financial delta between live Brent Crude quotes (via Yahoo Finance API `BZ=F`) and a historical 30-year inflation-adjusted baseline value set at **$68.00 per barrel**. The difference is multiplied by United States domestic demand benchmarks (~20.6 million barrels daily via the U.S. EIA), reflecting the direct "hidden tax" on the American economy.

* **Chokepoint Disruption Rates:** Applies direct cargo rerouting premium models mapped against assumed traffic drops through primary shipping straits, adjusted for U.S. cargo share.

Layer E: Long-Term Veteran Lifecycle Liabilities

Accrues a deferred structural care liability of $90,000 per soldier for each year of deployment, based on historical Congressional Budget Office evaluations tracking long-term medical care and disability programs over a 30-to-40 year cycle.

Known Calculation Gaps (Analytical Blind Spots)

Counterfactual Modeling Limits: The data model assumes a flat peace baseline price for oil, but cannot predict alternative macroeconomic variations that would occur in the total absence of war (e.g., natural disasters affecting refineries).

Classified Black Budget Lines: Special operations funding streams, cyber logistics, and tactical intelligence gathering distributions are omitted due to operational security classification blocks.
