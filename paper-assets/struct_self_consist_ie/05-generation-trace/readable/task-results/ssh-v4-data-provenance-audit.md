# ssh v4 data provenance audit

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_v4_data_provenance_audit_20260521T143559_result.json`
- **Structured JSON:** [`d824a1df341c51403398.json`](../../sessions/d8/d824a1df341c51403398.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息收集完毕。汇总如下。

---

## Part 1: CoNLL v4 Strict 精确值

**注意**: `conll_mf4v2_seed42` 目录**不存在**。Seed 42 使用的是 `exp002_conll2003`（May 14 旧 pipeline，9.8MB vs mf4v2 的 ~58MB），无 per-token logprobs。但 recompute 脚本只用 entities 字段，MV 指标计算有效。

| Seed | greedy_f1 | mv_strict | mv_incl | oracle_f1 | δ | α_crit | Δ_strict (pp) | Δ_incl (pp) |
|------|-----------|-----------|---------|-----------|------|--------|----------------|-------------|
| 42 (exp002) | 0.9123 | 0.9142 | 0.9132 | 0.9543 | 56.7% | 0.4561 | **+0.20** | +0.09 |
| 123 (mf4v2) | 0.9119 | 0.9123 | 0.9151 | 0.9542 | 60.3% | 0.4560 | **+0.04** | +0.32 |
| 456 (mf4v2) | 0.9116 | 0.9121 | 0.9133 | 0.9502 | 60.4% | 0.4558 | **+0.04** | +0.17 |
| **3-seed mean** | **0.9119** | **0.9129** | **0.9139** | **0.9529** | **59.1%** | **0.4560** | **+0.09** | **+0.19** |

**关键结论**: s123 和 s456 的 Δ_SC_strict 均为**正值** (+0.04pp)，非常小但为正。三个 seed 无一为负。δ 极高（57-60%），α_crit_eff > 1，MV 几乎没有实质改善空间。

---

## Part 2: FewNERD MF4v2 数据溯源

| 属性 | seed42 | seed123 | seed456 |
|------|--------|---------|---------|
| 路径 | `output/fewnerd_mf4v2_seed42/` | `output/fewnerd_mf4v2_seed123/` | `output/fewnerd_mf4v2_seed456/` |
| 文件大小 | 672 MB | 684 MB | 689 MB |
| 行数 | 37,648 | 37,648 | 37,648 |
| 创建时间 | May 21 20:33 | May 21 20:34 | May 21 16:06 |
| report.json | 有 (verdict: FAIL) | **无** | 有 (verdict: MARGINAL) |
| 5090b 副本 | 有 (673MB, 15:38) | 有 (685MB, 15:36, 有 report.json MARGINAL) | 无 |
| 日志文件 | 无 | 无 | 无 |

**JSON 格式检查**: 结构为 `{id, text, gold, samples[8], greedy, logprobs}`，每个 sample 含 `entities, relations, events, cumulative_logprob, n_tokens, mean_logprob, token_logprobs, token_texts`。这是标准 MF4v2 pipeline 输出格式，包含 per-token logprobs。

**report.json 指标对比**:
| | seed42 | seed123 (5090b) | seed456 |
|--|--------|-----------------|---------|
| greedy_f1 | 0.7887 | 0.7883 | 0.7889 |
| oracle_f1 | 0.8784 | 0.8891 | 0.8810 |
| fleiss_kappa | 0.3524 | 0.3483 | 0.3557 |

**结论**:
1. **数据可靠**。三个 seed 均有 37,648 行（FewNERD test set 完整），JSON 格式正确，由 MF4v2 pipeline 生成（含 8 samples + greedy + per-token logprobs）。
2. **时间线**: seed456 最早完成（16:06），seed42/123 紧随（20:33-20:34）。5090b 上有更早的副本（15:36-15:38），说明数据先在 5090b 生成后复制到 5090 并可能在 5090 上重跑。
3. **seed123 的 report.json 缺失**: output/ 目录下无 report.json，但 output_from_5090b/ 下有（verdict: MARGINAL）。数据本身完整，仅 report 生成可能被中断。
4. **不需要等 mf4v2_v3 重跑**——数据已就绪可用。唯一需注意的是 CoNLL 缺 `conll_mf4v2_seed42`（当前用的是旧 pipeline 的 exp002 数据）。

---
