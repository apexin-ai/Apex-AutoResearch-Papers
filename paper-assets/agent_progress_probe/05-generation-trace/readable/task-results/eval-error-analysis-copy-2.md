# eval error analysis

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_error-analysis_20260514T154931_result.json`
- **Structured JSON:** [`b1317f2c5ffb23fea32f.json`](../../sessions/b1/b1317f2c5ffb23fea32f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。整理报告。

---

## Probe-001 错误分析报告

### 总览

| 指标 | 值 |
|---|---|
| Test set 大小 | 1824 (conf≥2) |
| 总错误 | **131** (7.18%) |
| FP (预测 progress 实为 stagnation) | **85** (64.9%) |
| FN (预测 stagnation 实为 progress) | **46** (35.1%) |
| Macro F1 | 0.9055 (F1_prog=0.9518, F1_stag=0.8593) |

---

### 1. 按 LF 投票分析

**各 LF 投票的错误率：**

| LF | 投票 | 总数 | 错误 | 错误率 |
|---|---|---|---|---|
| command_repetition | stagnation (0) | 306 | 39 | **12.75%** |
| outcome_backprop | stagnation (0) | 403 | 37 | 9.18% |
| file_diff_delta | abstain (-1) | 794 | 62 | 7.81% |
| file_diff_delta | progress (1) | 705 | 52 | 7.38% |
| outcome_backprop | abstain (-1) | 1382 | 93 | 6.73% |
| command_repetition | progress (1) | 946 | 61 | 6.45% |
| command_repetition | abstain (-1) | 572 | 31 | 5.42% |
| file_diff_delta | stagnation (0) | 325 | 17 | 5.23% |
| outcome_backprop | progress (1) | 39 | 1 | **2.56%** |

**关键发现**：
- `command_repetition=stagnation` 的窗口错误率最高 (12.75%)，是均值的近2倍
- `outcome_backprop=progress`（resolved 最终窗口）几乎不出错 (2.56%)

**LF 冲突分析：**

| 子集 | 一致 | 冲突 | 全弃权 |
|---|---|---|---|
| 全部 test | 1089 (59.7%) | 565 (31.0%) | 170 (9.3%) |
| 错误样本 | 68 (51.9%) | 52 (**39.7%**) | 11 (8.4%) |

错误样本中 LF 冲突率 (39.7%) 显著高于全集 (31.0%)，说明 LF 不一致是错误的重要信号。

---

### 2. 按 Confidence 分

| Conf | 样本数 | 错误 | 错误率 | Macro F1 |
|---|---|---|---|---|
| 2 | 1780 (97.6%) | 126 | 7.08% | 0.9078 |
| 3 | 44 (2.4%) | 5 | 11.36% | 0.6906 |

Conf=3 的 macro F1 大幅下降到 0.69，但样本量极小（44个），其中 stagnation 仅 4 个。**conf=3 的低 F1 是小样本效应，非系统性退化。**

---

### 3. 按 Trajectory Outcome 分

| Outcome | 样本数 | 错误 | 错误率 | FP | FN |
|---|---|---|---|---|---|
| Resolved | 77 | 1 | **1.30%** | 1 | 0 |
| Unresolved | 1747 | 130 | **7.44%** | 84 | 46 |

**Resolved 轨迹几乎无误**（仅1个FP），说明 outcome_backpropagation 为模型提供了强信号。131个错误中130个来自 unresolved 轨迹。

---

### 4. 按时序位置分

| 位置 | 总数 | 错误 | 错误率 | FP | FN |
|---|---|---|---|---|---|
| Early (0-33%) | 351 | 23 | 6.55% | 16 | 7 |
| **Middle (33-66%)** | 353 | **36** | **10.20%** | 20 | 16 |
| Late (66-100%) | 1070 | 69 | 6.45% | 46 | 23 |
| Single window | 50 | 3 | 6.00% | 3 | 0 |

**轨迹中段错误率最高 (10.2%)**，比两端高约50%。中段 FN 比例也更高（16/36=44% vs early 的 30%），说明模型在轨迹中段更难区分「探索中的进展」和「停滞」。

---

### 5. FP vs FN 模式深度对比

#### FP（85个，预测 progress 实为 stagnation）

- **模型极度自信**：mean prob=0.922，73% 的 FP 概率>0.9，median=0.98
- LF 投票：41/85 (48%) 的 `file_diff_delta` 弃权，35/85 (41%) 的 `command_repetition` 投 progress——说明这些窗口在文件编辑和命令多样性上看起来像 progress，但 ground truth 是 stagnation
- 33% 的 `outcome_backprop` 投 stagnation，但模型忽略了这个信号
- 集中在 late 位置 (46/85=54%)

**FP 核心模式**：agent 在做编辑、命令多样（LF 看起来像 progress），但实际是无效编辑/错误方向的修改。模型被表面行为特征欺骗，且预测概率极高，说明这不是边界案例而是系统性盲区。

#### FN（46个，预测 stagnation 实为 progress）

- 模型概率较低但有分散：mean=0.205，35% prob<0.1
- LF 投票：26/46 (57%) 的 `command_repetition` 投 progress，但 22/46 (48%) 的 `file_diff_delta` 弃权
- 80% 的 `outcome_backprop` 弃权
- middle + late 占 85%

**FN 核心模式**：agent 实际在做有效进展，但因为重复了某些命令模式（或文件编辑信号弱），模型将其判为 stagnation。

---

### 6. 错误集中度

- 77 条轨迹包含至少 1 个错误（共 543 条测试轨迹，14.2%）
- **Top 2 轨迹贡献 24/131 = 18.3% 的错误**：
  - `astropy__specutils-976...r3071`：13/15 窗口全错 (87%)
  - `asottile__pyupgrade-360...r3069`：11/11 窗口全错 (100%)
- 有 4 条轨迹 100% 错误率，属于系统性误判

---

### 关键发现总结

1. **FP 占主导** (65%)，且模型对 FP 极度自信（prob>0.9），这是最需解决的问题
2. **LF 冲突是错误强信号**：错误样本冲突率 40% vs 全集 31%
3. **command_repetition=stagnation 时错误率最高** (12.75%)——该 LF 投 stagnation 但模型倾向预测 progress
4. **轨迹中段最容易出错** (10.2%)，进展与停滞的行为边界模糊
5. **Resolved 轨迹几乎免疫**（1.3% 错误率），unresolved 轨迹承担了 99% 的错误
6. **错误高度集中**：top 2 轨迹贡献 18% 错误，可能是 label noise 或极端边界案例

---
