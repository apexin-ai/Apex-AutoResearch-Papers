# analysis d108 domain gamma n24 v4

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d108_domain_gamma_n24_v4_20260516T150132_result.json`
- **Structured JSON:** [`f711cff43e983a0a6c8e.json`](../../sessions/f7/f711cff43e983a0a6c8e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/d108_v4_analysis.md` 并注册。

核心发现：

**N=24 结果有严重稳定性问题**：7 个 domain 中 5 个发生 γ 方向反转（相比 N=16），3 个 domain PPP=1.0（模型失配）。

可靠的结果：
- **STEM_Math**: γ=+0.97 [0.53, 1.43]，PPP=0.44，收敛良好 — D111 的方向反转问题已解决，N=24 下稳定为正
- **STEM_Science**: γ=+0.84 [0.39, 1.27]，PPP=0.81 — 从 N=16 的 borderline 变为显著

需要排除/谨慎处理：
- **Medical**: PPP=1.0（D112 已标记）
- **Humanities**: PPP=1.0 + rhat=1.0135 收敛失败
- **Social_Sciences**: PPP=1.0

方向反转的可能原因：N=24 混合了 0.5B/1.5B/3B 多尺度模型（N=16 仅 3B），小模型在人文/社科 domain 的污染模式可能质变不同。建议用 3B-only 子集重跑 Humanities/SocSci/Business_Law 以隔离原因。

---
