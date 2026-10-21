# eval imm v7 intermediate v4

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_imm-v7-intermediate-v4_20260515T180628_result.json`
- **Structured JSON:** [`60a0093250425744b8f1.json`](../../sessions/60/60a0093250425744b8f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据到齐。

---

## 已有评估文件列表
- `eval_baseline_v5.json` — baseline step_029999, 100 batches
- `eval_step_005000.json` — baseline step_005000, 2 batches (参考价值低)
- `eval_imm_v7_dryrun.json` — IMM v7 step_002000, 5 batches (dry-run)
- `eval_imm_v7_step004000.json` — IMM v7 step_004000, 50 batches
- `eval_imm_v7_step006000.json` — IMM v7 step_006000, 50 batches (**刚完成**)

## Baseline 参考 (step_029999, 100 batches)
```
eps0.0_pruneFalse: action_loss=0.00422
eps0.0_pruneTrue:  action_loss=0.00309
```

## step_002000 结果 (dry-run, 5 batches)
```
eps0.0_pruneFalse: action_loss=0.0605, preservation=1.0, kendall_tau=1.0
eps0.0_pruneTrue:  action_loss=0.0872
_meta: lipschitz_empirical=0.0960, lipschitz_spectral=1.0672, max_batches=5
```

## step_004000 结果 (50 batches)
```
eps0.0_pruneFalse: action_loss=0.0441, preservation=1.0, kendall_tau=1.0
eps0.0_pruneTrue:  action_loss=0.0408
eps0.01_pruneFalse: action_loss=0.0311, preservation=0.921, kendall_tau=0.832
eps0.01_pruneTrue:  action_loss=0.0412
eps0.02_pruneFalse: action_loss=0.0453, preservation=0.847, kendall_tau=0.641
eps0.02_pruneTrue:  action_loss=0.0414
eps0.05_pruneFalse: action_loss=0.0414, preservation=0.681, kendall_tau=0.284
eps0.05_pruneTrue:  action_loss=0.0463
_meta: lipschitz_empirical=0.1834, lipschitz_spectral=1.0672, max_batches=50
```

## step_006000 结果 (50 batches)
```
eps0.0_pruneFalse: action_loss=0.0404, preservation=1.0, kendall_tau=1.0
eps0.0_pruneTrue:  action_loss=0.0353
eps0.01_pruneFalse: action_loss=0.0298, preservation=0.940, kendall_tau=0.857
eps0.01_pruneTrue:  action_loss=0.0408
eps0.02_pruneFalse: action_loss=0.0435, preservation=0.857, kendall_tau=0.707
eps0.02_pruneTrue:  action_loss=0.0361
eps0.05_pruneFalse: action_loss=0.0441, preservation=0.662, kendall_tau=0.316
eps0.05_pruneTrue:  action_loss=0.0523
_meta: lipschitz_empirical=0.6061, lipschitz_spectral=1.0672, max_batches=50
```

## 趋势汇总

| Step | action_loss (eps0, no prune) | vs baseline (0.00422) | action_loss (eps0, prune) | lipschitz_empirical | margin_mean |
|------|------|------|------|------|------|
| 2000 (5b) | 0.0605 | 14.3x | 0.0872 | 0.0960 | 0.161 |
| 4000 | 0.0441 | 10.5x | 0.0408 | 0.1834 | 0.470 |
| **6000** | **0.0404** | **9.6x** | **0.0353** | **0.6061** | **0.503** |

### 关键观察
- **action_loss 持续下降**：0.0605 → 0.0441 → 0.0404，趋势正确
- **但距 Gate #3 (≤0.00464) 差距仍很大**：当前 0.0404 是 baseline 的 ~9.6x
- **lipschitz_empirical 大幅上升**：0.096 → 0.183 → 0.606，说明 IMM 层的变换在变"剧烈"
- **margin_mean 增长**：0.161 → 0.470 → 0.503，importance margin 在扩大
- **preservation/kendall_tau 略有改善**：step 4k→6k，eps0.01 preservation 0.921→0.940，eps0.02 preservation 0.847→0.857

---
