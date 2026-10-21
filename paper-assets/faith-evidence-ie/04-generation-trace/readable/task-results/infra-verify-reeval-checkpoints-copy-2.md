# infra verify reeval checkpoints

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_verify-reeval-checkpoints_20260516T030954_result.json`
- **Structured JSON:** [`16dce13bb516cc2b9194.json`](../../sessions/16/16dce13bb516cc2b9194.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

命令文件已写入。汇总：

### Checkpoint 验证

| Re-eval | 预期路径 | 状态 | 文件大小 |
|---------|---------|------|---------|
| reeval_ced_s42 | `rsft_output/checkpoint-510` | ✓ 存在 | 528MB |
| reeval_ced_s44 | `rsft_output_s44/checkpoint-510` | ✓ 存在 | 528MB |
| reeval_flat_nli_s42 | `rsft_output_flat_nli/checkpoint-510` | **✗ 不存在** | — |

### 问题：reeval_flat_nli_s42 的 checkpoint

`rsft_output_flat_nli/` 最大 checkpoint 是 **507**（非 510）。该目录的 checkpoint 列表：350, 400, 450, 500, **507**。checkpoint-507 的 adapter_model.safetensors 存在（528MB）。命令文件中已改用 checkpoint-507。

### 命令模板修正

任务模板与实际运行命令有 4 处差异（已按实际修正）：

| 项 | 模板（错误） | 实际 |
|----|------------|------|
| 模块 | `freige.evaluation.evaluate_docred` | `freige.eval.inference` |
| RSFT adapter 参数 | `--rsft_adapter` | `--model_path`（adapter checkpoint 路径） |
| 底座模型参数 | 无 | `--base_model /root/autodl-tmp/models/Qwen3-4B` |
| 数据路径参数 | `--data_dir` | `--data_path` |

### 3 条完整 eval 命令

已写入 `/root/autodl-tmp/reeval_commands_d076.txt`。`CUDA_VISIBLE_DEVICES={GPU}` 需在提交时替换为实际空闲 GPU 编号。当前 4 张 GPU 全部被占用（cuda:0/1/2/3 各有 eval 在跑），需等现有 eval 完成后才能提交。

---
