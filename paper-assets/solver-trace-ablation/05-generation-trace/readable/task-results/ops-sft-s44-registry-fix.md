# ops sft s44 registry fix

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_sft-s44-registry-fix_20260515T084021_result.json`
- **Structured JSON:** [`78b0f22ae1fbe174fffa.json`](../../sessions/78/78b0f22ae1fbe174fffa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All steps complete. Here's the summary:

---

## 1. 修正后的 s44 指标

| Metric | 旧值 (test_100.jsonl) | 新值 (proofwriter_fol_100.jsonl) |
|--------|----------------------|--------------------------------|
| prove_rate | 0.14 (14/100) | **0.17 (17/100)** |
| mean_isr | 0.0784 | **0.0974** |
| proved_only_isr | 0.56 | **0.5729** |
| isr_std | 0.2454 | **0.2409** |
| by_answer_type | 50/44/6 | **34/25/41** |

Registry 已更新。

## 2. H7/H1/Genuine 分类 (s44, 17 proved)

| Category | Count | Rate |
|----------|-------|------|
| H7 | 0 | 0.000 |
| H1 | 2 | 0.118 |
| Genuine | **15** | **0.882** |

H1 样本：folio_1117 (idx=59, conclusion `Like(fabien,cheese)` 出现在 P3 中), folio_167 (idx=70, `Leader(elizabeth)` 直接作为 P5)。

## 3. SFT 3-seed Pooled Wilson CI

| Metric | Pooled | 95% CI |
|--------|--------|--------|
| Prove Rate | 46/300 = 0.153 | [0.117, 0.199] |
| Genuine Rate | 42/300 = 0.140 | [0.105, 0.184] |
| Genuine/Proved | 42/46 = 0.913 | [0.797, 0.966] |
| H7 Rate | 0/300 = 0.000 | [0.000, 0.013] |
| H1 Rate | 4/300 = 0.013 | [0.005, 0.034] |
| ISR* (proved-only) | 0.580 ± 0.014 | — |

**Fisher exact: SFT vs Exec-Only pooled genuine:**
- SFT: 42/300 (14.0%), Exec-only: 12/300 (4.0%)
- Odds ratio = 3.91, **p = 0.000023** (significant)

Per-seed breakdown:
- s42-r4: PR=0.14, genuine=13, H1=1
- s43: PR=0.15, genuine=14, H1=1
- s44: PR=0.17, genuine=15, H1=2

## 4. 错误 eval 排查

训练日志中无 eval 命令记录（log 仅包含 SFT 训练输出）。错误 eval 由 worker 单独执行，registry 中旧 by_answer_type 分布为 True=50/False=44/Unknown=6，这是 **test_100.jsonl** 的特征分布（vs proofwriter_fol_100.jsonl 的 34/25/41）。违反 C008/C009 约束——eval 时使用了 test_100.jsonl 或脚本默认值指向了错误数据集。

---
