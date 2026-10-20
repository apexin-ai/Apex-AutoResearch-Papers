# ops fill 3 idle gpus

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fill-3-idle-gpus_20260516T182115_result.json`
- **Structured JSON:** [`41daadc04d293218cd59.json`](../../sessions/41/41daadc04d293218cd59.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

## GPU 分配总览

| GPU | 任务 | PID | 状态 | 预计完成 |
|-----|------|-----|------|---------|
| cuda:0 | Llama d005 eval | 825638 | 运行中 | ~1-2h (4 benchmarks) |
| cuda:1 | **Llama d000 MMLU signals** | 830115 | 运行中 (embedding 15%) | ~30-40min |
| cuda:2 | 1.5B-Instruct ARC signals v1 | 823710 | 运行中 (37min elapsed) | ~20-30min |
| cuda:3 | Llama d025 eval | 822390 | 运行中 | ~1-2h |
| cuda:4 | **Llama d000 ARC signals** | 831353 | 运行中 (embedding starting) | ~15-20min (ARC 仅 1172 items) |
| cuda:5 | **Llama d100 eval** | 831033/831490 | 运行中 (evaluating MMLU 0/14042) | ~2-3h (4 benchmarks) |

## 已完成操作
- C001 违规修复：killed `exp_002_signals_15B_instruct_arc_v2` (PID 826497)
- d100 SFT registry 标记 DONE (train_loss=1.5435, accuracy=0.6505)
- 3 个新实验注册 RUNNING
- 清理 stale session `exp_001_eval_3B_d100_v2_para_aligned`
- cuda:4/5 首次启动因缺 `network_turbo` 超时，已重启修复

---
