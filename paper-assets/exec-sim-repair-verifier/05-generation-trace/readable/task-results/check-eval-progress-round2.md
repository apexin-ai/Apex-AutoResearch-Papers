# check eval progress round2

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_eval-progress-round2_20260522T075425_result.json`
- **Structured JSON:** [`1889e7becd89db197213.json`](../../sessions/18/1889e7becd89db197213.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

| exp_id | GPU | PID | alive? | 进度 | running_acc | jsonl行数 | 速率 | ETA (CST) |
|--------|-----|-----|--------|------|-------------|-----------|------|-----------|
| qwen3-8b-cwm-repo-s123-eval | 0 | 94100 | Rl ✅ | 7376/9784 (75.4%) | 67.3% | 7380 | ~12 样本/min | ~19:15 |
| deepseek-cwm-repo-s123-e3-eval | 2 | 100824 | Rl ✅ | 6728/9784 (68.8%) | 57.1% | 6732 | ~13 样本/min | ~19:50 |
| qwen3-8b-cwm-repo-s456-eval | 3 | 96722 | S ✅ | 6676/9784 (68.2%) | 66.6% | 6680 | ~11 样本/min | ~20:30 |
| deepseek-cwm-repo-s123-1epoch-eval | 1 | 111113 | S ✅ | 4304/9784 (44.0%) | 75.6% | 4316 | ~13 样本/min | ~23:05 |

## GPU 利用率

| GPU | Util | VRAM |
|-----|------|------|
| 0 | 100% | 22159/32607 MiB |
| 1 | 85% | 30427/32607 MiB |
| 2 | 84% | 30427/32607 MiB |
| 3 | 61% | 22159/32607 MiB |

## 备注

- 全部 4 个 eval 进程存活，无异常
- Qwen 两个（GPU 0/3）用 22GB VRAM，DeepSeek 两个（GPU 1/2）用 30GB
- DS 1epoch running_acc 75.6% 显著高于 DS e3 的 57.1%——1epoch 未过拟合，e3 可能过拟合导致泛化变差
- Qwen s123 (67.3%) 和 s456 (66.6%) 接近，seed 稳定性好
- 日志路径与预期不同：实际分别在 `/root/runs/`、`/root/autodl-tmp/eval_results/*/final_eval.log`、monitor log 中
- 无已完成实验，最早完成的是 Qwen s123 (~19:15 CST)

---
