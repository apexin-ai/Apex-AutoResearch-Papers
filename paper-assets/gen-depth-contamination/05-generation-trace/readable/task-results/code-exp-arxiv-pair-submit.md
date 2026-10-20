# code exp arXiv pair submit

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_arXiv_pair_submit_20260517T112129_result.json`
- **Structured JSON:** [`eb44f5423d705c25f943.json`](../../sessions/eb/eb44f5423d705c25f943.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已经有这两个实验的条目（状态 ALLOCATED），且 `submit_training_job` 已自动更新了 spec 中的 command/server/gpu/pid/log_path 等信息。不需要再手动 update_registry。

两个实验已成功提交并在运行：

| 实验 | GPU | PID | 模型 | 状态 |
|------|-----|-----|------|------|
| exp_arXiv_olmo | cuda:0 | 26733 | OLMo-1B-hf | RUNNING (4908 MiB) |
| exp_arXiv_llama8b | cuda:1 | 27469 | Meta-Llama-3.1-8B | RUNNING (3350 MiB, 加载中) |

- OLMo-1B 预计 1-2 小时完成
- LLaMA-3.1-8B (8B) batch_size 已降到 8，预计 3-4 小时
- 日志路径：`~/runs/gen-depth-contamination/exp_arXiv_olmo.log` 和 `exp_arXiv_llama8b.log`

---
