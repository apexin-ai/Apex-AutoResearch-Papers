# diag gemma2 s0 sweep exit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_gemma2-s0-sweep-exit_20260520T123248_result.json`
- **Structured JSON:** [`c4722b8325e69b181a0c.json`](../../sessions/c4/c4722b8325e69b181a0c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：假警报，sweep 正常运行。**

| 组件 | 状态 |
|------|------|
| **PID 314035** | 已正常退出（d000 训练/eval 的子进程，exit code=0） |
| **PID 314029** | 父脚本 `run_gemma2_s0.sh` 仍在运行（2h47m） |
| **PID 342346** | 当前活跃子进程，正在训练 **d005_s0**（7分钟，GPU 1, 94.5GB） |

**Checkpoint 状态：**

| Dosage | 训练 | Eval | 备注 |
|--------|------|------|------|
| d000_s0 | ✅ 完成 | ✅ MMLU 完成 | lora_alpha=32 ✓, checkpoint-3125, adapter 216MB |
| d005_s0 | 🔄 进行中 | ⏳ 待做 | 刚启动 7min |
| d025_s0 | ⏳ 待做 | ⏳ 待做 | 空目录（预创建） |
| d050_s0 | ⏳ 待做 | ⏳ 待做 | 空目录（预创建） |
| d100_s0 | ⏳ 待做 | ⏳ 待做 | 目录尚未创建 |

**死因：** PID 314035 不是崩溃，是 bash 脚本正常的子进程生命周期——d000 完成后子进程退出，父脚本 fork 新子进程继续 d005。

**cuda:1 当前状态：** 98% 利用率，94.5GB 显存，被 d005 训练独占。

**进度估算：** 1/5 dosage 完成（含 eval）。按 d000 耗时推算，全部完成约需 ~20h。

Registry 中无 `sft_gemma2_s0_sweep` 条目，是否需要创建？

---
