# agent / loop_19.md

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_19.md`
- **Structured JSON:** [`6c2561a06c15ba711ef3.json`](../../sessions/6c/6c2561a06c15ba711ef3.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 19
reason: idle_timeout
updated: '2026-05-24T03:59:24+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 仅限 autodl-5090 cuda:0-3（config 也含 autodl-5090-c cuda:0-3，但当前 servers 只列 autodl-5090）
- D244 决策：DDL eve 不启动新实验，4×5090 保留给 rebuttal 期间使用
- SciERC construction 指标：+0.32pp n.s.（单种子 seed42），不可 overclaim
- 三张表的 F1 基线不同：tab:scale_comparison 用 entity-type-averaged macro-F1(.667)；tab:selection 用 macro-F1(.645)；tab:fewnerd 用 instance-averaged(.663）——各表内部一致但不可混用
- autodl-5090 上 vLLM Unicode surrogate bug 尚未修复（autodl-5090-c 已修复），在 5090 跑新实验前需先同步 `sampling.py:673` 的 `errors='replace'` 修复
- 论文 N-scaling 图表必须用统一 instance 集 + 统一 greedy baseline（非各自独立解码的 greedy）

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090（主），autodl-5090-c（备用）
- 工作目录：`/root/autodl-tmp/struct_self_consist_ie`
- Python：aml-train 镜像，`/root/miniconda3/bin/python`（conda base 环境）
- 模型：qwen3-8b-fewnerd-exp021-merged（finetuned），Qwen2.5-7B-Instruct（pretrained）
- 匿名 repo commit：`58d1be8`
- 活跃进程：无（0 RUNNING，0 cron）
- GPU：4×RTX 5090 全部空闲

### 3. 📊 当前状态
论文 **submission-ready**，EMNLP 2026 DDL 是 2026-05-25。编译通过（46 pages, 0 errors），ARR checklist 15/15，匿名 repo 就绪。

- 0 个 RUNNING 实验
- 18 个 PREPARING 实验（rebuttal 备用池：entity verifier B2 系列、cross-task A1、signal routing E1、diversity/budget 系列等）
- R41 审稿已提交，等用户确认结果
- 最新审稿分数：R39 Fresh mode R1=3.5 / R2=3.0，realistic target 3.5 (Borderline Conference)

全部待办 blocked on 用户：OpenReview 提交、R41 确认、Figure 1 最终版。

### 4. 📋 待办（条件触发式）
- 用户完成 OpenReview 提交 → 确认提交成功，进入 rebuttal 准备模式
- R41 审稿结果返回 → 分析 reviewer comments，规划 rebuttal 实验（从 18 个 PREPARING 池中选最相关的）
- 收到 reviewer 质疑 epoch confound → 5-epoch 数据已就绪（memory.md 有完整对比），可直接引用
- 收到 reviewer 质疑 cross-task generalizability → 启动 exp_a1_spider_sql_sc（SQL on Spider）
- 收到 reviewer 质疑 entity verifier → 启动 exp_b2 系列（已有 4 个变体 PREPARING）
- autodl-5090 需要跑新实验前 → 先同步 vLLM unicode bug fix

### 5. 🎯 战略上下文
- **核心结论**：Self-Consistency 在 NER 上存在 correlation-selection gap——agreement signals（SJ, κ）与 correctness 正相关，但 MV 聚合无法利用这一相关性。Finetuned MV 负向（3 datasets），pretrained MV 正向（3 datasets）。Gap 是 model-intrinsic。
- **Framing 演化链**：D235→D236→D237→D238→D239→D240，最终收敛为 "NER diagnostic framework + correlation-selection gap"
- **易错点 1**：SciERC finetuned MV Δ = -0.50±0.74pp，方向不一致（s42 负、s123 正、s456 负），属于 noise regime——不可 claim MV hurts SciERC，只能说 n.s.
- **易错点 2**：3-epoch degen(8.8%) < pretrained degen(11.7%)——fine-tuning 与 degeneracy 关系非单调，叙事需处理
- **易错点 3**：18 个 PREPARING 实验是 rebuttal 备用，不要在 DDL 前启动（D244 决策）
- **研究已收敛（D243）**，当前阶段纯粹是等用户提交 + 准备 rebuttal


---
