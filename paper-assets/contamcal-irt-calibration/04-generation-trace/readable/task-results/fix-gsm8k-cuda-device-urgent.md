# fix gsm8k cuda device urgent

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_gsm8k-cuda-device-urgent_20260520T052753_result.json`
- **Structured JSON:** [`2b0986dddaaa1734743a.json`](../../sessions/2b/2b0986dddaaa1734743a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**任务假设与实际情况严重不符，暂停执行。** 报告如下：

### 实际状态

| 项目 | 任务假设 | 实际 |
|------|---------|------|
| GPU 数量 | 多卡（有 cuda:0/1/3） | **单卡** RTX 4090 D (24GB) |
| GPU 0 进程 | Phi-4 s0 sweep | **Qwen2.5-7B d000 s0 SFT** (PID 313418, 21318 MiB) |
| PID 287533 | 活跃，需 kill | **已死** |
| 脚本路径 | `scripts/gsm8k_s42/` | `exp001/` |
| 目标 GPU | Gemma→3, Qwen14B→1 | **GPU 3 和 GPU 1 不存在** |

### 结论

1. **PID 287533** 已不存在，无需 kill
2. 两个 eval 脚本确实写死 `CUDA_VISIBLE_DEVICES=0`，但**本服务器只有 1 块 GPU**，改成 3 或 1 会导致 `CUDA error: no device`
3. GPU 0 被 Qwen2.5-7B d000 s0 SFT 占满（21318/24564 MiB），**无法同时跑 eval**
4. 脚本实际路径：
   - `/root/contamcal-irt-calibration/exp001/eval_gsm8k_gemma2_s42.sh`
   - `/root/contamcal-irt-calibration/exp001/eval_gsm8k_qwen14b_s42.sh`

### 需要你确认

- GSM8K eval 是否应等 Qwen2.5-7B SFT 完成后再跑？
- 还是要在**另一台多卡服务器**上执行？
- 是否仍需要验证 Gemma-2 checkpoint 完整性（可以先做，不需要 GPU）？

---
