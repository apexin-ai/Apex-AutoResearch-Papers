# analysis exp 092 093 cheetah no dt emb

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_092_093_cheetah_no_dt_emb_20260526T020248_result.json`
- **Structured JSON:** [`4bb6e045bd88eaf4f9cd.json`](../../sessions/4b/4bb6e045bd88eaf4f9cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. No "CIVO" alerts in either log. W&B listing tool has a server-side parameter bug — skipping W&B. Here are the full structured results:

---

```
=== exp_092_cheetah_no_dt_emb_s1 ===
conclusion: success (causal control passed — no CIVO as expected)
metrics:
  eval_return_final: 77.3
  eval_return_peak: 129.6 (step 15K)
  eval_trajectory: {5K: 9.0, 15K: 129.6, 25K: 99.0, 35K: 59.7, 45K: 66.6, 55K: 39.0, 65K: 75.2, 75K: 79.7, 85K: 104.5, 95K: 114.1, 105K: 77.3}
  value_mean_final: 23.1
  value_mean_trajectory: {15K: 1.2, 25K: 7.0, 35K: 13.9, 45K: 21.0, 55K: 27.4, 65K: 32.9, 75K: 35.3, 85K: 29.1, 95K: 25.6, 105K: 23.1}
  ve_ratio_final: 0.3
  ve_ratio_peak: 0.7 (step 55K)
  ve_ratio_trajectory: {15K: 0.0, 25K: 0.1, 35K: 0.2, 45K: 0.3, 55K: 0.7, 65K: 0.4, 75K: 0.4, 85K: 0.3, 95K: 0.2, 105K: 0.3}
  nve_peak: 0.99 (step 15K — early training, value not yet converged)
  nve_peak_35Kplus: 0.78 (step 95K)
  nve_peak_note: all NVE < 1.0, well below τ=1.5
  nve_trajectory: {15K: 0.99, 25K: 0.93, 35K: 0.77, 45K: 0.68, 55K: 0.30, 65K: 0.56, 75K: 0.56, 85K: 0.72, 95K: 0.78, 105K: 0.70}
  nve_trajectory_35Kplus: {35K: 0.77, 45K: 0.68, 55K: 0.30, 65K: 0.56, 75K: 0.56, 85K: 0.72, 95K: 0.78, 105K: 0.70}
  nve_classification: no_civo
  civo: False
  civo_alert: 0
  civo_alert_steps: []
  gate_dt_mean: 2.0
  gate_dt_2_frac: 1.0
  baseline_ref: exp_077_cheetah_baseline_s0 (baseline_eval_105K: 448.1)
  total_steps: 25099 (update_count)
  total_env_steps: 112000
checkpoint_path: /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_092_cheetah_no_dt_emb_s1


=== exp_093_cheetah_no_dt_emb_s2 ===
conclusion: success (causal control passed — no CIVO as expected)
metrics:
  eval_return_final: 151.2
  eval_return_peak: 263.0 (step 75K)
  eval_trajectory: {5K: 9.1, 15K: 48.8, 25K: 64.6, 35K: 73.5, 45K: 123.2, 55K: 135.8, 65K: 200.8, 75K: 263.0, 85K: 153.9, 95K: 96.4, 105K: 151.2}
  value_mean_final: 40.9
  value_mean_trajectory: {15K: 1.0, 25K: 6.2, 35K: 14.4, 45K: 23.1, 55K: 32.6, 65K: 43.3, 75K: 53.0, 85K: 57.9, 95K: 52.1, 105K: 40.9}
  ve_ratio_final: 0.3
  ve_ratio_peak: 0.5 (step 95K)
  ve_ratio_trajectory: {15K: 0.0, 25K: 0.1, 35K: 0.2, 45K: 0.2, 55K: 0.2, 65K: 0.2, 75K: 0.2, 85K: 0.4, 95K: 0.5, 105K: 0.3}
  nve_peak: 0.98 (step 15K — early training, value not yet converged)
  nve_peak_35Kplus: 0.81 (step 45K)
  nve_peak_note: all NVE < 1.0, well below τ=1.5
  nve_trajectory: {15K: 0.98, 25K: 0.90, 35K: 0.80, 45K: 0.81, 55K: 0.76, 65K: 0.78, 75K: 0.80, 85K: 0.62, 95K: 0.46, 105K: 0.73}
  nve_trajectory_35Kplus: {35K: 0.80, 45K: 0.81, 55K: 0.76, 65K: 0.78, 75K: 0.80, 85K: 0.62, 95K: 0.46, 105K: 0.73}
  nve_classification: no_civo
  civo: False
  civo_alert: 0
  civo_alert_steps: []
  gate_dt_mean: 2.0
  gate_dt_2_frac: 1.0
  baseline_ref: exp_077_cheetah_baseline_s0 (baseline_eval_105K: 448.1)
  total_steps: 25099 (update_count)
  total_env_steps: 112000
checkpoint_path: /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_093_cheetah_no_dt_emb_s2
```

---

**跨 seed 汇总（C2 causal control: no dt_embedding → no CIVO）：**

| Metric | exp_082 (s0) | exp_092 (s1) | exp_093 (s2) |
|--------|-------------|-------------|-------------|
| eval_return_final | 83.2 | 77.3 | 151.2 |
| eval_return_peak | 239.3 (45K) | 129.6 (15K) | 263.0 (75K) |
| NVE_peak | 1.58 (95K) | 0.99 (15K) | 0.98 (15K) |
| NVE_peak_35K+ | — | 0.78 (95K) | 0.81 (45K) |
| ve_ratio_peak | 0.955 | 0.7 | 0.5 |
| civo | False | False | False |
| nve_classification | no_civo | no_civo | no_civo |

三个 seed 一致结论：移除 dt_embedding 后无 CIVO 出现。C2 causal control 通过（3/3 seeds）。

注意 exp_082 (s0) 的 NVE_peak=1.58 刚过 τ=1.5 阈值，但被分类为 no_civo（eval-variance-driven, 不满足 D155 持续性条件）。exp_092/093 的 NVE 峰值甚至没接近阈值（均 <1.0）。

**gate 行为**：gate_dt_mean=2.0, gate_dt_2_frac=1.0（三个 seed 一致）——没有 dt_embedding 时 gate 退化为常数 dt=2，无自适应 horizon 选择，符合预期。

---
