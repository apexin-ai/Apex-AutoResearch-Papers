# ops d102 eval monitor

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d102_eval_monitor_20260518T085458_result.json`
- **Structured JSON:** [`fdcfa860dc069489131d.json`](../../sessions/fd/fdcfa860dc069489131d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## D102 Eval 进程状态

### GPU 使用率

| GPU | 利用率 | 显存占用 | 总显存 |
|-----|--------|----------|--------|
| cuda:0 | 58% | 18,887 MiB | 32,607 MiB |
| cuda:1 | 52% | 18,733 MiB | 32,607 MiB |
| cuda:2 | 34% | 5,473 MiB | 32,607 MiB |
| cuda:3 | 70% | 18,421 MiB | 32,607 MiB |

### 进程状态

全部 4 个进程存活，无 error，正常推理中。结果在推理完成后一次性写入 output_dir。

| GPU | PID | 模型 | 进度 | 速度 | 预计剩余 |
|-----|-----|------|------|------|----------|
| cuda:2 | 519811 | 1.7B k=1 s42 | 117/247 (47%) | ~38s/it | ~82 min |
| cuda:3 | 523336 | LLaMA k=1 s42 | 46/247 (19%) | ~35s/it | ~117 min |
| cuda:0 | 523743 | 8B k=1 s42 | 35/247 (14%) | ~49s/it | ~173 min |
| cuda:1 | 524152 | 8B k=1 s43 | 33/247 (13%) | ~50s/it | ~178 min |

### 预计完成时间 (UTC)

| 模型 | 预计完成 |
|------|----------|
| 1.7B k=1 s42 | ~18:20 |
| LLaMA k=1 s42 | ~18:55 |
| 8B k=1 s42 | ~19:50 |
| 8B k=1 s43 | ~19:55 |

### 备注
- 1.7B 进程命令是 `eval.inference`（非 `freige.eval.inference`），但功能相同，正常运行
- 所有 output_dir 目前为空，结果在全部 batch 完成后写入
- 无 error/warning（除 torch_dtype deprecated 的无害警告）

---
