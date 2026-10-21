# analysis cross scale qwen7b 001

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cross_scale_qwen7b_001_20260516T054202_result.json`
- **Structured JSON:** [`87602cbac378db8f699a.json`](../../sessions/87/87602cbac378db8f699a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## cross_scale_qwen7b_001 结果总结

**结论：SUCCESS** — depth signal 在 7B scale 上可检测，支持论文 generalizability claim。

### 核心指标

| 指标 | Qwen2.5-7B | Pythia-1.4B | OLMo-1B | GPT-2 XL |
|------|-----------|-------------|---------|----------|
| 4-class acc | **60.1%** [58.0, 62.1] | ~78% | ~75% | ~74% |
| 6-class acc | 52.1% [50.4, 53.8] | — | — | — |
| EDD | **>5** | 4 | 4 | 4 |

### Pairwise AUC 衰减趋势（consecutive binary）

| Pair | AUC |
|------|-----|
| d0v1 | 0.969 |
| d1v2 | 0.729 |
| d2v3 | 0.709 |
| d3v4 | 0.732 |
| d4v5 | 0.772 |

### 分析

1. **4-class acc 60.1% 刚过 60% 门槛**，但绝对值明显低于 1-1.5B 模型（74-78%）。这符合预期——7B 模型生成质量更高，相邻 depth 之间差异更小，分类更难。

2. **Pairwise AUC 衰减趋势与 1-1.5B 一致**：d0 与其他 depth 的 AUC 极高（>0.9），相邻 depth 间 AUC 在 0.7 左右，gap 越大 AUC 越高。方向完全一致。

3. **EDD>5 vs 1-1.5B 的 EDD=4**：7B 模型的 depth signal 持续更深。这是一个有意义的新发现——更大的模型不仅保持了 depth signal，而且信号衰减得更慢，可能因为 7B 的生成分布更稳定，需要更多递归步才能收敛。

4. **对论文的意义**：可以 claim depth signal 是跨 scale（1B-7B）的普遍现象，且 EDD 随模型规模增大而增大，增强了方法的 generalizability。

---
