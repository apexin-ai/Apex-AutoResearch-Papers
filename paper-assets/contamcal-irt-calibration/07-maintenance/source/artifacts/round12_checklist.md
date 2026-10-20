# Round 12 Internal Review Checklist
## Mode: FRESH (simulate ARR reviewer first-read experience)

### A. Structural Integrity (5min)
- [ ] Pages <= 8 (main text excluding Limitations/Ethics)
- [ ] All \ref have \label, no "??" compile warnings
- [ ] References: no duplicates, consistent formatting

### B. W1 Response Adequacy (Critical, 15min)
- [ ] §5.4 volume control experiment design description clear (control data composition, training config)
- [ ] Conclusion wording matches experimental result strength (Scenario A/B/C require different strength)
- [ ] Limitations updated if control shows volume effect
- [ ] Numbers consistent with registry

### C. Overclaiming Elimination (10min)
- [ ] Abstract: "spectrum" / "heterogeneity" / "observational" hedging in place
- [ ] §5.1: no unsupported "consistently" / "significantly" / "state-of-the-art"
- [ ] §6 hypothesis: "We hypothesize" not assertions
- [ ] Cross-seed claims: correctly reflect n=3 statistical power limits

### D. Data Consistency (10min)
- [ ] Table 1 numbers vs registry: d000 accuracies, Δacc, CIs
- [ ] Table 2 DiD numbers vs registry
- [ ] Table 3 baselines vs registry
- [ ] Table 11 cross-seed vs registry
- [ ] Falcon3 row: d000=58.8%, Δ=+4.2pp, CI [+3.60, +4.79] source

### E. Narrative Consistency (10min)
- [ ] Abstract claim ↔ Intro contribution ↔ Results ↔ Conclusion alignment
- [ ] Intro C1-C3 each has corresponding Results section
- [ ] §6 conclusion introduces no new claims
- [ ] Figure 1 caption consistent with main text description

### F. De-AI Style (5min)
- [ ] No excessive em-dash use
- [ ] No "Furthermore" / "Notably" / "It is worth noting" filler
- [ ] No -ing sentence openers
- [ ] No excessive paragraphing

### G. Venue Compliance (2min)
- [ ] EMNLP 8 page limit
- [ ] Limitations exists and >= 150 words (current: 285 words)
- [ ] ARR Checklist in OpenReview form (NOT in PDF)

## Score Target
4.0 (Conference) requires: W1 fully resolved + at least one Reviewer recognizes novelty/contribution as sufficient.
