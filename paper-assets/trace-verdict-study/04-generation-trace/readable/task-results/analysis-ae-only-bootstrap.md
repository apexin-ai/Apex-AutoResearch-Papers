# analysis ae only bootstrap

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_ae_only_bootstrap_20260515T121705_result.json`
- **Structured JSON:** [`1ebc38fec5735ab4f2fb.json`](../../sessions/1e/1ebc38fec5735ab4f2fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已收集全部数据。以下是完整分析：

---

## ae_only 完整 Metrics

| 指标 | 值 | 95% CI |
|------|------|--------|
| **Accuracy** | **99.92%** | [99.75%, 100%] |
| Majority baseline | 71.51% | — |
| Lift over baseline | +28.40pp | — |
| Pass precision | 100% | [100%, 100%] |
| Pass recall | 99.88% | [99.64%, 100%] |
| Pass F1 | 99.94% | [99.82%, 100%] |
| Fail precision | 99.71% | [99.07%, 100%] |
| Fail recall | 100% | [100%, 100%] |
| Fail F1 | 99.85% | [99.53%, 100%] |

## 全条件 Accuracy 对比

| 条件 | Accuracy | 95% CI | vs ae_only Δ |
|------|----------|--------|-------------|
| **ae_only** | **99.92%** | [99.75, 100] | — |
| exception_only | 99.83% | [99.58, 100] | -0.08pp |
| vota_no_ae | 99.41% | [98.91, 99.83] | -0.50pp |
| VOTA | 99.16% | [98.57, 99.66] | -0.76pp |
| loop_only | 85.63% | [83.53, 87.56] | -14.29pp |
| full_trace | 81.76% | [79.66, 83.95] | -18.15pp |
| no_trace | 75.13% | [72.77, 77.48] | -24.79pp |

## 关键发现

1. **ae_only 是所有条件中 accuracy 最高的**（99.92%），甚至超过完整 VOTA（99.16%）和 exception_only（99.83%）。

2. **但 99.9% 的 accuracy 几乎肯定是因为数据污染**——你已知 88% 样本的 actual/expected 字段 fallback 为 full locals dump。模型很可能在 locals dump 中直接匹配到了 pass/fail 的答案，而非真正学习 assertion error 的语义。CI 非常窄 [99.75%, 100%] 也佐证了这一点。

3. **ae_only 与 exception_only 的差异极小**（0.08pp），两者 CI 高度重叠。在干净数据上无法区分。

4. **排序异常**：ae_only > exception_only > vota_no_ae > VOTA。理论上信息量更大的条件反而更差，进一步说明 ae_only 的 locals dump 泄漏了标签信息。

## 训练参数确认

从 `trainer_state.json` 提取：

| 参数 | 值 |
|------|------|
| Epochs | 3 |
| Total steps | 444 (= 148 steps/epoch) |
| Train batch size | 4 |
| Peak LR | ~2e-4 (cosine schedule) |
| Framework | TRL SFT, Transformers 4.57.6, PyTorch 2.10.0+cu128 |
| Final train loss | 0.022 |
| Final eval loss | 0.166 |
| Final eval token accuracy | 96.76% |

**结论**：ae_only 的 99.9% accuracy 不可信，因 88% 样本存在 locals dump 数据泄漏。Bootstrap 对比在现有脚本下不直接适用（脚本仅支持原始 3 条件），但从 CI 重叠情况看，ae_only 与 exception_only 无统计显著差异，两者都远超 VOTA/full_trace/no_trace。

---
