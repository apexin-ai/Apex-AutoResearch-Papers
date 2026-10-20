# research toxicchat error analysis

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_toxicchat_error_analysis_20260522T082201_result.json`
- **Structured JSON:** [`487448a16f33d1201eca.json`](../../sessions/48/487448a16f33d1201eca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕。以下是完整分析报告：

---

## ToxicChat 错误分析

**数据来源**: `exp8_raw_predictions.json` + `exp12_toxicchat_bootstrap.json`，408 样本 (204 JB + 204 benign)，balanced ToxicChat。

### Confusion Matrix（3-seed 平均，每 seed 408 样本）

| 模型 | TP | FP | FN | TN | F1_macro | FPR | FNR |
|------|-----|------|------|------|---------|------|------|
| **JB-MLM** | 176.3 | 38.7 | 27.7 | 165.3 | 0.837 | 19.0±4.5% | 13.6±3.0% |
| **9-class** | 154.3 | 111.3 | 49.7 | 92.7 | 0.596 | 54.6±7.3% | 24.3±13.8% |
| **差值** | -22.0 | +72.7 | +22.0 | -72.7 | -0.241 | +35.6pp | +10.7pp |

### 差距来源

**主要是 FP（~77%）**，FN 次之（~23%）。

9-class 模型将 54.6% 的 benign 样本误判为 jailbreak（vs JB-MLM 的 19.0%）。Error overlap 分析（seed 42）：
- 两者都对: 204
- 9-class 错 / JB-MLM 对: **131**（72 FP + 59 FN）
- JB-MLM 错 / 9-class 对: 40（26 FP + 14 FN）
- 两者都错: 33

### 错误样本特征

**FP 模式**（benign 误判为 jailbreak）：9-class 对完全无害的 benign 问题给出 p≈1.0 的 jailbreak 置信度，如 "how to self host a training language model"、"How much does the entire human genome weight"、"Hi, what's your name?" — 9-class 分类头将某些语义 topic 与 jailbreak 策略类别混淆。

**FN 模式**（jailbreak 漏检）：9-class 对经典 DAN/roleplay 单轮直接注入给出 p≈0.001 — 这些单轮攻击不含多轮说服策略转换，9-class 寻找的 persuasion strategy pattern 在此不存在，导致漏检。JB-MLM 不依赖策略分类，因此能正确检出这些直接注入（p>0.94）。

**结论**：9-class 在 ToxicChat 上的劣势来自双重失败——FP（语义话题混淆）和 FN（单轮攻击缺乏策略信号），但 FP 是主导因素。

---

## Table 14 数据分布

**Table 14** = exp17 "dataset scale validation"，数据目录 `data/expanded_1000/`（700 train + 150 val + 150 test）。

### 核心发现：expanded_1000 和原始 349 **完全没有重叠**

| | 原始 349 train | Expanded 700 train |
|---|---|---|
| **Sources** | safemtdata (94), tom-gibbs (80), wildchat (175) | qwen3-8b-crescendo-expanded (345), crescendo (178), qwen3-8b-topic-anchored-v2 (177) |
| **Attack types** | persuasion-based (94), cipher-based (80), benign (175) | persuasion-based (172), Classic Crescendo (22), Obfuscation Path (20), Academic Disguise (23), Full Spectrum (23), Emotional Path (23), Mixed Emotional (20), Role+Obfuscation (22), DAN Variant (25), benign (350) |
| **Cipher-based** | 80 (23%) | **0** |
| **Benign source** | WildChat 真实对话 | LLM 生成的 crescendo 对话 |
| **ID overlap** | — | **0 条** |

### 分布偏移分析

这不是 "350 扩大到 1000"，而是**完全不同的数据集**：
1. **丢失了 cipher-based 攻击**（tom-gibbs 80 条全部消失）
2. **Benign 来源从真实对话变为 LLM 生成对话**
3. **所有数据都是 crescendo 风格的合成数据**

### exp17 结果（1000 样本训练后的 OOD 性能）

| 变体 | DD OOD F1 (avg) | AA OOD F1 (avg) | vs 350 原始 |
|------|-----|------|------|
| 9-class | 0.889 | 0.913 | DD -10.5pp, AA -5.9pp |
| MLM | 0.338 | 0.351 | **崩溃至 vanilla 水平** |
| Vanilla | 0.326 | 0.508 | — |

### 是否需要控制实验

**需要**。Reviewer 提出的 "1000 中随机抽 350 检验稳健性" 控制实验**不可行**——因为 expanded_1000 和原始 349 是完全不同的数据，不是超集关系。

正确的控制实验应该是：
1. 将原始 349 扩展到 1000（保持相同 source/attack-type 分布比例）
2. 或者在 expanded_1000 中加入 cipher-based + wildchat benign 数据来匹配原始分布
3. 性能下降的最可能解释是 **数据分布变化**（cipher-based 消失 + benign 来源变化），而非 "数据量增加导致下降"

---
