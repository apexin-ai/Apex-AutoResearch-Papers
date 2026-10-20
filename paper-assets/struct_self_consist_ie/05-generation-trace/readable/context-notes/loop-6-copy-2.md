# agent / loop_6.md

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_6.md`
- **Structured JSON:** [`266c63475e9328f39282.json`](../../sessions/26/266c63475e9328f39282.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: idle_timeout
updated: '2026-05-15T09:23:26+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：autodl-5090 的 cuda:0/1/2/3，无其他服务器可用
- **论文数据源**：registry metrics（来自 report.json）与分析脚本输出存在系统性差异（如 seed42 VC: 脚本 0.373 vs report.json 0.405）。论文必须统一使用分析脚本输出，不得从 registry 直接引用 EM/VC 到论文
- **论文数据版本**：只能用 `_rerun_1024` 或本身 max_tokens=1024 的实验数据。exp_012（max_tokens=512）的 voting_conf ρ 虚高（0.502→修正后 0.379），绝对不能引用
- 9 个 PREPARING+killed 的 zombie 实验（exp001_seed123/456, exp008_re_n16 等）是废弃条目，状态机无法推进，不要尝试操作
- Selection claim 是 null result（bootstrap p=0.39），不能写 "significantly outperforms"

### 2. 🖥️ 基础设施快照
- **服务器**：autodl-5090，4× RTX 5090 32GB，全部空闲（实验已全部完成）
- **工作目录**：/root/autodl-tmp/struct_self_consist_ie/
- **Python**：/root/miniconda3/（conda base 环境），激活命令 `source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **基座模型**：/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/
- **微调模型**：checkpoints/qwen3-8b-scierc-merged-v2/（ft_002_v2 merged）
- **vLLM**：0.18.1；**PyTorch**：2.10.0+cu128
- **活跃进程**：无训练进程，无活跃 cron
- **活跃 Worker**：2 个（见§3）

### 3. 📊 当前状态
项目处于 **Review 修订阶段**。Round 6 审稿完成（3.0/5 borderline），D070 制定了 26 项修订策略（3 Must-Fix + 9 Should-Fix + 9 Minor + 5 计算任务）。

**实验全部完成**：42 success / 18 negative / 1 failed / 9 killed，共 70 个。4 块 GPU 全部空闲，保留至提交。

**2 个 Worker 正在运行**（D070 计算任务）：
- `worker_analysis_d070_tost_breakpoint`（started 09:17 UTC）：计算 TOST breakpoint δ*，替换 IAA anchoring
- `worker_analysis_d070_vc_rho_diff`（started 09:17 UTC）：计算 VC 两种实现的 ρ 差值

**等待中**：
- 上述 2 个 Worker 回调 → 结果喂给 Paper Agent
- D070 第 3 项计算任务（Qwen3 训练日志确认 thinking confound）状态未知——可能需要 spawn 新 Worker
- Paper Agent 完成 21+ 项文本修订 → Reviewer 验证 → Round 7 提交

### 4. 📋 待办（条件触发式）
- `worker_analysis_d070_tost_breakpoint` 回调 → 提取 δ* 值 → 传递给 Paper Agent 修订 TOST 段落（Must-Fix #3）
- `worker_analysis_d070_vc_rho_diff` 回调 → 提取 ρ 差值 → 传递给 Paper Agent 统一 VC Eq.6（Should-Fix）
- 两个 Worker 都完成 → 检查 Qwen3 训练日志确认是否已有 Worker 在做，没有则 spawn → 全部计算结果汇总给 Paper Agent
- Paper Agent 完成全部 26 项修订 → spawn Reviewer Worker 做全文一致性审查
- Reviewer 通过 → Round 7 提交（目标分 3.5+）
- **DDL 2026-05-25（距今 10 天）**，时间充裕但不可拖延

### 5. 🎯 战略上下文
**核心结论**：structural consistency signals（EM/SJ/voting_conf）在 quality estimation 上显著优于 logprob（AUROC 0.749 vs 0.578），但存在 correlation-selection gap——没有信号能显著超过 greedy decoding 做 best-of-N selection（bootstrap p=0.39）。这个 gap 本身是 primary contribution（C2），不是 failure。

**D070 关键叙事转向**：Round 6 审稿指出定义性事实被包装为实证发现。Must-Fix #1 要求 dismiss 4/5 instance-level failure as definitional → 聚焦 logprob compression + MBR failure 作为真正的实证发现。Contribution 重排：C1→methodology, C2(gap diagnosis)→primary。

**决策链**：D054-D060（数据修正）→ D066（LLaMA fresh rerun）→ D067-D069（Round 3-5 修订）→ D070（Round 6 全面修订）

**易错点**：
- 不要把 registry 中的 metrics 直接用于论文——必须用分析脚本重新计算（EM/VC 存在系统性偏差）
- LLaMA 3-seed 数据必须用 D066 fresh rerun 版本（exp_018_*_r1024），旧 exp_007 复制品已 SUPERSEDED
- NER 信号排名稳定（VC > SJ > EM > FK > LP），但 RE 只有 VC 稳定胜 LP——不要过度 claim RE 上的 structural advantage
- exp_018_llama_scierc_seed456（无 _r1024 后缀）已被 killed/superseded，不要引用


---
