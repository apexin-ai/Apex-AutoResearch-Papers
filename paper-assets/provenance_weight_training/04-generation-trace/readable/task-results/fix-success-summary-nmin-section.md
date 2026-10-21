# fix success summary nmin section

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_success_summary_nmin_section_20260515T153705_result.json`
- **Structured JSON:** [`b5513c8769fe14977537.json`](../../sessions/b5/b5513c8769fe14977537.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。修改内容：

1. **Adaptive 表 variant 标签**：`original` → `n_min=3 (pre-D012)`，`n_min fix` → `n_min=2 (post-D012)`，表下注释同步更新
2. **新增 `## n_min Sensitivity Analysis` 小节**（第 93–129 行），包含：
   - Per-seed PPL 对比表（n_min=1/2/3/4）
   - 5 条 key observations，核心叙事：n_min=2 优势在稳定性（std 0.009 vs 0.032, 3.8×）而非均值（差 0.002）
   - b* 分布对比表（n_min=1 和 n_min=2 有详细数据，n_min=3 仅有 range 字符串）
3. **Key Findings #4 更新**：补充了稳定性叙事和具体数值

所有数值均从 registry 取得，std 使用 sample standard deviation (ddof=1)。

---
