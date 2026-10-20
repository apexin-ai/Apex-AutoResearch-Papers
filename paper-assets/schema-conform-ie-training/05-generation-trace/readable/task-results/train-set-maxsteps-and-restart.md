# train set maxsteps and restart

**schema conform ie training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_set-maxsteps-and-restart_20260512T115727_result.json`
- **Structured JSON:** [`b05cfa7673afe4c7275b.json`](../../sessions/b0/b05cfa7673afe4c7275b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过：

### 产出汇总

| | Group A (baseline) | Group B (conformance+GDPO) |
|---|---|---|
| **PID** | 25841 (python: 25842) | 26252 (python: 26253) |
| **GPU** | GPU 0, 22340MiB, 88% util | GPU 1, 22340MiB, 84% util |
| **进度条** | `0/500` | `0/500` |
| **Config** | `max_steps: 500` | `max_steps: 500` |

### 额外修复

`train_grpo.py` line 216 有 bug：YAML 中的 `max_steps` 被忽略，代码只读命令行参数。已修改为：
```python
max_steps = args.max_steps if args.max_steps else config.get("max_steps", -1 if not args.dry_run else 5)
```
服务器和本地代码均已同步修改。

---
