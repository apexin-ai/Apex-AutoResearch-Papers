# reviewer / loop_10.md

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_10.md`
- **Structured JSON:** [`fe5f3ea8f312cb026f64.json`](../../sessions/fe/fe5f3ea8f312cb026f64.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: max_wall_time
updated: '2026-05-17T07:38:13+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单: cuda:0 / cuda:1 on westd-11235。越界即 CRITICAL。
- GPU 0 有 49GB dead memory（无进程），新实验可能需要先释放或用 GPU 1。
- CodeLlama-13B 模型在 `/root/autodl-tmp/models/CodeLlama-13b-Instruct-hf`，不在 `/root/trace-verdict-study/models/`。之前 nomarker 实验因路径错误失败，重试时务必指向 autodl-tmp 路径。
- 论文 token 数字已统一：exception_only = "median 150 tokens, mean 398"（非 ~200）。任何新 patch 必须沿用此措辞，三处位置：experiments.tex L55, discussion.tex L43, appendix.tex L466。

### 2. 🖥️ 基础设施快照
- 服务器: westd-11235 (root), 2× RTX PRO 6000 Blackwell (96GB each)
- 远程代码: `/root/trace-verdict-study/`
- 本地论文: `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/docs/paper/`
- 模型路径: Qwen → `/root/trace-verdict-study/models/Qwen2.5-Coder-{7B,1.5B}-Instruct`; CodeLlama → `/root/autodl-tmp/models/CodeLlama-13b-Instruct-hf`; DeepSeek → `/root/autodl-tmp/.hf_cache/hub/deepseek-coder-6.7b-instruct`
- Checkpoints: `/root/autodl-tmp/trace-verdict-study-checkpoints/{experiment_name}/final/eval_results.json`
- 数据: `/root/autodl-tmp/trace-verdict-study-data/`
- 活跃进程: 无（两卡空闲，GPU 0 有 dead memory）
- tmux sessions: 无

### 3. 📊 当前状态
**论文已通过 3 轮内部审查**（Overall 7/10, Soundness 4/4, 无 critical/warning），等待 Round 6 正式审稿批准。

**本轮完成的审查工作**:
- Paper patch 3 轮迭代审查 → 收敛（Abstract/Intro/Discussion/Conclusion 数据-claim 对齐）
- 6 个补充分析全部审查完毕: token efficiency, silent error, exception type breakdown, calibration diagram, error overlap, attention pilot
- Tail-truncation 两个实验审查: tail-2048=97.31%, tail-512=93.61%（vs head-2048=81.76%）— 已验证 eval_results.json
- DeepSeek seed123 error analysis 审查: format collapse（非 semantic failure），长输入 >4000 chars 触发
- ROADMAP 审查: PASS
- CodeLlama-13B nomarker 训练失败（模型路径错误）→ 已报告 Director

**Registry RUNNING**: 无。全部完成。

### 4. 📋 待办
- Round 6 正式审稿反馈到达 → 按审稿意见逐条核实 claim（用 registry 交叉验证）
- 如审稿人要求 nomarker 跨架构 → 提醒 Agent 修正 CodeLlama 模型路径后重跑（~2h）
- 如 tail-truncation 结果写入论文 → 审查新 patch 的数字一致性（97.31%/93.61% 与正文统一）
- `sec:exception_type` (appendix L250) 仍缺正文 \ref 引用 → 下次 paper patch 时提醒修复
- 如 Agent 提交新实验 → 核查 GPU 合规（cuda:0/1）+ 模型路径

### 5. 🎯 战略上下文
**核心结论**: Exception events 是 verdict prediction 的 minimal sufficient signal。99.83%±0.00 (Qwen 3 seeds), 99.89%±0.10 (CodeLlama 3 seeds, 1 seed=100%), 99.33% (DeepSeek 2/3 seeds)。Signal-limited not capacity-limited。

**关键决策链**: D049 (irreducible ceiling) → D057 (falsified: CodeLlama seed123=100%, 改为 "near-perfect floor") → D053 (signal-limited claim 升级) → D055/D056 (nomarker: 91% semantic)

**易错点**:
1. DeepSeek 99.33% 是 2/3 seeds（排除 seed123 outlier 91.09%）。论文 Abstract/Intro 写 "≥99.33% across all four models (≥99.83% on three of four)"。不要写成"所有模型 ≥99.83%"。
2. Tail-truncation 结果（97.31%/93.61%）是**新实验**，尚未写入论文。如果 Agent 写入需要审查数字一致性。
3. "~200 tokens" 已全文修正为 "median 150, mean 398"。如果看到 ~200 残留就是 bug。
4. 0.56pp 是 cross-model exception gap（99.89-99.33），不是 0.50pp（0.50pp 仅出现在 appendix epoch degradation 语境中，不同指标）。
5. Attention pilot 结论：建议不放正文（source_code > error_marker 会被攻击），最多 Discussion 加一句话引用 locals dump 的低 per-token density。


---
