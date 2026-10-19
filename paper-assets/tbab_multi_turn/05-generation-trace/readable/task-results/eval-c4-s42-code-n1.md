# eval c4 s42 code n1

**tbab multi turn** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_c4-s42-code-n1_20260518T152237_result.json`
- **Structured JSON:** [`c8518acb3042de2ef922.json`](../../sessions/c8/c8518acb3042de2ef922.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 正常推进中，已完成前 2 个 sample，正在处理第 3 个。

**汇总：**

| 项目 | 值 |
|---|---|
| tmux session | `eval_c4_s42` |
| PID | 48198 |
| condition | `full_tbab` (use_bridge=True, use_reset=True) |
| GPU 占用 | ~17.2GB（与训练共用，总 55.6GB / 97.9GB） |
| 进度 | 3/91 处理中 |

**修复了两个 bug：**
1. `model_local.py`：加载 adapter 前需 `resize_token_embeddings(32004)` 以容纳 bridge tokens [32000-32003]
2. `run_eval.py`：添加 `os.chdir(LIC_DIR)` 解决 lost_in_conversation 中相对路径问题

**速度估算：** 每个 sample 约 1-2 分钟（TBAB token-by-token + API 调用），91 个 sample 预计 **1.5-3 小时**完成。与训练共享 GPU 可能会更慢。

---
