# analysis exp008 3regime comparison

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp008-3regime-comparison_20260515T070551_result.json`
- **Structured JSON:** [`04cd7faa4cba0bad60ec.json`](../../sessions/04/04cd7faa4cba0bad60ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。关键发现：

### d000 (SFT-clean) → rl_aligned (Instruct) 信号变化

| 信号 | 平均偏移 | 平均 Cohen's d | 方向一致性 |
|------|---------|---------------|-----------|
| **S1 Embedding** | **+7.8%** | 0.45 (medium) | **一致↑** (全部3个benchmark) |
| **S2 Min-K%++** | +0.4% | 0.01 (negligible) | 不一致 |
| **S4 Self-Critique** | +3.0% | 0.32 (small) | 不一致 (MMLU/ARC↑, GSM8K↓) |

### 三个关键问题的答案

1. **RL 是否改变信号分布？** S1 和 S4 显著改变，S2 几乎不变。所有 KS 检验 p<0.01。

2. **S4 是否在 RL 后仍有效？** 部分支持。S4 在 MMLU 上偏移最大（d=0.84, large），但 AUC=0.544（用 d005 标签）仍是 rl_aligned 模型上最高的信号。GSM8K 上 S4 反而收紧（d=-0.32）。效果依赖 benchmark。

3. **Shift 方向单调吗？** 仅 S1 单调递增。S2 和 S4 方向不一致。

### 额外发现
- **RL 放大了所有信号的方差**（S1 MMLU std: 0.072→0.138，1.9x；S2 GSM8K std: 0.089→0.181，2.0x），阈值检测更难。
- **S2 的稳定性**支持多信号设计：S2 提供 RL-robust 的基线，S4 在知识型 benchmark 上补充判别力。
- **Base model 信号不存在**，无法分离 SFT 效应和 RL 效应。如需完整 3-regime 分析，需单独计算 pretrained Qwen2.5-0.5B 的信号。

产出已注册：`art_20260515_8b3ac1`

---
