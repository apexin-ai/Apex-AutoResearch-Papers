# code exp 015 v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_015_v2_20260514T152014_result.json`
- **Structured JSON:** [`8b58682b56883f53b472.json`](../../sessions/8b/8b58682b56883f53b472.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结如下：

## exp-015 v2 结果

**覆盖范围**: 5 信号 × 10 数据集 × 2 subtask(NER/RE) = 18 组合 × 4 指标 = 360 个指标点，全部附带 bootstrap 95% CI

### AUROC 关键发现

| 数据集组 | SJ | FK | logprob | EM | voting_conf |
|---|---|---|---|---|---|
| CoNLL NER | 0.80 | 0.77 | 0.75 | **0.82** | 0.79 |
| SciERC NER (avg) | 0.73 | 0.62 | 0.59 | **0.79** | 0.74 |
| SciERC RE (avg) | 0.68 | 0.59 | 0.58 | **0.72** | 0.72 |
| LLaMA NER (avg) | 0.70 | 0.65 | 0.56 | **0.75** | 0.72 |
| LLaMA RE (avg) | 0.71 | 0.68 | 0.65 | **0.76** | 0.75 |
| WNUT NER | 0.58 | 0.58 | 0.36 | 0.57 | **0.87** |

### 排名

- **AUROC**: EM 在绝大多数数据集上最强 (12/18)；voting_conf 在 WNUT 上大幅领先 (0.87)
- **Spearman ρ**: voting_conf 在 15/18 组合上最高（rank correlation 与 F1 的关联最强）
- **Kendall τ**: voting_conf 同样领先
- **ECE**: voting_conf 在 RE 上校准最好 (ECE < 0.20)；EM 在 NER 上校准最好

### LOO-SJ Robustness

所有 18 个组合的 |Δρ| < 0.001，LOO-SJ 与 full SJ 相关系数 ≥ 0.9999。**无循环性问题**。

### 产出

- JSON 结果: `autodl-5090:/root/autodl-tmp/struct_self_consist_ie/output/exp_015_v2/exp015_v2_metrics.json` (82KB)
- Registry: `exp_015_v2` → DONE/success
- Artifact: `art_20260514_adacf4` 已注册

---
