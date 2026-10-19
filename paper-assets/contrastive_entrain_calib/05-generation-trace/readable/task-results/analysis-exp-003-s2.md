# analysis exp 003 s2

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-003-s2_20260522T153328_result.json`
- **Structured JSON:** [`ef296f2f1baaa15f41da.json`](../../sessions/ef/ef296f2f1baaa15f41da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-003-s2 训练分析完成。报告已写入 `artifacts/exp-003-s2/training-analysis.md`。

**核心结论: SUCCESS** — 8000/8000 steps 正常完成，EXIT_CODE=0。

关键数据：
- 总耗时 ~63.2h，16 个中间 checkpoint + final，共 12GB
- 最终 reward 0.50–0.67，loss 0.0006–0.0007，KL 0.016–0.019
- 所有生成被截断到 max_completion_length=256（clipped_ratio=1.0），无自然终止——R3-only 模式预期行为
- 无 W&B（report_to=none）
- 根分区 78% 使用，数据盘充裕（4%）

---
