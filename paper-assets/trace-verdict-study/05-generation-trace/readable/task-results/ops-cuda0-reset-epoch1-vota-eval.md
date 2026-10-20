# ops cuda0 reset epoch1 vota eval

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cuda0_reset_epoch1_vota_eval_20260515T221615_result.json`
- **Structured JSON:** [`f215e3a781e8c99a8cad.json`](../../sessions/f2/f215e3a781e8c99a8cad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三步全部完成。汇报如下：

---

## 结果汇报

### Step 1: GPU 0 Reset
- GPU 0 有 49GB 残留显存但无活跃进程
- `nvidia-smi --gpu-reset -i 0` **不支持**（硬件限制）
- 直接使用 GPU 0 跑 eval，PyTorch 成功分配显存，不受影响
- GPU 1 (PID 163109, deepseek_full_trace_v3) 未受任何干扰

### Step 2: seed456 epoch1 (checkpoint-148) eval
| 指标 | 值 |
|------|-----|
| Accuracy | **99.3%** (95% CI: [98.8%, 99.7%]) |
| fail F1 | **0.99** (P=0.98, R=1.00) |
| pass F1 | 1.00 (P=1.00, R=0.99) |
| Majority baseline | 71.5% |

**关键发现：epoch1 (99.3%) 与 epoch3 (99.33%) 几乎无差异，1 epoch 即已收敛。**

Predictions 已保存至：`/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_exception_only_seed456/checkpoint-148/predictions.jsonl`

### Step 3: DeepSeek VOTA eval
| 指标 | 值 |
|------|-----|
| Accuracy | **16.0%** (95% CI: [13.9%, 18.0%]) |
| fail F1 | 0.61 (P=0.90, R=0.47) |
| pass F1 | 0.07 (P=1.00, R=0.04) |

**VOTA 表现极差** — accuracy 仅 16%，远低于多数类基线 71.5%。模型严重偏向预测 fail（pass recall 仅 4%），几乎把所有样本都判为 fail。这说明 DeepSeek VOTA 模型未正确学到 VOTA 条件下的判别模式。

Predictions 已保存至：`/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_vota/final/predictions.jsonl`
Results JSON：`/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_vota/final/eval_results.json`

---
