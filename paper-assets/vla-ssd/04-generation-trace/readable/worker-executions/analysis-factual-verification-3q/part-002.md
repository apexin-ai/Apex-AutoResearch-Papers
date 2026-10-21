# analysis factual verification 3q — Part 2 of 2

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../analysis-factual-verification-3q.md) · [Structured JSON](../../../sessions/b3/b3025f9a310d6a171f72.json)

## Before a recorded user message

### Assistant

_source line 164_

<details><summary>Logged reasoning block</summary>

```text
The LOOCV (leave-one-out cross-validation) results give different numbers:

**LOOCV untrained_last_preaction:**
- L8: mean=0.9664, std=0.0707 (per_fold: 0.982, 0.756, 0.972, 1.0, 0.996, 0.994, 0.994, 0.994, 0.976, 1.0)
- L16: mean=0.935, std=0.0719 (per_fold: 0.928, 0.744, 0.89, 0.99, 0.99, 0.988, 0.974, 0.976, 0.912, 0.958)


The LOOCV approach yields 96.64% for L8 and 93.5% for L16, which are closer to the paper's reported 95.5% and 91.1% but still don't align perfectly. The single split results (L8=98.2%, L16=92.3%) and dense variant (L8=98.6%) diverge even further, suggesting the paper may have used a different validation approach or data subset.

Now I'm pulling together the comprehensive results. Looking at the per-sample attention data from the summary file, I'm seeing around 25-26 instruction-attending heads across the samples, with most clustering around 25 heads above the 50% threshold, though a couple of heads are borderline. Let me count how many samples had exactly 25 heads to get a clearer picture for the final report. Looking at the averaged attention decomposition values across all 5 samples, I can see a clear clustering pattern: 24 heads are solidly above 50% in the instruction-dominant range, with two additional heads barely crossing that threshold around 50.8%, while the remaining 6 heads fall noticeably below 50%, creating a sharp boundary at roughly the 25th head.

For the frame count discrepancy, I'm realizing the paper likely excluded the final frame of each demonstration since there's no subsequent action to predict from it—that's exactly 500 frames (10 tasks × 50 demos), which accounts for the difference between the reported 63,228 and the actual 63,728 frames in the extracted features.

Now I'm putting together the full report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "face9bf5-3f87-4ce7-bcfa-f12fbdcef51d",
  "uuid": "8628b6f2-0785-447c-9765-aa51cadd74e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WabohawcJPS9dpV6u2VFNZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6877,
      "cache_read_input_tokens": 136210,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6877
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 165_

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

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "face9bf5-3f87-4ce7-bcfa-f12fbdcef51d",
  "uuid": "27d655b8-d252-4dcd-a24c-b7ef3240f7e7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WabohawcJPS9dpV6u2VFNZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6877,
      "cache_read_input_tokens": 136210,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6877
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Task result

_source line 166_

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

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 451836,
  "duration_api_ms": 425783,
  "num_turns": 65,
  "stop_reason": "end_turn",
  "session_id": "face9bf5-3f87-4ce7-bcfa-f12fbdcef51d",
  "total_cost_usd": 2.186249,
  "usage": {
    "input_tokens": 25,
    "cache_creation_input_tokens": 131246,
    "cache_read_input_tokens": 1548739,
    "output_tokens": 23582,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 131246,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 3393,
        "cache_read_input_tokens": 136210,
        "cache_creation_input_tokens": 6877,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 6877
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-opus-4-6": {
      "inputTokens": 25,
      "outputTokens": 23582,
      "cacheReadInputTokens": 1548739,
      "cacheCreationInputTokens": 131246,
      "webSearchRequests": 0,
      "costUSD": 2.1843320000000004,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    },
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1797,
      "outputTokens": 24,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001917,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "0e3f2e13-1295-4ff2-bd97-376d97099da9"
}
```

</details>

---
