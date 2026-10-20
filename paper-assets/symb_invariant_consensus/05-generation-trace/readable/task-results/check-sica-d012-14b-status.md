# check sica d012 14b status

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_sica_d012_14b_status_20260516T044207_result.json`
- **Structured JSON:** [`0d0d465f771312f6eb85.json`](../../sessions/0d/0d0d465f771312f6eb85.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报：sica_d012_14b 实验

### 状态：**仍在运行**
- 启动时间：12:05 UTC（约 38 分钟前，不是 3+ 小时）
- 当前进度：**36/60 题已完成**，正在处理 folio 子集
- 预计剩余：~25 分钟（avg 64s/题）
- 所有进程正常：tmux session 存在，PID 177188 (python) 活跃

### 中间结果（36/60）

| 指标 | 值 |
|------|-----|
| **SICA accuracy** | 25/36 = **69.4%** |
| **SC accuracy** | 25/36 = **69.4%** |
| C0 多候选率 | 19/36 = 52.8% |
| C1 约束提取率 | 432/432 = **100%** (每条 trace 都成功提取) |
| C2 跨路径矛盾题数 | 20/36 = **55.6%** |
| C3 SICA vs SC | **持平** (SICA wins 1, SC wins 1) |

**Per-dataset:**
- ProofWriter (30题): SICA=66.7%, SC=66.7%
- FOLIO (6题已完成): SICA=83.3%, SC=83.3%

### SICA ≠ SC 的两题

| 题目 | GT | SICA | SC | 结果 |
|------|-----|------|-----|------|
| PW-D5-347_Q11 | True | Unknown | True | SC+ (SC对，SICA错) |
| PW-D5-813_Q17 | Unknown | Unknown | False | **SICA+** (SICA对，SC错) |

### 关键观察

1. **约束管线工作正常**：100% 提取率，55.6% 的题检测到矛盾（excluded>0）
2. **但 SICA 尚未展现优势**：36 题中 SICA 和 SC 仅在 2 题上不同，互为一胜一负
3. 剩余 24 题全是 FOLIO，格局可能还会变化

建议等实验跑完（~25 分钟后）再做最终评估。需要我到时候再查一次吗？

---
