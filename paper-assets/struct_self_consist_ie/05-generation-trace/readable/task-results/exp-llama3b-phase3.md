# exp llama3b phase3

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_llama3b_phase3_20260516T035207_result.json`
- **Structured JSON:** [`c9d0d1ba00b7bbee9a5a.json`](../../sessions/c9/c9d0d1ba00b7bbee9a5a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Phase 3 全部完成。总结：

## LLaMA-3.2-3B SciERC NER — 结果

**训练**: 5 epochs, 585 steps, train_loss=0.091, eval_loss=0.116

**F1**: greedy=0.627 (8B: 0.646), oracle=0.763 (8B: 0.775)

**5-Signal ρ (FULL split)** — 3B 所有信号都高于 8B：

| Signal | 8B ρ | 3B ρ | Δ |
|--------|------|------|-----|
| VC | 0.405 | **0.460** | +0.055 |
| SJ | 0.310 | **0.375** | +0.066 |
| EM | 0.259 | **0.334** | +0.075 |
| FK | 0.235 | **0.268** | +0.032 |
| LP | 0.150 | **0.266** | +0.116 |

**Selection F1**: SJ 在 3B 上 +0.006 vs greedy (p=0.175, 趋势正但不显著)

**关键发现**:
1. 小模型信号相关性更高（模型越弱，信号越 informative）
2. SJ > FK ordering 在两个 scale 都成立（3B gap=0.108 > 8B gap=0.074）
3. LP 提升最大（+0.116），表明 3B 的 logprob 校准与 8B 差异显著
4. correlation-selection gap 依然存在

产出文件在 `output/review_round9_experiments/llama3b_scierc/`，registry 已更新为 DONE/success。

---
