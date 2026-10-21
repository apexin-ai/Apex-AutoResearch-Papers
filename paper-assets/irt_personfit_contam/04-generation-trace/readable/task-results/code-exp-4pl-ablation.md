# code exp 4pl ablation

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-4pl-ablation_20260520T130416_result.json`
- **Structured JSON:** [`42824c8583c3d33fa2f7.json`](../../sessions/42/42824c8583c3d33fa2f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。核心结果：

**4PL vs 3PL — hypothesis confirmed**：d 参数显著提升检测灵敏度。

| Benchmark | 平均 power 增益 | 最大 power 增益 |
|-----------|----------------|----------------|
| MMLU | +27.3pp | +49.0pp |
| HellaSwag | +26.1pp | +59.6pp |
| GSM8K | +20.3pp | +39.7pp |
| ARC_C | +14.8pp | +54.6pp |
| HumanEval | +13.7pp | +30.6pp |

**校准验证**：4PL FAR ≈ 5%（正确校准），3PL FAR 略偏高（4.7–16.5%），2PL FAR 灾难性膨胀（50–100%，c=0.25 的固定假设完全不成立，power 数值无意义）。

**d-bucket 分析**：d < 0.8 的 items 上 4PL 优势最大（MMLU +61pp, HellaSwag +58pp），d ≥ 0.95 时差异可忽略 — 证实 d 参数捕捉的 ceiling effect 是检测力提升的关键来源。

产出文件在 `artifacts/4pl_ablation/`，共 7 个文件已注册。

---
