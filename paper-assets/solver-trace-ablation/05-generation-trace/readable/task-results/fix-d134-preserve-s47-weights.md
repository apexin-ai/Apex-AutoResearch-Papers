# fix d134 preserve s47 weights

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_d134-preserve-s47-weights_20260518T104733_result.json`
- **Structured JSON:** [`7755a5a027faf99469d8.json`](../../sessions/77/7755a5a027faf99469d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成。汇报：

**Pipeline 状态**：已崩溃，未在运行。ISR s47 在 step 21/500 OOM 退出，尚未产生任何 model weights。GPU 空闲，无残留进程。

**脚本修改**（第 80-91 行）：
- `SEED != 47`：正常删除 safetensors、index.json、optimizer、training_args、global_step
- `SEED == 47`：保留 safetensors 和 index.json，仅清理 optimizer 和 global_step（节省空间但保留推理所需权重）

**需要注意**：4B 模型在单卡 A100 95GB 上 OOM，pipeline 重启前需要解决显存问题（减小 batch size、启用 gradient checkpointing 等），否则 s47 训练会再次失败。

---
