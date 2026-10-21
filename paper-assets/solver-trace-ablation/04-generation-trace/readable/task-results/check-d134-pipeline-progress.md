# check d134 pipeline progress

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_d134-pipeline-progress_20260518T114744_result.json`
- **Structured JSON:** [`e7f85c2d71c5d5f48e4f.json`](../../sessions/e7/e7f85c2d71c5d5f48e4f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**D134 Pipeline 状态：1/10，第一个 run 接近完成**

- **当前 run**: `d134_4b_isr_b01_s47` (ISR β=0.1, seed=47) — step **479/500** (96%)
- **已完成 run**: 0/10（无 COMPLETE 标记，无 classify.log）
- **GPU**: 83% 利用率，84809 MiB 显存占用
- **Pipeline 启动时间**: Mon May 18 10:52:28 UTC（约 45 分钟前）
- **预计当前 run 训练剩余**: ~21 步 × ~3s/step ≈ 1 分钟，之后还有 eval + classify

Pipeline 刚启动不久，第一个 run 的训练马上完成，后面还有 eval/classify 阶段，然后才进入第 2 个 run。按每个 run ~1h 估算，全部 10 个 run 预计还需 ~9-10 小时。

---
