# director / loop_2.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_2.md`
- **Structured JSON:** [`6199de3c851856cc320f.json`](../../sessions/61/6199de3c851856cc320f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-13T19:18:24+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westb-13313 的 cuda:0 和 cuda:1（2× RTX 5090 32GB）
- AutoDL 实例：pip install / git clone 前必须 `source /etc/network_turbo`
- HF 下载设 `HF_HUB_DISABLE_XET=1`，大模型优先 ModelScope
- 根分区 ~30GB，所有大文件放 `/root/autodl-tmp/`
- Episode-level labeling 策略已定（D011），不要回退到 1-step counterfactual 或 fork-based

### 2. 🖥️ 基础设施快照
- 服务器：westb-13313 (connect.westb.seetacloud.com)，用户 root
- 工作目录：/root/autodl-tmp/simgate-modular-routing
- Python/conda：未确认（上一轮 Agent 未汇报，需 SSH 探查）
- W&B/Git：未配置
- 活跃进程：research-prescreening-gpu0（cuda:0），research-boil-v3-gpu1（cuda:1，接近完成）
- 脚本已就绪：episode_level_collection.py / router_sft_train.py / rule_based_routing.py / collect_trajectories.py

### 3. 📊 当前状态
- **GPU0**: research-prescreening-gpu0 RUNNING — 8/25 tasks 完成，预计还需 ~5h
- **GPU1**: research-boil-v3-gpu1 ANALYZING — 17/20 episodes，~25min 完成
- Agent 刚收到 D011 指令（framing 调整 + death-aware labeling），正在处理
- Agent 队列中有 D011 执行指令（death-aware 后处理脚本修改 + plan-001b 准备）
- Reviewer 刚重置

### 4. 📋 待办
- Boil v3 完成（~25min）→ Agent 最终分析含 death 统计 → registry DONE → GPU1 加入预筛
- 预筛全部完成（~5h）→ Agent 汇总含 Δ_no_death + Signal_type 的完整表 → 选 task list for plan-001b
- Plan-001b task list 确定 → Agent 提交方案（含 task list + 预估 label 分布，要求 internal ≥15%）→ 审批
- Plan-001b 数据收集完成 → plan-002 (router SFT) + plan-004 (explicit vs implicit) 双卡并行
- 如果 internal-preferred tasks < 3 个 → Agent 报告 → 需要决策是否调整 labeling 策略

### 5. 🎯 战略上下文
**D011 核心发现**：Det 全部优势 = 纯 death avoidance。Non-death Δ(D-I) = -4.5 ~ -0.4（internal 略优）。13 tasks 一致确认。

**Framing 已调整**：从"学习路由"→"safety-efficiency tradeoff，router 做 death-risk detection"。Paper claim：selective routing 在 death-risk 时用 det（避免 -100），safe steps 保留 internal 优势。

**决策链**：D001(MVP) → D005(MVP PASS) → D008(1-step 失败) → D010(Plan C episode-level) → D011(death avoidance 发现，framing 调整)

**易错点**：
- SFT 标签全标 det 是预期行为（death episodes 主导），不是 bug。需要通过 task 选择（混合 death-prone + internal-preferred tasks）平衡
- plan-012 (death decomposition) 是论文核心证据，优先级实质上已升为 P0
- DDL 5/25（剩 12 天），critical path ~2.3 天实验 + ~3 天写作，余量极小
- Dream 审稿 best 4/6 / median 3/6 / worst 2/6，容错率低——C1 "selective > unconditional" 依赖 plan-003 结果


---
