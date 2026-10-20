# diag n paired investigation

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_n-paired-investigation_20260514T045036_result.json`
- **Structured JSON:** [`893d1d50ada4ec78739c.json`](../../sessions/89/893d1d50ada4ec78739c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

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

---
