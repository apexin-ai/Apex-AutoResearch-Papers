# ssh fix resubmit seed123

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix-resubmit-seed123_20260513T204058_result.json`
- **Structured JSON:** [`416fa36ebae6053c8369.json`](../../sessions/41/416fa36ebae6053c8369.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个 runs 全部成功启动，训练已开始：

```
GPU 1 (0.5B s123): 成功启动, PID=216028, 已开始训练 (2/3125 steps, ~1.87s/it)
GPU 2 (1.5B s123): 成功启动, PID=216106, 已开始训练 (1/3125 steps, ~2.58s/it)
GPU 3 (3B s123):   成功启动, PID=216249, 已开始训练 (初始化完成，step 即将开始)
```

`libnvJitLink.so.13` 警告无影响，训练正常推进。无 OOM 错误。

---
