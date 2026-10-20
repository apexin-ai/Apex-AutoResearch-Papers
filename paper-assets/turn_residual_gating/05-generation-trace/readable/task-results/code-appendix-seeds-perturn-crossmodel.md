# code appendix seeds perturn crossmodel

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_appendix_seeds_perturn_crossmodel_20260524T150612_result.json`
- **Structured JSON:** [`dd6307741d7c8758d53a.json`](../../sessions/dd/dd6307741d7c8758d53a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。产出汇总：

**第 1 项：Per-seed 详细结果表**
- `tab_perseed_ss.tex` — SS 3-seed (s42/s123/s456) × TF+AR(β=0/3/5)，含 GAR-ours、GAR-Dongre、PPL、Mean±Std
- `tab_perseed_tg.tex` — TG 2-seed (s42/s123) × TF+AR，含 gap ratio

**第 2 项：Per-turn GAR 衰减详表 + 图**
- `tab_perturn_qwen.tex` — Qwen 6-way (Base/TG/PCGrad/UG/LoRA/SS) × Turn 1-5
- `tab_perturn_llama.tex` — Llama 3-way N=20 T=4 + Base 衰减 T=10 (subtable 格式)
- `fig_perturn_qwen_detail.pdf/.png` — 6 条线 × 5 turns，SS 远高于其他配置
- `fig_perturn_llama_detail.pdf/.png` — 左 panel: TG/LO 维持 GAR vs Base 衰减；右 panel: Base 10-turn −90.1% 衰减曲线

**第 3 项：跨模型详细对比表**
- `tab_crossmodel_detail.tex` — Qwen vs Llama × Base/TG/LoRA-only，含 TF GAR、AR GAR、TF PPL、AR PPL、Gap ratio

数据说明：
- SS s42 AR 使用 d048_final_ar N=50 评估（GAR 0.347），与 s123/s456 一致
- TG s123 AR 仅有 N=5 T=10 评估（GAR 0.017），已在表注中说明
- Llama per-turn T=10 数据 (TG/LO) 因 N=5 噪声极大，图中改用 N=20 T=4 数据

---
