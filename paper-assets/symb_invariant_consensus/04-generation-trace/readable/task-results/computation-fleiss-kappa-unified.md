# computation fleiss kappa unified

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_computation_fleiss-kappa-unified_20260519T040611_result.json`
- **Structured JSON:** [`db543eb2f608a6761fe2.json`](../../sessions/db/db543eb2f608a6761fe2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

## 产出

**脚本**: `scripts/compute_fleiss_kappa_unified.py` — 已部署到 westd-25068 和 westd-16639
- 从原始 trace 答案重新归一化（非标准→Unknown，空→排除）
- Fleiss' kappa 支持变长 N（方案 B）
- Eff-K = K / (1 + (K-1) * kappa)，K=12
- 自动检测数据集类型（FOLIO/PW → True/False/Unknown，LogiQA → A/B/C/D）

**合并结果**: `artifacts/fleiss_kappa_unified_merged.json`

## Table 3 核心数据（9 个实验）

| Exp | Model | Dataset | κ | Eff-K | SC Acc | SICA Acc | Δpp | Valid Rate |
|-----|-------|---------|------|-------|--------|----------|------|------------|
| 027 | Qwen3-14B | FOLIO-204 | 0.773 | 1.26 | 85.29 | 84.31 | -0.98 | 99.96% |
| 033 | Mistral-7B | FOLIO-204 | 0.460 | 1.98 | 55.88 | 59.31 | +3.43 | 87.58% |
| 035 | Qwen2.5-7B | FOLIO-204 | 0.658 | 1.46 | 77.45 | 76.47 | -0.98 | 99.96% |
| 036 | Qwen2.5-14B | FOLIO-204 | 0.744 | 1.31 | 76.47 | 75.49 | -0.98 | 100% |
| 038 | Qwen2.5-14B | LogiQA-200 | 0.821 | 1.20 | 79.00 | 78.00 | -1.00 | 100% |
| 046 | Mistral-7B | PW-600 | 0.200 | 3.76 | 38.33 | 36.67 | -1.67 | 83.96% |
| 052 | Mistral-7B | FOLIO-204 (s123) | 0.457 | 1.99 | 54.41 | 57.35 | +2.94 | 87.09% |
| 053 | Mistral-7B | FOLIO-204 (s456) | 0.457 | 1.99 | 54.41 | 55.88 | +1.47 | 87.13% |
| 055 | Mistral-7B | FOLIO-204 (multi-T) | 0.427 | 2.11 | 57.35 | 57.84 | +0.49 | 85.58% |

## 关键发现

- Mistral-7B 的非标准答案问题严重：102-359 个答案被映射为 Unknown，12-16% 的 trace 为空
- 强模型（Qwen3-14B、Qwen2.5-14B）几乎没有非标准答案（0-2 个）
- 旧脚本 kappa=0.5006（exp-033），新统一脚本 kappa=0.4598 — 差异来自非标准答案归一化
- **exp-026/041 在两台服务器上均未找到**，exp-036 (Qwen2.5-14B FOLIO-204) 可能是对应实验

---
