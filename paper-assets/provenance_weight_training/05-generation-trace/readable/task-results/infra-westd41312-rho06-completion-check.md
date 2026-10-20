# infra westd41312 rho06 completion check

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westd41312_rho06_completion_check_20260520T075327_result.json`
- **Structured JSON:** [`3d0f180e61d0c20e50ae.json`](../../sessions/3d/3d0f180e61d0c20e50ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. GPU 状态
四卡全部空闲（0 MiB / 0% utilization），无 GPU 进程。训练已结束。

### 2. 三组训练完成状态

| Seed | 最终 Step | EXIT_CODE | 耗时 | 状态 |
|------|----------|-----------|------|------|
| 42 | 6103/6103 | 0 | 3:44:11 | **正常完成** |
| 123 | 6103/6103 | 0 | 3:44:13 | **正常完成** |
| 456 | 6103/6103 | 0 | 3:43:17 | **正常完成** |

### 3. Checkpoint 目录

| Seed | `final/` | `checkpoint-6103/` | model.safetensors |
|------|----------|-------------------|-------------------|
| 42 | ✓ | ✓ | 1.19 GB |
| 123 | ✓ | ✓ | 1.19 GB |
| 456 | ✓ | ✓ | 1.19 GB |

每个 final 目录包含完整文件：config.json, model.safetensors, tokenizer.json, tokenizer_config.json, training_args.bin, generation_config.json, chat_template.jinja。

### 4. Final Metrics

| Seed | train_loss | train_samples/s | train_steps/s | epoch |
|------|-----------|----------------|--------------|-------|
| 42 | 9.358 | 7.259 | 0.454 | 0.2629 |
| 123 | 9.352 | 7.258 | 0.454 | 0.2629 |
| 456 | 9.342 | 7.289 | 0.456 | 0.2629 |

三组 seed 全部在 step 6103 正常完成，train_loss 一致（~9.35），模型已保存到 final 目录。服务器 GPU 已释放。

---
