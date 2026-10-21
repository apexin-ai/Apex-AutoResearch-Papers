# ops verify grpo eos and fix 25

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify_grpo_eos_and_fix_25_20260516T120722_result.json`
- **Structured JSON:** [`6f9ba49248783b203b49.json`](../../sessions/6f/6f9ba49248783b203b49.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 1. 20% GRPO 状态：❌ EOS 无效 — 进程卡死

| 指标 | RASP (PID 5033/5038) | Standard (PID 5111/5116) |
|------|---------------------|--------------------------|
| 运行时间 | 8h25m | 8h23m |
| 步数完成 | 0/100 | 0/100 |
| GPU 利用率 | 100% | 100% |
| 显存占用 | 35GB | 30GB |
| wandb 更新 | 无（启动后 4 分钟停止写入） | 无 |
| checkpoint | 无 | 无 |

**诊断**：generation_config.json 修复在磁盘上是正确的（20% 模型在 19:44 已修为 `[151643, 151645]`），GRPO 在 20:03 启动。但进程卡死在第一步 generation 调用——8 小时零完成。`max_completion_length=1024` 本应硬限制生成长度，但看起来 generation 根本没有返回。

**可能原因**：非均匀剪枝架构（intermediate_size range [8128, 18944]）与 TRL GRPOTrainer 的 batched generation 不兼容，导致 `model.generate()` 挂死。

**需要 kill 重启。** PID 5033 和 5111（及其子进程 5038、5116）需要终止，排查 generation 兼容性问题后重启。

### 2. 25% generation_config.json：✅ 已修复

两个文件均已更新为 `eos_token_id: [151643, 151645]`：
- `/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_25/generation_config.json`
- `/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_standard_25/generation_config.json`

### 3. 附加发现

GPU 2/3 上正在跑 25% rasp 模型的 eval_gsm8k（PID 6140/6220），利用率 92-95%。

---
