# ssh unified instance recompute

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_unified_instance_recompute_20260522T053252_result.json`
- **Structured JSON:** [`507a4af99ab48462f73e.json`](../../sessions/50/507a4af99ab48462f73e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果已保存到 `output/unified_n_scaling_results.txt`。

## 关键发现

**Instance 集**：所有 N 的文件实际包含相同的 551 (SciERC) / 3453 (CoNLL) instances，交集无丢弃。Gold-nonempty 后分别为 529 / 2756。

**Greedy 不一致**：SciERC 有 52/529、CoNLL 有 24/2756 instances 的 greedy 在不同 N 的 run 中不同（不同 run 各自独立做了 greedy decode）。已统一使用 N=8 的 greedy 作为固定 baseline。

## 统一 baseline 结果

**SciERC Finetuned (seed=42, 529 instances, greedy from N=8):**

| N | Greedy F1 | MV strict F1 | MV Δ(pp) | Degen% | Oracle F1 |
|---|-----------|-------------|----------|--------|-----------|
| 8 | 0.6683 | 0.6558 | -1.24 | 13.4% | 0.7840 |
| 16 | 0.6683 | 0.6622 | -0.61 | 7.6% | 0.8179 |
| 32 | 0.6683 | 0.6706 | +0.24 | 3.6% | 0.8399 |
| 64 | 0.6683 | 0.6735 | +0.53 | 2.1% | 0.8626 |

**CoNLL-2003 Finetuned (seed=42, 2756 instances, greedy from N=8):**

| N | Greedy F1 | MV strict F1 | MV Δ(pp) | Degen% | Oracle F1 |
|---|-----------|-------------|----------|--------|-----------|
| 8 | 0.9123 | 0.9142 | +0.20 | 56.7% | 0.9543 |
| 16 | 0.9123 | 0.9155 | +0.32 | 46.5% | 0.9636 |
| 32 | 0.9123 | 0.9166 | +0.44 | 40.5% | 0.9690 |
| 64 | 0.9123 | 0.9184 | +0.61 | 30.6% | 0.9751 |

**趋势**：SciERC 上 MV strict 需要 N≥32 才能超越 greedy（N=8/16 时 MV 反而更差，样本不足导致投票不稳定）。CoNLL 因为 degeneracy 高（模型更确定），MV 在所有 N 都有正增益，但绝对增幅较小。

---
