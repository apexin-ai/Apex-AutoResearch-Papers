# ops v3 exit investigation

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_v3_exit_investigation_20260515T220606_result.json`
- **Structured JSON:** [`f4a5c6a3688a76db17be.json`](../../sessions/f4/f4a5c6a3688a76db17be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐了。整理报告。

---

## sica_aime30_v3 调查报告

### 1. 退出原因：**静默崩溃（疑似 signal kill）**

- 进程 129992 已 DEAD
- 日志无任何 error / exception / traceback
- 日志在 P23 (aime2024_I_08) 的 trace 生成阶段（HTTP 200 OK）突然停止于 `2026-05-16 03:19:27`
- 无 core dump，dmesg 无法确认 OOM
- 原始 v2 运行曾因 SIGHUP 被终止（EXIT_CODE=129），resume 运行无退出消息——可能同样被信号杀死（OOM killer 或 Z3 segfault）
- vLLM 服务（PID 129131）仍然存活，排除推理服务崩溃

### 2. 最终进度：**22/30**

8 题未完成（aime2024_I_08 到 I_15）。

### 3. 最终准确率

| 方法 | 正确 | 准确率 |
|------|------|--------|
| SICA | 16/22 | 72.7% |
| SC   | 16/22 | 72.7% |
| **Gap** | — | **0.0pp** |

每题详细：

| 题目 | SICA | SC | Gold | 对错 |
|------|------|----|------|------|
| II_01 | 73 | 73 | 73 | Y |
| II_02 | (空) | (空) | 236 | N |
| II_03 | 45 | 45 | 45 | Y |
| II_04 | 33 | 33 | 33 | Y |
| II_05 | 80 | 80 | 80 | Y |
| II_06 | 55 | 55 | 55 | Y |
| II_07 | 699 | 699 | 699 | Y |
| II_08 | (空) | (空) | 127 | N |
| II_09 | (空) | (空) | 902 | N |
| II_10 | 468 | 468 | 468 | Y |
| II_11 | (空) | (空) | 601 | N |
| II_12 | 23 | 23 | 23 | Y |
| II_13 | 321 | 321 | 321 | Y |
| II_14 | (空) | (空) | 211 | N |
| II_15 | (空) | (空) | 315 | N |
| I_01 | 204 | 204 | 204 | Y |
| I_02 | 25 | 25 | 25 | Y |
| I_03 | 809 | 809 | 809 | Y |
| I_04 | 116 | 116 | 116 | Y |
| I_05 | 104 | 104 | 104 | Y |
| I_06 | 294 | 294 | 294 | Y |
| I_07 | 540 | 540 | 540 | Y |

**0 题 SICA vs SC 正确性不一致。**

### 4. Vote Diversity

**0/22 题有 >1 unique candidate。Vote diversity = 0.0%。**

SICA multi-candidate 也是 0/22。

关键观察：
- 6 道错题 (II_02, II_08, II_09, II_11, II_14, II_15) 全部是 SICA 和 SC 都给出空答案
- 一些题有大量 constraint 被 exclude（II_05: 40/42, II_11: 12/12, II_13: 16/16, II_12: 8/8）
- 即便有大量 exclusion，最终答案也没变

### 5. 结论

**标记为：negative result（partial）**

- 进度只完成 22/30（73%），因静默崩溃未跑完
- SICA 在已完成的 22 题上与 SC **完全一致**，零差异
- Vote diversity 为 0%——constraint filtering 没有改变任何投票结果
- 约束提取和 MaxSAT 增加了计算开销（每题 ~40s extraction），但没有带来任何准确率提升
- 需要：(a) 在更有 vote diversity 的 benchmark 上测试，或 (b) 增大 k 让 trace 之间产生更多分歧，或 (c) 检查为什么 12 条 trace 几乎总是给出完全相同的答案

---
