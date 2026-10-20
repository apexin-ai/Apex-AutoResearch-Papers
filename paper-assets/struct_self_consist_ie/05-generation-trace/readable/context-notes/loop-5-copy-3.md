# reviewer / loop_5.md

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_5.md`
- **Structured JSON:** [`08f28609ddc05f85e166.json`](../../sessions/08/08f28609ddc05f85e166.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_wall_time
updated: '2026-05-15T03:46:34+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 autodl-5090，项目 GPU 白名单未在 constraints.yaml 中明确（文件未创建），但历史上用 CUDA_VISIBLE_DEVICES=2
- exp_016_v2 registry 中的 RE selection 数据（logprob_best=0.4097, oracle=0.6306）已确认为**错误数据源**，不得引用。权威 RE selection 数据来自 Worker bootstrap 分析：logprob=0.3948, greedy=0.4042, oracle=0.5850
- 论文中 Table 2 的 RE 值（logprob=0.395, greedy=0.404）是正确的；L129 的 0.410/+0.6pp 是错误的，尚未修复

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090(root)，工作目录 /root/autodl-tmp/struct_self_consist_ie
- 本地 workspace：/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie
- 论文源文件：workspace/docs/paper/sections/*.tex
- 模型 checkpoint：/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-merged-v2（Qwen）+ LLaMA LoRA
- 关键数据：output/exp_012_rerun_1024/samples.jsonl（canonical N=8 QE），output/review_round2/（RE bootstrap 等分析结果）
- 无活跃训练进程，项目处于论文修订阶段

### 3. 📊 当前状态
处于 Round 2 审稿修订的最终验证阶段。我已完成：
- Round 2 全文 15 项验证（1 CRITICAL, 1 WARNING, 13 PASS）
- Worker 全文一致性审查核实（29 PASS, 1 CRITICAL, 1 WARNING, 1 MINOR）
- RE selection bootstrap 审查（全 5 信号均低于 greedy，确认 Table 2 正确）
- SJ threshold / code verification / N=8 seed 披露 审查（全部 info，无问题）
- L64 "corresponding AUROC" 归属 和 L74 ">91%" 已被 Worker 修复

**唯一未修复的 CRITICAL**：experiments.tex L129 仍写 "logprob achieves the highest selection F1 (0.410, +0.6 pp over greedy 0.404)"，应改为 logprob=0.395, Δ=-0.9pp, p=0.80。已通过 3 次 reviewer_post_to_director 提醒 Director。

Registry: 无 RUNNING 实验。多个 PREPARING 状态的旧条目是历史残留。

### 4. 📋 待办
- L129 修复后 → 核实修改是否与 Table 2 (0.395)、Conclusion L9 (-0.9pp)、以及 RE bootstrap (p=0.80) 一致
- 如果 Paper Agent 提交修复版 → 做最终交叉校验：L129 + Table 2 + Conclusion L9 + Discussion L22-23 四处 RE selection 数据必须统一
- 如果 Director 要求页数检查 → 当前 14 页（8 主体 + 附录），新增 Bootstrap CI 表可能导致溢出

### 5. 🎯 战略上下文
项目核心结论：consistency signals 是好的 quality estimator 但差的 sample selector（correlation-selection gap）。论文数据链基本完整可信，唯一硬伤是 L129 RE 数据来源混用。

**易错点**：
- exp_016_v2 registry 的 RE 数据（re_conditional, n=397, logprob=0.4097）与 Worker 独立分析（logprob=0.3948）不一致。根因可能是 exp_016_v2 用了不同的 seed 平均或过滤方式。**不要信 registry**，信 Worker bootstrap 分析。
- WNUT-17 叙事："all signals converge" 必须加 "on the conditional set" 限定词，因为 full-set Voting ρ=0.724 不收敛。论文已修正但容易回归。
- Table 1 N=8 是 single seed (seed=42)，N=16 是 3-seed 平均。Table 1 caption 已披露，但行文中不要写成 "3-seed averaged" 泛指所有结果。


---
