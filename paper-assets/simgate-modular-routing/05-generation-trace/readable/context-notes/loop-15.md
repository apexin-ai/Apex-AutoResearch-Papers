# agent / loop_15.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_15.md`
- **Structured JSON:** [`e6e70f28d4f6e661c458.json`](../../sessions/e6/e6e70f28d4f6e661c458.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 15
reason: idle_timeout
updated: '2026-05-16T04:41:21+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：仅 `cuda:0` 和 `cuda:1`（westb-13313），禁止用其他设备
- r7n2 系列已 OOM 3 次：eval batch_size 必须 ≤2，脚本必须增量保存（每个 scale/seed 完成即写入）
- Episode-level eval 是唯一可信 eval，step-level eval 存在 data leakage（65/66 episodes 跨 train/val），不能用 step-level 数字做 claim
- 论文以 `docs/paper/` 为准（5/15 23:20），`artifacts/_project/paper/latex/` 是旧版，不要改错地方
- EMNLP 2026 DDL：**2026-05-25**，剩 9 天
- 启动 GPU 进程前必须 `nvidia-smi` 确认空闲 + `CUDA_VISIBLE_DEVICES` 隔离

### 2. 🖥️ 基础设施快照
- 服务器：**westb-13313**，工作目录 `/root/autodl-tmp/simgate-modular-routing`
- Python：aml-train 镜像，conda base 环境（`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- 模型：Qwen3-1.7B（router SFT），Qwen2.5-7B-Instruct（backbone/vLLM）
- 数据：`data/plan-004-implicit/implicit_sft.jsonl`（2040 steps, 66 episodes）
- 活跃进程：`r7n2-data-size-ablation-r3` PID=934738, cuda:0, command=`python src/r7n2_scale_study.py`
- Cron：r7n2-data-size-ablation-r3 活跃（reconcile 确认 job still running）
- GPU1：空闲（leave-one-tasktype-out 已完成）
- Worker 池：0 个运行中

### 3. 📊 当前状态
- **r7n2-data-size-ablation-r3**（RUNNING, cuda:0）：第三次重启（降 eval batch=2 + OOM 防护 + 增量保存）。进度：25pct×3seeds + 50pct_seed42 已完成。25pct episode-level balanced_acc=0.5（collapse，全预测 internal）。剩余：50pct×2 + 75pct×3 + 100pct×3 = 8 个 run
- **leave-one-tasktype-out**（DONE, negative）：7/11 task types 全 deterministic，4 个有两类，grand mean step-level 59.8%。不改变 episode-level 随机结论
- **majority-vote-baseline**（DONE, negative）：router 47.1% < always-det 50.0%，C2 最终定调
- Registry 总计：82 DONE + 1 RUNNING = 83 实验（success 32 / negative 18 / killed 18 / failed 14）
- 无待审批实验，无 pending Worker

### 4. 📋 待办（条件触发式）
- r7n2-data-size-ablation-r3 cron 回调到达 → spawn Worker 分析 episode-level 结果 → **D090 contingency**：任一 scale 3-seed mean balanced_acc > 0.55 且单调递增 → Outcome A（data scarcity narrative, 改写 §4.3）；各 scale 均 ≈50% → Outcome B（structural limitation, 当前 framing 不变）
- r7n2 完成 + narrative 选定 → spawn Worker 更新 Appendix router 部分
- GPU1 当前空闲 → 如有新实验需求可立即使用（但项目已接近终稿阶段，无新实验排队）
- Reviewer Round 8 一致性验证待启动 → 需用户审批（**BLOCKING**）
- Round 8 完成 → 迭代修复 → 终稿 → 5/24-25 ARR 提交

### 5. 🎯 战略上下文
- **核心结论链**：C1（DAF=90.41%, r=0.97）SOLID，独立于 router → C2 reframed（D089）：router episode-level 失败是 C1 的 corollary，降至 Appendix，诚实报 negative → C3（cross-model + MATH）SOLID
- **D090 是最后悬念**：r7n2 scaling study 决定 Appendix 叙事走 data scarcity 还是 structural limitation。25pct 已 collapse（0.50），如果后续 scale 也 ≈0.50 则 Outcome B（大概率，因为问题是 episode-level 泛化而非数据量）
- **最容易判断错的事**：不要把 step-level 数字（55.7%、59.8%）当真实 signal——episode-level 才算数。step-level 高是因为 data leakage
- **易踩坑**：r7n2 脚本极其脆弱（已崩 3 次），任何修改后必须 dry-run 验证；seeds 123/456 的 val set 100% deterministic（无 internal 样本），只有 seed=42 给出有信息量的 episode-level 评估
- **关键决策**：D083-D089 是一条连续 reframe 链（router 从 "works" → "step-level leak" → "episode-level random" → "below majority-vote" → "honest negative in Appendix"），Director 已全部批准，不要试图翻转


---
