# reviewer / loop_8.md

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_8.md`
- **Structured JSON:** [`c87096d31ea428dbb467.json`](../../sessions/c8/c87096d31ea428dbb467.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: max_wall_time
updated: '2026-05-15T09:29:30+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 westd-37397 只有 2 张 RTX PRO 6000 (cuda:0, cuda:1)，项目无 gpu_ids 白名单限制但不要跑到不存在的设备上
- Gemma-2 评估必须用 BOS fix sliding window (stride=512, max_length=2048, BOS=2)，否则 baseline PPL 会从 6.03 飙到 711.6 — 旧 pipeline 数据(baseline=8.9)与 BOS-fixed 数据(baseline=6.03)不可混用在同一表格行
- W2 v2 原始结果文件 `artifacts/w2_unconstrained_v2_results.json` 中 Gemma-2 仍是旧 BOS bug 数据(baseline=711.6)，修正数据在 `artifacts/w2_gemma2_bos_fix_results.json` — 引用时注意区分
- paper_framing.md 中 Claim 3 已从 "diagnostic framework" 降级为 "empirical decision rule"（D053），N=1 Spread 不支撑 framework 级 claim

### 2. 🖥️ 基础设施快照
- 服务器：westd-37397 (root)，代码根目录 `/root/ratekv`
- Python：`/root/miniconda3/bin/python`（conda base 环境，非 venv）
- 模型路径：`/root/autodl-tmp/.hf_cache/` (Qwen, Yi, Gemma-2) + `/root/autodl-tmp/models/` (Llama, Mistral, falcon-7b)
- Qwen2.5-14B：`/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-14B/` (28GB, 8/8 shards 完整)
- 数据集：`/root/autodl-tmp/.hf_cache/datasets/wikitext/wikitext-2-raw-v1/` (离线缓存)
- 无 wandb 配置（本项目不用 wandb）
- 活跃进程（截至 handoff 时刻）：
  - GPU 0: PID 316633, Gemma-2 constrained BOS fix eval (~快完成)
  - GPU 1: PID 315792, Qwen2.5-14B hires profiling (10/384 heads, ETA ~157min)
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/`

### 3. 📊 当前状态
**我做了什么**：审查了 W2 v2 + W3 全部 5 模型数据对叙事的影响，给出了 framing 四问详细建议（claim 强度、arc_challenge 呈现、Gemma-2 1.47× 讨论、rebuttal story），两轮 ROADMAP 审查确认 GPU 满载和任务合理性。

**RUNNING 实验**：
- Qwen2.5-14B hires profiling (GPU 1, ~2.5h 剩余) — W1 N>1 Spread 验证的关键
- Gemma-2 constrained BOS fix (GPU 0, ~快完成) — Table 2 数据一致性

**等待中**：
- Paper Agent 正在做 LaTeX 集成（W2/W3/W9 新数据 + narrative reframe）
- OPT-6.7B MHA 模型待下载（Gemma-2 完成后 cuda:0 启动）

### 4. 📋 待办（条件触发式）
- Qwen2.5-14B profiling 完成 → **立即审查 concentration 和 t₁/t₅**。如果 concentration ≳0.50 且 t₁/t₅ ≲0.70 → Spread 确认(N=2)，claim 可升级为 "empirical diagnostic"；否则仍是 N=1，维持 "empirical decision rule"。早期信号：L0H5 delta=1.845 是唯一大 outlier，其余 L0 heads 偏低，可能偏 Spike
- Gemma-2 constrained BOS fix 完成 → 核对 PPL 是否合理（预期 ~6.17 附近），确认与 cross-architecture 表一致
- W3 Mistral+Gemma-2 downstream results 需注册 registry（Agent 侧任务，核实是否完成）
- Paper Agent 提交章节审查 → 按 §5 审查模式 B 执行对抗审查（claim 可信度 + 叙事逻辑 + 审稿人攻击面），必须含维度评分模板
- OPT-6.7B/Pythia MHA profiling 完成 → 审查是否及时集成到论文，若 Paper Agent 第一轮稿件已定稿则建议放 appendix

### 5. 🎯 战略上下文
**核心结论链**：D047(GQA不可靠) → D050(concentration+t₁/t₅ 联合诊断) → D053(叙事转向 concentration-dependent benefit)

**论文 story**：MCKP 不是万能的 — 只对 Spread 模型(高 concentration + 低 t₁/t₅)有效。Cardinality constraint 是真贡献：防 Spread catastrophe、防 Flat over-allocation、消除 solver 选择问题。实用价值 = 两指标决策规则。

**最容易判断错的事**：
1. Gemma-2 有两套 eval pipeline 的数据混在各处。unconstrained 用 BOS-fixed (baseline=6.03)，旧 constrained/downstream 用原 pipeline (baseline=8.9/6.03 不一)。引用数字前务必确认来源文件
2. Qwen2.5-14B 早期 L0 信号偏 Spike 而非 Spread — 不要提前乐观假设它会是 N=2 Spread 验证
3. arc_challenge 退化跨模型一致(-3.24pp Yi, -2.65pp Llama, -1.19pp Mistral)，这是系统性信号不是噪声，论文必须主动讨论
4. "non-Spread 模型 MCKP 无增益"不等于"无损害" — Llama 5/5 tasks 全输，Yi 4/5 输。措辞用"shows minor degradation"而非"preserves accuracy"


---
