# infra bjb1 21071 gpu check

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_bjb1_21071_gpu_check_20260514T134621_result.json`
- **Structured JSON:** [`b64a04810fcbd5ee4e0c.json`](../../sessions/b6/b64a04810fcbd5ee4e0c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

检查完成，汇总如下：

## GPU 状态

| GPU | 型号 | 显存总量 | 已占用 | 利用率 | 状态 |
|-----|------|---------|--------|--------|------|
| 0 | RTX 5090 | 32607 MiB | 2 MiB | 0% | 空闲 |
| 1 | RTX 5090 | 32607 MiB | 2 MiB | 0% | 空闲 |
| 2 | RTX 5090 | 32607 MiB | 2 MiB | 0% | 空闲 |
| 3 | RTX 5090 | 32607 MiB | 2 MiB | 0% | 空闲 |

## 遗留进程
无。`nvidia-smi` 查询无 GPU 计算进程。

## LLaMA Checkpoint
**完整。** `llama3.1-8b-scierc-lora/` 包含：
- `adapter_model.safetensors` (335MB)
- `adapter_config.json`、tokenizer 文件、训练日志
- 3 个中间 checkpoint（400/500/585 步）
- `all_results.json`、`eval_results.json`、`train_results.json`

此外 checkpoints 目录下还有多个 Qwen3 模型（conll2003/scierc/wnut17 的 lora 和 merged 版本）。

## 代码版本
项目目录 `/root/autodl-tmp/struct_self_consist_ie/` 不是 git 仓库（无 `.git` 目录），无法查看 git log。代码可能是直接复制上去的，不受版本控制。

**结论：4 张 RTX 5090 全部空闲可用，无遗留进程，checkpoint 完整。如需 git 管理代码需重新初始化或 clone。**

---
