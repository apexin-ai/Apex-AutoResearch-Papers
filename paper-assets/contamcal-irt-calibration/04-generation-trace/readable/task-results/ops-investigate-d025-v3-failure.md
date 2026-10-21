# ops investigate d025 v3 failure

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_investigate-d025-v3-failure_20260515T203116_result.json`
- **Structured JSON:** [`f9892fad5606280500b4.json`](../../sessions/f9/f9892fad5606280500b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`.INVALID` 目录已删除，释放 21MB。

---

## 失败原因分析

### exp_001_sft_d025_3B_v3：cron 误判为 failed，训练实际已完成

**时间线：**
1. **00:12:34** — v3 训练进程启动，写入 checkpoint `Qwen2.5-3B_d025_v3_s42`
2. **00:15:19** — 一个重复提交（a32 命名）打到同一 GPU，因 GPU 已被 v3 进程占满（17.21 GiB）立即 OOM 崩溃（`exp_001_sft_3B_d025_s42_a32.log`）
3. **~04:15** — v3 训练正常完成 3384/3384 步，epoch 1.0，train_loss=1.146，保存了完整 LoRA adapter（119MB）
4. cron 5 次检查未发现活跃进程（可能在追踪 OOM 崩溃的 PID） → auto-resolved as failed

**根因：C001 违规（重复提交）+ cron 追踪了错误的 PID。**

**Checkpoint 完整性：** `Qwen2.5-3B_d025_v3_s42/lora_adapter/` 完好——`adapter_model.safetensors`（119MB）、`adapter_config.json`（r=16, alpha=32）、`checkpoint-3384` 目录均存在。缺少 sentinel 文件是 cron 判定 failed 的直接原因。

**对其他 PREPARING 实验的影响：** 无。这是该特定 GPU 上的重复提交问题，不影响其他 GPU 上的实验。

**建议：** registry 中该实验状态应从 failed 改回 completed，无需重训。

### Stale 文件清理

`/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d000_s42.INVALID/`（21MB，旧 alpha=16 d000_s42 信号，12 个 JSON 文件）已删除。

---
