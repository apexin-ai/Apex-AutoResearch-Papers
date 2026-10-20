# monitor pass k results check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_pass_k_results_check_20260516T173614_result.json`
- **Structured JSON:** [`f1684881e4ed052b88a1.json`](../../sessions/f1/f1684881e4ed052b88a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个实验均在运行中，尚无结果文件。当前进度：

| 实验 | GPU | PID | 进度 | 中间 pass@8 | 预估剩余 | 备注 |
|------|-----|-----|------|------------|---------|------|
| unpruned (grpo_unpruned_v2) | cuda:1 | 25341 | **137/200** (68%) | 0.9500 @100 | ~20 min | 运行顺畅 |
| RASP-20 SFT (sft_qwen_math_rasp_20) | cuda:2 | 25442 | **90/200** (45%) | 0.9000 @50 | ~40-60 min | 有 max_length 4096 溢出，多次严重减速 |
| RASP-20 GRPO (grpo_rasp_qwen_math) | cuda:3 | 25538 | **130/200** (65%) | 0.8900 @100 | ~25 min | 同样有 max_length 溢出减速 |

**关键观察**：
- SFT 和 GRPO 模型都触发了 `max_length (4096)` 警告，导致个别 sample 生成时间从 ~15s 暴涨到 100-200s+，严重拖慢进度（sample 28、64、89 附近）
- 中间指标趋势：unpruned (0.95) > SFT (0.90) > GRPO (0.89)，但中间值会波动，需等最终结果
- GPU 0 上另有一个 `sft_rasp_rlvr_qwen_math` 训练在跑（PID 28243，占用 50.9GB 显存）

unpruned 和 GRPO 预计 ~20-25 分钟内完成，SFT 因减速最慢，预计 ~40-60 分钟。需要稍后再查最终结果。

---
