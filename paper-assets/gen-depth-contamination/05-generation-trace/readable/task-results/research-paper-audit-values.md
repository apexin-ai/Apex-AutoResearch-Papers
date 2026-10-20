# research paper audit values

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_paper-audit-values_20260518T052213_result.json`
- **Structured JSON:** [`0e3e618d2b3e6f4b4931.json`](../../sessions/0e/0e3e618d2b3e6f4b4931.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕。

---

## 1. Qwen-7B C4 1v2 AUC

**文件不存在。** `results/exp_004_7b_crossscale/` 目录在服务器上不存在。

exp-004 仅完成了 VRAM 评估（见本地 `artifacts/exp-004/report/vram_assessment.md`），当时 7B 模型尚未下载，实验被 VRAM 占用阻塞，从未执行。

服务器上已有的 Qwen-7B 实验均非 C4 域：
- `exp_arXiv_qwen7b`: 1v2 = **0.8347** (fold mean)
- `exp_wiki_qwen7b`: 1v2 = **0.6108** (fold mean)
- `exp_arXiv_qwen7b_crossscorer`: 1v2 = **0.8163** (bootstrap OOF)

**结论：Qwen-7B × C4 实验从未完成，无数据。**

---

## 2. Pythia decoding 0v1

文件目录：`/root/autodl-tmp/gen-depth-contamination/results_exp020_pythia_*/pairwise_auc.json`

| 策略 | fold mean 0v1 |
|------|--------------|
| greedy | 0.9992 |
| nucleus p=0.9 | 0.9948 |
| temperature=0.7 | 0.9965 |
| temperature=1.2 | 0.9933 |

bootstrap OOF 0v1：**无。** exp020 目录下不存在 bootstrap_ci 文件，仅有 `pairwise_auc.json`、`jsd.json`、`ordinal_results.json`、`feature_importance.json`、`summary.txt`。

**结论：Tab S10 中 0v1 用的是 fold mean。**

---

## 3. Wiki 0v1

文件：`/root/autodl-tmp/gen-depth-contamination/results/exp_023_wiki/pairwise_auc.json`
值：**0.9961** (fold mean)

所有 wiki 实验 0v1 汇总：

| 实验 | 0v1 |
|------|-----|
| exp_023_wiki (Qwen-1.5B gen) | 0.9961 |
| exp_wiki_pythia | 0.9961 |
| exp_wiki_olmo | 0.9961 |
| exp_wiki_olmo_v2 | 0.9932 |
| exp_wiki_pythia_v2 | 0.9750 |
| exp_wiki_scorer_confound_1b5 | 0.9729 |
| exp_wiki_qwen7b | 0.9673 |
| exp_wiki_mistral7b | 0.9607 |
| exp_wiki_scorer_confound | 0.9404 |
| exp_wiki_llama8b | 0.9316 |

**.985 来源：无法从现有文件中找到。** 没有任何 wiki 实验的 0v1 等于 0.985。最接近的是 exp_arXiv_qwen7b 的 0.983（但那是 arXiv 域）和 results_exp016_qwen_base 的 0.987（但那是 C4 域）。.985 可能是旧版实验结果、手动四舍五入、或论文中的笔误。

---

## 4. Wikipedia JSD λ

文件：`/root/autodl-tmp/gen-depth-contamination/artifacts/jsd_decay_analysis.json`

| 模型 × 域 | λ | a | c (floor) |
|-----------|---|---|-----------|
| Qwen-1.5B × Wiki | **2.9782** | 0.143721 | 0.004475 |
| OLMo × Wiki | **6.2836** | 0.165744 | 0.003035 |
| Pythia-1.4B × Wiki | **3.3062** | 0.074962 | 0.005102 |

Wikipedia 域平均 λ = **4.1893**

另有 `results/exp_023_wiki/jsd.json` 的原始 JSD 值（Qwen-1.5B × Wiki）：
- 0v1: 0.148199, 1v2: 0.011665, 2v3: 0.006087, 3v4: 0.004085, 4v5: 0.003764

---

## 5. Retrain-chain bootstrap_ci_v2

文件（远程）：`/root/autodl-tmp/gen-depth-contamination/results/exp_008_retrain_chain/bootstrap_ci_v2.json`
文件（本地）：`artifacts/exp_008_retrain_chain_v2/bootstrap_ci_results.md`

两处数据一致：

| Pair | OOF AUC | 95% CI | boot_std |
|------|---------|--------|----------|
| 0v1 | 0.9842 | [0.9823, 0.9860] | 0.0009 |
| 1v2 | 0.9471 | [0.9432, 0.9509] | 0.0020 |
| 2v3 | 0.8888 | [0.8832, 0.8943] | 0.0028 |
| 3v4 | 0.7994 | [0.7920, 0.8067] | 0.0037 |

备注：bootstrap OOF AUC（10,000 resamples, doc-level），Scorer = Qwen2.5-1.5B, K*=4（所有 CI lower > θ=0.60）。Permutation p < 0.001 for all pairs。

---
