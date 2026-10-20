# debug dose response reduce tasks

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_dose_response_reduce_tasks_20260518T160611_result.json`
- **Structured JSON:** [`b524390641b05dd14c17.json`](../../sessions/b5/b524390641b05dd14c17.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个进程运行正常。关键数据：

- **总 calls**: 7500（原来 12500，因为 3 tasks × 10 demos × 50 timesteps × 5 conditions = 7500 per condition set）
- **速度**: ~6.4-6.6 calls/s
- **ETA**: ~1100s ≈ 18 min per task，3 tasks 总共 ~55 min
- **PIDs**: cuda:0 = 61607, cuda:1 = 61682
- **screen sessions**: dose0, dose1

完成。修改了 `n_tasks = 5` → `3`，kill 旧进程，重启了两个 screen session。8 个条件全部保留，预计约 55 分钟完成（比原 5 tasks 省约 40%）。

---
