# analysis llama tg completion check

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_llama_tg_completion_check_20260521T032624_result.json`
- **Structured JSON:** [`a25961e19800c825ca34.json`](../../sessions/a2/a25961e19800c825ca34.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已不在当前 session，无需删除。

## Llama TG 训练汇报

**状态**: 成功完成

| 项目 | 值 |
|------|-----|
| 模型 | Meta-Llama-3.1-8B-Instruct |
| Epochs | 3 (3000 steps) |
| 总训练时长 | 26212s (**7.28h**) |
| GPU | NVIDIA RTX PRO 6000 Blackwell, 63.4/102 GB |
| Final Avg Loss | 0.9233 (NTP=0.9224, GAR=0.0009, DIV=0.0) |
| Final Gate | mean=**0.9099**, std=0.0701, min=0.7188, max=0.9922 |
| Gate 最低层 | **L25=0.719**, L26=0.762, L28=0.801 |
| Checkpoint | `/root/turn_residual_gating/runs/phase2_llama_tg_s42/` (gate 4.2MB + LoRA 26MB) |

**与 Qwen v7 对比**:
- Llama gate mean 0.910 vs Qwen 0.934 — Llama gate 更积极下调
- Llama gate std 0.070 vs Qwen 0.049 — Llama 层间分化更大
- Llama 最低层在 L25 (0.719)，Qwen 在 L3/L4 (~0.79) — 不同模型的 gate profile 分布不同，Llama 偏后层抑制
- L_GAR 同样坍塌到 ~0.001，与 Qwen 一致

**下一步**: 需要跑 Llama 的 eval（IID + model-gen GAR）来验证 C5 hypothesis — 是否同样出现 30x training-inference GAR gap。

---
