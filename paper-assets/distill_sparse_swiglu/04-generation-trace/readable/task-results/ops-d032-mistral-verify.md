# ops d032 mistral verify

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d032_mistral_verify_20260516T032843_result.json`
- **Structured JSON:** [`9429ce23e909f91a8def.json`](../../sessions/94/9429ce23e909f91a8def.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集。以下是完整结论：

---

## 验证结果

### 1. Mistral PPL eval 结果文件

**存在**，位于 `/root/runs/distill_sparse_swiglu/eval_mistral_kl_s42.log`：

| 指标 | 值 |
|------|-----|
| Dense PPL | **5.52** |
| Hard Mask PPL | **7.30** |
| TEAL Sparse PPL | **8.98** |

dense=5.52 ≠ Llama 的 6.12，确认评估使用的是 Mistral-7B 模型。

### 2. Mistral checkpoint 验证

**确认是 Mistral 训练产物。** checkpoint args 明确记录：
- `model_name_or_path: /root/autodl-tmp/models/mistral-7b`
- `wandb_run_name: mistral_kl_s42`
- `loss_type: kl_normalized`, `num_steps: 1000`, `seed: 42`

### 3. cuda:1 lm_eval_mistral_kl_50pct

**使用了正确的 Mistral 模型。** PID 195242 仍在运行，命令行参数：
```
--model_name_or_path /root/autodl-tmp/models/mistral-7b/
--predictor_path checkpoints/mistral_kl_s42/predictor_kl_normalized.pt
```
当前进度约 37%（generate_until 489/1319），预计还需 ~40 分钟。

### 4. 未启动 PPL re-eval

不需要。现有 PPL 结果已验证为独立的 Mistral 评估。

### 5. GPU 状态

| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| cuda:0 | **0 MiB** / 97887 MiB | 0% (空闲) |
| cuda:1 | 62082 MiB / 97887 MiB | 96% (lm_eval 运行中) |

### 6. 关键发现：**污染在 Llama 30% 端，不在 Mistral 端**

对比 eval 日志的实际值：

| 条件 | Dense | Hard Mask | TEAL Sparse | 来源日志 |
|------|-------|-----------|-------------|---------|
| **mistral_kl_s42** (50%) | 5.52 | **7.30** | **8.98** | `eval_mistral_kl_s42.log` |
| **kl_sparsity30_s42_v3** (30%→eval@50%) | 6.12 | **7.30** | **13.63** | `eval_kl_sparsity30_s42_v3.log` |

- `hard_mask_ppl=7.30` 两者确实相同（巧合——不同模型、不同稀疏度碰巧相等）
- `teal_sparse_ppl`：Llama 30% 实际是 **13.63**，**不是 8.98**

**结论：Registry 中 `kl_sparsity30_s42_v3` 的 `teal_sparse_ppl` 被错误录入为 8.98（Mistral 的值），正确值应为 13.63。** Mistral 端的数据是正确的。

---
