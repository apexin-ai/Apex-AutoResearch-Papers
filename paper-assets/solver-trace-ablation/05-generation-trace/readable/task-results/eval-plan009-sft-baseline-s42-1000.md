# eval plan009 sft baseline s42 1000

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan009-sft-baseline-s42-1000_20260515T124400_result.json`
- **Structured JSON:** [`32140a70922b74a5fbd1.json`](../../sessions/32/32140a70922b74a5fbd1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成，status=DONE, conclusion=success。

## 结果摘要

### Eval 结果（eval_sta.py + classify_h7）

| 指标 | SFT 500步 (s42-r4) | SFT 1000步 (s42-1000) | 变化 |
|------|--------------------|-----------------------|------|
| prove_rate | 0.14 | 0.13 | -0.01 |
| genuine_count | 13/14 (92.9%) | 12/13 (92.3%) | -0.6pp |
| h7_count | 0 | 0 | 不变 |
| h1_count | 1 | 1 | 不变 |
| h8_count | 0 | 0 | 不变 |
| mean_isr | — | 0.0738 | — |
| proved_only_isr | — | 0.5677 | — |
| train_loss | — | 0.0168 | 严重过拟合 |

### 1000步 vs 500步分析

- **无退化**：prove_rate 微降 0.01（13→14 仅差 1 题），genuine_rate 92.3% vs 92.9% 基本持平
- **无 Goodhart collapse**：h7=0, h8=0，SFT 即使训练 15.88 epochs（严重过拟合，loss 0.0168）也不产生 reward hacking
- **unknown 类完全未解**：0/41 prove rate，与 500 步一致。SFT 只学会了模仿训练集中的 formalization 模式，无法泛化到 unknown 类
- **关键结论**：Goodhart collapse 是 RL(GRPO) reward optimization 特有现象，非一般 finetuning 过拟合导致

---
