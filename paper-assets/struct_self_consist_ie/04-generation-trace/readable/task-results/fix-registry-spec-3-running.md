# fix registry spec 3 running

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_registry-spec-3-running_20260519T162019_result.json`
- **Structured JSON:** [`c9c4dff39bd143377aff.json`](../../sessions/c9/c9c4dff39bd143377aff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 3 个实验的 registry spec 已经是完整的，无需补全。

当前 registry 中的 spec 状态：

**1. exp_qwen25_32b_fewnerd** (autodl-5090, PID 804438 仍在运行)
- command: `CUDA_VISIBLE_DEVICES=0,1,2,3 FORCE_TORCHRUN=1 NNODES=1 NPROC_PER_NODE=4 llamafactory-cli train /root/autodl-tmp/struct_self_consist_ie/train_config_qwen25_32b_fewnerd_s42.yaml`
- server: autodl-5090
- gpu_ids: `["cuda:0", "cuda:1", "cuda:2", "cuda:3"]`
- model_name: Qwen2.5-32B-Instruct
- seed: 42
- data_path: `/root/autodl-tmp/struct_self_consist_ie/data/fewnerd/llmfactory_train.json`
- data_count: 131767
- log_path: `/root/autodl-tmp/struct_self_consist_ie/logs/train_qwen25_32b_fewnerd_s42.log`

**2. exp_qwen25_14b_fewnerd** (autodl-5090-c, PID 56773 仍在运行)
- command: `CUDA_VISIBLE_DEVICES=0,1 FORCE_TORCHRUN=1 NNODES=1 NPROC_PER_NODE=2 llamafactory-cli train train_config_qwen25_14b_fewnerd_s42.yaml`
- server: autodl-5090-c
- gpu_ids: `["cuda:0", "cuda:1"]`
- model_name: Qwen2.5-14B-Instruct
- seed: 42
- data_count: 131767
- log_path: `/root/autodl-tmp/struct_self_consist_ie/logs/train_qwen25_14b_fewnerd_s42.log`

**3. exp_qwen25_7b_fewnerd** (autodl-5090-c)
- command: `nohup bash run_fewnerd_qwen25_7b_pipeline.sh > logs/pipeline_qwen25_7b_fewnerd.log 2>&1 &`
- server: autodl-5090-c
- gpu_ids: `["cuda:2", "cuda:3"]`
- model_name: Qwen2.5-7B-Instruct
- seed: 42
- data_count: 131767
- log_path: `/root/autodl-tmp/struct_self_consist_ie/logs/pipeline_qwen25_7b_fewnerd.log`

关于 14B 日志文件名：registry 中记录为 `train_qwen25_14b_fewnerd_s42.log`（完整命名），注意日志实际在 `/root/autodl-tmp/struct_self_consist_ie/logs/` 而非 `/root/struct_self_consist_ie/logs/`。

---
