# ops urgent collect all results

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent_collect_all_results_20260520T052441_result.json`
- **Structured JSON:** [`224cca74f17e31a2aa9f.json`](../../sessions/22/224cca74f17e31a2aa9f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有实验均已完成。汇总如下：

---

## 实验结果汇总

### 1. MSE 30% Eval (westd-41718 cuda:0) — 已完成 ✓

| Task | Metric | Value |
|------|--------|-------|
| WikiText-2 | PPL | **20.43** |
| ARC-Challenge | acc_norm | **0.3123** |
| WinoGrande | acc | **0.6038** |
| MMLU | acc | **0.3179** |
| GSM8K | exact_match | **0.0197** |
| HellaSwag | acc_norm | **0.5248** |
| PIQA | acc_norm | **0.6937** |

### 2. MSE 50% Eval (westd-41718 cuda:1) — 已完成 ✓

| Task | Metric | Value |
|------|--------|-------|
| WikiText-2 | PPL | **229.26** |
| ARC-Challenge | acc_norm | **0.2500** |
| WinoGrande | acc | **0.5059** |
| MMLU | acc | **0.2379** |
| GSM8K | exact_match | **0.0159** |
| HellaSwag | acc_norm | **0.2722** |
| PIQA | acc_norm | **0.5577** |

### 3. SNR Full Curve 1000 Steps (westd-34887 cuda:0) — 已完成 ✓

| Step | KL SNR (mean) | BCE SNR (mean) | KL/BCE Ratio |
|------|--------------|----------------|-------------|
| 0 | 0.0000130 | 0.0000699 | — |
| 50 | 0.0002534 | 0.0000082 | — |
| 100 | 0.0006114 | 0.0017290 | — |
| 200 | 0.0002357 | 0.0030785 | — |
| 300 | 0.0003465 | 0.0017422 | — |
| 500 | 0.0003501 | 0.0016771 | — |
| 700 | 0.0002145 | 0.0014132 | — |
| 1000 | 0.0008777 | 0.0020263 | **0.4332x** |

BCE loss curve 稳定在 ~0.636, sparsity 收敛到 ~0.300。

### 4. GPU 状态

| Server | GPU 0 | GPU 1 |
|--------|-------|-------|
| westd-41718 | 0 MiB, 0% | 0 MiB, 0% |
| westd-34887 | 0 MiB, 0% | 0 MiB, 0% |

所有任务完成，四卡均已释放。

---
