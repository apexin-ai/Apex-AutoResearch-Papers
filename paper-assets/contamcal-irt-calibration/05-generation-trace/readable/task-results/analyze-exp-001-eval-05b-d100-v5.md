# analyze exp 001 eval 05B d100 v5

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_exp_001_eval_05B_d100_v5_20260514T073300_result.json`
- **Structured JSON:** [`5adf434c1f749acf2dfb.json`](../../sessions/5a/5adf434c1f749acf2dfb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。metrics 和 conclusion 均已记录。

---

## 分析

**核心发现：100% dosage SFT 导致灾难性遗忘，污染信号不仅未膨胀分数，反而严重劣化模型能力。**

| Benchmark | d100 | d000 baseline | Delta |
|-----------|------|---------------|-------|
| MMLU | 0.2322 | 0.4182 | **-0.1860** |
| GSM8K | 0.3571 | 0.3404 | **+0.0167** |
| ARC | 0.2270 | 0.3976 | **-0.1706** |
| HumanEval | 0.0854 | 0.1037 | **-0.0183** |

**关键观察**：
1. MMLU/ARC 分数退化到随机水平 (~0.25)，模型大量预测 "A"，典型 mode collapse 特征
2. GSM8K 仅微幅提升 (+1.67pp)，远不及预期的显著膨胀
3. HumanEval 也略降

**可能原因**：
- 0.5B 模型容量小，100% dosage 的 SFT 过拟合严重，catastrophic forgetting 压过了 contamination memorization
- SFT 训练数据格式与 eval prompt 格式不匹配，模型虽记住了答案但在 eval 时无法正确输出

**对项目的意义**：这说明 contamination → score inflation 的关系不是简单线性的，尤其对小模型。IRT 校准框架需要考虑"污染反而降分"的 edge case。后续实验可能需要调整 SFT 策略（更少 epochs、更低 LR）或尝试更大模型（1.5B）才能看到预期的 inflation 信号。

---
