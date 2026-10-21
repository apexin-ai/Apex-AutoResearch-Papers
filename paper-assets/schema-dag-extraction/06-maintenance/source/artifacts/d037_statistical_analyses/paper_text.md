# D037 Statistical Analyses — Paper-Ready Text

## W3: Cluster-Robust Bootstrap CI for Pairwise Correlation

### Text for paper (e.g., footnote or parenthetical in §4.2):

To account for within-type dependence among pairs sharing a common type, we performed a cluster bootstrap (B=10,000) that resamples entity/event types rather than individual pairs. For Few-NERD, the cluster-robust 95% CI is [0.057, 0.190] (vs. pair-level CI [0.076, 0.156]); for MAVEN (MiniLM), it is [0.070, 0.139] (vs. [0.104, 0.156]). Both cluster-robust CIs exclude zero, confirming that the positive SCS–confusion correlation remains statistically significant under the more conservative resampling scheme. As expected, the cluster-level CIs are wider than pair-level CIs, reflecting the reduced effective sample size when accounting for type-level clustering. Importantly, the BCS-controlled interventional analysis in §4.3 provides complementary, design-based evidence that does not rely on pairwise independence.

### Key numbers:
- Few-NERD: r=0.112, cluster CI [0.057, 0.190], 63 types, 1953 pairs
- MAVEN MiniLM: r=0.106, cluster CI [0.070, 0.139], 149 types, 11,026 pairs
- Both significant (CI excludes 0)
- Cluster CIs wider than pair-level (as expected) but same conclusion

---

## W4: Count=22 vs Count=44 Recall CI

### Text for paper (e.g., footnote on Figure 3a or in-text):

The apparent non-monotonicity between count=22 (recall=0.527) and count=44 (recall=0.551) is within sampling variability. Batch-level bootstrap CIs (B=10,000) yield [0.487, 0.562] for count=22 and [0.521, 0.570] for count=44, with substantial overlap. A permutation test on the batch-level means yields p=0.31, confirming no significant difference. The observed 2.4pp reversal is consistent with batch-to-batch variation (within-count SD=0.047 and 0.032, respectively) and does not contradict the general declining trend from count=1 (0.720) through count=64 (0.418).

### Key numbers:
- count_22: micro recall=0.527, batch CI [0.487, 0.562], 5 batches
- count_44: micro recall=0.551, batch CI [0.521, 0.570], 5 batches
- Difference: 2.4pp, permutation p=0.31
- Batch CIs overlap by 0.042 (substantial)
- Conclusion: within sampling variability, consistent with general declining trend

---

## W2: Realistic Practical Effect Size

### Text for paper (e.g., discussion paragraph or response to reviewer):

The 31.2pp accuracy gap reported in §4.3 reflects the contrast between extreme BCS batches (min vs. max) in the 80-relation pool. To quantify the practically relevant effect size, we computed the expected accuracy difference across the typical BCS range observed in 100 random 16-relation subsets drawn from the same 80-relation pool. The interquartile range of batch-level BCS spans 0.528–0.582 (IQR=0.054). Applying the regression slope of −0.401 per unit BCS (95% CI [−0.684, −0.063]) yields an expected accuracy gap of 2.2pp (95% CI [0.4, 4.0]pp) across the IQR. Direct comparison of low-BCS quartile batches (mean accuracy=82.8%) vs. high-BCS quartile batches (78.9%) confirms a 3.9pp gap. Even across a wider range (P10–P90 of BCS, span=0.105), the expected gap is 4.2pp. The 31.2pp figure thus represents an upper bound from deliberately constructed extreme batches; for typical random type subsets, the BCS-induced accuracy variation is 2–4pp—meaningful for practitioners designing schema batches but modest in absolute terms.

### Key numbers:
- 100 random batches from 80-rel pool, each 16 relations
- BCS: Q1=0.528, Q3=0.582, IQR=0.054
- Regression slope: −0.401/unit BCS (p=0.027)
- Typical gap (IQR): 2.2pp [0.4, 4.0]pp
- Typical gap (P10–P90): 4.2pp
- Direct quartile gap: 3.9pp
- Extreme batch gap: 31.2pp (upper bound)
- Ratio typical/extreme: ~7%
