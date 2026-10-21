# run mmlu domain gamma

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_mmlu_domain_gamma_20260516T075234_result.json`
- **Structured JSON:** [`4e663a6cb749ff1412e8.json`](../../sessions/4e/4e663a6cb749ff1412e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Stan NUTS 采样已启动，第一个 domain (STEM_Math, 478 items) 正在 warmup。

完成情况：
- 修复了 `load_1_5b_mmlu_data` 中 item alignment bug（para 模型 6596 items 是非连续子集，旧代码用 `min(lengths)` 截断导致跨模型 item 错位）
- 新实现用 index intersection 对齐，domain_indices 正确映射到 response matrix 列位置
- 任务已重新提交：16 models × 6596 common items → 8 domains，预计 ~35 min
- Registry 状态 RUNNING，PID 731055，tmux session `exp_006_mmlu_domain_gamma`

---
