# research adaptive k mechanism design

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_adaptive-k-mechanism-design_20260519T163026_result.json`
- **Structured JSON:** [`a3087c49e3f01ae80471.json`](../../sessions/a3/a3087c49e3f01ae80471.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

方案已写入 `artifacts/adaptive_k_design.md`。

核心结论：

**推荐 FMVD (Flow Velocity Dispersion) 作为主信号**——在 K=1 denoising ODE 中零成本提取 velocity norm 的标准差，作为不确定性度量。高 FMVD → ODE 轨迹湍流 → 模型不确信 → 触发 K_full + CRM。

与现有 v0 (K=2 L2 Disagreement) 的关键区别：
- 真正实现 K=1 快速通道（v0 最少需要 K=2）
- 零额外推理开销（velocity 在 denoising 中已计算）
- 非 batched K=1 fast path 可将平均延迟从 ~183ms 降到 ~131-145ms（取决于 fast path 占比）

最大风险：FMVD 与实际 action quality 的相关性未验证。Phase 1 实验（FMVD signal validation，验收标准 Spearman ρ > 0.5）是 go/no-go gate。

---
