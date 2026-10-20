# ssh verify grpo standard 25 and submit evals

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify_grpo_standard_25_and_submit_evals_20260523T192034_result.json`
- **Structured JSON:** [`d09a5ff0a73cb815b68d.json`](../../sessions/d0/d09a5ff0a73cb815b68d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

TRL GRPOConfig 默认 `beta=0.0`（无 KL 惩罚）。但 `grpo_standard_25` 是用旧版 `train_grpo.py` 训练的，该脚本没有显式传 beta，所以用了 TRL 默认值 **beta=0.0**。

而 `train_grpo_v5.py`（新版）默认 `beta=0.01`，retrain 日志确认 beta=0.01。qwen_math 日志显示 beta=0.04（可能是显式传参）。

## 产出

```
grpo_standard_25 checkpoint 路径: /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25/model.safetensors
grpo_standard_25 模型大小: 11,582,559,224 bytes (~10.8GB)
beta 参数: 0.0 (来源: train_grpo.py 未传 beta → TRL GRPOConfig 默认 beta=0.0)
sft_standard_25 checkpoint 路径: /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/model.safetensors (10.8GB, May 24)
westd GPU 空闲: No — 全部 4 张 GPU 在使用中
  - cuda:0: 55833 MiB used, 91% util
  - cuda:1: 17541 MiB used, 98% util
  - cuda:2: 19251 MiB used, 98% util
  - cuda:3: 19251 MiB used, 98% util
eval_math500.py: 存在 (/root/recovery_aware_struct_prune/src/eval_math500.py, 8568 bytes)
```

**注意**：
- 原始 `grpo_standard_25` 用的是旧版 `train_grpo.py`，beta=0.0（无 KL 惩罚，无 ref model）
- `grpo_standard_25_retrain` 用新版 `train_grpo_v5.py`，beta=0.01
- `grpo_standard_25_qwen_math` 用新版，beta=0.04
- 4 张 GPU 目前全部占用，无法立即跑 eval

---
