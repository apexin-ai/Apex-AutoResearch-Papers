# check qwen3 n problems investigation

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_qwen3-n-problems-investigation_20260524T040958_result.json`
- **Structured JSON:** [`e87c0360b7dede037380.json`](../../sessions/e8/e87c0360b7dede037380.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 调查结论：results.json 是中间 checkpoint，实验仍在正常运行

### 核心事实

| 项目 | 值 |
|------|-----|
| `proofwriter_full.json` 实际问题数 | **600** |
| 脚本 `--n-questions` 限制 | `0`（无限制，处理全部 600 题） |
| results.json 性质 | **中间 checkpoint**，每处理完一题就 `_save_checkpoint` 更新 |

### 当前进度（实时）

| Seed | 已完成 | 进度 |
|------|--------|------|
| 123 | 347/600 | 57.8% |
| 456 | 348/600 | 58.0% |
| 789 | 350/600 | 58.3% |

### 进程状态

- 三个 PID 均 CPU ~1.6%，已运行 ~10 小时
- 中间文件持续产生（最新文件 12:10，几分钟前）
- **进程正常运行中，不是 idle**

### 预估剩余时间

- 平均每题 ~1.7 分钟
- 剩余 ~252 题 × 1.7 min ≈ **7 小时**
- 预计完成时间：今天 ~19:00-20:00（+8 时区）

### 结论

**不需要干预。** n_problems 低于 600 是因为实验还在跑，不是因为数据或脚本有问题。results.json 的 `n_problems` 字段只反映已处理完的题目数，会随进程推进持续增长直到 600。

---
