# infra folio 2x2 completion check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_folio-2x2-completion-check_20260522T053202_result.json`
- **Structured JSON:** [`a03e02361c4b1b99ad8f.json`](../../sessions/a0/a03e02361c4b1b99ad8f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验正常完成。4 个 cell 文件均存在（metrics JSON 已确认每个 204 items），sentinel found。

## FOLIO 2×2 Results

|  | **Mistral ext** | **Qwen3 ext** |
|---|---|---|
| **Mistral gen** (SC=55.88%, κ=0.46) | SICA=56.86%, Δ=+0.98pp, BR=2.70 | SICA=59.80%, Δ=+3.92pp, BR=1.94 |
| **Qwen3 gen** (SC=83.33%, κ=0.79) | SICA=81.86%, Δ=−1.47pp, BR=2.66 | SICA=84.80%, Δ=+1.47pp, BR=2.35 |

**McNemar tests** (cross-extractor comparison, same generator):
- Mistral ext: A vs C → p≈0.000 (10 vs 61 discordant)
- Qwen3 ext: B vs D → p≈0.000 (7 vs 58 discordant)

**Key observations:**
- 跨模型提取（off-diagonal）对弱 generator（Mistral）有 +3.92pp 提升（Cell B vs A），对强 generator（Qwen3）有 −1.47pp 下降（Cell C vs D）
- BR 值均 >1，说明 SICA 在所有 cell 中都优于随机纠错
- McNemar 两组均极显著，generator 质量是主导因素
- 总耗时 ~98.5 min（Cell D），整个实验约 4 cells × ~100 min

---
