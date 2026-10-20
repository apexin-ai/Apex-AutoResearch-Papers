# Handover — 2026-05-17

> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。

## 运行中
| exp_id | 假设 | 状态 | 关键指标 | W&B |
|--------|------|------|---------|-----|
| carr_qwen25_1-5b_lora_k4_random | Random selection baseline for Qwen2.5-1.5B-Instruct LoRA K=4: establishes diversity trajectory without reward signal at 1.5B scale, enabling curated vs random gap measurement to test whether direction reversal or suppression patterns differ from 0.6B | — | — | — |
| carr_qwen25_1-5b_lora_k4_curated | Semantic resilience to reward curation generalizes across model families and scales: Qwen2.5-1.5B-Instruct (2.5x larger, different architecture family) under LoRA K=4 curated top-1 ArmoRM shows Vendi Score change within ±5% over 3 generations, consistent with Qwen3-0.6B findings | — | — | — |

## 待处理
（无）

## 近期结论
- **carr_qwen25_1.5b_lora_k4_random** (killed): Random selection baseline for Qwen2.5-1.5B-Instruct LoRA K=4: establishes diversity trajectory without reward signal at 1.5B scale, enabling curated vs random gap measurement to test whether direction reversal or suppression patterns differ from 0.6B
- **carr_qwen25_1.5b_lora_k4_curated** (killed): Semantic resilience to reward curation generalizes across model families and scales: Qwen2.5-1.5B-Instruct (2.5x larger, different architecture family) under LoRA K=4 curated top-1 ArmoRM shows Vendi Score change within ±5% over 3 generations, consistent with Qwen3-0.6B findings
- **carr_fullft_lr2e5_nocuration_01** (success): Full-FT LR=2e-5 no-curation baseline: random 1-of-4 selection at aggressive learning rate shows diversity trajectory unaffected by reward signal, isolating curation's causal effect on C4

## 趋势
成功 4 / 负向 5 / 失败 5 / 共 17

## 下一步
（无活跃 idea，请通过 ideas.md 添加）

## 资源状态
bjb2-23165: 空闲 cuda:0, cuda:1

## 告警
- carr_quick_probe_01: 训练失败 — unknown
- carr_quick_probe_02: 训练失败 — unknown
- carr_quick_probe_k8_01: 已被终止 — unknown
- carr_fullft_k4_probe_01: 训练失败 — unknown
- carr_fullft_k4_probe_02: 训练失败 — unknown
- c1-regen-lora-k4-curated: 训练失败 — unknown
- carr_qwen25_1.5b_lora_k4_curated: 已被终止 — unknown
- carr_qwen25_1.5b_lora_k4_random: 已被终止 — unknown
