# ops full status westb v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_full_status_westb_v2_20260518T174958_result.json`
- **Structured JSON:** [`6dc3a772d03115ecf9cf.json`](../../sessions/6d/6dc3a772d03115ecf9cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westb-23072 状态汇报

### GPU 状态

| GPU | PID | 任务 | 进度 | Interim Acc | Avg Len | ETA (服务器时间) |
|-----|-----|------|------|-------------|---------|-----------------|
| cuda:0 | 823050 | `eval_gsm8k_grpo_cka_only_20_1p5b` | **695/1319 (52.7%)** | **36.77%** | 315 | ~02:55 (约65min) |
| cuda:1 | 822503 | `eval_gsm8k_grpo_standard_20_1p5b` | **413/1319 (31.3%)** | **23.25%** | 434 | ~04:25 (约155min) |

### tmux sessions
- `eval_gsm8k_cka_only` — 承载 GPU 0 任务
- `scoring_ablation_v2` — 旧 session（May 17）

### 已完成的 quick eval（pruned-only baselines, pre-GRPO）
| Model | GSM8K Quick Acc |
|-------|----------------|
| standard_20_1p5b | 6% |
| cka_only_20_1p5b | 2% |
| rasp_20_1p5b | 8% |

### 结果 JSON
三个 GRPO full eval 的 JSON 均**未生成**（仍在运行）。

### RASP eval 启动
`eval_gsm8k_grpo_rasp_20_1p5b` checkpoint 已就绪（`/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_20_1p5b/checkpoint-100`），但两张 GPU 都被占用。**预计 GPU 0 在 ~65 分钟后空闲**，届时可启动 RASP eval。

### 初步观察
GRPO 后提升显著：CKA-only 从 2% → 36.77%（interim），Standard 从 6% → 23.25%（interim）。CKA-only 在 1.5B 上也大幅领先 Standard，与 7B 趋势一致。

---
