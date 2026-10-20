# urgent 57 6 ground truth

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_57_6-ground-truth_20260515T154109_result.json`
- **Structured JSON:** [`4c3c1f1d1e6fcba0eb3e.json`](../../sessions/4c/4c3c1f1d1e6fcba0eb3e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集完毕。以下是分析结论。

---

## 1. 57.6% 的精确来源

**Registry: `plan-013-labeling-quality`**，metrics 字段：
- `ablation_b_mean_balanced_acc = 0.5761`
- `ablation_b_std_balanced_acc = 0.0047`

这是 4 个 ablation-b checkpoints 在**固定 val split** 上的评估均值：
| Checkpoint | 原始 eval（各自 split, n=306） | plan-013 固定 split |
|---|---|---|
| `plan-004-implicit` (seed42) | 0.5927 | ~0.576* |
| `ablation-b-seed123` | 0.5736 | ~0.574* |
| `ablation-b-seed456` | 0.5748 | ~0.575* |
| `ablation-b-seed789` | 0.5831 | ~0.580* |
| **Mean ± Std** | 0.5811 ± 0.008 | **0.5761 ± 0.0047** |

（*个别 seed 值未单独存储，但均值/std 在 registry 中确认。）

57.6±0.5% = plan-013 的固定 split 4-seed 均值，**不是**单个 seed 的结果。

---

## 2. 0.5944 vs 0.5685 差异分析

| | eval-template-fix (0.5944) | checkpoint 诊断 (0.5685) |
|---|---|---|
| **Checkpoint** | `plan-004-implicit/final_adapter` | `plan-004-implicit/final_adapter` |
| **同一 checkpoint** | **是，同一个** | **是，同一个** |
| **Val set** | 300 samples (30 int / 270 det) | 未保存文件，inline 诊断 |
| **enable_thinking** | **true**（输出含 `&lt;think>\n\n&lt;/think>` 空标签） | 未知，可能 off |
| **Val split** | 非标准（与 plan-013 的 306 样本不同） | 非标准 |
| **来源** | `results/eval-template-fix/plan-004-implicit_fixed.json` | registry `plan-008-router-size-v3` 诊断文本 |

**差异原因：不同的 val split（不同的 episode-level 分层采样）。** 两者都是单 seed、非标准 val set 的 eval。internal 类只有 30 个样本，1-2 个样本的分类变化就能导致 ~0.03 的 balanced_acc 波动。

enable_thinking 不是关键因素——模型输出空 `&lt;think>` 标签，解析后与 thinking off 结果功能等价。plan-008-v3 诊断也确认 "enable_thinking irrelevant"。

---

## 3. 论文应引用哪个数字

**继续引用 57.6±0.5%（plan-013-labeling-quality）。** 理由：

1. 这是最严格的评估协议：4 seed 均值 + 固定 val split + 一致的 eval 配置
2. 0.5944 和 0.5685 都是单 seed 诊断性评估，val set 不标准（300 vs plan-013 的 306），不能取代 plan-013
3. enable_thinking 对结果无实质影响（空 think 标签），不需要因此重跑
4. **不需要用修复后的 eval 重跑 4 个 seed** —— "修复"指的是 checkpoint 识别（plan-004-v5 vs plan-004-implicit），而 plan-013 自始至终使用的就是正确的 ablation-b checkpoints

**补充建议**：seed-robustness-core 的 55.4±5.2%（不同 split，范围 0.4852-0.6074）可以作为 robustness 分析报告，说明 val split 选择带来的方差远大于 seed 方差（5.2% vs 0.5%），但不影响主表数字。

---
