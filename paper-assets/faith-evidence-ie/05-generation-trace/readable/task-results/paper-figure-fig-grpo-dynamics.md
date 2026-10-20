# paper figure fig grpo dynamics

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fig_grpo_dynamics_20260517T181631_result.json`
- **Structured JSON:** [`49a6876515a60321060c.json`](../../sessions/49/49a6876515a60321060c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图表已生成并注册。

**输出文件**：
- PDF: `artifacts/fig_grpo_dynamics.pdf`
- PNG: `artifacts/fig_grpo_dynamics.png`

**数据来源**：
- G=4 QLoRA: `grpo_ced_kl001` checkpoints 10/20/30/50/60/90/100
- G=8 bf16: `plan_011_bf16_g8` steps 30/50/70 + `grpo_g8_bf16` checkpoints 80/90/100
- Step 0 = SFT baseline (`sft_baseline_noquant`)

**关键发现**：
- **(a)** G=4 QLoRA 的 Rel F1 在 step 10 从 0.41 崩塌至 0.003（catastrophic collapse），之后缓慢恢复但始终远低于 SFT baseline。G=8 bf16 全程稳定且略优于 SFT。
- **(b)** 两组的 Evidence F1 均维持在 0.56-0.81 范围，证明 evidence 生成机制本身并未崩溃。
- **(c)** G=4 QLoRA 的 EDCR 在 step 10 跳至 0.998（几乎所有 citation 指向 distractor），随后缓慢下降。G=8 bf16 维持 0.63-0.69 并持续改善。

---
