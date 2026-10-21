# ops cwm8b shard progress cuda2

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cwm8b-shard-progress-cuda2_20260516T024358_result.json`
- **Structured JSON:** [`806d123b703f4b6df86a.json`](../../sessions/80/806d123b703f4b6df86a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总：

## CWM 8B ckpt-400 Test Eval 全局进度

| Shard | GPU | PID | 范围 | 已完成/总量 | 当前 idx | 状态 |
|---|---|---|---|---|---|---|
| **v3** | cuda:3 | 443221 | 0-9783 (全量, auto-resume) | 6296/9784 | 6295 | 运行 ~2h |
| **shard2** | cuda:1 | — | 7680-9783 | 680/2104 | 8359 | 运行 ~80min |
| **shard3** | cuda:0 | 453335 | 6200-7679 | 56/1480 | 6255 | 运行 ~7min |
| **shard4** ✨ | cuda:2 | 454722 | 9100-9783 | 8/684 | 9103 | **刚启动** |

### 覆盖分析

- **0-6295**: 已完成 (v3 产出)
- **6296-7679** (1384 samples): v3 + shard3 双进程推进，预计 ~165 min
- **7680-8359**: 已完成 (shard2 产出)
- **8360-9099** (740 samples): shard2 继续推进，预计 ~88 min
- **9100-9783** (684 samples): shard4 接管，预计 ~85 min

### 影响

shard4 将 8360-9783 范围的完成时间从 ~170 min 压缩到 ~90 min。整体瓶颈转为 v3 处理 6296-7679 范围的 ~165 min。4 卡全部跑满，无空闲 GPU。

---
