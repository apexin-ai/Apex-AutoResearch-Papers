# ops westb check harvest fill 20260522

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westb_check_harvest_fill_20260522_20260522T031815_result.json`
- **Structured JSON:** [`13e8bb4b510b52eacfff.json`](../../sessions/13/13e8bb4b510b52eacfff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都在跑，无需收割。westd 连接失败。

```
== westb GPU 状态 ==
GPU 0: 17053/97887 MiB, 100% util
GPU 1: 4395/97887 MiB, 81% util

== eval_math500_sft_cka_only_20_v7 ==
状态: RUNNING (361/500, ~2h37m elapsed)
进度: 72% complete, ~1h remaining
Registry: 未更新（仍在运行）

== eval_math500_sft_cka_only_20_1p5b ==
状态: RUNNING (204/500, ~45m elapsed)
进度: 41% complete, ~1h remaining
Registry: 未更新（仍在运行）

== westd ==
连接: FAILED (Unable to connect to port 29022 on 36.103.198.204)

== 空卡填充 ==
空闲 GPU: 无（两卡均被占用）
新提交: 无
```

---
