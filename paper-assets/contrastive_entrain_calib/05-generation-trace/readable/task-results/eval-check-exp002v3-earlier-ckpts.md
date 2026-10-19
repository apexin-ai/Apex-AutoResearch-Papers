# eval check exp002v3 earlier ckpts

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_check-exp002v3-earlier-ckpts_20260522T130113_result.json`
- **Structured JSON:** [`b03884524bb189dbd6d2.json`](../../sessions/b0/b03884524bb189dbd6d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### Checkpoints 可用性（westd-28034）

路径：`/root/autodl-tmp/checkpoints/exp002v3_dcgrpo_scaled_cosine/`

| Checkpoint | 时间 | adapter 文件 | 状态 |
|---|---|---|---|
| checkpoint-500 | May 20 05:23 | ✅ adapter_model.safetensors | 完整可用 |
| checkpoint-1000 | May 20 07:14 | ✅ adapter_model.safetensors | 完整可用 |
| checkpoint-1500 | May 20 08:53 | ✅ adapter_model.safetensors | 完整可用 |
| checkpoint-2000 | May 20 10:18 | ✅ adapter_model.safetensors | 完整可用 |
| checkpoint-2500 | May 20 11:45 | ✅ adapter_model.safetensors | 完整可用 |

### Eval 结果

- **ckpt-2000**：已有 eval → **SYCONScore = 0.0**，ToF = 0.0，NoF = 1.0（完全坍塌，模型对所有样本输出相同的无关废话，NLI 全判 neutral）
- **ckpt-500 / 1000 / 1500 / 2500**：**无 eval 结果**，需要新跑

### GPU 状态（westd-28034）

| GPU | 利用率 | 显存占用 |
|---|---|---|
| GPU 0 | 48% | 16.5GB / 32GB（忙） |
| GPU 1 | 0% | 空闲 |
| GPU 2 | 0% | 空闲 |
| GPU 3 | 0% | 空闲 |

### 结论

需要对 **ckpt-500、ckpt-1000、ckpt-1500** 跑 eval（ckpt-2500 比 2000 更晚大概率也是坍塌），GPU 1/2/3 空闲可用。建议优先 eval ckpt-1500 → ckpt-1000 → ckpt-500，从接近坍塌点向前追溯，找到 collapse 前最后稳定 checkpoint。

---
