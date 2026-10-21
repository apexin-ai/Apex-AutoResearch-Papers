# analysis plan 009 dynamics figure

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan_009_dynamics_figure_20260515T230715_result.json`
- **Structured JSON:** [`6b6af70d5bedbd4c97e4.json`](../../sessions/6b/6b6af70d5bedbd4c97e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图已生成并拷贝到本地。

3-panel figure 清晰展示了 forgetting dynamics：
- **(a) Relation F1**：QLoRA GRPO 从 0.003 缓慢爬升到 0.22，始终远低于 SFT baseline (0.41)；BF16 GRPO 全程稳定在 0.43-0.45，高于 SFT baseline
- **(b) Evidence F1**：QLoRA 初始骤降到 0.42 后回升到 ~0.57，仍低于 SFT baseline (0.80)；BF16 全程稳定在 ~0.80
- **(c) EDCR**：QLoRA 的 EDCR 高达 0.85-1.0（严重 evidence-dominated），BF16 稳定在 ~0.46（均衡）

文件位置：
- 服务器：`/root/autodl-tmp/figures/plan_009/forgetting_dynamics.{pdf,png}`
- 本地：`artifacts/plan_009/figures/forgetting_dynamics.{pdf,png}`

---
