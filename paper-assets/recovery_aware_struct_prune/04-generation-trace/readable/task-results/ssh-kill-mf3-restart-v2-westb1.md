# ssh kill mf3 restart v2 westb1

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill_mf3_restart_v2_westb1_20260522T142504_result.json`
- **Structured JSON:** [`f284bd0aa29a600af6ac.json`](../../sessions/f2/f284bd0aa29a600af6ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

5 个 sample 完成，实际平均 61s/sample（305s / 5）。有的 sample 很快（<10s, 早 EOS），有的约 100s（接近 2048 token 上限）。

## 汇报

| 项目 | 结果 |
|------|------|
| 1. 旧进程 kill | 成功 (PID 202364 已终止) |
| 2. 参数名 | `--max_new_tokens`（默认 4096，第 320 行） |
| 3. 新 PID | **217798**（python 子进程，bash wrapper PID 217793） |
| 4. GPU 显存 | GPU:1 占用 **16307 MiB**，利用率 99% |
| 5. 前 5 个 sample 速度 | 平均 **~61s/sample**，比之前快（部分 sample <10s 因 EOS 提前终止） |

注意事项：
- 模型路径需用绝对路径 `/root/autodl-tmp/recovery_aware_struct_prune/grpo_qwen_math_cka_only_20`（脚本目录在 `/root/recovery_aware_struct_prune/`，相对路径找不到）
- Log 文件中混有旧进程（217502）的 traceback，是因为两个进程短暂同时写同一文件，不影响当前评估

---
