# submit eval 05B d025 aligned

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_eval_05B_d025_aligned_20260514T131427_result.json`
- **Structured JSON:** [`e9ab00c3f13ec8c9952b.json`](../../sessions/e9/e9ab00c3f13ec8c9952b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### Part A: 0.5B d025 eval (GPU 5) — C001 阻止，已有同类进程

| 项目 | 值 |
|------|------|
| PID | 374947 |
| tmux session | `exp_001_sft_0pct_05B`（复用已有 session） |
| GPU 5 占用 | 1501 MiB（模型刚加载，占用还会上升） |
| 运行时间 | ~43 秒 |
| Registry | `exp_001_eval_05B_d025_aligned` — RUNNING（已由之前的流程创建） |

**注意**：当前进程只跑了 **original** eval（裸 `python evaluate.py` 启动，不含 `--paraphrase-dir`）。paraphrase eval 不会自动执行。original 完成后需要单独提交 paraphrase，或者用已有的 `run_aligned_eval_05B_d025.sh paraphrase` 启动。

### Part B: 3B d005 eval (GPU 4) — 正常运行中

| 项目 | 值 |
|------|------|
| PID | 373931 |
| GPU 4 占用 | 8985 MiB |
| 运行时间 | ~5 分 54 秒 |
| 命令 | `evaluate.py --model-path Qwen2.5-3B --adapter-path ...d005_s42/lora_adapter --mc-format aligned` |
| 启动脚本 | `run_aligned_eval_3B_d005.sh` |

3B eval 通常比 0.5B 慢（模型更大），预估 2-4 小时完成。

### 待处理

0.5B d025 的 **paraphrase eval** 缺失。original 完成后（预估 ~1-2h），需要在 GPU 5 上提交 paraphrase。是否需要我现在就准备好提交命令？

---
