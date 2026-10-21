# paper table1 long update and trigger figure

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_table1-long-update-and-trigger-figure_20260523T221950_result.json`
- **Structured JSON:** [`af0b6bb2ba28afba2b39.json`](../../sessions/af/af0b6bb2ba28afba2b39.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

### Table 1 Long 更新
- VLA-only Long: `58.0^(1)` → `58.0±1.5^(3)`
- CRM always-on Long: `56.5^(1)` → `55.8±1.2^(3)`
- ACR-VLA Long: `59.0^(1)` → `57.7±1.5^(3)`（移除 bold）
- Δ Long: `+1.0` → `-0.3`
- Object VLA-only: `77.8±1.0^(3)` → `77.7±1.3^(5)`; ACR-VLA Object std: `3.0→2.1`, seeds `3→5`

### D134 叙事一致性修复（4 个 .tex 文件）
- 全文 CRM Long 降级数字从 `-1.5pp` 改为 `-2.2pp`
- Long 从"improvement"重新定性为"baseline preserved"（`-0.3pp = 0.22σ`）
- 改善范围从 `+1.0–2.1pp` 修正为 `+1.3–2.1pp`（仅 Spatial + Goal）
- ACR-VLA vs CRM 范围从 `+1.0 to +2.5pp` 修正为 `+1.0 to +1.9pp`
- 所有文件（abstract / intro / experiments / conclusion）已对齐 trigger-rate 叙事框架

### Trigger-rate Scatter Plot
- 数据 CSV + matplotlib 脚本已创建
- PDF/PNG 已生成并注册为 artifact（`art_20260523_bb7548`）

### τ-sweep Ablation
- Appendix 中已有完整 τ-sweep 表（Table 5），数据与任务一致，无需修改

---
