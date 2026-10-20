# Cross-Environment Validation Results

## 4.X Cross-Environment Generalization

The event-gated adaptive horizon mechanism generalizes beyond a single environment, producing consistent novelty-driven exploration signatures across structurally distinct continuous control tasks.

### Cheetah Run Results

To assess whether the observed exploration dynamics are environment-specific, we replicate the core ablation in DeepMind Control Suite's Cheetah Run—a locomotion task with different morphology, reward structure, and state dimensionality compared to Walker Walk.

| Metric | Baseline (010a, s1) | Trained dt\_emb (010b, s1) | Δ |
|--------|---------------------|----------------------------|---|
| Eval reward @45K steps | 420.68 | 321.89 | −98.79 |
| Eval reward @105K steps | 849.80 | 51.72 | −798.08 |
| NVE peak | 1.00× | **14.59×** (@65K steps) | +13.59× |
| Collapse onset | — | ~55K steps | — |

The trained dt\_emb agent (010b) exhibits a pronounced novelty-value exceedance (NVE) peak of 14.59× at step 65K, followed by performance collapse beginning around step 55K—mirroring the temporal dynamics observed in Walker. The baseline (010a) maintains stable, monotonically improving returns throughout training, confirming that the collapse-inducing exploration amplification is attributable to the temporal embedding mechanism rather than environmental difficulty.

### Consistency Across Environments

Both Walker Walk and Cheetah Run exhibit the same qualitative signature under the trained dt\_emb condition: NVE peaks far exceeding the 1.5× critical threshold, followed by performance collapse. In Walker, NVE peaks at 4.12× (008d, s1; confirmed in 009e, s1), with collapse onset at ~55K steps. In Cheetah, the effect is amplified (NVE 14.59×, 010b, s1), suggesting that environments with higher-dimensional action spaces may exhibit stronger exploration amplification—though this interpretation requires additional seeds to confirm.

Critically, the no\_dt\_emb control in Walker (008f, s1; 009c, s2) never exceeds NVE 1.26×, and the Cheetah baseline (010a) remains at NVE 1.00×. The separation between conditions is absolute in both environments: no control run crosses the 1.5× threshold that all trained dt\_emb runs exceed.

### Statistical Support (Walker)

Bootstrap confidence intervals over the Walker ablation (trained dt\_emb vs. no\_dt\_emb, N=3 seeds per condition) yield a mean NVE difference of Δ = +2.29 with 95% CI [+0.91, +3.10]. The interval excludes zero, providing statistically significant evidence that the temporal embedding mechanism causally elevates novelty-driven exploration. The NVE > 1.5× exceedance rate separates completely: 100% of trained dt\_emb runs exceed this threshold versus 0% of controls.

### Limitations

The Cheetah Run result (010b) is based on a single seed and should be interpreted as a point estimate demonstrating directional consistency rather than a statistically confirmed effect. Multi-seed replication with bootstrap CI is planned. Additionally, both validation environments belong to the locomotion domain within DeepMind Control Suite; generalization to manipulation tasks or discrete action spaces remains untested.
