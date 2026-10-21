# train cls 8b conda westd

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_cls-8b-conda-westd_20260513T220537_result.json`
- **Structured JSON:** [`2c3fec80665cfcc2f068.json`](../../sessions/2c/2c3fec80665cfcc2f068.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功启动并更新为 RUNNING。

**总结：**
- 实验 `repo-level-cls-8b-conda` 在 westd-48478 cuda:3 上运行中
- tmux session: `cls8b-conda`, PID: 185438
- 配置: Qwen3-8B, batch=1, grad_accum=32, LoRA r=16, conda env (transformers 4.57.6)
- GPU 显存: 25751/32607 MiB，无 OOM 风险
- 6633 total steps, ~8.3s/step, 预计约 15 小时完成
- 模型通过 ModelScope 下载到 `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/`（HuggingFace 不可达）

---
