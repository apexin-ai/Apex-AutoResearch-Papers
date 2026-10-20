# ops check 34685 all gpus

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_34685_all_gpus_20260524T143422_result.json`
- **Structured JSON:** [`057f2b7eb581fdd43aa4.json`](../../sessions/05/057f2b7eb581fdd43aa4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已修正。汇总如下：

**Report 误报：全4卡满载运行中，非空闲。**

| GPU | exp_id | PID | Step/Total | Progress | Speed | ETA (UTC) |
|-----|--------|-----|------------|----------|-------|-----------|
| cuda:0 | cutoff_45k_s1 | 882188 | 5433/50005 | 11% | ~1.07 it/s | ~May 25 02:10 |
| cuda:1 | cutoff_15k_s1 | 861222 | 7645/50005 | 15% | ~1.07 it/s | ~May 25 01:35 |
| cuda:2 | cutoff_25k_s1 | 672857 | 49411/50005 | 99% | ~1.06 it/s | ~May 24 14:45 |
| cuda:3 | reverse_cutoff_s1 | 673004 | 49457/50005 | 99% | ~1.06 it/s | ~May 24 14:45 |

**GPU 使用率**: 80% / 99% / 99% / 43%，显存 62GB/98GB 全卡占用。

**cuda:1 确认**: cutoff_15k_s1，PID 861222 与 registry 一致。

**Registry 修正**: cutoff_15k_s1 的 `gpu_id: 1` 已统一为 `gpu: ["cuda:1"]` 格式。cutoff_45k_s1 信息核实无误。

**注意**: cutoff_25k_s1 和 reverse_cutoff_s1 约 10 分钟内完成。

---
