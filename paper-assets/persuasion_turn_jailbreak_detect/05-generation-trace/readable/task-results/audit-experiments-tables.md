# audit experiments tables

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_experiments-tables_20260523T102207_result.json`
- **Structured JSON:** [`29530451ac618df2ff1b.json`](../../sessions/29/29530451ac618df2ff1b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。检查了 ~120 个定量声明，报告已写入 `artifacts/audit_experiments.md`。

**需修正 (5 项)**:

1. **9-class DD-Full .994→.997** — 3 seed 均值 = (1.0+1.0+0.9904)/3 = 0.9968。影响 Table 1/2/3 及 ~8 处行内引用。
2. **Scrambled DD-Full .994→.997** — 同上逻辑，exp4 确认 scrambled_3seed.clean_full = 0.9968。
3. **Mean pooling DD-K=2: 1.000→.994±.009** — 论文用了 seed42 单种子值，但表格其他行都是 3-seed mean。exp13 3-seed = 0.9936±0.009。
4. **Llama Guard DD-Full .025→.024** — Registry f1_jb = 0.0244，四舍五入应为 .024。
5. **"4–20× lower variance"** — 实际范围 3–23×（DD: 23×, AA: 3.1×），上下界都超出。

**无法追溯 (6 项)**: MLM seed456 recall=0.64、turn-order shuffling Δ (DeBERTa/RoBERTa-large)、McNemar p>0.13、κ=0.78/0.126 — 均无对应 registry 条目。

---
