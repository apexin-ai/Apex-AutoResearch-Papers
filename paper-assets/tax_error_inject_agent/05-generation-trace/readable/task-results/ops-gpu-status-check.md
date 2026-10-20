# ops gpu status check

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-status-check_20260515T224259_result.json`
- **Structured JSON:** [`1d62ac58392bc3f18ead.json`](../../sessions/1d/1d62ac58392bc3f18ead.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 4 个实验都还在运行中。

## GPU 状态

| GPU | 显存占用 | GPU利用率 | PID | 进程 |
|-----|---------|----------|-----|------|
| cuda:0 | 17082/32607 MiB | 78% | 205279 | v4-taxei-fixed-inject25-s1-eval |
| cuda:1 | 17082/32607 MiB | 72% | 205415 | v4-random-fixed-inject25-s1-eval |
| cuda:2 | 17082/32607 MiB | 0% | 205863 | v4-taxei-fixed-inject25-s1-eval-r2 |
| cuda:3 | 18587/32607 MiB | 77% | 203885 | v4-random-fixed-inject25-s7 (训练) |

## 实验状态

| 实验 | 状态 | 进度 |
|------|------|------|
| **v4-taxei-fixed-inject25-s1-eval** (cuda:0) | 运行中 | 14/47 tasks (OK: 8, FAIL: 6) |
| **v4-random-fixed-inject25-s1-eval** (cuda:1) | 运行中 | 20/47 tasks (OK: 13, FAIL: 7) |
| **v4-taxei-fixed-inject25-s1-eval-r2** (cuda:2) | 运行中 | 14/47 tasks (OK: 8, FAIL: 6) — 与 cuda:0 结果完全一致 |
| **v4-random-fixed-inject25-s7** (cuda:3) | 训练中 | step 741/1635 (45%), ~31min 剩余, loss=0.40, token_acc=0.86 |

eval_results/ 目录中尚无 `v4_taxei_fixed_inject25_s1_eval.json` 或 `v4_random_fixed_inject25_s1_eval.json`，这些文件会在 eval 完成后生成。

**注意**: cuda:0 和 cuda:2 跑的是同一个 checkpoint 的 eval（r2 是重跑），当前 14/47 的结果完全一致。cuda:2 GPU利用率为 0% 可能是任务间的间歇。

---
