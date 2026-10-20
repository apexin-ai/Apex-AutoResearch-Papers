# diag n paired investigation — Part 2 of 2

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../diag-n-paired-investigation.md) · [Structured JSON](../../../sessions/14/1401fdbdba527fa537ef.json)

## Round 1

### Assistant

_source line 244_

<details><summary>Logged reasoning block</summary>

```text
This is the complete picture now. Let me summarize:

**bf16 result:** 0 NaN in 410 positions → **bf16 completely eliminates NaN**

**fp16 NaN-filtered PPL recovery:**
- ALL 4 low segments had NaN, ALL can be RECOVERED with 7.5-16.3% NaN tokens filtered out
- All 4 mid segments: 2 had NaN (recoverable), 2 were already OK
- 11 high segments: 8 had NaN (recoverable), 3 were already OK
- PPL values after filtering look reasonable (1.09 - 1.70)


- Valid fraction ranges from 0.792 to 1.000 (mostly >0.85)

So NaN filtering would recover all 19 segments for this problem, turning ii_low from None to a valid value. The root cause is DeepSeek-R1-Distill-Qwen-7B in fp16 with eager attention producing NaN logits at roughly 8% of positions, originating in attention layer 27 and propagating through to the final logits. The low_sparsity segments are most affected because NaN positions are scattered throughout the sequence.

For smaller problems with fewer, larger segments, nearly every segment gets hit with at least one NaN position. The low_sparsity phase, which has the fewest segments concentrated early in generation, bears the brunt of this. Whether a problem is affected depends on the model and input—some inputs trigger NaN in layer 27 while others don't, and across 50 problems, roughly 23 consistently show NaN affecting their low phase.

I'm looking at two potential fixes: switching to bf16 eliminates NaN entirely but requires re-running profiling, while the quicker approach is to filter out NaN values before computing the mean perplexity, which recovers all segments with valid fractions above 80%.

The real question now is how these fixes affect the paired count—bf16 could potentially get us to 50/50 paired problems if no issues remain, while NaN filtering might recover most of those 23 missing problems. Let me draft the report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d74c8917-8deb-4a32-960f-664c8cbe8e4d",
  "uuid": "2b7ffd9b-1a53-4125-9693-66ea0859fd7d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LxGb5EdrVTsL6BgERqE6Dp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1879,
      "cache_read_input_tokens": 119964,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1879
      },
      "output_tokens": 8,
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

_source line 245_

数据完整了。以下是完整诊断报告。

---

## 诊断报告：per_problem_ii 低配对率根因分析

### 1. 根因

**DeepSeek-R1-Distill-Qwen-7B 在 fp16 + eager attention 下，约 8% 的 logit 位置产生 NaN。** 

验证 (problem `prealgebra/192`)：
- fp16 dense forward: **65/823 位置 logits NaN**，attention layer 27 有 NaN
- bf16 dense forward: **0/410 NaN**，零 NaN attention layers
- NaN 与 `output_attentions` 和 `.float()` 无关——源头在模型 fp16 推理的数值不稳定

### 2. 传播路径

```
Layer 27 attention NaN → logits NaN → CE loss NaN → ppl_from_cached_losses mean(含NaN)=NaN 
→ ppl_d=NaN → NaN>0=False → ii_val=NaN → 所有含NaN位置的segment全部失效
→ 若phase的ALL segments都有NaN → per_problem_ii记录None
```

### 3. 为什么 low_sparsity 受影响最重

NaN 位置散布在整个序列中（不局限于特定 phase）。但因为 quantile segmentation 产生的段数较多（每 problem 平均 20-34 个段），NaN 散点几乎命中每个段。low_sparsity 段集中在序列前半部，且段数通常 < high，被 100% 命中的概率更大。

### 4. 缺失矩阵

| 统计 | s015 | s020 | s025 | s030 |
|------|------|------|------|------|
| n_low present | 24 | 21 | 21 | 20 |
| n_paired(h∩l) | 22 | 19 | 19 | 16 |
| 始终缺失low (全4级) | 23/50 problems |

在 23 个始终缺失 low 的 problem 中：
- 15 个有 `ii_high=ok`（high段有NaN-free segments）
- 8 个 high 或 mid 也缺失
- 2 个三个 phase 全缺失 (precalculus/1199, geometry/465)

**缺失与段数、序列长度、token比例无统计相关性** ——纯粹取决于输入是否触发 layer 27 的 fp16 NaN。

### 5. 修复方案

| 方案 | 代码改动 | 效果 | 风险 | 需要重跑 |
|------|---------|------|------|---------|
| **A: bf16** | `torch_dtype=torch.bfloat16` | 0 NaN，预期 ~50/50 paired | 生成内容与fp16略有差异 | 需全量重跑 4 个 sparsity level |
| **B: NaN-filtered PPL** | PPL 计算中过滤 NaN CE | 恢复所有 valid_frac>0.79 的段 | PPL 估计有轻微偏差（丢弃 ~8% tokens） | 需重跑或写后处理脚本 |
| **A+B** | 两者并用 | bf16 消除 NaN + 过滤兜底 | 最稳健 | 重跑 |

NaN-filtered PPL 恢复效果 (prealgebra/192 实测)：
```
Phase low [  0:101] nan=11/101(10.9%) ppl=NaN → 1.69 (valid=89.1%) RECOVERED
Phase low [101:144] nan= 7/ 43(16.3%) ppl=NaN → 1.70 (valid=83.7%) RECOVERED
Phase low [144:197] nan= 4/ 53( 7.5%) ppl=NaN → 1.29 (valid=92.5%) RECOVERED
Phase low [197:292] nan= 8/ 95( 8.4%) ppl=NaN → 1.29 (valid=91.6%) RECOVERED
```
**全部 19 个段均可恢复。**

### 6. 具体代码位置

**需修改的文件：**

`pacs/profiling/run_profiling.py` line 69-72:
```python
# 改 torch.float16 为 torch.bfloat16
model = AutoModelForCausalLM.from_pretrained(
    model_path, torch_dtype=torch.bfloat16, ...  # FIX
)
```

`pacs/utils/metrics.py` line 56-80 (`ppl_from_cached_losses`):
```python
# 添加 NaN 过滤
selected = ce_losses[idx]
nan_mask = torch.isnan(selected) | torch.isinf(selected)
if nan_mask.any():
    selected = selected[~nan_mask]
if selected.numel() == 0:
    return float("nan")
return torch.exp(selected.mean()).item()
```

`pacs/profiling/interaction_index.py` line 293 (`compute_dense_forward_with_importance`):
```python
# 也加 .float() 保持与 compute_perplexity 一致
ce_losses = F.cross_entropy(logits[:-1].float(), labels[1:], reduction="none")
```

### 7. 建议

**推荐方案 A+B**：用 bf16 重跑 profiling（根治），同时在 PPL 计算中加 NaN 过滤作为安全网。重跑后预期 n_paired 达到 45-50/50。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d74c8917-8deb-4a32-960f-664c8cbe8e4d",
  "uuid": "8dc13171-ce24-4e6e-9d26-8045246640f5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LxGb5EdrVTsL6BgERqE6Dp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1879,
      "cache_read_input_tokens": 119964,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1879
      },
      "output_tokens": 8,
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

_source line 246_

数据完整了。以下是完整诊断报告。

---

## 诊断报告：per_problem_ii 低配对率根因分析

### 1. 根因

**DeepSeek-R1-Distill-Qwen-7B 在 fp16 + eager attention 下，约 8% 的 logit 位置产生 NaN。** 

验证 (problem `prealgebra/192`)：
- fp16 dense forward: **65/823 位置 logits NaN**，attention layer 27 有 NaN
- bf16 dense forward: **0/410 NaN**，零 NaN attention layers
- NaN 与 `output_attentions` 和 `.float()` 无关——源头在模型 fp16 推理的数值不稳定

### 2. 传播路径

```
Layer 27 attention NaN → logits NaN → CE loss NaN → ppl_from_cached_losses mean(含NaN)=NaN 
→ ppl_d=NaN → NaN>0=False → ii_val=NaN → 所有含NaN位置的segment全部失效
→ 若phase的ALL segments都有NaN → per_problem_ii记录None
```

### 3. 为什么 low_sparsity 受影响最重

NaN 位置散布在整个序列中（不局限于特定 phase）。但因为 quantile segmentation 产生的段数较多（每 problem 平均 20-34 个段），NaN 散点几乎命中每个段。low_sparsity 段集中在序列前半部，且段数通常 < high，被 100% 命中的概率更大。

### 4. 缺失矩阵

| 统计 | s015 | s020 | s025 | s030 |
|------|------|------|------|------|
| n_low present | 24 | 21 | 21 | 20 |
| n_paired(h∩l) | 22 | 19 | 19 | 16 |
| 始终缺失low (全4级) | 23/50 problems |

在 23 个始终缺失 low 的 problem 中：
- 15 个有 `ii_high=ok`（high段有NaN-free segments）
- 8 个 high 或 mid 也缺失
- 2 个三个 phase 全缺失 (precalculus/1199, geometry/465)

**缺失与段数、序列长度、token比例无统计相关性** ——纯粹取决于输入是否触发 layer 27 的 fp16 NaN。

### 5. 修复方案

| 方案 | 代码改动 | 效果 | 风险 | 需要重跑 |
|------|---------|------|------|---------|
| **A: bf16** | `torch_dtype=torch.bfloat16` | 0 NaN，预期 ~50/50 paired | 生成内容与fp16略有差异 | 需全量重跑 4 个 sparsity level |
| **B: NaN-filtered PPL** | PPL 计算中过滤 NaN CE | 恢复所有 valid_frac>0.79 的段 | PPL 估计有轻微偏差（丢弃 ~8% tokens） | 需重跑或写后处理脚本 |
| **A+B** | 两者并用 | bf16 消除 NaN + 过滤兜底 | 最稳健 | 重跑 |

NaN-filtered PPL 恢复效果 (prealgebra/192 实测)：
```
Phase low [  0:101] nan=11/101(10.9%) ppl=NaN → 1.69 (valid=89.1%) RECOVERED
Phase low [101:144] nan= 7/ 43(16.3%) ppl=NaN → 1.70 (valid=83.7%) RECOVERED
Phase low [144:197] nan= 4/ 53( 7.5%) ppl=NaN → 1.29 (valid=92.5%) RECOVERED
Phase low [197:292] nan= 8/ 95( 8.4%) ppl=NaN → 1.29 (valid=91.6%) RECOVERED
```
**全部 19 个段均可恢复。**

### 6. 具体代码位置

**需修改的文件：**

`pacs/profiling/run_profiling.py` line 69-72:
```python
# 改 torch.float16 为 torch.bfloat16
model = AutoModelForCausalLM.from_pretrained(
    model_path, torch_dtype=torch.bfloat16, ...  # FIX
)
```

`pacs/utils/metrics.py` line 56-80 (`ppl_from_cached_losses`):
```python
# 添加 NaN 过滤
selected = ce_losses[idx]
nan_mask = torch.isnan(selected) | torch.isinf(selected)
if nan_mask.any():
    selected = selected[~nan_mask]
if selected.numel() == 0:
    return float("nan")
return torch.exp(selected.mean()).item()
```

`pacs/profiling/interaction_index.py` line 293 (`compute_dense_forward_with_importance`):
```python
# 也加 .float() 保持与 compute_perplexity 一致
ce_losses = F.cross_entropy(logits[:-1].float(), labels[1:], reduction="none")
```

### 7. 建议

**推荐方案 A+B**：用 bf16 重跑 profiling（根治），同时在 PPL 计算中加 NaN 过滤作为安全网。重跑后预期 n_paired 达到 45-50/50。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 1324713,
  "duration_api_ms": 1213089,
  "num_turns": 49,
  "stop_reason": "end_turn",
  "session_id": "d74c8917-8deb-4a32-960f-664c8cbe8e4d",
  "total_cost_usd": 3.866710799999999,
  "usage": {
    "input_tokens": 43,
    "cache_creation_input_tokens": 110002,
    "cache_read_input_tokens": 3230771,
    "output_tokens": 53808,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 110002,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 2188,
        "cache_read_input_tokens": 119964,
        "cache_creation_input_tokens": 1879,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1879
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2391,
      "outputTokens": 8098,
      "cacheReadInputTokens": 858318,
      "cacheCreationInputTokens": 71748,
      "webSearchRequests": 0,
      "costUSD": 0.2183978,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 43,
      "outputTokens": 53808,
      "cacheReadInputTokens": 3230771,
      "cacheCreationInputTokens": 110002,
      "webSearchRequests": 0,
      "costUSD": 3.648312999999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "c22bdf10-a5ab-4a0f-b4ca-8f2e64820389"
}
```

</details>

---
