# analysis model size scaling 8b

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_model-size-scaling-8b_20260512T092221_result.json`
- **Structured JSON:** [`0634bf905e0aa9975cf4.json`](../../sessions/06/0634bf905e0aa9975cf4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

grep 带 pipe 被 read_only 阻止了，但从日志和 JSON 已经获取了全部关键信息。

---

## 实验结果汇总

### 1. 完整 Metrics

| Metric | 8B CLS | 8B CWM |
|--------|--------|--------|
| **accuracy** | **90.48%** | 87.67% |
| pass_precision | 90.22% | 91.53% |
| pass_recall | 91.51% | 83.95% |
| **pass_f1** | **90.86%** | 87.57% |
| fail_precision | 90.76% | 84.19% |
| fail_recall | 89.36% | 91.67% |
| **fail_f1** | **90.06%** | 87.77% |
| exact_match_rate | — | 84.39% |
| train_loss | 0.3125 | 0.2290 |
| eval_loss | 0.0783 | 0.0564 |
| unparseable | 0 | 0 |

### 2. Scaling Deltas

#### 8B CLS vs 4B CLS (classification scaling gain)

| Metric | 4B (3-seed mean) | 8B | **Delta** |
|--------|:-:|:-:|:-:|
| accuracy | 88.41% | 90.48% | **+2.07pp** |
| pass_f1 | 88.41% | 90.86% | **+2.45pp** |
| fail_f1 | 88.40% | 90.06% | **+1.66pp** |

#### 8B CWM vs 4B CWM (CWM scaling gain)

| Metric | 4B | 8B | **Delta** |
|--------|:-:|:-:|:-:|
| accuracy | 87.51% | 87.67% | **+0.16pp** |
| pass_f1 | 87.31% | 87.57% | **+0.26pp** |
| fail_f1 | 87.71% | 87.77% | **+0.06pp** |
| exact_match | 84.02% | 84.39% | **+0.37pp** |

#### 8B CLS vs 8B CWM (classification advantage at 8B)

| Metric | CLS | CWM | **CLS advantage** |
|--------|:-:|:-:|:-:|
| accuracy | 90.48% | 87.67% | **+2.81pp** |
| pass_f1 | 90.86% | 87.57% | **+3.29pp** |
| fail_f1 | 90.06% | 87.77% | **+2.29pp** |

### 3. Hypothesis 验证：Classification 优势是否随模型增大扩大

| Gap (cls - cwm) | 4B | 8B | 变化 |
|:--|:-:|:-:|:-:|
| accuracy | +0.90pp | **+2.81pp** | **3.1×** |
| pass_f1 | +1.10pp | **+3.29pp** | **3.0×** |
| fail_f1 | +0.69pp | **+2.29pp** | **3.3×** |

**结论：Classification 优势随模型增大显著扩大。** 4B 时两种方法几乎等价（gap <1pp），8B 时 classification 全面领先 2-3pp。原因很清晰：**Classification 从 4B→8B 获得了 ~2pp 的真实 scaling gain，而 CWM 基本持平（<0.3pp）——CWM 在 4B 就已经饱和了。**

### 4. 训练信息

| | CLS 8B | CWM 8B |
|--|--|--|
| 训练开始 | 15:46:09 | 15:46:10 |
| 训练结束 | 17:19:43 | 17:19:01 |
| wall clock | **1h33m34s** (5614s) | **1h32m50s** (5570s) |
| throughput | 8.17 samples/s | 8.24 samples/s |
| checkpoint | `checkpoints_cls8b/best` | `checkpoints_cwm8b/best` |
| 模型参数 | 8.2B total, 15.3M trainable (0.19% LoRA) | 同左 |
| epochs | 3 | 3 |

### 5. 异常检查

无异常。两个实验均：
- 训练完整跑完 3 epochs (1434 steps)
- 无 OOM、NaN、early stopping
- unparseable_predictions = 0
- Loss 曲线正常收敛（CLS: 7.50→0.07→0.08 eval, CWM: 5.48→0.05→0.06 eval）
- CWM 8B 注意 pass_recall 偏低（83.95%），fail_recall 偏高（91.67%），存在明显 bias 倾向把 pass 预测为 fail

### CWM error-type 亮点

CWM 8B 在不同错误类型表现分化很大：
- SyntaxError: exact_match 98.8%, accuracy 100% (最强)
- AssertionError: exact_match 86.7%, accuracy 91.0%
- IndexError: exact_match 仅 30.0%（最弱，但 pass/fail accuracy 仍 85%）
- OverflowError: exact_match 0%，但 pass/fail accuracy 100%

这说明 CWM 在 pass/fail 二分类上的瓶颈不在错误类型预测失败，而在于即使预测了正确的错误类型，exact match 也不够精确——但这不影响 pass/fail 分类性能。

---
