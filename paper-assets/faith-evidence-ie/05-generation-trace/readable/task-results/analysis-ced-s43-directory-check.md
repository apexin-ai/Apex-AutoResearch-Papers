# analysis ced s43 directory check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_ced_s43_directory_check_20260516T000646_result.json`
- **Structured JSON:** [`fb9411b251aa0ae74229.json`](../../sessions/fb/fb9411b251aa0ae74229.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 1. rsft_output_s43 真实状态

**存在**，但**不是 CED 数据**。它是标准 RSFT（非 CED-filtered）seed=43 训练产物：
- Base model: Qwen3-4B, LoRA r=64/alpha=128
- Checkpoints: 350, 400, 450, 500, 510（训练已完成）
- 与 `rsft_output_s44` 同系列，属于原始 RSFT seed 扩展实验
- CED-filtered RSFT 的输出目录应为 `rsft_output_ced_s43`，该目录**不存在**

### 2. rsft_ced_s43_train 启动状态

**未在运行**。GPU 1 完全空闲（0MiB）。Registry 中 `rsft_ced_s43_train` 状态为 DONE/failed（~8小时前标记）。之前 worker 报告的"已提交"实际未成功启动。

### 3. 当前 GPU 占用

| GPU | 占用 | 进程 |
|-----|------|------|
| 0 | 10.8GB | eval flat_nli_s44 |
| 1 | **空闲** | - |
| 2 | 19.9GB | eval rsft_topk3 reeval |
| 3 | 10.8GB | eval flat_nli_s45 |

### 4. rsft_ced_s45_train_r2

已创建，状态 PREPARING。

**下一步**：GPU 1 空闲，可立即提交 CED RSFT s43 训练（需重新提交），s45 等后续 GPU 释放。

---
