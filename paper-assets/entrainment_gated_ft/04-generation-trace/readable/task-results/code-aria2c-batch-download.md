# code aria2c batch download

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_aria2c-batch-download_20260518T102414_result.json`
- **Structured JSON:** [`323f51efc24d4887e264.json`](../../sessions/32/323f51efc24d4887e264.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载稳定运行中：
- 当前：`1.3B-100B-GatedDeltaNet-pure` shard 1/2，193MiB/4.6GiB，**3.9 MB/s**，ETA ~19 分钟
- 每个模型约 9.2G (2 shards)，13 个模型共 ~65G
- 预估总耗时：**~4-5 小时**

下载在 screen `download` 中运行，不占 GPU。可以随时用以下命令监控：
```bash
screen -S download -X hardcopy /tmp/dl_status.txt && cat /tmp/dl_status.txt
du -sh /root/autodl-tmp/models_1.3b/*/
```

需要我过一会儿再检查进度吗？

---
