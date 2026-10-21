# ops gsm8k both westd fix

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gsm8k-both-westd-fix_20260520T053102_result.json`
- **Structured JSON:** [`2d17d9e2d58fbd73cac5.json`](../../sessions/2d/2d17d9e2d58fbd73cac5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部确认正确。汇总：

### 结果

| GPU | 进程 | PID | 显存 | 状态 |
|-----|------|-----|------|------|
| 0 | Phi-4 SFT (d005_s0) | 286341 | 57,646 MiB | 未受影响 ✓ |
| 1 | **Qwen-14B GSM8K eval** | 289218 | 33,322 MiB | 新启动 ✓ |
| 2 | OLMo-2 SFT (d025_s0) | 280811 | 66,742 MiB | 未受影响 ✓ |
| 3 | **Gemma-2 GSM8K eval** | 289137 | 24,856 MiB | 新启动 ✓ |

1. **cuda:0 错误进程已清理** — PID 287548 已 kill，tmux session 已删除
2. **脚本 CUDA_VISIBLE_DEVICES** — Gemma-2→3, Qwen-14B→1
3. **Checkpoint 验证** — 4 个 adapter 均 >100MB，lora_alpha=32
4. **新 PID** — Gemma-2: 289137 (cuda:3), Qwen-14B: 289218 (cuda:1)
5. **四卡状态正确** — 两个 SFT 训练不受影响，两个 GSM8K eval 在正确 GPU 上运行

---
