# exp gpu cleanup and dual restart

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_gpu-cleanup-and-dual-restart_20260520T063801_result.json`
- **Structured JSON:** [`7eaae18fc592c68c2b6c.json`](../../sessions/7e/7eaae18fc592c68c2b6c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**执行结果：**

| 步骤 | 状态 |
|------|------|
| Step 1: 杀孤儿进程 | 清理了 tmux server + 多轮重生的 vLLM 进程树，GPU 0/1 归零 |
| Step 2: 代码修复 | `sanitize_messages_for_template` 改为 try-except 方式；新增 `tensor_parallel_size` 参数兼容远程版本 |
| Step 2.5: Dry-run | Gemma + ScienceWorld 1 episode 通过，无 system role 错误 |
| Step 3: 双实验启动 | GPU 0=Llama ALFWorld, GPU 1=Gemma ScienceWorld，严格隔离 |
| Step 4: 验证 | 两个 tmux session + vLLM 进程正常 |
| Step 5: Registry | 两个实验状态更新为 RUNNING |

**发现并修复的额外问题：** `CUDA_VISIBLE_DEVICES` 在 shell 和代码中冲突——代码内部 `os.environ["CUDA_VISIBLE_DEVICES"] = str(gpu_id)` 会覆盖 shell 设定值。解决方案：不在 shell 设 `CUDA_VISIBLE_DEVICES`，用 `--gpu_id` 参数让代码自行管理。

---
