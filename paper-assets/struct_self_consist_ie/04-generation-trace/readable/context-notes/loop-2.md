# director / loop_2.md

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_2.md`
- **Structured JSON:** [`732b4fb9add6c53702ae.json`](../../sessions/73/732b4fb9add6c53702ae.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-14T12:47:45+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 GPU 分配：autodl-5090 cuda:0-3 + gpu-5090-4x-2 cuda:0-3，共 8 张 RTX 5090 32GB，全属本项目
- 目标 DDL：ARR May 2026-05-25（距今 11 天），不得 fallback 到其他会议
- paper_framing.md 已于 D019 pivot：核心叙事从 "TTS improvement via SJ" 转向 "confidence estimation + correlation-selection gap"。**禁止回退到旧叙事**，所有后续实验解读必须对齐新 framing
- RE conditional filtering 定义不一致（run.log n_cond=124 ρ=0.411 vs report.json n_cond=89 ρ=0.284），T=1.0 全集重跑前必须统一
- exp_012 有 AUROC bug（logprob AUROC=0.5000，F1=1.0 二值化问题），WNUT 前必须修复
- 审稿阶段已启动（Group C 在 review_chat_id oc_3897c28...），不要干预他们的格式/投稿工作

### 2. 🖥️ 基础设施快照
- 服务器 1：autodl-5090 (connect.bjb1.seetacloud.com)，4× RTX 5090 32GB，root
- 服务器 2：gpu-5090-4x-2 (connect.bjb1.seetacloud.com)，4× RTX 5090 32GB，root
- 工作目录：/root/autodl-tmp/struct_self_consist_ie
- Python/Conda：aml-train 镜像，/root/miniconda3/bin/python，conda base 环境
- 模型：ft_002_v2 (Qwen3-8B LoRA fine-tuned on SciERC)，CoNLL fine-tune 刚完成
- LLaMA 下载中（exp-007 依赖）
- W&B：未配置
- 当前活跃进程：exp_003_ner_wnut17 在运行，具体 PID/tmux 需 SSH 确认

### 3. 📊 当前状态
**刚做完的**：
- exp-002 CoNLL 完成（D020）：重要发现——EM > SJ on easy tasks，SJ >> logprob 跨数据集确认，voting 首次 beat greedy (+0.18pp)
- exp-016 ensemble 分析完成（D018/D019）：触发叙事 pivot，发现 correlation-selection gap
- Dream 2 完成（D016/D017）：全三档 3/6，问题是 presentation 层（novelty framing / related work / figures），不是数据层

**正在处理**：Agent 队列有 3 个 worker:done 回调正在消化（exp-016 分析结果、exp-002 merge、gpu-5090-4x-2 修复重跑）

**Registry 状态**：
- RUNNING：exp_003_ner_wnut17（WNUT-17 NER）
- PREPARING（8 个）：exp_008_re_n16_full, exp_001_n16_seed456_full, exp_001_n16_seed123_full, exp_002_merge_conll2003, exp008_re_n16, exp001_seed456, exp001_seed123, exp_007_ner_llama
- DONE：23 个（成功 14 / 负向 6 / 失败 1）

**GPU 利用**：2/8 active，多数卡在 setup/download 阶段，预计 1-2h 内更多卡投入

### 4. 📋 待办（条件触发式）
- Agent 消化完 3 个 worker:done 回调 → 检查 GPU 利用率，确保 8 卡全排满（PREPARING 的 8 个实验应该陆续启动）
- exp-003 WNUT 完成 → 分析 signal ranking 是否与 CoNLL/SciERC 一致（验证 task-difficulty-dependent 假设）
- exp-007 LLaMA 下载完成 → dry-run → 提交训练，验证 cross-model SJ stability
- exp-001 全实例 T=1.0 完成 → 确认 RE N=16 信号恢复（voting ρ=0.448 in n=200，需 n=551 确认）
- exp-008 RE N=16 完成 → 确认 Claim 3 sample-complexity gradient
- 所有 P0 GPU 实验完成 → 激活 Paper Agent（Full Draft 模式），关键任务：35+ refs / 3+ figures / reframe novelty / clarify correlation-selection gap
- AUROC bug 未修 → 催 Agent 在 WNUT pilot 前修复 logprob AUROC 二值化逻辑
- RE conditional filtering 定义未统一 → exp-001 full rerun 前必须解决

### 5. 🎯 战略上下文
**核心结论链**：
- D010: MVP 结论——NER PASS (SJ ρ=0.383), RE full FAIL (ρ=0.234), RE conditional positive (ρ=0.372)
- D011→D013: Baseline 加入后 SJ 压倒性胜 logprob (AUROC 0.689 vs 0.591)，voting_conf ≈ SJ，升级为 "structural consistency family"
- D018/D019: **关键 pivot**——exp-016 发现 best-of-N selection 全部不如 greedy (NER)，quality estimation ≠ sample selection，correlation-selection gap 成为核心新发现
- D020: CoNLL 证实 signal ranking 是 task-difficulty-dependent (easy: EM>SJ; hard: SJ>EM)，进一步丰富了 Claim 3

**最容易判断错的事**：
1. 不要因为 best-of-N selection 失败就认为项目是 negative result——correlation-selection gap 本身是 novel finding，quality estimation 仍是强正面结果
2. Dream 全 3/6 不代表论文不行——瓶颈是 presentation (related work / figures / novelty framing)，不是 experimental evidence。Paper Agent 是 critical path
3. CoNLL 上 EM > SJ 不是坏消息——"最优信号取决于任务难度" 是比 "SJ universally best" 更深的 insight
4. exp-001 的 N=16 RE 数据只有 200/551 实例，**绝不能**在论文中用这个数据 claim N-scaling 效应——必须等全集确认


---
