# director / loop_8.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_8.md`
- **Structured JSON:** [`597c008a7cc2e1d66e4e.json`](../../sessions/59/597c008a7cc2e1d66e4e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: max_messages
updated: '2026-05-15T13:29:04+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单: cuda:0 ~ cuda:5（6 张），不得使用其他卡
- 服务器: `westd-8x6000`，不要连其他服务器
- D045 约束: 0.5B 模型必须排除出 MMLU IRT 拟合（contamination 已确认）
- D047 约束: base_pretrained 模型不参与 IRT 拟合（无 SFT 不可比）
- IRT Stan 模型必须用 `contam_irt_2pl_gamma.stan`（D041 修复后版本），不要用旧版
- CSV 真源在远程，sync 到本地路径是 `artifacts/exp001/data/eval_summary_matrix.csv`（不是 `artifacts/eval_summary_matrix.csv`，刚修过这个 bug）

### 2. 🖥️ 基础设施快照
- 服务器: `westd-8x6000`，工作目录 `/root/contamcal-irt-calibration`
- Python: conda base 环境（`/root/miniconda3/bin/python`）
- 本地 workspace: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/`
- 产出目录: `artifacts/exp001/` 下各子目录
- Pooled IRT 输出目录: `results_pooled_4bench_aligned_2pl/`（MCMC 运行中，完成后结果在这里）
- CPU 长任务: exp_004 extreme gamma sweep (PID 528993)

### 3. 📊 当前状态
6 张 GPU 全满运行:
- cuda:0: 1.5B d025 s123 SFT
- cuda:1: 1.5B d005 s123 SFT
- cuda:2: 3B d005 s123 SFT + 0.5B base eval v2（共存）
- cuda:3: 3B d000 s123 eval（GSM8K ~51%）
- cuda:4: 3B d025 s123 SFT（~26%, ETA ~2h from 12:30 UTC）
- cuda:5: 3B d005 s42 eval（GSM8K ~49%）

关键等待:
- **Pooled IRT 4-bench aligned MCMC**（CPU，4 chains × 4 benchmarks，预计 2-3h）— 这是判断 coverage collapse 能否修复的分水岭
- SFT/eval 完成后 cron 自动回调，需依次提交对应 aligned eval
- 3B d005/d025 s123 两个实验 registry 卡在 PREPARING 但有 PID，Agent 已派 Worker 修复状态

### 4. 📋 待办
- cuda:4 3B d025 SFT 完成 → 提交 3B d025 s123 aligned eval
- cuda:2 0.5B base eval 完成 → 提交 0.5B d000 s42 aligned eval
- cuda:3 或 cuda:5 eval 完成 → 提交 Instruct eval（0.5B-Instruct 无 adapter）
- 1.5B SFT 完成 → 提交 1.5B d005/d025 s123 aligned eval
- Pooled IRT MCMC 完成 → Reviewer 审查收敛诊断（R-hat, ESS）+ gamma 参数 → 判断 coverage collapse 是否可修
- Pooled IRT 结果如果 MMLU N=10 的 R-hat 差 → 需要等更多 3B 中间 dosage（d005/d025）SFT 完成后重跑

### 5. 🎯 战略上下文
- DDL: **May 25**（10 天）
- 核心假设: contamination 通过 IRT gamma 参数可检测，不同 dosage 产生可区分的校准偏移
- Pooled IRT 4-bench aligned 是当前最关键的分析——如果 gamma 在 contaminated benchmarks 上显著偏离 clean benchmarks，核心 claim 成立
- 覆盖度隐患: MMLU 当前只有 N=10 models，3B 缺 d005/d025 中间 dosage，IRT 参数估计可能不稳——关注 R-hat 和 ESS
- 项目已进入审稿阶段（Review Group C 在独立审论文），我们专注推实验
- exp_004 extreme gamma sweep 是 CPU 长任务，不要杀掉


---
