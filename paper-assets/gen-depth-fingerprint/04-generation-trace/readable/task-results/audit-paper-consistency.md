# audit paper consistency

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_paper-consistency_20260516T022243_result.json`
- **Structured JSON:** [`f351ded80454f704e4cc.json`](../../sessions/f3/f351ded80454f704e4cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 审计结果

**通过（有条件）** — 0 CRITICAL / 3 WARNING / 5 INFO

### WARNING（建议修复）

1. **results.tex:30** — `"best single-model ceiling (Pythia-1B, 0.862)"` 与 LOGO 表中 Pythia-1B=**0.856** 不符。0.862 来源不明（疑为 5-fold CV 或 CI 上界误用），需确认或修正。

2. **discussion.tex:67 + limitations.tex:6** — Instruct 对比中 base Qwen3-0.6B=**0.816**，但 LOGO 表中同一模型=**0.824**。差异源于不同 reference model 设置（cross-ref Qwen3-0.6B=0.816），但论文未解释，读者会困惑。

3. **discussion.tex:69 + limitations.tex:8** — "reverse sign" 措辞与叙事规范（应用 "degradation" 而非 "方向反转"）存在张力。建议改为 "shift to positive" 或 "sign change"。

### INFO

- appendix_human_edit 表 delta 列有轻微舍入不一致（从原始值 vs 显示值计算 delta 的经典问题）
- Sampling ablation default 3-class=0.788 vs 主结果 0.789（数据重生成所致）
- "~6pp" 近似值（实际 6.2-6.6pp）

其余所有主要数字（binary F1、CI、std、baseline 全表、downstream PPL、ablation、cross-ref、LOFO、5-class、human edit）均与 ground truth 完全一致。报告已注册为 `art_20260516_c94dd3`。

---
