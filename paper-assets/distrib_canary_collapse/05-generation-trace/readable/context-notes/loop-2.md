# director / loop_2.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_2.md`
- **Structured JSON:** [`6e6bbe2d90f66ac3b6ac.json`](../../sessions/6e/6e6bbe2d90f66ac3b6ac.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-14T18:56:29+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 仅限 cuda:0 / cuda:1 on westd-19828（项目配置 `execution.gpu_ids`）
- 服务器名已从 autodl-rtx6000 / gpu-6000pro-3 统一为 **westd-19828**，submit_training_job 必须用此名
- α-sweep 代码部署前**必须**完成双向 mix_datasets 修复（单向修复在 α>0.50 下静默产生错误比例）
- MVP verdict 是 4-seed STRONG PASS，但 claim scope 硬限：canary 仅 lead diversity（distinct_1/2），**不能 claim lead perplexity**（D006）
- Dream (dream_20260514T184925) 完成回调前**禁止批准 P0 实验**——post-mvp-kickoff skill 硬约束

### 2. 🖥️ 基础设施快照
- 服务器：westd-19828 (connect.westd.seetacloud.com:19828)，2× RTX PRO 6000 Blackwell 96GB
- 工作目录：/root/autodl-tmp/distrib_canary_collapse
- Python：/root/miniconda3/bin/python（conda base, Python 3.12.3, PyTorch 2.10.0+cu128）
- 数据：/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k/
- MVP 结果：/root/autodl-tmp/distrib_canary_collapse/results/mvp/（rep42-45 + analysis/）
- HF cache：/root/autodl-tmp/.hf_cache（HF_ENDPOINT=https://hf-mirror.com）
- 活跃进程：无（rep44/rep45 已完成，GPU 双卡空闲）
- 远程 iterative_train.py **仍为旧版**（257行，无 accumulate，无双向 mix）——本地 artifacts 已有修复版但未部署

### 3. 📊 当前状态
刚完成 post-MVP kickoff 全流程：paper_framing.md + experiment_plan.yaml + dream_simulate + ROADMAP 更新。
- Dream dream_20260514T184925 **pending**（full review mode，预计 10-25min 完成后注入 session）
- Agent 队列 depth=3，正在处理综合指令（rep44 registry 修正已确认完成，后续是 worker:done 回调处理）
- 双卡空闲，等 Dream 通过 + 代码部署后启动 α-sweep
- report.md 过时（仍显示 rep44=failed），需 auto_build_report_facts 刷新

### 4. 📋 待办
- Dream 回调到达 → Read dream-report-action skill → 按三档审稿结果决策（通过→批准 plan_001 α-sweep；结构性问题→回改 framing/plan 再 re-dream）
- Agent 处理完队列 → 确认双向 mix_datasets + accumulate 已部署到远程 → α-sweep 可启动
- α-sweep 启动时记得包含 α=0.0 null control（Reviewer 建议已纳入 plan_001，4 个 α 点 × 3 seeds）
- plan_003 (max_lag=7 重分析) 零 GPU → 可立即派 Agent 执行不等 Dream

### 5. 🎯 战略上下文
- **决策链**: D006（predictability boundary framing）→ D007（优先级 α-sweep >> ablation > C4 > scale）→ D008（distinct_3 降级 supplementary）
- **论文最强 framing**: "delineating predictability boundaries" — null results 变成 evidence for the boundary，对 reviewer 攻击天然鲁棒
- **最大未验证赌注**: α<100% 下 canary→perplexity 是否恢复 lead。如果 α-sweep 全线 null → claim scope 锁死在 diversity-only，仍可投但需更多 ablation 充实
- **易错点**: (1) 不要在 Dream 完成前批准实验 (2) 部署代码前确认双向 subsample 用 random sampling 不是 range(n) (3) token_entropy→perplexity lag=-5 可能是 max_lag 截断，不要引用为精确 lead time
- **Reviewer 反复强调的**: 2 卡不能空着——Dream 等待期可以让 Agent 做零 GPU 任务（plan_002 准备代码、plan_003 重分析）


---
