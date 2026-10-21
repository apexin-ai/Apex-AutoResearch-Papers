# ops gpu eval status check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-eval-status-check_20260514T114145_result.json`
- **Structured JSON:** [`b6f571a4e52e3fa34b99.json`](../../sessions/b6/b6f571a4e52e3fa34b99.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have the full picture. Here's the summary:

---

## GPU 状态总览 (2026-05-14 19:42 UTC)

| GPU | 实验 | PID | VRAM | 进度 | ETA |
|-----|------|-----|------|------|-----|
| 0 | exp-002 signals 0.5B | 353390 | 2.1/24.6 GB | Task 4/9 (d005/mmlu)，task 1-3 标记 FAIL | ~未知 |
| 1 | 1.5B d000 aligned eval | 336765 | 5.9/24.6 GB | GSM8K 1308/1319 (99%) | GSM8K ~1min，之后 ARC+HumanEval ~30-45min |
| 2 | **0.5B d005 aligned eval (NEW)** | **356787** | 3.7/24.6 GB | 刚启动 26min | ~1h |
| 3 | 3B d100 SFT | 319555 | 13.3/24.6 GB | **3846/4159 (92%)** | **~22min** |
| 4 | 3B d005 SFT | 335351 | 21.8/24.6 GB | 2170/3177 (68%) | ~65min |
| 5 | 3B d000 aligned eval | 342940 | 9.0/24.6 GB | GSM8K 289/1319 (22%) | GSM8K ~86min，之后 ARC+HumanEval |

---

## 已完成：0.5B d000 aligned eval (PID 354435)

| Benchmark | Score |
|-----------|-------|
| MMLU | **39.79%** (5587/14042) |
| GSM8K | **36.92%** |
| ARC Challenge | **46.93%** |
| HumanEval | **pass@1 = 10.98%** |

GPU 2 已自动接续启动 **0.5B d005 aligned eval** (PID 356787)。

---

## exp-002 signals (GPU 0) — 有问题

Batch runner 日志显示 task 1-3 (d000 的 mmlu/gsm8k/arc_challenge) 全部标记 **FAIL**，stderr 中出现模型类型列表输出（可能是 `selfcritique` signal 的兼容性问题）。但部分 signal 文件已成功写入：

**d000 已有文件:**
- `signal_embedding_mmlu.json` (6.1MB)
- `signal_embedding_gsm8k.json` (568KB)
- `signal_embedding_arc_challenge.json` (515KB)
- `signal_minkpp_mmlu.json` (2.1MB)
- 缺失: minkpp_{gsm8k,arc_challenge}, selfcritique_{mmlu,gsm8k,arc_challenge}

**d005 已有文件:**
- `signal_embedding_mmlu.json` (6.1MB)
- 其余待计算

当前 PID 353390 仍在运行 d000/mmlu 的 compute_signals.py，说明可能有子任务仍在计算或重试。

---

## 训练进度

- **3B d100 SFT** (GPU 3): epoch 0.83, loss ~1.13, 92% 完成，**~22 min 完成**
- **3B d005 SFT** (GPU 4): epoch 0.60, loss ~1.12, 68% 完成，~65 min
- 3B d100 的 checkpoint 目录还是空的（未保存 lora_adapter），3B d005 的 lora_adapter 目录已创建但为空

---

## 关键关注点

1. **3B d100 SFT 即将完成** (~22min)，完成后 GPU 3 空闲，可安排 3B d100 eval
2. **exp-002 signals selfcritique 可能有 bug**，embedding 和 minkpp 能产出但 selfcritique 导致 task 标记 FAIL，需要排查
3. **1.5B aligned eval 接近完成** GSM8K (99%)，但还有 ARC+HumanEval 要跑

---
