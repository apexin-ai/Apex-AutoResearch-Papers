# agent / loop_8.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_8.md`
- **Structured JSON:** [`c09633dd0dd7d2453df9.json`](../../sessions/c0/c09633dd0dd7d2453df9.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: idle_timeout
updated: '2026-05-14T17:41:03+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：`cuda:0`, `cuda:1`（westb-13313）。绝对不用其他 GPU
- 唯一可用训练数据：`data/plan-004-implicit/implicit_sft.jsonl`（MD5: c9b59e04de78, 2040 samples）。`results/plan_c_test_labels/implicit_sft.jsonl` 标签损坏，禁止使用
- Checkpoint 路径：`checkpoints/plan-004-implicit/final_adapter` = ablation-b（正确）；`checkpoints/plan-002-generative-v1/final_adapter` = gen-v1（失败实验），两者 eval_routing_metrics 相似，极易混淆
- Table 1 数字只能来自 `eval_end_to_end.py`：trained-router=-10.70, always-det=-9.47, oracle=-6.58。`eval_implicit_router.py` 的 -12.84 不入表
- 所有 eval 脚本必须 `enable_thinking=False` + `re.sub` 清理 `&lt;think>` tags（Qwen3 thinking mode 干扰）
- 论文定位 = **analysis paper**（D046 撤销了 D041/D042 的 method paper pivot）。贡献 = empirical finding + diagnostic methodology，非 router 架构
- Worker 池当前 0（后端无可用账号），只能 main agent 自己做轻量操作

### 2. 🖥️ 基础设施快照
- 服务器：**westb-13313**，2× RTX 5090 32GB
- 工作目录：`/root/autodl-tmp/simgate-modular-routing`
- Python/conda：AutoDL 镜像，用 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- HF_HOME：`/root/autodl-tmp/.hf_cache`
- 网络：必须 `source /etc/network_turbo` + `HF_HUB_DISABLE_XET=1` + SSL cert env vars
- 活跃进程：`alfworld-counterfactual-full`（PID=alfworld_cf, tmux session, cuda:1）—— cron 监控中
- cuda:0 空闲（写作热备）
- Cron：1 个活跃（alfworld-counterfactual-full），reconcile 刚跑过

### 3. 📊 当前状态
**Registry**：54 DONE + 1 RUNNING + 3 PREPARING（后两者是历史残留，不活跃）

**正在跑**：`alfworld-counterfactual-full`——ALFWorld 全量 counterfactual 收集（135 games, 6 task types），D044 标记为 exploratory。进程存活，cron 监控正常。

**论文进度**：Paper Writing Sprint 阶段。核心实验全部完成。LaTeX 编译通过，正文 ≤4 页。页数压缩已完成（Discussion→Limitations 节, Labeling Quality→Appendix A, Table 2 per-task→Appendix B）。

**等待中**：
- alfworld-counterfactual-full cron 回调（完成后需分析结果 → 更新 Limitations 中 ALFWorld 占位符）
- Worker 池 = 0（后端无可用账号），无法 spawn worker

**Critical Path**：EMNLP 2026 ARR short paper DDL = **2026-05-25**（剩 11 天）。目标 5/17 初稿。

### 4. 📋 待办（条件触发式）
- alfworld-counterfactual-full cron 回调到达 → spawn worker 分析结果（death decomposition + per-task breakdown）→ 更新 registry → 将 ALFWorld 结果写入 Limitations/Discussion 占位符 → 向 Director 汇报
- Worker 池恢复（后端账号可用）→ 立即铺：(1) docs/paper 远程同步 + 重编译验证 (2) 98.2% tie rate 数值修正 (3) experiments_v2_patch + conclusion + abstract-sync 等写作任务
- 5/17 前 → 整合完整 LaTeX 初稿（需确认所有 section 已写完 + CI 数字已更新）
- Director 要求 review 迭代 → 按 5/17-22 窗口安排对抗迭代

### 5. 🎯 战略上下文
**核心结论**：Death avoidance 占 ~90% routing signal（DAF=90.41%, r=0.9698）。Router balanced_acc=58.1±0.8%（仅比随机高 8pp），near-random 本身就是 finding。Classification head 路线全部失败（D025），generative SFT ablation-b 是唯一非退化配置但 e2e 仍 negative（D035）。

**决策链关键节点**：
- D046：撤销 pivot，回归 analysis paper。MATH pilot 结果入 Discussion 即可，不扩全量
- D044：ALFWorld = exploratory（不是核心证据），MATH = 主要跨环境验证
- D039：Oracle circularity 不成立（0% tie-break），labeling quality confirmed
- D033：Framing 定稿 Option B（方法论贡献），router near-random IS the finding

**易错点**：
- 不要把 MATH counterfactual 的"反转信号"（internal 反而更好）当 bug——这是真实发现，支撑"router 的最优策略因环境而异"
- ALFWorld 结果无论正负都只入 Discussion/Limitations，不改核心 claim
- 论文是 analysis paper 不是 method paper，不要写成"我们提出了一个 router"
- 3 个 PREPARING 实验（plan-003-baseline, plan-001b-gpu1-rebalance, mvp-p1-signal）是历史残留，不需要推进


---
