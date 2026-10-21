# ssh d034 kill orphan processes

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d034-kill-orphan-processes_20260515T012004_result.json`
- **Structured JSON:** [`63ffad6d7665ad23ac3f.json`](../../sessions/63/63ffad6d7665ad23ac3f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程已不存在（`ps` 返回码 1，无输出），且 cuda:0 显存已为 0 MiB。

```
== D034 Step 1 结果 ==
杀前: PID 90084 不存在, PID 90085 不存在（已自然退出）
杀后: N/A
cuda:0 显存: 0 MiB（已空闲）
GPU 全局状态: gpu0=0MiB/0%, gpu1=24005MiB/83%, gpu2=1435MiB/38%, gpu3=0MiB/0%
结论: cuda:0 已释放，无需手动杀进程
```

---
