# ops gpu status fill 0516c

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-status-fill-0516c_20260516T191647_result.json`
- **Structured JSON:** [`be4354eee0dc3e5bb5cc.json`](../../sessions/be/be4354eee0dc3e5bb5cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态截面 (2026-05-17)

| GPU | 状态 | 进程 | 已运行 | ETA |
|-----|------|------|--------|-----|
| cuda:0 | **忙** | eval d005 (PID 825638) | 1h22m | ~40-90min |
| cuda:1 | **忙** | signals mmlu d000 s4_selfcritique (PID 830115) | 55m | ~90min |
| cuda:2 | **空闲** | — | — | — |
| cuda:3 | **忙** | eval d025 (PID 822385/822390) | 1h43m | ~20-70min |
| cuda:4 | **空闲** | — | — | — |
| cuda:5 | **忙** | eval d100 (PID 831033) | 54m | ~60-120min |

### Cron 注册的 4 个实验状态

- exp_001_eval_llama32_3B_d025_s42 (PID 822385) ✓ 存活 (GPU 3)
- exp_001_eval_llama32_3B_d005_s42 (PID 825638) ✓ 存活 (GPU 0)
- exp_002_signals_llama32_3B_d000_mmlu (PID 830115) ✓ 存活 (GPU 1)
- exp_001_eval_llama32_3B_d100_s42 (PID 831033) ✓ 存活 (GPU 5)

### cuda:2/cuda:4 上次进程已完成

PID 835983 (gsm8k selfcritique) 和 PID 831936 (gsm8k signals) 均已结束。

### Llama d000 signals 完整性

| Benchmark | s1_embedding | s2_minkpp | s4_selfcritique | merged |
|-----------|:---:|:---:|:---:|:---:|
| arc_challenge | ✓ | ✓ | ✓ | ✓ |
| gsm8k | ✓ | ✓ | ✓ | ✓ |
| mmlu | ✓ | ✓ | **进行中** (4/~14 chunks, ~28%) | 待生成 |

mmlu s4_selfcritique 进度: chunk rate ~9.4min/1000 items, 剩余 ~10k items → **ETA ~90min**

### 填补决策

按 P1→P2→P3 优先级评估：

- **P1** (mmlu s4_selfcritique): 已在 GPU 1 运行，无需重复提交
- **P2** (RRF 聚合): CPU 任务，阻塞于 mmlu signals 完成
- **P3** (d005 signals): 阻塞于 d005 eval 完成 (GPU 0)

**结论: cuda:2 和 cuda:4 当前无可调度的 GPU 任务。** 最早可调度时间点：
- d005 eval 完成后 (~40-90min) → 提交 d005 signals 到空闲卡
- d025/d100 eval 完成后 → 各自 signals 可提交

无操作执行，两卡暂时空置等待上游任务完成。

---
