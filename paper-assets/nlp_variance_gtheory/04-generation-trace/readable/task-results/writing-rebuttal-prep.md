# writing rebuttal prep

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_rebuttal-prep_20260524T100307_result.json`
- **Structured JSON:** [`08467209653a8683060b.json`](../../sessions/08/08467209653a8683060b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文档已保存到 `docs/rebuttal_prep.md`。

覆盖 4 个主要攻击点 + 3 个补充攻击点，所有 section/table 编号和数字均从论文 tex 原文逐一核对：
- **攻击点 1** (C2 p=0.10)：论文已三处标注 exploratory，C1 完全独立不受影响
- **攻击点 2** (prompt <3% vs Sclar 50-76%)：accuracy range ≠ variance share，prompt×item=5.5% 说明 item-conditional 效应存在但总份额小
- **攻击点 3** (binary only)：5 项 robustness check + partial-credit G 降至 0.768 + text-exact-match G=0.007，且论文在 §3.4/§6/§5 三处限定 scope
- **攻击点 4** (scale invariance)：Qwen 3B/7B/72B 跨 24× + Llama-70B 跨架构，item dominance 73-83%，§4.6 标题已注明 Preliminary

---
