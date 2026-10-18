# diagnose exp docred bcs expanded

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_docred_bcs_expanded_20260519T124512_result.json`
- **Structured JSON:** [`ddcfff9d6bd96d2b7f72.json`](../../sessions/dd/ddcfff9d6bd96d2b7f72.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断结果：

**进度**: 完成 6/40 新 batches（batch 7 正在推理时被 kill）。日志显示 batch 1-6 的 accuracy 在 0.42-0.47 之间。

**无法 resume**: 
- 脚本**不支持断点恢复**——没有 resume/checkpoint 逻辑
- `run_incremental_inference` 将所有新 batch 结果累积在内存中的 `all_results` 列表，只在全部 40 个 batch 跑完后一次性写入 `all_predictions.json`
- 输出目录只有 `preprocess_config.json`（686KB）和 `run.log`（23KB），没有中间结果文件
- 已完成的 6 个 batch 的推理结果**全部丢失**

**可复用的部分**: 
- `preprocess_config.json` 仍在，包含 batch 配置和样本数据，preprocess 阶段不需要重跑
- 旧实验 `exp_docred_confusability` 的 predictions 仍可复用（脚本设计就是增量的，从那里加载已有 BCS predictions）

**GPU 状态**: RTX PRO 6000 (98GB), 0% 利用率，完全空闲可用。

**建议**: 直接用 `--stage infer` 重跑推理阶段（跳过 preprocess），40 个 batch 全部重跑。每个 batch 约 3-4 秒推理，加上模型加载 ~40 秒，总计约 3-4 分钟。或者，可以先给脚本加 per-batch checkpoint 逻辑再跑，避免下次中断又白跑。

---
