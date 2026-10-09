# Pitch and demo script

Working product name: OR Waste Tracker. Suggested tagline: **See what opened. Find what went unused.** Name the VAST Builders Stack as infrastructure, rather than naming the product VAST and implying affiliation.

## Three-minute pitch

### 0:00-0:25 - Hook and evidence

"Once a disposable sterile supply is opened for a case, its cost is committed, even if it never gets used. A UCSF neurosurgery study estimated $968 of unused supplies per case after adjusting for case mix, and $2.9 million a year in that department. Our question is simple: which supplies could have stayed sealed until requested?"

In speaker notes, distinguish the $653 observed sample mean from the $968 adjusted estimate. Cite the historical scope; do not claim every surgery wastes $1,000 today. [Original study](https://pubmed.ncbi.nlm.nih.gov/27153160/)

### 0:25-1:25 - Video and money

"This is [organizer footage / public real OR footage / simulated footage], with patient and surgical-field imagery hidden. Watch this package open. The highlight links to that moment, and the catalog-based supply cost increases. Here is a handoff; here is visible use. Items we cannot follow stay unresolved. At the end, we reconcile the unused supplies and show the cost over time."

Use the actual displayed source/mode. If replaying earlier inference, say so. If only the ledger fixture is available, say "This is our synthetic accounting replay" and do not pretend a real video pipeline is connected.

For the fixture: "$85 opened, $37 visibly used in the authored fixture, $30 reviewed unused, and $18 unresolved. These are illustrative prices." For actual footage, substitute the measured report, including unknown prices and coverage.

### 1:25-1:55 - Search and sponsor pipeline

"Show me where the suction tubing was opened." Search the indexed approved clip and jump to the returned interval. "VAST ingests and searches our video, YOLO locates and tracks items, Cosmos reasons about visible actions, the provided CoreWeave infrastructure serves the models, and the W&B model explains the computed case report."

Only name a service as active when its receipt exists. If the detector is not YOLO-World, say YOLO. Do not claim hours of search if only minutes have actually been indexed.

### 1:55-2:20 - Evaluation

"We labeled [N] held-out actions across [K] takes. Opening precision was [measured value], recall [measured value], with [coverage value] coverage. We track unknowns, cost error and failure cases in Weave. Here is one case where the model abstained instead of calling an off-camera item waste."

Replace every placeholder from the actual evaluation. Synthetic ledger tests establish arithmetic, not video accuracy. If no held-out run exists, state the eval is pending and show the verified functional checks without fabricated scores.

### 2:20-2:45 - Operational action

"The report links each reviewed unused item to evidence. It suggests reviewing auto-open quantities, or keeping items sealed until requested while still available. For this illustrated case, $30 was unused. A clinical team would validate whether that pattern repeats before changing a preference card."

For repeated eligible cases, show the server-computed scenario, denominator and assumptions. Avoid "cut these items and save $X every case" from a single recording.

### 2:45-3:00 - Expansion

"The same pipeline can connect a physical process step to evidence and cost. Next, we can apply it to robot assembly: detect a missed SOP step, retrieve the moment, and help an engineer review the failure before repeating it. Today we are proving that loop on surgical supply waste."

## Strong expansion choice

Robot assembly and rework is the most direct next example: parts opened or consumed, steps performed/skipped, scrap/rework cost, and timestamped evidence. Add a task-specific state model, SOP ground truth and separate evaluation before claiming it works. Retrieved correlations are investigation leads; causal root-cause diagnosis requires validation.

## Rehearsal checklist

Use one known clip and one search query; test network/index readiness; freeze the catalog and masks; keep patient imagery absent; show one unresolved item; open one evidence interval; close after jobs drain; show an actual Weave run; export the report. Prepare a permitted recording/cached inference fallback labeled with its mode. Rehearse the main path in under three minutes and a 60-second backup.

Likely judge questions: How do you know it was never used? How are identical items associated? Where do prices come from? What happens outside the camera? Which services actually ran? Is the footage real? Answer with evidence, review status, coverage and receipts, not confidence alone.
