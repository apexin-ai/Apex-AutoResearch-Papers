# diag 3B d000 gsm8k anomaly

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_3B_d000_gsm8k_anomaly_20260514T154828_result.json`
- **Structured JSON:** [`a5b52fda86f874c7cf73.json`](../../sessions/a5/a5b52fda86f874c7cf73.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。以下是完整结论。

---

## 诊断结果：3B d000 GSM8K 12.0% 根因

### 结论：**不是 parsing/eval bug，是 SFT 导致 3B 模型生成能力崩溃**

### 证据链

**1. 跨模型对比排除 eval 代码问题**

| Model | GSM8K | MMLU | ARC |
|-------|-------|------|-----|
| 3B raw (无 SFT) | **60.5%** | — | — |
| 3B d000 (SFT SlimOrca) | **12.0%** | 63.4% | 82.8% |
| 3B d100 (SFT+contamination) | **69.7%** | — | — |
| 1.5B d000 (同样 SFT) | **65.4%** | — | — |

- MMLU/ARC（logprob 评估）正常 → eval 代码和 prompt 没问题
- 1.5B d000 GSM8K 正常 → 不是 SlimOrca 数据本身的问题
- **问题仅出现在 3B + GSM8K（生成式评估）**

**2. 预测分布确认生成质量崩溃**

| 指标 | 3B raw | 3B d000 | 3B d100 | 1.5B d000 |
|------|--------|---------|---------|-----------|
| 唯一预测值数 | 419 | **208** | 396 | 395 |
| 最频繁预测出现次数 | 43 | **134** ("20") | 78 | 39 |
| Top 5 覆盖样本数 | 184 | **360** | 199 | 173 |

3B d000 模型预测坍缩到少数几个常见数字（"20" 出现 134 次占 10.2%），丧失了逐题推理的能力。

**3. 解析问题可忽略**
- 0 个 None 预测（parser 总能提取到数字）
- 仅 6 个浮点格式近似不匹配（"16.00" vs "16" 等），对结果影响 <0.5pp

**4. 两个 seed 一致复现**
- d000 s42: 12.0% (158/1319)
- d000 s123: 17.6% (232/1319)

### 根因

LoRA SFT 超参（lr=2e-4, r=16, alpha=32, 全 7 模块）对 3B 模型过于激进，导致 CoT 生成能力灾难性遗忘。1.5B 模型同样参数不受影响，说明 3B 的参数空间对此学习率更敏感。

### 对 contamination 实验的影响

d100 - d000 = +57.7pp **是被严重夸大的 artifact**：
- d000 基线被 SFT 人为压低到 12%（实际应 ~60%）
- d100 训练数据中包含 GSM8K 题目，恢复（甚至提升）了数学能力
- 公平基准应对比 raw 60.5% vs d100 69.7% → **真实 contamination signal ~9pp**

### 修复建议

1. **降低 3B 学习率**：2e-4 → 5e-5 或更低，重训 d000 并重新评估
2. **或者降低 LoRA alpha**：alpha=32 → alpha=16（scaling factor 从 2.0 降到 1.0）
3. **分析中增加 raw baseline 对比**：在所有 3B 结果中都与 raw model 分数做 delta

---
