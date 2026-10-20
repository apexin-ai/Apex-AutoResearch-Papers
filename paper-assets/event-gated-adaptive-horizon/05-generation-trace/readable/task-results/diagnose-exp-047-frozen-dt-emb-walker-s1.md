# diagnose exp 047 frozen dt emb walker s1

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_047_frozen_dt_emb_walker_s1_20260522T185736_result.json`
- **Structured JSON:** [`454a9e01cfbbc9447f6c.json`](../../sessions/45/454a9e01cfbbc9447f6c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**exp_047 没有失败，是监控误报。** 训练在 bjb1-40020 上正常跑完，metrics 到 step 224000，checkpoint 到 225000，数据完整可用。

误报原因：训练命令缺少 `> train.log 2>&1` stdout 重定向，dreamer.py 不写 sentinel 文件，进程正常退出后监控 5 次轮询发现 "process dead" 就判定为失败。

不需要重试。报告已保存到 `artifacts/exp_047_diagnosis.md`。

---
