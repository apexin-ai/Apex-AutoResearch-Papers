# ops gpu cascade fix v2

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_cascade_fix_v2_20260515T182206_result.json`
- **Structured JSON:** [`c1282d7944fa4408ad43.json`](../../sessions/c1/c1282d7944fa4408ad43.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

双卡满载运行，任务完成。

---

## 执行结果汇总

### 1. 清理前后 nvidia-smi 对比

| 时间 | GPU 0 | GPU 1 |
|------|-------|-------|
| 清理前 | 0 MiB (空闲) | 31820 MiB (PID 295339 Qwen 错误占用) |
| 清理后 | 0 MiB | 0 MiB |
| 重新提交后 | 37807 MiB / 99% (Llama) | 44597 MiB / 99% (Qwen) |

### 2. 训练脚本 CUDA_VISIBLE_DEVICES 检查

两个脚本中 `CUDA_VISIBLE_DEVICES=0` 仅出现在 docstring 的 usage 示例中（注释），**无实际代码硬编码**，无需修改。`os.environ` 只设置 WANDB 变量，无 `cuda:X` 硬编码。

根因确认：之前提交命令中手动写了 `CUDA_VISIBLE_DEVICES=0`，覆盖了 wrapper 注入的值。

### 3. 提交命令和 PID

| 任务 | GPU | PID | CUDA_VISIBLE_DEVICES |
|------|-----|-----|---------------------|
| Qwen DocRED LoRA (`w5_qwen_docred_lora_training`) | cuda:1 | 298245 (实际 GPU 进程 298250) | 1 |
| Llama DocRED LoRA (`w5_llama_docred_lora_training`) | cuda:0 | 298323 (实际 GPU 进程 298328) | 0 |

命令均为：`bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/schema_semantic_constrained_ie && WANDB_MODE=disabled python3 scripts/train_lora_docred{_llama}.py"`，不含 CUDA_VISIBLE_DEVICES，由 submit_training_job wrapper 自动注入。

### 4. 最终双卡状态

- **GPU 0**: Llama, 37807 MiB / 97887 MiB, 99% util, 462W
- **GPU 1**: Qwen, 44597 MiB / 97887 MiB, 99% util, 449W
- 两个训练都已进入 training loop (0/573 steps)

---
