# pipeline crossbench local

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_pipeline_crossbench-local_20260522T231414_result.json`
- **Structured JSON:** [`7625d3bad3e9dc944a4e.json`](../../sessions/76/7625d3bad3e9dc944a4e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

### 配置 A: AlpacaEval × Llama-70B × formality
| 指标 | 值 |
|---|---|
| N | 100 pairs, 61 consistent (61%) |
| **BT** | win_prob=0.775, CI=[0.72, 0.83], p<0.001 ✓ |
| **Likert** | ATE=0.451, d=1.12, p<0.001 ✓ (sign-test) |
| **GEE style OR** | 12.14 [5.47, 26.92], p<0.001 |
| **GEE orig OR** | 1.44 [0.67, 3.06], p=0.348 (NS) |
| **Blindspot** | No — BT sig + Likert sig |

### 配置 B: MT-Bench × Qwen3-32B × formality
| 指标 | 值 |
|---|---|
| N | 80 pairs, 40 consistent (50%) |
| **BT** | win_prob=0.700, CI=[0.64, 0.76], p<0.001 ✓ |
| **Likert** | ATE=0.301, d=0.25, p=0.035 ✓ (paired t-test, N=73 NLI≥0.90) |
| **GEE style OR** | 4.73 [1.23, 18.24], p=0.024 |
| **GEE orig OR** | 4.73 [1.23, 18.24], p=0.024 |
| **Blindspot** | No — BT sig + Likert sig |

**关键发现**:
- 两个配置均无 blindspot（BT 和 Likert 一致显著）
- Llama-70B 对 formality 偏好更强（BT 0.775 vs 0.700），GEE style OR 也更高（12.1 vs 4.7）
- AlpacaEval × Llama-70B 的 GEE 成功分离了 style 效应（OR=12.1, p<0.001）和 originality 效应（OR=1.4, NS），说明偏好主要来自风格偏差而非原创性偏好
- MT-Bench × Qwen3-32B 的 GEE 两个 OR 完全相同，因为 original_formality 分布极度不平衡（69 formal : 11 casual），style 和 original 高度共线（r=0.725），无法有效分离

产出已写入 `/root/causal_style_decomp_judge/artifacts/r14_fixes/cross_benchmark_local.json`。

---
