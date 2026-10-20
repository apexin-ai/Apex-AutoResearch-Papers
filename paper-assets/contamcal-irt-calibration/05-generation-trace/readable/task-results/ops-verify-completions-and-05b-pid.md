# ops verify completions and 05b pid

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-completions-and-05b-pid_20260516T014832_result.json`
- **Structured JSON:** [`63699286d5585763836e.json`](../../sessions/63/63699286d5585763836e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 05B batch
- **PID**: N/A — tmux session `exp_002_signals_05B_s123_batch` 不存在
- **GPU 1**: 0 MiB / 24564 MiB, 0% util — 完全空闲
- **所有 tmux sessions**: 无任何 05B 相关 session
- **结论**: 任务未成功提交或已崩溃退出。需要重新提交。

## d100_s42_a32_v3
- **Completed**: YES
- **Checkpoint**: `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_a32_s42_v3/lora_adapter/`
- **adapter_model.safetensors**: 存在, 119.8 MB
- **lora_alpha**: 32 ✓
- **Final loss**: 1.206, epoch 1.0, mean_token_accuracy 0.723
- **Train runtime**: 17645s (~4.9h), 4159/4159 steps
- **EXIT_CODE**: 0
- **Conclusion**: **success**

## sim_sweep_v7
- `exp004/` 目录不存在，全盘 `find *sim_sweep*` 也无结果
- **Conclusion**: 路径可能有误，或结果在其他位置。需要 Reviewer 确认实际路径。

## v8_recovery outputs
- **signal_s1_embedding_mmlu.json**: 存在, 14042 items, 7.8 MB
- **signal_s2_minkpp_mmlu.json**: 存在, 14042 items, 2.9 MB
- **signal_s4_selfcritique_mmlu.json**: 不存在（OOM 前未完成）
- **Conclusion**: s1 + s2 完整 (各 14042 items)，s4 缺失

---
