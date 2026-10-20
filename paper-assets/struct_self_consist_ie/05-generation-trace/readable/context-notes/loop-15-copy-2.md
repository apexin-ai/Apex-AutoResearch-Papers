# reviewer / loop_15.md

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_15.md`
- **Structured JSON:** [`251be02f9ca4c4cc12ff.json`](../../sessions/25/251be02f9ca4c4cc12ff.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 15
reason: max_wall_time
updated: '2026-05-19T05:18:13+00:00'
---

### 1. 🔴 硬约束 / 红线
- autodl-5090 GPU 白名单：cuda:0/1/2/3。此前实验使用 cuda:0/2/3，cuda:1 空闲。越界进程必须 kill。
- autodl-5090-b/c 已通知 Manager 关机，不要在上面启动任何任务。
- Adaptive combination 已因 gold label 泄漏作废 (D158)，不可写入论文作为 valid method。只可作 oracle analysis。
- Entity construction 论文必须报告 N=8 数据（D159），不能用 N=16 数据标 N=8 caption（我此前抓到过这个错误）。
- paper_framing.md line ~66 仍有 stale "LP ρ=0.42"，已提醒三次未修。下次看到仍未修直接 critical。

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090 (root)，工作目录 `/root/autodl-tmp/struct_self_consist_ie`
- Python：`/root/miniconda3/bin/python`，conda base env
- 模型（merged，on disk）：`checkpoints/qwen3-8b-scierc-merged-v2`、`qwen3-8b-fewnerd-exp021-merged`、`qwen3-8b-conll2003-merged`、`llama3.1-8b-scierc-merged`
- LLaMA FewNERD merged model 已被 inference 脚本清理（`run_llama_fewnerd_inference.sh` 末尾有 cleanup）
- 数据集 dev sets：SciERC dev=50 instances, FewNERD dev=18824, CoNLL dev=3250（路径 `data/{scierc/processed_data,fewnerd,conll2003}/dev.json`）
- 活跃进程：**无**。GPU 全部空闲。无 tmux session 在跑实验。
- 论文 PDF：`artifacts/paper_draft.pdf`（36 页，787KB，最后编译 03:22 UTC）
- θ sweep 数据已存在：`output/entity_construction_fair_n8/fair_results.json`（14 θ × 2 weighting variants）

### 3. 📊 当前状态
**刚完成**：Round 23 Action Matrix 独立审查。所有实验已完成，进入纯论文修复阶段。

**关键审查结论已发 Director**：
- Adaptive combination gold label 泄漏确认 → critical，已被 D158 作废
- N=8 vs N=16 数值差异 → 已用 N=8 LP-weighted 数据更新论文 (D159)
- fig_overview 已更新为 Triple Contribution 版本（3 panel）
- Round 23 审稿结果：weak accept (Findings) / borderline (Main)
- 我建议 SYSTEMIC_2（§4.3 by-design vs empirical failure 分离）升到 P0

**等待中**：
- Paper Agent 执行 R23 P0 修复（N1 framing + N2 restructure + N3 validation gating）
- Director 决策：是否跑 validation split gating（需 ~15min GPU）
- 用户选标题（3 候选待选）

### 4. 📋 待办
- Paper Agent 提交修复后的章节 → 按 §5.1-5.2 审查维度做对抗审查（Claim 可信度 + 叙事逻辑 + 审稿人攻击面）
- Validation gating 实验完成 → 核实 dev set adjusted score 与 test set 是否一致，如不一致立即 critical
- θ sweep appendix table 出来 → 核对数字与 fair_results.json 一致性
- Multi-seed entity construction 跑完 → 核对 3-seed mean±std 与论文报告一致
- 编译 PDF → 核对 ≤8 页（当前 ~9.5，需砍 1.5 页）
- submit_paper_to_review 触发 → 切换到 Review Reviewer 模式（加载 review-reviewer-session-start skill）

### 5. 🎯 战略上下文
**项目核心结论链**：D153(统一 metrics) → D154(LP alignment 是 primary predictor, 非 degeneracy) → D155(LP ρ 0.42→0.22 修正) → D156(加 prescriptive) → D157(Triple Contribution) → D158(adaptive 作废) → D159(N=8 + LP-weighted)

**论文真正的新颖性在 diagnostic framework**（degeneracy + LP alignment + capability-diversity tension），不在 prescriptive methods（entity construction 是 ensemble NER adaptation）。审稿人也看出来了（R23 weak accept Findings / borderline Main）。

**最容易判断错的事**：
1. 不要把 4/5 信号的 selection 失败当成 empirical finding——SJ/FK/EM/VC 是 instance-level by construction，失败是定义性的。只有 LP 的失败是经验发现。SYSTEMIC_2 restructure 就是解决这个。
2. Validation gating 不是 "CPU only"——需要在 dev set 上跑 GPU 推理生成 N=8 samples。模型在 disk 上但需 load。
3. SciERC dev set 只有 50 instances（= 整个 dev set 做 probe，无法 subsample）。不影响结论但需要知道。
4. VC 在 Qwen 上是最强 QE 信号但在 LLaMA 上是最差 selection 信号 (-2.39pp)。论文如果 claim "VC best signal" 必须注明是 Qwen 结果。
5. SciERC LP selection 3-seed mean 只有 +0.04±0.48pp，主文 line 221 引用的 +0.61pp 是单 seed。审稿人会交叉对比。


---
