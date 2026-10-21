# setup qwen3 7b pilot prep

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_setup_qwen3-7b-pilot-prep_20260516T085843_result.json`
- **Structured JSON:** [`aaae4fa929fe01b3e7b0.json`](../../sessions/aa/aaae4fa929fe01b3e7b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. PID 768865 (sweep-exec-only-s45-r2)
- **状态**: 存活，运行 36 分钟
- **进度**: step 496/500（即将完成）
- prove_rate=1.0, reward_mean=1.0

### 2. 模型
- **Qwen3-8B** 已存在于 `/root/autodl-tmp/models/Qwen3-8B`
- 16GB，5 个 safetensors 分片，完整可用

### 3. Config 文件
| 文件 | 关键参数 |
|------|----------|
| `configs/grpo_exec_only_8b.yaml` | batch=2, grad_accum=4, K=4, adamw_bnb_8bit, gradient_checkpointing=true |
| `configs/grpo_additive_bonus_b01_8b.yaml` | 同上 + beta=0.1, reward_mode=additive_bonus |

### 4. Dry-run 结果
- **K=4 可以跑，但需要 8-bit optimizer**
- 8B + 标准 Adam 不可能在单卡 98GB 上跑（model 16GB + optimizer 64GB + gradients 16GB = 96GB 最低，不含 activations）
- 使用 `adamw_bnb_8bit` + `gradient_checkpointing` + `batch_size=2`：峰值约 79GB，在 95GB 可用显存内
- **当前阻塞**：eval_sta.py (PID 785241) 占用 GPU 0 共 16GB，已设后台脚本（PID 794397）等其结束后自动执行验证

### 5. 磁盘
- 69GB 可用 / 250GB 总量（73% 使用率）
- Qwen3-8B 占 16GB，足够

### 6. 脚本修改
`train_grpo.py` 新增：
- `--optim` 参数（传递到 GRPOConfig）
- `gradient_checkpointing` 从 YAML config 传递到 GRPOConfig

### 待确认
后台 PID 794397 会在 eval 结束后自动跑 2-step dry-run。可稍后 `tail /tmp/8b_dryrun_final.log` 查看结果。如果成功，8B pilot 可直接启动训练。

---
