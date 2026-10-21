# check hsweep h2 seed1 progress

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_hsweep_h2_seed1_progress_20260517T072406_result.json`
- **Structured JSON:** [`791a7b6c314e859a5ad3.json`](../../sessions/79/791a7b6c314e859a5ad3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已有足够信息。总结结果：

---

## hsweep_h2_seed1 训练状态

| 项目 | 值 |
|------|------|
| **当前 step** | 2 / 15 |
| **启动时间** | 2026-05-17 12:17 (约 3.2h 前) |
| **GPU 使用** | cuda:0 96%, cuda:1 97% (各 34GB/98GB) |
| **进程** | 正常运行 (pid 920380) |

### 训练指标 (train)
| Step | success | pass@8 |
|------|---------|--------|
| 1 | 18.75% | 43.75% |
| 2 | 14.84% | 50.00% |

### Val 结果
- **step 0 (val_before_train)**: success = 0.0%, pass@1 = 0.0%
- 下一次 val 待确认（可能在 step 5）

### 时间估算
- Step 1 耗时: ~3150s (~52min)
- Step 2 耗时: ~2650s (~44min)
- 平均 ~48min/step，剩余 13 steps → **预计还需 ~10.4 小时**

### auto_next_hsweep.sh 状态
- **就绪**，序列: `2:1 → 2:2 → 2:3 → 5:1 → ...`
- h=2 seed2 的 `LOG_PER_SAMPLE_ADV=1` 已配置
- **但 launch_hsweep.sh 没有自动调用 auto_next**——训练结束后需要手动触发 `auto_next_hsweep.sh 2 1`

---
