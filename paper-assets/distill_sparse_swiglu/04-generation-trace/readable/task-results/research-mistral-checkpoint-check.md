# research mistral checkpoint check

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_mistral-checkpoint-check_20260516T235806_result.json`
- **Structured JSON:** [`899130443c3f08ade922.json`](../../sessions/89/899130443c3f08ade922.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报如下：

## 检查结果

### 1. Mistral 基础模型
**存在** — `/root/autodl-tmp/models/mistral-7b/`（Mistral-7B-v0.3，3 分片 safetensors）

### 2. Mistral predictor checkpoint
| 路径 | 说明 |
|------|------|
| `/root/distill_sparse_swiglu/checkpoints/mistral_kl_s42/predictor_kl_normalized.pt` | 唯一 checkpoint，~145MB |
| `/root/distill_sparse_swiglu/checkpoints/mistral_dryrun/` | 空目录 |

### 3. Sparsity target 确认
日志 `lm_eval_mistral_kl_50pct.log` 明确显示：
```
Computing TEAL global masks (sparsity=0.5)
Model-level: 0.500
```
**现有 checkpoint 是 50% sparsity 训练的，没有 30% sparsity 的 checkpoint。**

30% cross-architecture 验证需要重新训练 predictor。

### 4. GPU 状态
| GPU | 型号 | 显存 | 占用 | 利用率 |
|-----|------|------|------|--------|
| cuda:0 | RTX PRO 6000 Blackwell | 97887 MiB | 0 MiB | 0% |
| cuda:1 | RTX PRO 6000 Blackwell | 97887 MiB | 0 MiB | 0% |

**双卡完全空闲**，可以立即启动 30% sparsity predictor 训练。

---
