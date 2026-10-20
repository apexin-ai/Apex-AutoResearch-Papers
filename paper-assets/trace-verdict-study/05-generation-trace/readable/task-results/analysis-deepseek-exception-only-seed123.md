# analysis deepseek exception only seed123

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_deepseek_exception_only_seed123_20260515T200548_result.json`
- **Structured JSON:** [`08c45df705dac69eb635.json`](../../sessions/08/08c45df705dac69eb635.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已获取。以下是结果汇总：

---

## deepseek_exception_only_seed123 实验结果

### 评估指标

| 指标 | seed123 | seed42 | 差异 |
|------|---------|--------|------|
| **Accuracy** | **91.09%** | 99.83% | **-8.74pp** |
| Majority baseline | 71.5% | — | — |
| Lift over majority | +19.6pp | — | — |
| n | 1190 | — | — |

**Per-class metrics (seed123):**

| Class | Precision | Recall | F1 |
|-------|-----------|--------|-----|
| pass | 1.00 | 0.993 | 0.996 |
| fail | 0.976 | **0.705** | 0.818 |

**95% CI:** accuracy [89.4%, 92.6%]

### 训练信息

- train_loss: 0.1220
- epochs: 3.0
- train_runtime: 6384s (~106 min)
- train_samples/sec: 2.218
- train_steps/sec: 0.07

### 文件路径

- Checkpoint: `/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_exception_only_seed123/final`
- eval_results.json: 同上目录
- predictions.jsonl: `/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_exception_only_seed123/final/predictions.jsonl`

---

### 关键发现：seed123 大幅退化

**Accuracy 从 99.83% (seed42) 跌至 91.09% (seed123)，差 8.74pp。** 这与 Qwen exception_only 的跨种子稳定性完全不同。

问题定位在 **fail recall = 0.705**——模型漏判了约 30% 的 fail 样本。pass 侧几乎无影响（recall 0.993）。pass precision = 1.0 说明模型预测 pass 时基本不会错，但倾向于把 fail 样本也预测为 pass（保守偏移）。

这意味着：
- **DeepSeek 在 exception_only condition 上对种子不鲁棒**，seed42 的 99.83% 可能是运气好
- exception signal 的 universality claim 需要修正：信号本身是有效的（91% >> 71.5% baseline），但 DeepSeek 利用该信号的能力不如 Qwen 稳定
- train_loss 0.122 偏高（seed42 应该更低），暗示 LoRA 初始化随机性导致收敛到了较差的局部最优

---
