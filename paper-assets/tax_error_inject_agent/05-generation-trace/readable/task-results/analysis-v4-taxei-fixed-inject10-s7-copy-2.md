# analysis v4 taxei fixed inject10 s7

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v4-taxei-fixed-inject10-s7_20260515T210048_result.json`
- **Structured JSON:** [`c310385e84ec8575ca10.json`](../../sessions/c3/c310385e84ec8575ca10.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验 v4-taxei-fixed-inject10-s7 训练报告

| 项目 | 值 |
|------|-----|
| **checkpoint_path** | `/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject10_s7/v1-20260516-040128/checkpoint-1635` |
| **wandb_run_id** | 无（未配置 W&B） |
| **final_train_loss** | 0.4212 (avg)，末步 loss=0.237 |
| **final_token_acc** | 0.905 (末步) |
| **total_steps** | 1635 (3 epochs) |
| **training_time** | 57m 17s (3437s) |
| **train_speed** | 2.10 s/it |
| **memory** | 18.15 GiB |

### Checkpoint 结构

3个 epoch checkpoint，均为 LoRA adapter：
- `checkpoint-545` (epoch 1)
- `checkpoint-1090` (epoch 2)  
- `checkpoint-1635` (epoch 3, 最终)

每个 checkpoint 含 `adapter_model.safetensors` + `adapter_config.json`。

### 注意事项

1. **存在两个版本**：v0 (`v0-20260516-025729`) 和 v1 (`v1-20260516-040128`)，当前完成的是 v1。v0 也有完整的 3 个 checkpoint，可能需要清理以释放磁盘空间。
2. **bitsandbytes 警告**：`libnvJitLink.so.13` 加载失败，但未影响训练（量化功能未被使用）。
3. **模型**：Qwen3-8B + LoRA rank 16，cosine lr schedule，lr=1e-4，weight_decay=0.1。

---
