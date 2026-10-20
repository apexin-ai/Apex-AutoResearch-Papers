# code eval 3B d005 s123 para

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval_3B_d005_s123_para_20260515T155342_result.json`
- **Structured JSON:** [`19552db03863c4bff5ac.json`](../../sessions/19/19552db03863c4bff5ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 5 被占用，不能提交。当前运行的是：

| 项 | 值 |
|---|---|
| PID | 584315 |
| 运行时间 | 20 分钟 |
| 任务 | d025_s123 para_aligned eval |
| 命令 | `evaluate.py --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases` |

从这个进程也能看出 para_aligned 的参数格式：`--mc-format aligned` + `--paraphrase-dir &lt;path>`，不是单独的 mc-format 值。

**当前所有 6 张 GPU 都有进程在跑，没有空闲 GPU。** 需要等某张 GPU 释放后再提交 d005_s123 para_aligned eval。

---
