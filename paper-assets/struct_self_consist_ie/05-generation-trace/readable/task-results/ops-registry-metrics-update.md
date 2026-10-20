# ops registry metrics update

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_registry_metrics_update_20260515T113729_result.json`
- **Structured JSON:** [`bb9649b27ffe4371e5f5.json`](../../sessions/bb/bb9649b27ffe4371e5f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个实验全部更新完成。汇总：

### exp_001_n16_seed456 — Qwen SciERC N=16 seed456 → DONE

| Metric | NER | RE |
|--------|-----|------|
| Greedy F1 | 0.6617 | 0.4215 |
| Oracle F1 | 0.8075 | 0.4748 |
| ρ(SJ) | **0.4134** | 0.1966 |
| ρ(FK) | 0.3448 | 0.2179 |
| ρ(VC) | 0.4042 | 0.2155 |
| ρ(LP) | 0.2136 | **0.4006** |
| ρ(EM) | 0.2907 | 0.028 |
| AUROC(SJ) | **0.7094** | — |
| AUROC(FK) | 0.6499 | — |
| AUROC(VC) | 0.6776 | — |
| AUROC(LP) | 0.6121 | — |
| AUROC(EM) | 0.6542 | — |

### exp_017_llama_conll_n16_r1024 — LLaMA CoNLL N=16 seed42 → DONE

| Metric | Value |
|--------|-------|
| Greedy NER F1 | 0.9264 |
| Oracle NER F1 | 0.9494 |
| ρ(FK) | **0.8095** |
| ρ(VC) | 0.7949 |
| ρ(SJ) | 0.1815 |
| AUROC(FK) | **0.9070** |
| AUROC(VC) | 0.8757 |

### exp_017_llama_conll_n16_s456_r1024 — LLaMA CoNLL N=16 seed456 → DONE

| Metric | Value |
|--------|-------|
| Greedy NER F1 | 0.9265 |
| Oracle NER F1 | 0.9499 |
| ρ(FK) | **0.8085** |
| ρ(VC) | 0.7968 |
| ρ(SJ) | 0.1895 |
| AUROC(FK) | **0.9059** |
| AUROC(VC) | 0.8775 |

CoNLL AUROC 使用 `>=median` 阈值（median F1=1.0，87.6% 实例完全正确，`>median` 无正例）。CoNLL 上 FK 和 VC 显著优于其他信号；SciERC 上 SJ 最强。

---
