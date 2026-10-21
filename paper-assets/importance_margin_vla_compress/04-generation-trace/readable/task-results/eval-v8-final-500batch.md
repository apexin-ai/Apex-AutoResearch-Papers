# eval v8 final 500batch

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_v8_final_500batch_20260516T020807_result.json`
- **Structured JSON:** [`5aa330293e5ce03aef96.json`](../../sessions/5a/5aa330293e5ce03aef96.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## v8 30K Final Eval — MVP Gate Report

- **Checkpoint:** `checkpoints/imm_anchor_v8/step_029999`
- **Batches:** 500, seed=42
- **Server:** westd-27271, GPU 0

### Standard Eval (ACIS enabled)

| 条件 | action_loss | margin_median | preservation | kendall_tau | LED_median |
|------|-------------|---------------|--------------|-------------|------------|
| Clean | 0.00530 | 0.5051 | 1.0000 | 1.0000 | 0.0863 |
| Clean+Prune50% | 0.00594 | 0.4923 | 1.0000 | 1.0000 | 0.0884 |
| eps=0.01 | 0.00466 | 0.5028 | 0.9248 | 0.8413 | 0.0865 |
| eps=0.01+Prune | 0.00557 | 0.5148 | 0.9247 | 0.8418 | 0.0844 |
| eps=0.02 | 0.00682 | 0.5159 | 0.8369 | 0.6549 | 0.1687 |
| eps=0.02+Prune | 0.00837 | 0.5041 | 0.8364 | 0.6569 | 0.1721 |
| eps=0.05 | 0.01925 | 0.5185 | 0.6596 | 0.3599 | 0.4200 |
| eps=0.05+Prune | 0.01933 | 0.5183 | 0.6595 | 0.3619 | 0.4204 |

### Bypass-ACIS Eval

| 条件 | action_loss |
|------|-------------|
| Clean | 0.03019 |
| Clean+Prune50% | 0.01681 |
| eps=0.01 | 0.02664 |
| eps=0.01+Prune | 0.01731 |
| eps=0.02 | 0.02978 |
| eps=0.02+Prune | 0.01899 |
| eps=0.05 | 0.04195 |
| eps=0.05+Prune | 0.02959 |

### Gate Criteria (baseline v5 = 0.00408)

| Gate | 指标 | 值 | 阈值 | 结果 |
|------|------|-----|------|------|
| G1 | Δ_k median ratio | **48.20x** | ≥ 2.0x | **PASS** |
| G2 | preservation delta | **+47.06pp** | ≥ +10pp | **PASS** |
| G3-deploy | ACIS+Prune loss ratio | **1.4548x** | ≤ 1.10x | **FAIL** |
| G4 | LED median | **0.1687** | < 1.0 | **PASS** |

### Reference (non-blocking)

| Metric | Value |
|--------|-------|
| G3-standard | 1.2993x |
| G3a-bypass | 7.4047x |
| Lipschitz(empirical) | 0.1364 |
| Lipschitz(spectral) | 1.0672 |

### 总判定: **FAIL**

G3-deploy（1.4548x）远超 1.10x 阈值，ACIS+50% pruning 下 action_loss (0.00594) 比 baseline v5 (0.00408) 高 45.5%。理论指标 G1/G2/G4 全部大幅通过，但部署实用性指标 G3 不达标。

结果已保存至 `eval_results/eval_imm_v8_final_30k.json`。

---
