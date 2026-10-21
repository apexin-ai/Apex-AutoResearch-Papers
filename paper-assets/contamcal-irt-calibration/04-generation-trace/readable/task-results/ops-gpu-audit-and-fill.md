# ops gpu audit and fill

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_audit_and_fill_20260516T152622_result.json`
- **Structured JSON:** [`40c01572937fdb097040.json`](../../sessions/40/40c01572937fdb097040.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 6 卡已满载。最终汇报：

---

## 产出报告

### GPU 状态（全部占满）

| GPU | 显存 | 利用率 | 任务 | exp_id / tmux |
|-----|------|--------|------|---------------|
| cuda:0 | 16694 MiB | 68% | **1.5B-Instruct signals mmlu** | sig_15b_mmlu |
| cuda:1 | 6847 MiB | 80% | **Llama-3.2-3B d000 eval** (gsm8k→arc→humaneval) | eval_llama_d000_v3 |
| cuda:2 | 1511 MiB | 37% | 0.5B-Instruct eval (running) | — |
| cuda:3 | 17853 MiB | 56% | Llama-3.2-3B d025 SFT | exp_001_sft_llama32_3B_d025_s42 |
| cuda:4 | 3985 MiB | 57% | **1.5B-Instruct signals arc_challenge** | sig_15b_arc |
| cuda:5 | 21176 MiB | 70% | **1.5B-Instruct signals gsm8k** | sig_15b_gsm |

### 完成的操作

1. **cuda:4 孤儿清理**: PID 796493 已 kill，但副作用 kill 了 cuda:1 的 Llama d000 eval（exit 137）。已重启 eval（跳过已完成的 mmlu）。

2. **3B d000_s123 signals merge**: `signals_merged_mmlu.json` 创建完成（14042 items, s1+s2+s4, 0 missing）。

3. **0.5B-Instruct signals merge**: 3 个 merged 文件全部创建：
   - mmlu: 14042 items
   - arc_challenge: 1172 items
   - gsm8k: 1319 items

### 已完成实验结果摘要

| Model | MMLU | GSM8K | ARC | HumanEval |
|-------|------|-------|-----|-----------|
| Qwen2.5-1.5B-Instruct | 0.5775 | 0.5929 | 0.7654 | — |
| Qwen2.5-0.5B-Instruct | 0.2462 | 0.3882 | 0.2816 | — |
| Llama-3.2-3B d000_s42 | 0.4545 | (running) | (running) | (running) |

### 新派任务

| 任务 | GPU | 预计完成 |
|------|-----|----------|
| 1.5B-Instruct signals mmlu | cuda:0 | ~2-3h (s4 generation 14042 items) |
| 1.5B-Instruct signals arc | cuda:4 | ~30min |
| 1.5B-Instruct signals gsm | cuda:5 | ~30min |
| Llama d000 eval (gsm+arc+humaneval) | cuda:1 | ~3.5h |

### exposure_scores.json (`rrf_full_n_latest`)

| Benchmark | N (respondents) |
|-----------|-----------------|
| mmlu | 25 (含 0.5B-Instruct) |
| arc_challenge | 24 |
| gsm8k | 24 |

1.5B-Instruct signals 完成后可加入 RRF 重聚合，使 arc/gsm 达到 N=25，mmlu 达到 N=26。

---
