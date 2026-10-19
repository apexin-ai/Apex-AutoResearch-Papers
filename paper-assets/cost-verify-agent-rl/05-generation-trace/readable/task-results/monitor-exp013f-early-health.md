# monitor exp013f early health

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp013f-early-health_20260514T093311_result.json`
- **Structured JSON:** [`02656f3b399251801d52.json`](../../sessions/02/02656f3b399251801d52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**训练正在健康运行！**

- 进程存活：2:48 elapsed
- GPU 0: 44% 利用率, 191W, 48.2GB VRAM
- GPU 1: **100% 利用率**, 103W, 48.2GB VRAM
- 仍在 `actor_rollout_generate_sequences`（vLLM 推理生成 rollout）
- 显存从 10.9GB→48.2GB，vLLM KV-cache 已分配

日志文件 tail 仍显示同样内容（1599 行），说明 stdout 输出被 Ray 缓冲。这正常——generation 阶段通常是安静的。

---

## exp013f 早期健康报告

| 项目 | 状态 |
|------|------|
| **进程** | ALIVE, PID 313810, 运行 ~3 分钟 |
| **环境变量** | ✅ `RAY_memory_monitor_refresh_ms=0`, `RAY_SYSTEM_MEMORY=210GB`, `HYDRA_FULL_ERROR=1` 均已在脚本中设置 |
| **GPU 利用率** | ✅ GPU0 44%/191W, GPU1 100%/103W |
| **GPU 显存** | 48.2GB/97.9GB per card（vLLM KV-cache 已激活） |
| **训练进度** | Step 5/30 → rollout generation 进行中 |
| **val→train 过渡** | ✅ **已成功通过**（此前 5 次崩溃点） |
| **错误** | 无错误，仅有 FutureWarning（不影响运行） |
| **val env_groups** | 4（已从 16 降低） |

**结论：exp013f 已成功通过历史崩溃点，正在执行第 6 步（从 step 5 恢复）的 rollout generation。MemoryMonitor 修复有效。建议 5-10 分钟后再次检查，确认 generation→gradient update 循环正常完成。**

---
