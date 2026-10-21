# ssh analyze completed 5090

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_analyze_completed_5090_20260521T105140_result.json`
- **Structured JSON:** [`f94f4ce9d8b283cd5d5c.json`](../../sessions/f9/f94f4ce9d8b283cd5d5c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验2和3尚未完成，仍在运行中。** 以下是当前状态汇总：

---

### 汇总报告

| exp_id | status | greedy_f1 | mv_f1 | oracle_f1 | fleiss_κ | soft_jaccard | samples | notes |
|--------|--------|-----------|-------|-----------|----------|-------------|---------|-------|
| exp_scierc_mf4_v2_s42 | **DONE** | 0.6651 | — | 0.7815 | 0.4026 | 0.7075 | 551 | verdict=MARGINAL |
| exp_fewnerd_mf4v2_s123 | **RUNNING 25%** | — | — | — | — | — | 0 | 73976/301184 prompts, ~84min left |
| exp_fewnerd_mf4v2_s42 | **RUNNING 25%** | — | — | — | — | — | 0 | 73888/301184 prompts, ~84min left |

### 实验1详细指标 (SciERC MF4v2 seed42)

- **Greedy F1: 0.6651** (预期 ≈0.666 ✓)
- **Oracle F1: 0.7815** (预期 ≈0.78 ✓)
- Oracle headroom: +0.1164
- Fleiss' kappa: 0.4026, Soft Jaccard: 0.7075
- Sample F1 mean: 0.6044 (std=0.3206, 12.9% zero)
- Structural > Surface: **YES** (Δ=+0.1017)
- Logprob baseline: ρ=0.2098, AUROC=0.5676 (full)
- Verdict: **MARGINAL**

### GPU 状态

| GPU | Utilization | Memory |
|-----|------------|--------|
| 0 | 0% | 2 / 32607 MiB (idle) |
| 1 | 74% | 30214 / 32607 MiB (fewnerd exp) |
| 2 | 77% | 30256 / 32607 MiB (fewnerd exp) |
| 3 | 70% | 30044 / 32607 MiB (exp_e2_pretrained_fewnerd — 另一个实验) |

### 注意

- FewNERD 数据集有 37648 实例 × 8 samples = 301184 prompts，两个实验各自在 GPU 1/2 上运行，预计还需 ~80-90 分钟。
- GPU 3 上还有一个 `exp_e2_pretrained_fewnerd` 实验在跑（用的是 Qwen2.5-7B-Instruct 预训练模型，非 FT 版本）。

---
