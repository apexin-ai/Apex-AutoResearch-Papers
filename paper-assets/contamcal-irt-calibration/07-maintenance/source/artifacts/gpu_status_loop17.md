GPU & Process Status Report — 2026-05-16 ~23:00 UTC
=====================================================

## GPU 占用状态

| GPU | Memory Used | Util% | Status | PID | Task |
|-----|-------------|-------|--------|-----|------|
| 0 | 6577/24564 MiB | 62% | OCCUPIED | 780943 | compute_signals 3B_d000_s123_a32 (s4, mmlu) |
| 1 | 0/24564 MiB | 0% | **IDLE** | - | - |
| 2 | 1473/24564 MiB | 40% | OCCUPIED | 797754 | eval Qwen2.5-0.5B-Instruct (mmlu gsm8k humaneval) |
| 3 | 0/24564 MiB | 0% | **IDLE** | - | - |
| 4 | 8313/24564 MiB | 84% | OCCUPIED | 796493 | eval Llama-3.2-3B_d000_s42 aligned (mmlu gsm8k arc humaneval) |
| 5 | 3463/24564 MiB | 63% | OCCUPIED | 799315 | eval Qwen2.5-1.5B-Instruct paraphrased aligned (mmlu gsm8k arc humaneval) |

## RUNNING 实验存活状态

### 1. exp_001_eval_15B_instruct (PID 782625, cuda:5)
- **STATUS: ALIVE**
- Wrapper PID 782625 (bash, elapsed 01:57:42) → child 782626 → grandchild 799315
- Current: evaluating mmlu paraphrased at 71% (4731/6596, ~16 it/s)
- ETA: ~2 min to finish mmlu paraphrased, then gsm8k/arc/humaneval paraphrased remaining

### 2. exp_006_mmlu_domain_gamma_n24_v4 (PID 789935, CPU)
- **STATUS: COMPLETED**
- PID 789935 NOT FOUND (process exited)
- Output: 7/7 domains have irt_results.json (STEM_Math, STEM_Science, STEM_CS_Eng, Medical, Humanities, Social_Sciences, Business_Law)
- All results present → task completed successfully

### 3. exp_001_eval_05B_instruct (cuda:2, no PID recorded)
- **STATUS: ALIVE**
- PID 797754 on GPU 2, elapsed 13:12
- Command: evaluate.py --model-path Qwen2.5-0.5B-Instruct --mc-format aligned --instruct --benchmarks mmlu gsm8k humaneval

### 4. exp_006_pooled_irt_rrf_n25_v2 (CPU)
- **STATUS: COMPLETED**
- No matching process found
- Output: pooled_rrf_irt_results.json (13538 bytes, May 16 22:47) + subdirs for mmlu, gsm8k, arc_challenge
- Model type: 4pl_gamma, all benchmarks present → task completed successfully

## 历史 PID 状态（均已完成）

| PID | 原任务 | 状态 |
|-----|--------|------|
| 691872 | cuda:0 1.5B s123 signals | DONE |
| 760236 | cuda:1 0.5B d100_s123 | DONE |
| 764449 | cuda:3 3B-Instruct eval v2 | DONE |
| 752961 | cuda:4 Llama d000 SFT | DONE |
| 746777 | (unknown) | DONE |

## 未注册进程

| GPU | PID | Task | Elapsed | Notes |
|-----|-----|------|---------|-------|
| 0 | 780943 | compute_signals 3B_d000_s123_a32 (s4 mmlu) | 02:09:26 | 12/~15 chunks done (~80%), not in RUNNING registry |
| 4 | 796493 | eval Llama-3.2-3B_d000_s42_aligned | 17:07 | Not in RUNNING registry |

## 需要 Registry 更新的实验

1. **exp_006_mmlu_domain_gamma_n24_v4** → mark COMPLETED (7/7 domains done)
2. **exp_006_pooled_irt_rrf_n25_v2** → mark COMPLETED (results written)
3. GPU 0 signals task (PID 780943) → should be registered if not already
4. GPU 4 Llama eval (PID 796493) → should be registered if not already

## 空闲 GPU 可用于新任务

- **cuda:1** — fully idle
- **cuda:3** — fully idle
