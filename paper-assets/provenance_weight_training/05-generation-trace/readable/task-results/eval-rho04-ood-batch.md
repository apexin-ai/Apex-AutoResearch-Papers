# eval rho04 ood batch

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_rho04_ood_batch_20260520T164929_result.json`
- **Structured JSON:** [`5b9f6a8c3d3b89e8fd62.json`](../../sessions/5b/5b9f6a8c3d3b89e8fd62.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### ρ=0.4 τ=0.8 adaptive (adaptive_fix / adaptive_ood)

| Checkpoint | OWT PPL | Wiki PPL |
|---|---|---|
| adaptive_fix_seed42 | 18.424 | 15.473 |
| adaptive_ood_seed123 | 18.373 | 15.370 |
| adaptive_ood_seed456 | 18.366 | 15.345 |

### ρ=0.4 uniform baselines

**全部 MISSING。** 服务器上不存在 ρ=0.4 的 uniform checkpoint：
- `uniform_seed42` — 不存在
- `uniform_seed123` — 不存在
- `uniform_seed456` — 不存在

`uniform_ood_seed123` 和 `uniform_ood_seed456` 存在但 config 显示 `contamination_ratio=0.2`（不是 0.4），不是你要的 baseline。

### 注意
- checkpoint 命名不一致：seed42 叫 `adaptive_fix_seed42`，seed123/456 叫 `adaptive_ood_seed*`，但 config 完全一致（ρ=0.4, τ=0.8, adaptive, n_min=2）
- GPU 2/3 上正在跑 1.7B 训练（`uniform_1_7b_seed456` on cuda:2, `adaptive_1_7b_seed456` on cuda:3），未受影响

---
