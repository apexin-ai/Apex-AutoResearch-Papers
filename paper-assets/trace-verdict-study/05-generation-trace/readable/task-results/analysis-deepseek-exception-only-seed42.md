# analysis deepseek exception only seed42

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_deepseek_exception_only_seed42_20260515T150745_result.json`
- **Structured JSON:** [`3e8a0cecd3f2517192ca.json`](../../sessions/3e/3e8a0cecd3f2517192ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有 per-sample predictions 文件，无法做 paired bootstrap。但各条件的 CI 完全不重叠，显著性不存疑。

---

## DeepSeek exception_only (seed42) 实验结果

### 核心指标

| 指标 | 值 | 95% CI |
|------|-----|--------|
| **Accuracy** | **99.33%** | [98.8%, 99.7%] |
| Majority baseline | 71.5% | — |
| Lift | +27.8pp | [+25.5pp, +30.3pp] |
| Pass P / R / F1 | 1.00 / 0.99 / 1.00 | — |
| Fail P / R / F1 | 0.98 / 1.00 / 0.99 | — |
| N | 1190 | — |

### 条件对比（DeepSeek-Coder-6.7B）

| 条件 | Accuracy | 95% CI | vs exception_only |
|------|----------|--------|-------------------|
| **exception_only** | **99.33%** | [98.8%, 99.7%] | — |
| vota | 84.45% | [82.6%, 86.4%] | -14.88pp |
| no_trace | 73.36% | [70.8%, 75.7%] | -25.97pp |

CI 完全不重叠，差异极显著（exception_only 下界 98.8% >> VOTA 上界 86.4% >> no_trace 上界 75.7%）。

### 跨模型对比（exception_only 条件）

| 模型 | Accuracy |
|------|----------|
| Qwen-2.5-Coder-7B | 99.83% |
| DeepSeek-Coder-6.7B | 99.33% |

两模型在 exception_only 条件下均接近天花板，差距仅 0.5pp。

### 结论: **Success**

- exception_only 在 DeepSeek-Coder 上达到 **99.33%**，大幅超越 no_trace (+25.97pp) 和 VOTA (+14.88pp)
- 与 Qwen 上的 99.83% 高度一致，证明 exception_only 信号的有效性跨模型泛化
- 训练正常完成，eval 1190 样本，fail recall 达到 100%（所有 fail 样本都被正确识别）

---
