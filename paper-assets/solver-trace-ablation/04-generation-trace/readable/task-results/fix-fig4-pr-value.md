# fix fig4 pr value

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_fig4-pr-value_20260515T000220_result.json`
- **Structured JSON:** [`2ee98cc0efd1c3deeed8.json`](../../sessions/2e/2ee98cc0efd1c3deeed8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成：

- **Line 239**: `fol_isr = [0.1324, 0.13, 0.5816]` → `fol_isr = [0.1324, 0, 0.5816]`（还原 s43 ISR 为 0）
- **`fol_pr` 变量不存在**：fig4 不绘制 FOL prove rate，论文 experiments.tex 已写 `PR=13%`，无需修改

fig4 新文件：
- 大小：32663 bytes
- md5：`de74830013ab38436f2a3a9b5b72c408`

---
