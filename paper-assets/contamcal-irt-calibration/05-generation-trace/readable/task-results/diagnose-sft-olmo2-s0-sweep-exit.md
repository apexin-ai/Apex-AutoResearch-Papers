# diagnose sft olmo2 s0 sweep exit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_sft_olmo2_s0_sweep_exit_20260520T044050_result.json`
- **Structured JSON:** [`078b5ddd162ddc73b039.json`](../../sessions/07/078b5ddd162ddc73b039.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Sweep **仍在正常运行**，没有退出。

**诊断结果：**

| 项目 | 状态 |
|------|------|
| PID 261133 | 已退出（不是 sweep 脚本本身） |
| sweep 脚本 | PID 238801，bash `run_olmo2_s0.sh`，存活，已运行 3h30m |
| GPU 2 当前进程 | PID 280811，训练 **d025_s0**，已运行 ~6 分钟 |

**Checkpoint 完成情况：**
- d000: ✅ 完成（`adapter_model.safetensors` 存在）
- d005: ✅ 完成（`adapter_model.safetensors` 存在）
- d025: 🔄 训练中（目录已创建，PID 280811 刚开始）
- d050: ⏳ 未开始
- d100: ⏳ 未开始

**进度估算：** 2/5 dosage 完成，d025 刚启动。按 ~1.9s/step 估算，d025 (3384 steps) + d050 (3642) + d100 (4159) ≈ 11,185 steps ≈ **5.5-6 小时**后全部完成。

**不更新 registry，不删 cron** — sweep 正常推进中。westd cuda:2 **不空闲**，正在被 sweep 占用。

---
