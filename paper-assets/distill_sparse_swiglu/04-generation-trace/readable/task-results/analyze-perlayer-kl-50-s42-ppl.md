# analyze perlayer kl 50 s42 ppl

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_perlayer_kl_50_s42_ppl_20260522T071107_result.json`
- **Structured JSON:** [`122f9b8c16919c0340de.json`](../../sessions/12/122f9b8c16919c0340de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifact 已存在且数据完整。

## 结果汇总

**Benchmark eval PPL: 34.8473**

| 指标 | 值 |
|------|-----|
| WikiText-2 PPL | 34.8473 |
| 实际 sparsity | 0.496 (target 0.50) |
| Per-layer sparsity 范围 | 0.484 ~ 0.500 |
| 与训练 eval PPL (34.85) 一致性 | **完全一致** (34.8473 ≈ 34.85) |

**训练过程正常：**
- 10000/10000 steps 完成，EXIT_CODE=0
- avg_kl 从训练过程中稳步收敛至 0.0282
- 每层 sparsity 控制精确（均在 0.484–0.520 范围内，最终 eval 时 0.484–0.500）
- lambda 自适应调节工作正常（各层 final_lambda 从 0.01 到 5000 不等）

**结论：** PPL=34.85 已确认，远超预期范围 (11.84~18.52)。Sparsity 控制本身没有问题（精确达到 ~50%），问题出在 per-layer KL 训练方法在 50% sparsity 下的质量严重退化。

---
