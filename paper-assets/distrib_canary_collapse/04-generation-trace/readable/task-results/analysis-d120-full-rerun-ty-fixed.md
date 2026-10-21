# analysis d120 full rerun ty fixed

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d120_full_rerun_ty_fixed_20260520T062434_result.json`
- **Structured JSON:** [`3d4cc8ae7e87e3ef6899.json`](../../sessions/3d/3d4cc8ae7e87e3ef6899.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。核心结果：

**验证通过**: a050_s42_fp32 TY=3/8, K≥3=6/8 ✓

**TY 修复影响**:
- 13/17 实验 TY 非零（修复前全部 0/8）
- K≥3 在 6/17 实验中升高（最大 +3 在 c4_a025）
- K≥4 在 4/17 实验中升高（a075 和 c4_a075 各 +3）
- **dose-response 定性结论不变**：低α弱信号 → 高α强信号的梯度模式保持
- TY 种子波动大（α=0.50: s42→3/8, s43→0, s44→0），与 C003 约束一致——TY 适合作共识贡献者，不宜单独使用

报告已注册: `artifacts/d120_ty_fixed_full_rerun/report.md`

---
