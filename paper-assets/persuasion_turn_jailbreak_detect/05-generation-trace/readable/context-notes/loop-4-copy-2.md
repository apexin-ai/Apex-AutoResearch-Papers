# reviewer / loop_4.md

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_4.md`
- **Structured JSON:** [`16cdd15911429740b019.json`](../../sessions/16/16cdd15911429740b019.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_wall_time
updated: '2026-05-19T08:54:39+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0, cuda:1, cuda:2, cuda:3（westd-33183 共 9 张卡，本项目只分 4 张，C001）
- 论文 .tex 文件在**本地 workspace** `projects/persuasion_turn_jailbreak_detect/paper/`，不在远程服务器。Worker 多次查错位置（远程 `/root/.../paper/` 只有 figures/）。审查论文内容必须读本地。
- 远程服务器上代码/checkpoint/数据/进程在 `/root/persuasion_turn_jailbreak_detect/`
- Reproducibility 段描述 GRU "hidden=128, MLP 256→64→2" 与代码不符（代码默认 hidden=256, MLP 512→256→2）——尚未确认原始实验用哪组参数，这影响 exp15 比较的公平性

### 2. 🖥️ 基础设施快照
- 服务器：westd-33183 (root)，9× NVIDIA RTX PRO 6000 Blackwell (98GB each)
- 远程工作目录：`/root/persuasion_turn_jailbreak_detect/`
- 模型缓存：`/root/autodl-tmp/hf_cache/`（Qwen3-8B 16G, Qwen2.5-7B, DeBERTa-v3-base, RoBERTa-base/large）
- RoBERTa-large 本地：`/root/autodl-tmp/roberta-large-local/`
- Llama-3.1-8B：`/root/autodl-tmp/hf_cache/meta-llama/Llama-3.1-8B-Instruct/`
- Cross-LLM 数据：`/root/persuasion_turn_jailbreak_detect/data/cross_llm/`（dd/aa/benign_llama.jsonl 各 50 条）
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/`
- 活跃进程：无（exp14b + exp15 已完成，GPU 0-3 全部空闲）

### 3. 📊 当前状态
刚完成的审查：
- **exp14 + exp14b cross-LLM validation**：Llama-3.1-8B 数据生成 + 推理完成。关键发现：F1 崩溃 100% 来自 FP（Llama benign 被误判）。TP rate 在 exp14/14b 间完全一致 → DAPT jailbreak 特征跨 LLM 可迁移。Confusion matrix 分析已完成。
- **exp15 RoBERTa-large**：vanilla AA Full = 1.000±0.000（3 seeds），9class AA = 0.946。代码和数据验证通过，结果可信。DAPT 超参（LR=2e-5, epochs=5）对 355M 模型可能过高 → 可能导致 catastrophic forgetting。
- **AI 写作痕迹清理**：14 处 trailing -ing 全部修复验证通过。
- **薄弱点评估**已提交：Claim 2（2 encoder + confound）最弱，建议 RoBERTa-large 加固。

Registry: 无 RUNNING/PREPARING 实验。全部 DONE。
等待中：Paper Agent 整合 exp14b + exp15 到论文 → 可能再触发章节审查。Round 4 审稿待用户审批。

### 4. 📋 待办
- Paper Agent 提交 exp15 更新后的 §4.4 / Table 3 → 审查数字一致性 + claim 措辞
- Paper Agent 提交 Appendix F (cross-LLM) 更新（含 confusion matrix 分析句）→ 验证 FP rate 数据正确
- Director 决定是否用 LR=1e-5 重跑 exp15 DAPT → 审查结果是否改变 capacity-DAPT 交互结论
- Round 4 审稿报告到达 → 按 reviewer-audit-checklist 审查
- 论文 Reproducibility 段 GRU 描述修正 → 验证与代码一致
- DDL 2026-05-25 前最终提交 → 可能触发 paper-visual-review

### 5. 🎯 战略上下文
**论文核心 story**：DAPT 是跨攻击泛化的主要机制（~60pp on DeBERTa-base），classification supervision 稳定但 distribution-specific，encoder capacity 决定 difficulty threshold。

**关键决策链**：D036（drop verazuo）→ D037（mean pooling ≈ BiGRU）→ D038-D040（cross-LLM: benign 侧是主因）→ exp15（capacity-DAPT 交互）

**下一个"我"最容易判断错的事**：
1. **exp15 的 9class hurt 不一定是 capacity 效应**——可能纯粹是 DAPT LR 过高导致 catastrophic forgetting。在 LR=1e-5 对照跑出来之前，不要把 "DAPT hurts large models" 当确定结论写入论文。只能说 "under current hyperparameters, DAPT does not improve and may hurt"。
2. **论文在两个地方**：本地 `paper/*.tex`（真源）和远程 `paper/figures/`（只有图）。Worker 审查论文时经常只查远程然后报告"没有 .tex"——必须查本地。
3. **ddof 陷阱**：registry 用 numpy ddof=0（population std），部分 worker 用 ddof=1。比率 ≈ sqrt(3/2) ≈ 1.225。论文 §4.1 已注释。
4. **评分趋势**：R1 2.5 → R2 2.5 → R3 2.75 → R4 pending。目标 3.5+（borderline conference）。exp14b + exp15 是最大增量。


---
