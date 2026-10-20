# exp sft dryrun 73

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_sft-dryrun-73_20260514T080900_result.json`
- **Structured JSON:** [`b5e1ede96e7246e074dd.json`](../../sessions/b5/b5e1ede96e7246e074dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全流程验证完成。汇报如下：

---

## SFT Pipeline Dry Run 结果

### 1. 轨迹数据
- 成功轨迹：**124 条**（JSONL 格式，实际比预期 73 条多）
- 失败轨迹：37 条
- 注入变体（dry_run）：**96 条**（4 条因轨迹过短失败）

### 2. 注入算子分布（均匀）
| 算子 | 数量 |
|------|------|
| C1_context_truncation | 25 |
| C4_observation_masking | 24 |
| P1_step_order_swap | 25 |
| P2_sub_goal_deletion | 22 |

### 3. SFT 数据格式
- 格式正确：ms-swift `{"messages": [...]}` 多轮对话
- assistant 内容结构：`&lt;think>...&lt;/think>\n&lt;action>...&lt;/action>`
- vanilla 数据：124 条（实际入训 116 条，8 条可能因 max_length 截断被过滤）
- token 长度：平均 944 ± 415，min=345，max=2045

### 4. 训练结果（1 epoch, cuda:0）
- **成功完成** 8 步 / 42 秒
- 参数：batch_size=1, grad_accum=16, max_length=2048, lr=1e-4, LoRA r=16

| Step | Loss | Grad Norm | Token Acc |
|------|------|-----------|-----------|
| 1 | 2.436 | 3.060 | 0.682 |
| 4 | 2.012 | 2.568 | 0.697 |
| 7 | 1.388 | 1.210 | 0.719 |
| 8 | 1.543 | 1.038 | 0.696 |

- **初始 loss**: 2.436 → **最终 loss**: 1.543（平均 train_loss: 1.894）
- Loss 持续下降，最低到 1.388（step 7），说明模型在学习

### 5. 显存占用
- 峰值：**19.22 GiB** / 32 GiB（~59%）
- 稳定在 19 GiB 左右

### 6. 遇到的问题及修复
- **OOM**：batch_size=2 + max_length=4096 时 OOM（cross_entropy 分配 4.33 GiB 失败）
  - 修复：降 batch_size 到 1，max_length 降到 2048，加 `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True`
- **注入变体不能直接入 SFT**：dry_run 变体格式是 `corrupted_history`/`recovery_think=DRY_RUN`，没有 `steps` 字段，formatter 无法转换。正式跑需要 API 生成 recovery demonstration 才能产出完整 TaxEI 训练数据。

### 7. Checkpoint
- 保存于 `checkpoints/dryrun_sft_v2/v0-20260514-161410/checkpoint-8/`
- 含 `adapter_model.safetensors`（LoRA 权重）

### 正式训练建议参数
- `per_device_train_batch_size=1, gradient_accumulation_steps=16, max_length=2048` 在单卡 RTX 5090 上安全
- 如需 max_length=4096，需要多卡或进一步减少显存（如 LoRA rank 降到 8）

---
