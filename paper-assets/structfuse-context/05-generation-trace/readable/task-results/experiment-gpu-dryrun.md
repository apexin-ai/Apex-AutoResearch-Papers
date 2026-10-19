# experiment gpu dryrun

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_gpu_dryrun_20260512T111049_result.json`
- **Structured JSON:** [`b79008d9ec671582d1be.json`](../../sessions/b7/b79008d9ec671582d1be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证完成。汇总报告：

---

## Dry-Run 验证报告

### 1. 模型下载
- **路径**: `/root/structfuse/models/Qwen/Qwen2.5-Coder-3B/`
- **文件**: model-00001 (4.62GB) + model-00002 (1.13GB) + tokenizer + config 齐全
- **下载方式**: hf-mirror.com via huggingface-cli (AutoDL 网络受限，多进程竞争带宽是主要瓶颈)

### 2. Dry-Run 训练
- **Final eval loss**: 0.1949
- **训练步 loss**: 0.6604 (正常正数，非 nan/inf)
- **Recall@1/5/10**: 1.0 (dummy 数据上符合预期)

### 3. Checkpoint 验证
- **Projection head**: ✅ 4 keys (`projection.0.weight/bias`, `projection.2.weight/bias`)
- **LoRA**: ✅ 144 keys (q_proj + v_proj × 36 layers × lora_A/B)
- **Temperature**: ✅ `log_temperature`
- **总参数 keys**: 583

### 4. Eval 加载验证
- **Checkpoint 加载**: ✅ `load_state_dict` 成功
- **Embedding shape**: `(1, 256)` ✅ (proj_dim=256)
- **Embedding norm**: 1.0 ✅ (L2 归一化)

### 5. GPU 显存
- **推理峰值**: 11.54 GB / 24 GB
- **训练峰值**: 11.59 GB / 24 GB (batch_size=2, num_negatives=2, max_seq_length=512)
- **剩余**: ~12.4 GB — 24GB 充裕，可增大 batch_size 或 max_seq_length

### 6. 修复的问题
- **train.py bug**: `__getitem__` 中 miner 返回的 tuple 被当作 dict 调用 `.get()` → 添加 `isinstance(neg_item, tuple)` 分支处理
- **gradient checkpointing warning**: `None of the inputs have requires_grad=True` — LoRA 配合 gradient checkpointing 的已知 warning，不影响训练正确性（LoRA 参数的梯度正常计算）

---
