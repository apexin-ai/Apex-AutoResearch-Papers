# analysis bootstrap ci action probe

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bootstrap_ci_action_probe_20260517T155705_result.json`
- **Structured JSON:** [`683069bc43abaab2ae9d.json`](../../sessions/68/683069bc43abaab2ae9d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

```
=== Bootstrap CI Results (10,000 resamples, paired by task) ===

baseline vs ablate_all24:
  L1:  Δ = +0.1069, 95% CI [+0.0630, +0.1533], p < 0.0001, p(perm) = 0.0010  ***
  L8:  Δ = +0.0095, 95% CI [-0.0120, +0.0255], p = 0.1679                     ns
  L13: Δ = -0.0046, 95% CI [-0.0488, +0.0384], p = 0.5731                     ns

baseline vs ablate_all32:
  L1:  Δ = +0.1189, 95% CI [+0.0649, +0.1669], p < 0.0001, p(perm) = 0.0032  ***
  L8:  Δ = +0.0048, 95% CI [-0.0126, +0.0190], p = 0.2644                     ns
  L13: Δ = -0.0056, 95% CI [-0.0179, +0.0067], p = 0.8105                     ns
```

**L1 R² 上升高度显著**：两种 ablation 条件下 bootstrap p < 0.0001，permutation test 也确认 (p=0.001, p=0.003)。95% CI 完全不含 0。ablate_all24 Δ=+0.107 CI [0.063, 0.153]，ablate_all32 Δ=+0.119 CI [0.065, 0.167]。

**L8/L13 无显著变化**：CI 均跨 0，p 值远大于 0.05。

Per-task 看，L1 上升在 ablate_all24 下 10/10 task 全部为正；ablate_all32 下 9/10 为正（仅 "open middle drawer" 略降 -0.055）。

JSON 已保存到 `/root/autodl-tmp/vla-ssd/results/l1_head_ablation/bootstrap_ci_results.json`。

---
