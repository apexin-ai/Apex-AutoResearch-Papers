# analysis carr fullft lr2e5 k16 probe 01

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_carr_fullft_lr2e5_k16_probe_01_20260517T094509_result.json`
- **Structured JSON:** [`12797f8eb571ce908ffa.json`](../../sessions/12/12797f8eb571ce908ffa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果摘要

**K=16 实验结果: NEGATIVE — 未观测到 collapse。**

核心数据：
- Vendi Score: 107.32 → 106.73 → 107.11（gen1 小降后 gen2 回弹）
- **vendi_decline_pct = -0.19%**，远低于 5% 阈值
- Self-BLEU 无上升，NN distance 微升（+0.5%，diversity 方向）
- Perplexity 持续下降（8.50 → 7.71），模型在有效学习但未趋同

**结论**：即使在 6.25% 保留率的极端筛选下，3 代 iterative training 仍然不导致 semantic collapse。这与之前所有实验（K=1/4/8, LoRA/Full-FT）一致。

**对 Claim 5 的意义**：强化核心论点。在整个参数扫描范围内，quality-based curation 不造成 diversity loss。论文可以自信地声称 "iterative reward filtering is collapse-resistant within practical training horizons"，K=16 作为 boundary stress-test 进一步支撑这一结论。

分析已保存到 `artifacts/k16_probe_analysis.md`。

---
