# analysis reviewer fixes training dynamics

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_reviewer-fixes-training-dynamics_20260515T164443_result.json`
- **Structured JSON:** [`0dd205aa2096314aba1c.json`](../../sessions/0d/0dd205aa2096314aba1c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the summary:

---

## 1. 5-Seed TaxEI Full (100%) — Average Training Loss & SD

| Seed | Avg Loss | Final Loss | Logged Steps |
|------|----------|------------|-------------|
| 0 | 0.360364 | 0.165320 | 678 |
| 1 | 0.361245 | 0.166733 | 678 |
| 7 | 0.361865 | 0.175309 | 678 |
| 42 | 0.360925 | 0.173849 | 678 |
| 123 | 0.360178 | 0.165202 | 678 |

**Mean = 0.3609, SD = 0.0007** (ddof=1)

训练非常稳定，5-seed 之间 avg loss 的 SD 仅 0.0007。

---

## 2. taxei_10pct 训练动态数据

**不可用。** `taxei_fixed_inject10` 目录存在但为空（无 checkpoint、无 trainer_state.json）。Registry 中 `v4-taxei-fixed-inject10` 标记为 DONE（final_loss=0.308, 1635 steps），但服务器上无训练日志保留，无法提取 per-step loss。

D027 forward pass 有 taxei_10pct 的 **评估 loss**：clean_loss=0.6628, injected_loss=0.6464, gap=-0.016。

---

## 3. taxei_25pct 训练动态数据

**可用。** 两个 seed 的 trainer_state.json 都有完整 per-step loss（328 步/seed）：

| 配置 | Avg Loss | Final Loss | Steps |
|------|----------|------------|-------|
| taxei_inject25_s0 | 0.436386 | 0.286186 | 328 |
| taxei_inject25_s123 | 0.435931 | 0.285351 | 328 |

Per-step loss 曲线完整：从 ~4.175 起始，单调下降到 ~0.28。两个 seed 的曲线高度一致。

---

**结论**：
- 5-seed TaxEI 训练 loss：**Mean=0.3609 ± 0.0007 (SD)**
- taxei_10pct：训练日志已丢失，仅有 registry 记录和 forward pass 评估数据
- taxei_25pct：有完整 per-step loss 数据（328 步 × 2 seeds）

---
