# urgent bjb1 45299 full check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_bjb1-45299-full-check_20260519T233201_result.json`
- **Structured JSON:** [`0a1ee6d326425f46e492.json`](../../sessions/0a/0a1ee6d326425f46e492.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

| exp_id | server:gpu | step | eval_final | ve_ratio@105K | ve_ratio@最终 | status |
|--------|-----------|------|------------|---------------|---------------|--------|
| exp_025_obs_sgs_walker_s3 | bjb1-45299:cuda0 | 175K/210K | 193.92 | 0.5621 | 0.8274 @175K | **running** |
| exp_025_obs_sgs_walker_s4 | bjb1-45299:cuda1 | 145K/210K | 61.41 | 1.5704 | 1.2645 @145K | **running** |

### 关键发现

**s3** — 105K 时表现极好（eval=818.58, ve_ratio=0.56），但之后**严重崩塌**：
- 135K: eval=66.95, ve=5.47
- 145K: eval=43.75, ve=6.81（最低点）
- 175K: eval=193.92, ve=0.83（正在恢复，但远未回到 818 水平）

**s4** — eval 始终偏低（34~92 区间），从未突破 100。ve_ratio 从 65K 的 2.15 逐步收敛到 145K 的 1.26，趋势向好但绝对性能差。两个进程都在正常运行，无异常退出。

---
