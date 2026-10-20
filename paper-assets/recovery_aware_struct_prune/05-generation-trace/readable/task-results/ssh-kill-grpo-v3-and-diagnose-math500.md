# ssh kill grpo v3 and diagnose math500

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill_grpo_v3_and_diagnose_math500_20260523T141226_result.json`
- **Structured JSON:** [`2d0336a1036f87030282.json`](../../sessions/2d/2d0336a1036f87030282.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both servers have identical scripts now — the OLD version is lost. Here's the complete report:

---

## 产出

### 1. GRPO v3 Kill: **OK**
- PID 136598 force-killed, child PID 136607 also killed
- tmux session `eval_math500_grpo_standard_20_fair_2048_v3` killed
- GPU 2: **0% util, 0 MiB** (已释放)
- GPU 0 仍有进程 (PID 134268, 29650 MiB)；GPU 1/3 空闲

### 2. 脚本差异

**OLD 脚本已丢失**（westb-23072 和 westd-32935 上的 eval_math500.py 完全相同，都是 NEW 版本；git 只有一个 commit，无历史）。

但通过结果文件可以确认：**v2 和 v3 是同一模型的相同输出**（500 个样本 response_length 完全一致，eos_stats 一致：267 natural_eos, 233 truncated, avg_len=1145.74）。差异全部来自脚本。

**NEW (v3) 的 answer extraction/matching 有两类 bug：**

**Bug A — `extract_model_answer` 退化到 last-number fallback（11 个样本）：**
模型输出相同，但 NEW 版提取到了错误的单个数字，而 OLD 版能提取完整表达式。例如：
- gold=`6+9i`, OLD提取`6 + 9i`, NEW提取`9`
- gold=`(a+5)(b+2)`, OLD提取`(a + 5)(b + 2)`, NEW提取`2`
- gold=`15x - 80`, OLD提取`15x - 80`, NEW提取`80`

**Bug B — `answers_match` 归一化不够宽容（5 个样本）：**
提取结果相同但 NEW 版判错：
- `(15, -29)` vs `(15,-29)` — 逗号后空格差异未消除
- `C` vs `\text{(C)}` → normalize 后 `c` vs `(c)` — `\text{}` 剥离后保留了括号
- `(1, -16, -4, 43)` vs `(1,-16,-4,43)` — 同上空格问题
- `(2, 12) \cup (12, 102)` vs `(2,12) \cup (12,102)` — 同上

**净影响：** v2(OLD)=129/500=25.8%, v3(NEW)=117/500=23.4%。差 12 个正确（16 个 v2→v3 变错，4 个 v2→v3 变对）。

### 3. 全部 MATH-500 eval 脚本版本清单

| 文件 | 格式 | Accuracy | Correct/Total |
|------|------|----------|---------------|
| **autodl-tmp 目录** | | | |
| eval_math500_unpruned.json | OLD | 73.6% | 368/500 |
| math500_dense_unpruned.json | OLD | 73.6% | 368/500 |
| math500_dense_2048.json | OLD | 53.0% | 265/500 |
| math500_grpo_unpruned.json | OLD | 69.0% | 345/500 |
| math500_grpo_cka_only_20_2048.json | OLD | 29.2% | 146/500 |
| math500_sft_cka_only_20_v4.json | OLD | 29.0% | 145/500 |
| eval_math500_sft_cka_only_20.json | NEW | 26.8% | 134/500 |
| eval_math500_grpo_cka_only_20_2048_v2.json | NEW | 27.4% | 137/500 |
| eval_math500_grpo_rasp_alpha2p0_20.json | NEW | 26.2% | 131/500 |
| eval_math500_grpo_rasp_alpha4p0_20.json | NEW | 26.2% | 131/500 |
| math500_grpo_standard_20_fair_v2.json | OLD | 26.4% | 132/500 |
| eval_math500_sft_rasp_alpha4p0_20.json | NEW | 26.6% | 133/500 |
| eval_math500_sft_standard_20.json | OLD | 26.0% | 130/500 |
| math500_sft_standard_20_2048_v2.json | OLD | 25.8% | 129/500 |
| eval_math500_sft_rasp_alpha0p5_20.json | NEW | 25.4% | 127/500 |
| eval_math500_sft_rasp_20.json | OLD | 24.2% | 121/500 |
| math500_grpo_rasp_20_fair.json | OLD | 24.0% | 120/500 |
| eval_math500_sft_rasp_alpha2p0_20.json | NEW | 24.0% | 120/500 |
| eval_math500_sft_standard_20_2048_v3.json | **NEW** | 23.4% | 117/500 |
| eval_math500_sft_rasp_alpha3p0_20.json | NEW | 23.2% | 116/500 |
| eval_math500_grpo_rasp_alpha3p0_20.json | NEW | 22.8% | 114/500 |
| math500_sft_rasp_20_2048.json | OLD | 22.6% | 113/500 |
| eval_math500_grpo_rasp_alpha1p0_20.json | NEW | 22.6% | 113/500 |
| eval_math500_sft_rasp_alpha1p0_20_v2.json | NEW | 21.2% | 106/500 |
| eval_math500_sft_random_20_v3.json | NEW | 14.4% | 72/500 |
| eval_math500_grpo_random_20_v2.json | NEW | 13.4% | 67/500 |
| **recovery_aware 目录** | | | |
| eval_math500_grpo_standard_20_fair_2048_v2.json | OLD | 26.4% | 132/500 |
| eval_math500_sft_random_20_v3.json | NEW | 14.4% | 72/500 |
| eval_math500_sft_rasp_alpha2p0_20.json | NEW | 24.0% | 120/500 |

**结论：** NEW 脚本系统性低估 ~2-3%。所有 NEW 格式结果与 OLD 格式结果不可直接对比。需要修复 `normalize_answer`（消除空格差异）和 `extract_model_answer`（改善表达式提取）后重跑 NEW 格式的评估。

---
