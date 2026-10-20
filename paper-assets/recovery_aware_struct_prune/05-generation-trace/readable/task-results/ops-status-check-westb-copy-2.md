# ops status check westb

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_status_check_westb_20260518T170900_result.json`
- **Structured JSON:** [`9591da2c0e93b86104cf.json`](../../sessions/95/9591da2c0e93b86104cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westb-23072 状态汇报

### GPU 状态

| GPU | 进程 | 显存 | 利用率 | 功耗 |
|-----|------|------|--------|------|
| cuda:0 | eval_gsm8k_grpo_**standard**_20_1p5b | 6537/97887 MiB | 97% | 479W/600W |
| cuda:1 | eval_gsm8k_grpo_**cka_only**_20_1p5b | 6555/97887 MiB | 44% | 208W/600W |

### 评测进度

| 任务 | 进度 | 当前 acc | eos_rate | avg_len | 已用时间 | 预估剩余 |
|------|------|----------|----------|---------|----------|----------|
| grpo_cka_only_20_1p5b (cuda:1) | **313/1319 (24%)** | 0.4167 | 96.0% | 296 | ~32min | **~1h43m → ETA ~02:52** |
| grpo_standard_20_1p5b (cuda:0) | **201/1319 (15%)** | 0.2550 | 93.5% | 397 | ~29min | **~2h47m → ETA ~03:56** |

### 关键观察

- cka_only 模型速度更快（avg_len 更短 296 vs 397），且准确率大幅领先（41.7% vs 25.5%）
- 两个评测均未完成，结果 JSON 尚未生成
- tmux 命令被 read-only 模式拦截，但从进程列表看还有一个已结束的 `eval_unstructured_20` session（PID 680597，5月17日启动，对应结果文件 `eval_unstructured_20_n1319.json` 已存在）

---
