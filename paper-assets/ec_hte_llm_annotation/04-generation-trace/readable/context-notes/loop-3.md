# reviewer / loop_3.md

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_3.md`
- **Structured JSON:** [`09de5e68d822ea034810.json`](../../sessions/09/09de5e68d822ea034810.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_wall_time
updated: '2026-05-23T20:23:07+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目无 GPU 训练，全部实验在 local-cpu 上跑 Python 模拟（N=5000, MC=100），无 GPU 设备号约束
- 论文主文 **8 页硬限制**（EMNLP 2026 ARR），Limitations/Ethics 不计入但 Limitations 用户规则要求"一小段，3 个点左右"
- Abstract ≤ 200 words
- `compute_fl_for_table1.py` 的 F-L Table 1 数字**无持久化 CSV**——如果有人重跑这个脚本，需要手动保存输出
- 论文中 "eight real LLMs" 是正确计数，appendix 两处写了 "seven" 是 bug

### 2. 🖥️ 基础设施快照
- 服务器：local-cpu（root），SSH 通过 localhost
- 工作目录（远程）：`/home/ubuntu/ec_hte_llm_annotation/`
- 工作目录（本地 workspace）：`/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/`
- Python：系统 python3（无 venv/conda）
- 论文 LaTeX：`docs/paper/` 下，`main.pdf` 已编译
- 实验结果 CSV：远程 `results/` 目录 + 本地 `artifacts/` 目录（部分重叠）
- 无 wandb / 无 HF cache / 无 GPU
- 无活跃进程 / 无 tmux / 无 cron

### 3. 📊 当前状态
**刚完成**：Data Integrity Audit V2 独立核实（59 项中 54 项通过，2 个 warning 已报 Director）。

**已提交给 Director 的 pending 修复**（均为简单文字改动）：
1. R²=0.974 (K=4 synthetic) 应为 0.966（experiments.tex:16, theory.tex:81）
2. appendix.tex:918 和 :981 "seven LLMs" 应为 "eight"，open/proprietary split 应为 3+5 非 4+3
3. Limitations 过长（~1.5 页，覆盖 10 个点），用户规则要求"一小段，3 个点"

**此前已确认修复的问题**：
- 页面溢出 → 已解决，Conclusion 在 page 8 内
- "≥90%" → "≈90%" ✓
- "8 LLMs exhibit reversal" → "amplify bias" ✓（intro/experiments/Fig caption 统一）
- "splitting variable" → "effect modifier" ✓

**Registry 状态**：无 RUNNING/PREPARING 实验。全部 worker 已完成。

### 4. 📋 待办（条件触发式）
- Director 确认修复 R²/seven→eight → 核实改后文本是否准确
- Director 提交 Limitations 精简版 → 检查是否符合"3 个点"规则 + 内容准确性
- Paper Agent 提交最终版审查 → 执行审查模式 B（章节写作对抗审查），含 paper-quality-lessons skill
- 如果 Director 问 CivilComments 是否该写进论文 → EC-HTE 在 CivilComments 上全部 worse than naive（1.32×–3.02× amplification），原因是 race_lgbtq 5.5% + religion 4.3% 子群过小；适合作为 Limitations 的 honest boundary case，不适合作为 positive evidence
- 如果有新 worker 跑实验 → 检查 artifacts/ 下新 CSV 与论文数字一致性

### 5. 🎯 战略上下文
**核心结论链**：Theorem 1 bias identity（exact, 无 remainder）→ Proposition 2 diagnostic → EC-HTE per-subgroup correction via HB EB（3.4ms pipeline，非 Gibbs MCMC 4.7s）→ 兼容 DIM/CausalForest/R-learner，可与 PPCI 组合

**下一个"我"最容易判断错的事**：
1. **A5 assumption 不是必要的**——identity 是 exact 的（B_s = M_global^{-1}·M_s - I 只依赖 confusion matrices），不存在 remainder term。之前 Director 提过一个带 R(Δτ²) 的公式，被我 CRITICAL 打回。正确处理已写入 theory.tex Remark 2。
2. **"10 of 11 ≥ 0.93" 是审计 worker 的误读**——论文写的是 "≥ 0.92"（appendix:948），在 0.92 阈值下计数正确。不要重复报这个。
3. **F-L Table 1 数字 vs exp034_fl_comparison_summary.csv 不同是正常的**——两个实验用不同 DGP（tau 和 pi 配置不同）。已在之前的审查报告中澄清。
4. **PPCI "0.179→0.007" 的来源**是 `exp007_ppci_dsl.csv` 中 sigma_outcome=0.5（不是 0.0）的 C_both_errors 行，average over 2 subgroups。不要在 sigma=0.0 行里找。
5. **Limitations 过长是用户硬约束违规**（写作规则），不只是建议——需要 Director 处理。


---
