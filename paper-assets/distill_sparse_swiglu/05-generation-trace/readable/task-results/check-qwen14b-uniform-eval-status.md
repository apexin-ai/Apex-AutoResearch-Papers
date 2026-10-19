# check qwen14b uniform eval status

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_qwen14b_uniform_eval_status_20260518T002644_result.json`
- **Structured JSON:** [`7c7043facca066fac52b.json`](../../sessions/7c/7c7043facca066fac52b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 14B Uniform Eval 状态报告

### 进程状态

| 实验 | PID | GPU | VRAM | GPU Util | 运行时长 |
|------|-----|-----|------|----------|----------|
| `qwen14b_kl30_uniform_eval` | **79839** | cuda:0 | 93,978 MiB / 97,887 MiB | 79% | 1h32m |
| `qwen14b_teal30_uniform_eval` | **80810** | cuda:1 | 61,656 MiB / 97,887 MiB | 73% | 1h22m |

### 任务进度

两个实验都评估 5 个 task: `wikitext2, arc_challenge, winogrande, mmlu, gsm8k`

前 4 个 task 均为 loglikelihood 类型，已全部完成。当前都在跑最后一个 task **gsm8k** (generate_until, 1319 items):

| 实验 | GSM8K 进度 | GSM8K 耗时 | 速度 | 预估剩余 |
|------|-----------|-----------|------|---------|
| KL30 uniform | 337/1319 (26%) | 1h04m | ~13.3s/item | **~3h38m** |
| TEAL30 uniform | 217/1319 (16%) | 55m | ~15.1s/item | **~4h37m** |

### 预估完成时间 (UTC)

- **KL30**: ~12:05 (约 3.5h 后)
- **TEAL30**: ~13:05 (约 4.5h 后)

### 中间结果

结果目录已创建但尚无输出文件（benchmark_eval.py 在所有 task 完成后才写结果）:
- `/root/distill_sparse_swiglu/results/benchmark/qwen14b_kl30_uniform/` — 空
- `/root/distill_sparse_swiglu/results/benchmark/qwen14b_teal30_uniform/` — 空

### 日志路径

- `/root/runs/distill_sparse_swiglu/qwen14b_kl30_uniform_eval.log`
- `/root/runs/distill_sparse_swiglu/qwen14b_teal30_uniform_eval.log`

注意: KL30 的日志包含一段初始启动失败的 traceback（模型路径大小写问题 `qwen2.5-14b` vs `Qwen2.5-14B`），后续被重启成功覆盖。

---
