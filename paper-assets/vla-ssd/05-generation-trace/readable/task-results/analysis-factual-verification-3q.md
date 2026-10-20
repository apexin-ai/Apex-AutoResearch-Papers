# analysis factual verification 3q

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_factual_verification_3q_20260518T194526_result.json`
- **Structured JSON:** [`01d65c38fff11958a354.json`](../../sessions/01/01d65c38fff11958a354.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data needed. Let me compile the final report.

## 问题 1：24 vs 25 heads

**数据来源：** `/root/autodl-tmp/vla-ssd/results/attention_decomposition.json`（5 sample 平均）+ `/root/autodl-tmp/vla-ssd/results/attention/threshold_sensitivity.json`

**所有 32 个 L1 head 的 instruction attention fraction（trained model，降序）：**

| 排名 | Head ID | Instruction Fraction |
|------|---------|---------------------|
| 1 | head_0 | 85.70% |
| 2 | head_22 | 82.22% |
| 3 | head_25 | 78.50% |
| 4 | head_14 | 71.65% |
| 5 | head_10 | 71.64% |
| 6 | head_2 | 69.45% |
| 7 | head_27 | 68.22% |
| 8 | head_19 | 65.09% |
| 9 | head_15 | 61.97% |
| 10 | head_29 | 60.72% |
| 11 | head_8 | 58.93% |
| 12 | head_4 | 58.54% |
| 13 | head_23 | 58.34% |
| 14 | head_11 | 57.76% |
| 15 | head_7 | 57.37% |
| 16 | head_26 | 57.00% |
| 17 | head_17 | 55.88% |
| 18 | head_31 | 54.94% |
| 19 | head_30 | 54.58% |
| 20 | head_1 | 54.50% |
| 21 | head_18 | 54.14% |
| 22 | head_16 | 53.73% |
| 23 | head_20 | 53.43% |
| 24 | head_12 | 52.96% |
| **25** | **head_5** | **50.80%** |
| **26** | **head_28** | **50.76%** |
| 27 | head_3 | 47.27% |
| 28 | head_9 | 45.61% |
| 29 | head_21 | 45.26% |
| 30 | head_13 | 41.35% |
| 31 | head_6 | 40.70% |
| 32 | head_24 | 37.42% |

**第 25 个 head：** head_5, fraction=50.8%
**第 26 个 head：** head_28, fraction=50.76%

**结论：** 边界效应。head_5 和 head_28 的平均 instruction fraction 仅比 50% 高 0.8% 和 0.76%。但在单个 sample 中不一致（head_5 在 task_0 中为 49.8%，task_2 中为 50.2%；head_28 在 task_2 中为 49.9%，task_0 中为 50.3%）。

- `threshold_sensitivity.json` 记录 L1@0.5 = **24** heads（可能使用 per-sample majority voting）
- `attention_decomposition.json` 的 `head_classification` 列出 **24** instruction_dominant（将 head_5、head_28 归入 control）
- Registry `llama2_base_control` 记录 **25**（可能直接从平均值计数 >50%，但只计了一个边界 head）
- 从平均值严格计数 >50% 实际是 **26**

**论文用 24 是合理的** — 这是 robustly instruction-dominant 的集合，排除了两个在 50% 边界振荡的 head。Registry 的 25 是计数方法差异。

---

## 问题 2：总帧数

**数据来源：**
- `/root/autodl-tmp/vla-ssd/results/ood_diagnostics.log`："Loaded: **63728** samples"
- H5 文件直接计数（`/root/autodl-tmp/vla-ssd/features/trained_libero_goal/`）：10 tasks × 50 demos 逐 demo 求和 = **63,728**

**实际帧数：63,728**

**差异原因：** 63,728 − 63,228 = **500** = 10 tasks × 50 demos = 恰好每个 demo 1 帧。论文的 63,228 很可能是将每个 demo 的帧数计为 `(demo_length − 1)`（排除最后一帧，因为最后一帧没有 next action `a_{t+1}` 作为预测目标）。但实际提取的 H5 特征包含所有帧（含最后一帧）。

**结论：两个数字都可以是"正确的"，取决于上下文：**
- 63,728 = 实际提取的特征帧数（H5 文件中的总 sample 数）
- 63,228 = 可用于 action prediction 的帧数（排除每个 demo 的最后帧）

论文如果指的是 "total frames extracted"，应改为 63,728。如果指的是 "frames with valid next-action labels"，63,228 是正确的（但需要在文中说明）。

---

## 问题 3：Untrained readout 百分比

**数据来源及各实验结果：**

| 实验 | 文件 | 方法 | Untrained L8 | Untrained L16 |
|------|------|------|-------------|--------------|
| cross_instruction (sparse, single split) | `classification_results.json` | 8-task train, 2-task test, PCA256+LogReg | **98.2%** | **92.3%** |
| cross_instruction_dense (L0-L8) | `classification_results.json` | 同上, dense L0-L8 | **98.6%** | N/A |
| cross_instruction LOOCV | `loocv_results.json` | 10-fold LOOCV, PCA256+LogReg | **96.64%** (std=7.07%) | **93.5%** (std=7.19%) |
| cross_instruction_spatial | `classification_results.json` | LIBERO-Spatial, 10-layer | **68.3%** | **76.5%** |

**论文写 L8=95.5%, L16=91.1% — 在所有原始数据文件中均未找到精确匹配。**

**Registry 写 L8=98.6%, L16=92.0%：**
- L8=98.6% 来自 cross_instruction_dense 实验（`dense_probe_L8_acc.untrained=0.986`）
- L16=92.0% 来自 cross_instruction sparse 实验的 92.3% 四舍五入（sparse 实验 L16=0.923，dense 实验未覆盖 L16）

**两组数字来源差异：**
- Registry 的数字（98.6%, 92.0%）可以在原始数据中找到来源（dense 实验的 L8 和 sparse 实验的 L16 四舍五入）
- 论文的数字（95.5%, 91.1%）**无法在任何现存数据文件中找到**。最接近的是 LOOCV 结果（96.64%, 93.5%），但仍不匹配。可能来自已删除/覆盖的早期实验版本，或手动输入时的错误

**建议：** 论文应使用 registry 中的数字（即原始实验可追溯的数字），并注明实验设置（单次 train/test split vs LOOCV）。如果要用 LOOCV 数字，应报告 96.6% 和 93.5%。

---
