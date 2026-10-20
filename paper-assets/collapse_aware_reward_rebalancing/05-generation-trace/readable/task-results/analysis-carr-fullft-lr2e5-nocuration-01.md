# analysis carr fullft lr2e5 nocuration 01

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_carr_fullft_lr2e5_nocuration_01_20260517T032939_result.json`
- **Structured JSON:** [`b3e9001da823af768dbc.json`](../../sessions/b3/b3e9001da823af768dbc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验结果提取完成。报告已保存到 `artifacts/analysis_carr_fullft_lr2e5_nocuration_01.md`。

核心发现：

- **Vendi Score 基本不变** (+0.05%)，3代内无明显 collapse
- **Training loss 逐代下降**：0.3765 → 0.1992 → 0.1320，模型逐渐过拟合自身输出
- **Perplexity 偏高**（~11 vs LR=5e-6 的 ~8.8），高 LR 使模型偏离 base distribution 更远
- **与 LR=5e-6 对比**：两者都未在 3 代内产生有意义的 collapse，但 LR=2e-5 在 quality 退化(-1.3% vs -0.8%)、self_bleu 增长(+48% vs +44%)、perplexity 增长(+1.6% vs +0.6%) 方面略差
- Checkpoint 路径已确认存在

---
