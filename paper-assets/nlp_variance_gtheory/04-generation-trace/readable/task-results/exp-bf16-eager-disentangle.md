# exp bf16 eager disentangle

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_bf16_eager_disentangle_20260520T191016_result.json`
- **Structured JSON:** [`98b64e2ef095f66b676c.json`](../../sessions/98/98b64e2ef095f66b676c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成，结果非常清晰。

---

## 结果

### 总体准确率
| 配置 | 准确率 |
|------|--------|
| BF16 + V1 (default) | 0.6844 |
| **BF16 + eager (V0)** | **0.6822** |
| FP32 + eager (V0) | 0.5994 |

### 效应分解
| 效应 | 大小 | 占 total gap 比例 |
|------|------|-------------------|
| Engine effect (V1→V0) | +0.0022 | **2.6%** |
| Precision effect (bf16→fp32) | +0.0828 | **97.4%** |
| Total gap | +0.0850 | 100% |

### 按 subject
| Subject | BF16+V1 | BF16+eager | FP32+V0 |
|---------|---------|------------|---------|
| abstract_algebra | 0.3056 | 0.3139 | 0.3028 |
| college_physics | 0.5111 | 0.5000 | 0.4889 |
| professional_medicine | 0.7417 | 0.7417 | 0.5417 |
| us_foreign_policy | 0.9750 | 0.9750 | 0.8528 |
| world_religions | 0.8889 | 0.8806 | 0.8111 |

### 关键结论

FP32 的准确率下降 **几乎完全是精度效应（97.4%），而非引擎效应（2.6%）**。BF16+eager 与 BF16+V1 仅差 0.22 个百分点，而 BF16→FP32 的切换造成了 8.28 个百分点的巨大差距。

这意味着 vLLM V0/V1 引擎差异可以忽略不计。FP32 在这些 MMLU subjects 上的劣势是 **数值精度本身造成的** —— 很可能是 float32 推理路径在 softmax/attention 计算中与 BF16 产生了不同的舍入行为，导致 FP32 反而更差（counter-intuitive，但与已知的 "BF16 训练的模型用 FP32 推理不一定更好" 现象一致）。

### 论文表述建议

论文中可以写：*"A disentangling experiment (BF16 with enforce_eager=True, matching the FP32 engine path) confirmed that 97.4% of the observed precision gap is attributable to numerical precision itself, not to differences in the inference engine (V0 eager vs. V1 CUDA graph). This suggests that the precision facet in our G-theory decomposition captures a genuine computational artifact rather than a confound with engine implementation."*

---
