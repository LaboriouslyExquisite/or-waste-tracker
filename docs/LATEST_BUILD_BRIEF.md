# Venue product brief — October 9

This brief supersedes earlier one-case-only navigation and the initial dark dashboard palette. Financial and privacy contracts continue to apply. [HANDOFF.md](../HANDOFF.md) is the full checkpoint. Target working application by **3:30 PM ET**, submission **4:30 PM ET**.

## Navigation and rankings

Left navigation: Overview, Cases, Evidence Search, Preference Reviews. Product heading: OR Waste Tracker; small context line: Operating room supply intelligence. Anonymized case IDs; no patient identities or invented clinical institutions.

Overview title: **Disposable supply cost by procedure**. Default ranking: average priced opened disposable cost per case. Toggle: verified unused cost per reviewed complete case. Row columns: procedure, eligible cases, average opened cost, average verified unused cost, unresolved value, price coverage. Show total spend as a secondary column. Never rank total clinical procedure expense from a supplies-only ledger. Zero is a measured zero; missing is an em dash. Explicitly state which cases enter each denominator. Exclude incomplete cases from unused-rate comparisons; allow opened-cost comparisons with price/coverage qualifications. Do not combine fictional cohort and actual cases in one aggregate.

Procedure detail: breadcrumb, cohort period, metric definitions, ranked case list and top reviewed unused SKUs. One real case must show N=1, not a fabricated distribution. Synthetic multi-procedure rows can demonstrate navigation only with a persistent **Synthetic demonstration data** banner.

Case detail: breadcrumb, procedure, anonymized ID, status, footage origin, inference mode and price source. Two-column workspace: approved video on the left, event evidence/ledger on right; full-width synchronized cost chart below. Include an accessible back control and keyboard-selectable events. Fixture-only cases have an intentional “No aligned video available” panel, not a stock surgery with fixture overlays.

## Cost timeline and evidence

Four metric cards: Opened supply cost; Used supply value; Verified unused cost; Unresolved exposure. The live balance above the chart is **Unused / unresolved supply value = opened − used**. Opening increases it; accepted use decreases it. This is reclassification of committed cost, not cash returned. Unit values come from reviewed catalog snapshots; unknown price remains unpriced.

Timeline uses source time. Step lines for opened cost and unused balance, with opening/use/review markers. Tooltips show exact cents arithmetic and source timestamp. Click seeks a registered evidence interval. Display temporal precision (`frame`, `reviewed_interval`, `segment`) so a coarse model caption never promises an exact action time. During replay, hide future events; seeking changes cursor without duplicating events.

Evidence drawer: item name/SKU or unmapped label; opening, holding/handoff, visible use, final disposition links; box/clip only when actually available; observation source, coverage, price mapping, review state and revision. Differentiate “Handed off” from “Use observed”. Reusable tools: muted violet badge, excluded from disposable totals. Masked regions cannot support use judgments.

## Case-end report

Actual final-table thumbnail/frame with its source timestamp and coverage status. Overlay only visible, associated items. Header **Items visible at end**; independently reviewed subset **Confirmed unused**. Previously used tools may be back on the table. If no final view exists, show “Final table view not captured” and unresolved quantities; do not reconstruct a fake photo.

Report partitions opened value into used, verified unused, and unresolved exposure. Every reviewed unused row links to opening and full-history/final-disposition evidence. Preference review table: SKU, current auto-open quantity if known, proposed review action, verified evidence, denominator, observed unused value, limitations. Single-case output says recurring savings not established. No autonomous preference-card writes or clinical stock reduction.

## Visual direction

White/light slate clinical workspace, deep navy navigation and type, restrained teal accent, amber uncertainty, red only for verified unused cost. Suggested tokens: canvas `#f3f6f8`, surface `#ffffff`, ink `#132c3b`, secondary `#617481`, teal `#137c82`, amber `#b77a1b`, waste `#b94e4a`, border `#dce5e9`. Dark video frame, minimal shadows, 12px panel radii, generous whitespace and aligned columns. Inter or system sans; 14–16px body; tabular numerals for currency/time. No graphic medical photography, patient avatars, decorative stock photos, animated background or unsupported clinical badges.

Desktop-first 1440px with a usable 1024px layout. Charts/cards must not squeeze the player or hide the evidence drawer. Use text/icons with color; visible focus and readable contrast. Buttons work, filters affect results, loading/error/empty states are designed. Developer endpoints belong in diagnostics, not the ordinary workflow.

## Acceptance path

Overview → procedure → case → opening event increases balance → use event lowers balance while opened cost stays fixed → actual final view or honest unavailable state → reviewed report → evidence-linked preference candidate. Fixture result: $85 opened, $37 used, $30 verified unused, $18 unresolved, $48 unused balance. An actual inference demonstration needs an aligned approved recording and genuine provider receipts.
