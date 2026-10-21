# ops check and complete base model download

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-and-complete-base-model-download_20260515T182554_result.json`
- **Structured JSON:** [`9ac7e32afadd37b8a6f7.json`](../../sessions/9a/9ac7e32afadd37b8a6f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 模型下载状态
- **model-00002-of-000002.safetensors** (6.2G): 已完成 ✓
- **model-00001-of-000002.safetensors** (8.0G): 下载中，453MiB/8.0GiB (5%)，速度 **8.9MiB/s**，**ETA ~14分钟**
- 之前有 6 个冲突下载进程互相覆盖，已全部杀掉并用单个 aria2c (16连接) 重新下载

### 脚本状态
`run_grpo_unpruned.sh` 的 `--model_path` 已指向 `/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B`，**无需更新**。脚本使用 `CUDA_VISIBLE_DEVICES=0`，与当前 cuda:1 上运行的 v8 训练不冲突。

### GPU 占用
- **cuda:0**: 空闲，等模型就绪即可启动 unpruned GRPO
- **cuda:1**: 正在运行 `grpo_stage2_standard_20_v8` (PID 534667)

### 下一步
模型预计 **~14分钟后就绪**（约 02:42 UTC）。下载完成后需要验证 model-00001 完整性，然后即可执行 `bash /root/recovery_aware_struct_prune/run_grpo_unpruned.sh` 启动训练。

---
