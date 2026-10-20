# figure fig1 fontsize fix

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_fig1-fontsize-fix_20260517T171000_result.json`
- **Structured JSON:** [`9af0730a270c93b50aec.json`](../../sessions/9a/9af0730a270c93b50aec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

PDF (45.7KB) 和 PNG (180KB) 均已更新。

修改完成。总结变更：

1. **`figsize`**: `(16, 7)` → `(8, 3.5)`
2. **`ax.set_position([0, 0, 1, 1])`**: 让 axes 填满整个 figure，最大化元素间物理间距
3. **加宽 4 个溢出最严重的 box**：
   - Question: 1.5 → 1.8
   - K Reasoning: 1.5 → 1.7
   - MAX-SAT (Z3): 1.5 → 2.0
   - Most Frequent: 1.7 → 2.0
4. **字号全部保持不变** (8-14pt range)

输出 8.20 × 3.70 inches。放入 EMNLP 6.75" 双栏时 scale=0.823：
- Box 文字 (10pt) → **8.2pt** ✓
- 注释 (8pt) → **6.6pt** (接近可读)
- 标题 (13-14pt) → **10.7-11.5pt** ✓
- 最大 box 溢出从原来的 51% 降至 13%

---
