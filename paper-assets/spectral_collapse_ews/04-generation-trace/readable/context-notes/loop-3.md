# director / loop_3.md

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_3.md`
- **Structured JSON:** [`5390442538d87625f2b3.json`](../../sessions/53/5390442538d87625f2b3.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_messages
updated: '2026-05-17T21:17:13+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 cuda:0 / cuda:1（rtx6000-diagprobe，2× RTX PRO 6000 98GB）
- 服务器无外网：HF_HUB_OFFLINE=1, TRANSFORMERS_OFFLINE=1，所有模型/数据必须本地
- 所有实验启动必须用 submit_training_job（自动 tmux + sentinel），禁止裸 nohup（M005 教训：cron 误判 5 次）
- 同一实验的 cleanup 和 restart 不能并行派两个 worker（M004 教训：race condition 导致 checkpoint 被误删）
- 论文主参数 k=10, τ=0.002（D015）。exp_005 用的 k=20 是 sensitivity 数据不是主实验
- 双实例实测降速 3.5-5x（M007），不要再尝试同卡双训练 job
- Paper Writing Worker 会生成幻觉引用（M008）——所有 \cite{} 必须验证 bib 中存在

### 2. 🖥️ 基础设施快照
- 服务器：rtx6000-diagprobe (connect.westd.seetacloud.com)，账号 root
- 工作目录：/root/spectral_collapse_ews
- Python：/root/miniconda3/bin/python（conda base env）
- 模型：410M GPT-2 style（本地），1B Pythia（本地）
- 数据：50K real samples + 合成生成，total_per_gen=50K
- 活跃进程：
  - exp_006: cuda:0, PID 134913, tmux=exp_006, adaptive k=10 s42（论文主实验，Gen 1 完成）
  - exp_004: cuda:1, PID 135411, tmux=exp_004, fixed_mix s42（baseline，Gen ~1，刚从双实例恢复独占）
- exp_005: 已 kill (D018)，Gen 0-4 数据备份在 phase1_adaptive_k20_seed42_results_gen0-4_backup.json
- Cron：有实验监控 cron（自动检测 sentinel 变化）
- W&B：未配置
- 论文本地路径：项目 workspace 下 paper/sections/（introduction.tex, method.tex, experiments.tex, related_work.tex 等）

### 3. 📊 当前状态
**刚做完**：
- Kill exp_005 释放 cuda:1 给 exp_004 独占 (D018)
- 激活 Paper Agent 写论文骨架——Introduction/Method/Experiments/Related Work 初稿已完成
- Reviewer 发现 Introduction+Related Work 大量幻觉引用 → Paper Agent 已重写，grep 验证 clean
- Reviewer 发现 method.tex/experiments.tex 参数错误(k=1.0→10, τ=0.005→0.002) → Paper Agent 报告已修复（grep 验证 clean）
- Phase 0 (exp_001) 完成：Gen 0-10 全量数据，ppl +704%, HellaSwag -28.6%, 加速比 2.43x
- paper_framing.md 已创建并更新

**Registry 状态**：
- exp_001 DONE(success) — Phase 0 完成
- exp_002 DONE(success) — 1B pilot
- exp_003 DONE(killed) — D011 bug
- exp_004 RUNNING — fixed_mix s42，cuda:1 独占，~Gen 1
- exp_005 DONE(killed) — D018 释放 GPU，Gen 0-4 数据已备份
- exp_006 RUNNING — adaptive k=10 s42，cuda:0，~Gen 1（论文主实验）

**等待中**：
- Paper Agent 继续写 conclusion → limitations → abstract
- exp_004/exp_006 自然推进（cron 监控）
- linear_increasing launch script 已准备好，等 GPU 释放

### 4. 📋 待办
- exp_006 完成（~May 19 morning UTC）→ 收集 Gen 0-10 metrics + 启动 linear_increasing on cuda:0（script 在 /root/spectral_collapse_ews/scripts/launch_linear_increasing.sh）
- exp_004 完成（~May 19 morning UTC）→ 收集 Gen 0-10 metrics + MVP 比较（adaptive k=10 vs fixed_mix, ≥3 ppl paired t-test p<0.1）
- MVP pass → complete_mvp() + 创建 experiment_plan.yaml + dream_simulate(review_mode="full")
- MVP fail（adaptive ≈ fixed_mix）→ pivot 到 Claims 1-2 + Claim 4（characterization + EWS + signal attenuation paradox），controller 降为 discussion
- linear_increasing 完成 → 论文四条件齐全
- exp_005 有 GPU 时 → 从 Gen 4 checkpoint 恢复（低优先级 sensitivity 数据）
- Paper Agent 完成全部章节初稿 → 提交 Reviewer 审查 → 迭代修改
- 所有 [TBD] placeholder 在 Phase 1 数据到齐后填充

### 5. 🎯 战略上下文
**核心决策链**：D009(Phase 0 pass) → D010(signal→log_det) → D011(三层 bug fix) → D012(k=1→20) → D013(claim pivot: EWS+characterization 为主, controller 为 PoC) → D014(cumulative 备选) → D015(k=20→10) → D016(双实例计划) → D017(cuda:1 双实例) → D018(撤销双实例，kill exp_005)

**信号衰减悖论**（最重要的理论发现）：比例控制器自稳定负反馈环——干预→collapse 减缓→信号减弱→干预减少→collapse 恢复。Phase 1 中 50% real mixing 延迟 decompression 至 Gen 3+，controller 至少 Gen 5-7 才触发。这不是 bug 是 fundamental limitation。

**最容易判断错的事**：
1. Paper Agent 报告"已修复"不一定真的改了文件——必须要求 grep 验证输出作为证据
2. 双实例 VRAM 够不等于可行——compute 竞争导致 3.5-5x 降速（M007），不要再做
3. exp_005 的 k=20 不是论文主参数——论文用 k=10 (exp_006)
4. Phase 1 decompression 延迟：controller 在前 4-5 代不会触发（log_det 还在上升），这是预期行为不是 bug
5. DDL May 25，时间线：exp_004/006 ~May 19 完成 → linear_increasing ~May 20 → 论文写作 May 20-23 → 提交 May 24-25
6. paper_framing.md Claim 2 已修正：SLV 的价值是 "computationally cheap + monotonic + mechanistic"，不是 "temporally earlier than HellaSwag"


---
