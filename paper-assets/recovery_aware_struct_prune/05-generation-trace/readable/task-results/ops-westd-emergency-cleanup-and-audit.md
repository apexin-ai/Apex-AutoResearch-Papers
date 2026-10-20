# ops westd emergency cleanup and audit

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_emergency_cleanup_and_audit_20260520T055610_result.json`
- **Structured JSON:** [`8e8072ef17192b1c4aea.json`](../../sessions/8e/8e8072ef17192b1c4aea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 汇报

### 1. Checkpoint 列表

| 目录 | Checkpoints | Final Step | 备注 |
|------|------------|------------|------|
| grpo_stage2_standard_20_fair | ~~checkpoint-80~~, ~~checkpoint-90~~, **checkpoint-100** | 100 | ✅ 完整 (model 12G + optimizer 15G) |
| grpo_cka_only_20 | **checkpoint-100** | 100 | ✅ 完整 (model 12G + optimizer 15G, rng_state.pth.bak) |
| grpo_stage2_rasp_20_fair | ~~checkpoint-80~~, ~~checkpoint-90~~, **checkpoint-100** | 100 | ✅ 完整 (model 12G, 无 optimizer) |
| grpo_random_20 | 无 checkpoint（仅 completions 目录） | step-97 中断 | ⚠️ 在 westb-23072 上，非 westd |

**15% GRPO（已 crash）：**

| 目录 | Checkpoints | 状态 |
|------|------------|------|
| grpo_cka_only_15 | ~~checkpoint-10~~, checkpoint-20 (3.7G) | checkpoint-20 可用于重启 |
| grpo_standard_15 | ~~checkpoint-10~~, checkpoint-20 (48KB) | ⚠️ checkpoint-20 **损坏** (model.safetensors 仅 40KB) — 无法用于重启 |

### 2. Patience 参数

| Run | reward_desert_patience | 来源 |
|-----|----------------------|------|
| grpo_stage2_standard_20_fair | **50** (default) | W&B config 无显式设置 |
| grpo_cka_only_20 | **50** (default) | 同上 |
| grpo_stage2_rasp_20_fair | **50** (default) | 同上 |
| grpo_random_20 | **50** | 日志明确打印 |
| grpo_cka_only_15 | **50** | 日志明确打印 |
| grpo_standard_15 | **50** | 日志明确打印 |

**Random step-97 停止原因：`EXIT_CODE=124` (timeout 命令超时杀进程)，非 patience 触发。** 日志末尾 `97/100 [11:47:40] EXIT_CODE=124`。

### 3. 清理报告

| 删除项 | 大小 |
|--------|------|
| standard_20_fair/checkpoint-80 | 12G |
| standard_20_fair/checkpoint-90 | 12G |
| rasp_20_fair/checkpoint-80 | 12G |
| rasp_20_fair/checkpoint-90 | 12G |
| cka_only_15/checkpoint-10 | 28G |
| standard_15/checkpoint-10 | 28G |
| __pycache__ + *.pyc | ~微量 |
| **总计释放** | **~104G** |

**清理前后：** 619G/619G (100%) → 518G/619G (84%)，**可用 102GB**。

### 4. v5 step-100 Checkpoint 可用性

| Run | Eval 可用 | model.safetensors | optimizer.pt |
|-----|-----------|-------------------|--------------|
| Standard (fair) | ✅ | 12,323,931,184 bytes | ✅ 15.7GB |
| CKA-only | ✅ | 12,323,931,248 bytes | ✅ 15.7GB |
| RASP (fair) | ✅ | 12,323,931,224 bytes | ❌ 无 optimizer |

三个 checkpoint-100 的 model.safetensors 均完整（~12GB），可直接用于 eval。RASP 无 optimizer 不影响推理。

### ⚠️ 需注意

1. **grpo_standard_15/checkpoint-20 损坏**：重启 15% Standard GRPO 需从 pruned model 重新开始（或从 SFT 重来）
2. **grpo_random_20 无 model 产出**：因 timeout 中断且 save_steps 对齐在 100，无可用 checkpoint

---
