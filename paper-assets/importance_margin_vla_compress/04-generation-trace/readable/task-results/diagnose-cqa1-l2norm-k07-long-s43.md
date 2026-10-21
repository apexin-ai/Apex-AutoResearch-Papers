# diagnose cqa1 l2norm k07 long s43

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_cqa1_l2norm_k07_long_s43_20260525T162153_result.json`
- **Structured JSON:** [`a0f8902859487a21dae2.json`](../../sessions/a0/a0f8902859487a21dae2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验已完成诊断并注册到 registry（状态 DONE/success）。

**结果汇总：**

| 实验 | 方法 | keep_ratio | SR | 500 eps |
|------|------|-----------|-----|---------|
| `eval_pi05_l2norm_k07_long_seed43_v3` | l2norm | 0.70 | **65.0%** | 325/500 |
| `eval_pi05_random_k03_long_seed43_v4` | random | 0.30 | **27.2%** | 136/500 |

l2norm k=0.7 表现稳健（65%），random k=0.3 大幅退化到 27.2%，符合预期——在高压缩比下 importance-based pruning 的优势非常显著。

---
