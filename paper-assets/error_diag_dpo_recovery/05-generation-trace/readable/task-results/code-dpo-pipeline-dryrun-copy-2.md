# code dpo pipeline dryrun

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_dpo-pipeline-dryrun_20260513T085943_result.json`
- **Structured JSON:** [`7730248f06822b4191ea.json`](../../sessions/77/7730248f06822b4191ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全 pipeline dry-run 完成。汇报如下：

---

## v9 DPO Pipeline Dry-Run 报告

| 指标 | 值 |
|------|-----|
| **v9 早期数据（合并后）** | 75 条 trajectory（3 GPU × 1 file） |
| **failure trajectories（reward=False）** | 26 条 |
| **DPO pairs 产出** | **21 对** |
| **跳过** | 5 条（no_expert_match） |
| **匹配率** | 21/26 = 80.8% |

### d / gamma_e 值域

| 字段 | min | max | mean | median |
|------|-----|-----|------|--------|
| d | 0.0000 | 0.6250 | 0.0837 | 0.0000 |
| gamma_e | 0.8500 | 0.9437 | 0.8626 | 0.8500 |

### divergence 分布
- 90.5% early (d<0.2)，4.8% mid，4.8% late
- divergence_step: min=1, max=6, mean=1.8, step1=14（67% 在第一步就分歧）

### 输出字段
`prompt, chosen, rejected, error_type, gamma_e, d, correction_span, task_id, task_type, game_file, failure_step, divergence_step, metadata`

### train_dpo.py 数据加载
DPODataset 加载 21 samples 成功，tokenize 无报错。注意 sample 0 和 2 的 prompt_len 已达 max_length=2048 上限，训练时可能需要加大 `--max_length`。

### 需注意
1. **Qwen3-8B 模型路径缺失**：`/root/autodl-tmp/.hf_cache/Qwen3-8B/` 不存在（可能是 ModelScope 缓存格式），正式训练前需确认模型路径或重新下载
2. **5 条 no_expert_match**：这些 game_file 在 expert 库中没有对应项，属正常（expert 覆盖率非 100%）
3. **多数 divergence 发生在 step 1**：v9 ICL 数据中 agent 倾向在开头就偏离 expert 路径

---
