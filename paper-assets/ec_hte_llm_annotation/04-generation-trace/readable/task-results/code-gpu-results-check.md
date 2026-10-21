# code gpu results check

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gpu-results-check_20260521T214556_result.json`
- **Structured JSON:** [`59c37db79365d4592a32.json`](../../sessions/59/59c37db79365d4592a32.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 标注 CSV 完成情况（全部完成）

| 模型 | 文件 | 行数 | 状态 |
|------|------|------|------|
| Llama-3.1-8B | `exp008_checkpoint_llama-3.1-8b_balanced.csv` | 501 | 完成 |
| Qwen2.5-7B | `exp008_checkpoint_qwen2.5-7b_balanced.csv` | 501 | 完成 |
| Gemma-2-9B | `exp008_checkpoint_gemma-2-9b_balanced.csv` | 501 | 完成 |
| Mistral-7B | `exp008_checkpoint_mistral-7b_balanced.csv` | 501 | 完成 |

所有 4 个模型均已完成标注，每个 CSV 501 行（1 header + 500 数据行）。

### 初步分析结果（已自动生成 `multi_llm_summary.csv`）

| 模型 | Accuracy | RMSE (naive) | RMSE (global) | RMSE (ec_hte) | Winner |
|------|----------|-------------|---------------|---------------|--------|
| Llama-3.1-8B | 0.542 | 0.408 | 0.193 | 0.408 | global |
| Qwen2.5-7B | 0.702 | 0.440 | 0.325 | 0.440 | global |
| Gemma-2-9B | 0.616 | 0.325 | 0.278 | 0.325 | global |
| Mistral-7B | 0.668 | 0.453 | 0.314 | 0.453 | global |

### 当前服务器状态
- **GPU**: 4 块 GPU 全部空闲（0% 利用率，0 MiB 显存）
- **进程**: 无 Python 标注/下载进程运行中
- **所有任务已完成**

---
