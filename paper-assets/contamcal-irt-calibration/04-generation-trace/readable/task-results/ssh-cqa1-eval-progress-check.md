# ssh cqa1 eval progress check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cqa1-eval-progress-check_20260519T074033_result.json`
- **Structured JSON:** [`cd6a13eac083b66d812f.json`](../../sessions/cd/cd6a13eac083b66d812f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

**GPU 状态**: RTX 4090D — 91% 利用率, 17.8/24.6 GB VRAM, PID 211085

**当前在跑**: `OLMo-2-7B_d000_s42` 跨家族 eval（MMLU + ARC Challenge），已运行 ~8 分钟，输出目录暂为空（尚未写出结果）。adapter lora_alpha=32 ✓

**已完成 eval**: 无（只有 `OLMo-2-7B_d000_s42` 一个目录，状态 not done）

**待跑 eval**（checkpoints 已就绪但未创建 eval 目录）:
- `OLMo-2-7B_d005_s42`
- `OLMo-2-7B_d025_s42`

**OLMo-2-7B 模型**: 已完成 SCP（15 文件, 28GB）✓

总结：3 个跨家族 eval 中，第 1 个正在跑，还有 2 个待跑。

---
