# director / loop_5.md

**collapse aware mixing** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_5.md`
- **Structured JSON:** [`4afb81710c7d0ce91ce2.json`](../../sessions/4a/4afb81710c7d0ce91ce2.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_messages
updated: '2026-05-14T03:53:41+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只有 1 张 GPU：cqa1-38874 的 cuda:0（RTX PRO 6000）。没有其他卡。
- MVP 已判定 FAIL（D018），三条路径全封。**不要试图继续验证原假设或启动 post-MVP 研究规划**。
- 当前状态是**等待用户决策**：Q2（negative result paper → EMNLP Findings）或 archive。用户未回复前不要自行决定方向。
- ideas.md 中的 P0 实验（cross-scale、fixed ratio baselines、PI sweep 等）全部是为 post-MVP 准备的，MVP FAIL 后这些**不适用于当前状态**——除非用户选择 Q2 路线后需要 multi-seed/multi-scale 补充实验。

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-38874（connect.cqa1.seetacloud.com），1× RTX PRO 6000
- 工作目录：/root/collapse-aware-mixing
- Python：/root/miniconda3/bin/python（conda base 环境，不是 venv）
- 激活方式：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- HF_HOME：/root/autodl-tmp/.hf_cache
- 模型：Pythia-1B（HF 缓存）
- 数据集：wikitext-103（本地）
- flash-attn 不可用（A6000 编译失败），用 sdpa
- 环境初始化脚本：/root/collapse-aware-mixing/env_init.sh
- 活跃进程：mvp_seed0_replication_r2 可能在跑（registry 显示 RUNNING），但无 PID/tmux 信息——接手后需 SSH 确认
- Cron：无活跃项目 cron

### 3. 📊 当前状态
**刚做完**：D018 MVP 最终判定 FAIL。三条路径总结已写入 ROADMAP 和 decisions.yaml。已通知用户两个选项（Q2 negative result 或 archive），等待用户决策。

**Registry 状态**：
- mvp_seed0_replication_r2：RUNNING — seed=0 复验 holdout eff_rank 上升现象。这个实验在 D018 之前就启动了，**结果无论如何不改变 MVP FAIL 判定**（因为 Pivot B 失败原因是 generated eff_rank 噪声高 573 倍、无时间优势，与 seed 无关）。但如果用户选 Q2，multi-seed 数据可以直接用。
- mvp_pilot_v8 / v8_r2：PREPARING — 这两个在 D018 之前规划，现在意义不明，可能需要清理。
- mvp_pilot_v2 / v3：PREPARING (failed) — 早期失败实验的残留状态。

**等待中**：
- 等用户回复 Q2 or archive 决策
- mvp_seed0_replication_r2 完成回调（如果还在跑）

### 4. 📋 待办（条件触发式）
- 用户选 Q2（negative result paper）→ 确认 multi-seed + multi-scale 补充实验方案（~3-4 天 GPU），启动 post-mvp-kickoff 流程写 paper_framing.md（重新定位为 negative result），规划 Pythia-410M/2.8B 验证实验
- 用户选 archive → 调用 `archive_project("collapse-aware-mixing", reason="MVP FAIL, 用户决定归档")`
- mvp_seed0_replication_r2 完成回调 → 记录结果到 memory.md，如果用户已选 Q2 则作为 multi-seed 数据点之一
- 用户问"能不能救" → D015 已评估过：Q1 (multi-signal framework) 只够 Findings/workshop，不建议；唯一有价值的方向是 Q2 negative result

### 5. 🎯 战略上下文
**核心结论链**：
- D001→D008：MVP 设计（Pythia-1B, wikitext-103, 20M tokens/gen, 3 代迭代）
- D011→D014：C1 原假设 falsified — holdout eff_rank 在 collapse 中反向上升 +0.96%，与 collapse 完全解耦
- D012→D016→D018：Pivot B 从 GO 到最终 FAIL — 初始 3-checkpoint 对比误判为 GO（D016），全 18 checkpoint 公平对比推翻（D018）：generated eff_rank 与 n-gram entropy 同时检测，噪声高 573 倍
- D015：Q2 negative result paper 是唯一有投稿价值的保底方案

**最容易判断错的事**：
1. **不要被 ideas.md 里的 P0 实验列表误导**——那些是 MVP 通过后的规划，现在不适用
2. **不要试图 "救" 原假设**——D018 的 573 倍噪声差距是 definitive，细粒度 checkpoint 不会改变结论
3. **mvp_seed0_replication_r2 不是 "正在推进的实验"**——它是 D018 之前启动的遗留任务，结果只在 Q2 路线下有边际价值
4. **Pivot B 存活条件（memory 中记录）已确认不满足**——D013 提出的三个条件 (a)(b)(c) 全部 FAIL
5. **paper_framing.md 存在但内容是 MVP 前写的原始 framing**（spectral leading indicator → PI controller），如果走 Q2 需要完全重写为 negative result narrative


---
