# code d134 analysis recreate

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d134-analysis-recreate_20260518T134334_result.json`
- **Structured JSON:** [`1c1277cb995378727d54.json`](../../sessions/1c/1c1277cb995378727d54.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇报：

**1. classify.json 实际字段名**

嵌套在 `eval_results` 键下，主要字段：
- `n_total`, `n_proved`, `h7a_count`, `h7b_count`, `h7_total_count`, `h7_total_rate`
- `h1_strict_count`, `h8_conjunction_collapse_count`
- `genuine_count`, `genuine_rate`, `content_independent_count`
- `conclusion_in_premise_count`, `single_premise_count`, `isr_1_count`

**2. 脚本创建确认**
- 远程: `/root/solver-trace-ablation/scripts/d134_analysis.py` (shebang 已改为 `/root/miniconda3/bin/python`, chmod +x)
- 本地: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/scripts/d134_analysis.py`

**3. Dry run 输出**

```
Found 2 runs: 2 ISR, 0 RANDOM

  PER-SEED RESULTS
condition  seed  PR  H7_count  H7_rate  H1  H8  genuine  genuine_rate  CI  SNH  SNH_rate
      ISR    47  97       83   85.6%     1  10        3       3.1%       8    0     0.0%
      ISR    48  66       66  100.0%     0   0        0       0.0%       2    0     0.0%

  ISR (n=2 seeds):
    PR:           81.5 +/- 21.9
    H7 rate:      92.8 +/- 10.2%
    Genuine rate: 1.5 +/- 2.2%
    S-NH rate:    0.0 +/- 0.0%
```

s49 目录存在但尚无 classify.json（符合预期，还在训练中）。统计检验因只有 ISR 无 RANDOM 而跳过。运行命令需用 `/root/miniconda3/bin/python`（系统 python3 缺 numpy/pandas/scipy）。

**4. 依赖状态**
- `/root/miniconda3/bin/python`: numpy, pandas, scipy 均已安装，无缺依赖
- 系统 `/usr/bin/python3`: 缺 numpy/pandas/scipy（不可用）

---
