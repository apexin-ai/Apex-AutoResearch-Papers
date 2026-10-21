# analysis t20 power theory verification

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_t20_power_theory_verification_20260521T014415_result.json`
- **Structured JSON:** [`9044437f426f3ee272de.json`](../../sessions/90/9044437f426f3ee272de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/t20_power_theory_verification.md` 并注册。

核心结果：

- **5 个已完成 T=20 实验，4/5 区间验证 PASS (80%)**
- **α=0.45** 点预测失败（0/8→5/8），但观测值落在 bootstrap CI [0.015, 0.828] 内。blind zone 是统计功效问题，α_c 随 T 左移
- **α=0.50/0.75/1.00** 全部 T-invariant：T=10 和 T=20 均为 6/8，mauve pairs 构成结构性天花板
- **α=0.60** sync dip T-invariant（0/8→0/8），确认为 S×R 非单调的结构性现象
- **t20_a025** 仍在运行（null baseline）
- 点预测准确率仅 2/5（40%），但区间预测 4/5（80%）——理论适合作为相变理解框架，而非精确点预测器

---
