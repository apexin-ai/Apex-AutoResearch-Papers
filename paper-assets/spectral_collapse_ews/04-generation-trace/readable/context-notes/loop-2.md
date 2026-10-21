# director / loop_2.md

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_2.md`
- **Structured JSON:** [`73c0a38b62922f23379b.json`](../../sessions/73/73c0a38b62922f23379b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-17T16:59:58+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 cuda:0 / cuda:1（rtx6000-diagprobe，2× RTX PRO 6000 98GB）
- 服务器无外网：HF_HUB_OFFLINE=1, TRANSFORMERS_OFFLINE=1，所有模型/数据必须本地
- 所有实验启动必须用 submit_training_job（自动 tmux + sentinel），禁止裸 nohup（M005 教训：cron 误判 5 次）
- 同一实验的 cleanup 和 restart 不能并行派两个 worker（M004 教训：race condition 导致 checkpoint 被误删）
- 缺 PYTHONUNBUFFERED → stdout 缓冲延迟，查进度看 results 文件不是 log
- 论文主参数 k=10（D015），exp_005 用的 k=20 是 sensitivity 数据不是主实验

### 2. 🖥️ 基础设施快照
- 服务器：rtx6000-diagprobe (connect.westd.seetacloud.com)，账号 root
- 工作目录：/root/spectral_collapse_ews
- Python 路径：需 Agent 确认（之前未记录到 memory）
- 模型：410M GPT-2 style（本地），1B Pythia（本地）
- 数据：50K real samples + 合成生成，total_per_gen=50K
- 活跃进程：exp_001 和 exp_005 标记 RUNNING 但 GPU health 报告空闲——**刚派 Agent 去确认实际状态，可能已结束或崩溃**
- Cron：有实验监控 cron（自动检测 sentinel 变化）
- W&B：未配置

### 3. 📊 当前状态
**刚做完**：
- 更新 ROADMAP（D011-D015 全面同步）
- 派 Agent 综合任务：检查 exp_001/exp_005 实际进程状态 + 启动 exp_004/exp_006

**Registry 状态**：
- exp_001 RUNNING — Phase 0 410M Gen 10/10（最后一代，应接近完成）
- exp_005 RUNNING — Phase 1 adaptive k=20 s42（sensitivity 数据）
- exp_004 PREPARING — fixed_mix s42（launch script 已在 /root/spectral_collapse_ews/scripts/launch_exp_004.sh）
- exp_003 DONE(killed) — D011 bug 导致 adaptive ≡ fixed_mix
- exp_002 DONE(success) — 1B pilot

**等待中**：Agent 回复（刚派任务，idle 604s 后收到指令）

### 4. 📋 待办
- Agent 报告 exp_001 已完成 → 收集 Gen 0-10 metrics + HellaSwag Gen 9-10 + 启动 exp_004 (fixed_mix) on cuda:0
- Agent 报告 exp_001 崩溃 → 从 checkpoint 恢复或重启 Gen 10
- Agent 报告 exp_005 状态 → 如果到 Gen 3+，检查 ratio trajectory：ratio < 0.53 → 切 cumulative 模式重启(D014)；ratio > 0.55 → 继续 proportional
- cuda:0 空出 → 评估双实例可行性（19GB×2 vs 98GB），启动 exp_004 + exp_006(adaptive k=10) 并行
- Phase 1 核心对比出结果 → adaptive k=10 比 fixed_mix ≥3 ppl better (paired t-test p<0.1) → complete_mvp() 进入 research 阶段
- MVP pass 后 → 创建 paper_framing.md + experiment_plan.yaml + dream_simulate(review_mode="full") + post-mvp-kickoff skill

### 5. 🎯 战略上下文
**核心决策链**：D009(Phase 0 pass) → D010(signal→log_det) → D011(三层bug fix) → D012(k=1→20) → D013(claim pivot: EWS detection为主, controller为PoC) → D014(cumulative备选) → D015(论文k=20→10)

**信号衰减悖论**（最重要的理论发现）：比例控制器存在自稳定负反馈环——干预→collapse减缓→信号减弱→干预减少→collapse恢复。即使 k=50 ratio 也只在 0.50-0.60 小幅波动。这不是 bug 是 fundamental limitation，论文要把它写成 insight 而非缺陷。

**最容易判断错的事**：
1. k=20 的 exp_005 不是论文主实验——它是 sensitivity 数据。论文主实验用 k=10 (exp_006，还没启动)
2. Phase 0 Gen 0-5 有 decompression peak（log_det 高于 Gen 0），cumulative delta 在这段为 0。Phase 1 中混合抑制了 decompression，此问题不影响
3. report_actual 调用位置在 min() cap 之前（pipeline.py line 175 vs 199），功能上目前正确但脆弱，防御性修复待做
4. DDL 还剩 ~6 天（May 25），时间紧但 GPU 预算充裕（432h 总量），瓶颈在串行实验周期不是算力


---
