# paper group ablation logo

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_group-ablation-logo_20260522T132258_result.json`
- **Structured JSON:** [`4055faa44bf930577daf.json`](../../sessions/40/4055faa44bf930577daf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果：

**验证**：C_all7 3-class F1 = 0.7696，与预期 ~0.77 吻合。Binary F1 = 0.9475 而非预期的 ~0.694——因为本实验 binary 定义是 human(depth=0) vs machine(depth≥1)，而已有 pipeline 的 binary 是 gen-1 vs gen-2+（排除 depth=0），后者更难，所以 0.694 对应的是那个定义。

**Task 1: Group Ablation**

| Group | 3-class F1 | Binary F1 |
|-------|-----------|-----------|
| A: drifting-only | 0.7182±0.0877 | 0.8802±0.0667 |
| B: non-drifting | 0.6697±0.0491 | 0.8528±0.0303 |
| C: all-7 | 0.7696±0.0747 | 0.9475±0.0420 |

Drifting features (A) 单独已超过 non-drifting (B)，all-7 组合进一步提升。Mistral 在所有组中都是最难泛化的 generator。

**Task 2: max_depth Sensitivity**

| max_depth | 3-class F1 | Binary F1 |
|-----------|-----------|-----------|
| 3 | 0.7547±0.0772 | 0.9243±0.0500 |
| 4 | 0.7600±0.0762 | 0.9358±0.0456 |
| 6 | 0.7696±0.0747 | 0.9475±0.0420 |
| 8 | 0.7739±0.0703 | 0.9517±0.0392 |

性能随 depth 单调递增但边际递减，3→8 仅提升 ~2pp，说明分类器对超参不敏感。

脚本和 JSON 结果已保存到 `artifacts/_project/analysis/`。

---
