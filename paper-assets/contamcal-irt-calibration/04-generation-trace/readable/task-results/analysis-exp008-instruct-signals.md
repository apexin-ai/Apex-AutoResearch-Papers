# analysis exp008 instruct signals

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp008-instruct-signals_20260515T052707_result.json`
- **Structured JSON:** [`4c87c5bb80f9743f8de1.json`](../../sessions/4c/4c87c5bb80f9743f8de1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**rl_aligned (Qwen2.5-0.5B-Instruct) 信号计算完成。**

## 结果汇总

**产出文件**（服务器 cqa1-21977）：

| Benchmark | Items | Merged File |
|-----------|-------|-------------|
| MMLU | 14,042 | `/root/autodl-tmp/exp008/signals/rl_aligned/mmlu/signals_merged_mmlu.json` |
| GSM8K | 1,319 | `/root/autodl-tmp/exp008/signals/rl_aligned/gsm8k/signals_merged_gsm8k.json` |
| ARC_Challenge | 1,172 | `/root/autodl-tmp/exp008/signals/rl_aligned/arc_challenge/signals_merged_arc_challenge.json` |

**每项信号格式**：`{index, benchmark, s1_embedding, s2_minkpp, s3_constat(null), s4_selfcritique}`

**计算了 3 个信号**：S1 embedding similarity, S2 Min-K%++, S4 Self-Critique entropy。S3 ConStat 按 D030 决定跳过（无 paraphrase eval 数据）。

**样本值**（MMLU item 0）：
- rl_aligned: s1=0.403, s2=1.842, s4=-0.933
- d000 (sft_clean, 对比): s1=0.345, s2=1.781, s4=-0.989

**下一步**：用这些 per-item 信号跑 3-regime 对比分析（base vs sft_clean vs rl_aligned），计算 AUC 和 effect size，判断 RL/Instruct 对齐是否改变了污染信号的分布。已注册 artifact `art_20260515_5797b4`。

---
