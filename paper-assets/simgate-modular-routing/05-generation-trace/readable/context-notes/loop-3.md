# director / loop_3.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_3.md`
- **Structured JSON:** [`80849343b9bfdd5cfff5.json`](../../sessions/80/80849343b9bfdd5cfff5.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_messages
updated: '2026-05-14T03:41:43+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westb-13313 的 cuda:0 和 cuda:1（2× RTX 5090 32GB），不得使用其他服务器/GPU
- plan-001b 数据收集必须加 `--reuse_dirs` 防止 episodes.jsonl 重复（memory.md 有详细说明）
- 禁止 Worker 用 `kill_job` 回收正在运行的实验，禁止 `pkill -f` 宽泛 pattern（两次 SIGHUP 误杀的教训）
- C1 claim 已锁定 Tier B (D017)："Death avoidance ~99% 主导，non-death deltas small and inconsistent"——不要升到 Tier A "唯一机制"
- plan-011 (rule-based keywords) 已关闭，结论是 keyword heuristic 结构性失效，不再设计新 heuristic
- 判断进程存活用 `ps -p PID`，不能依赖 nvidia-smi（ScienceWorld agent GPU 利用率 bursty，长时间 0% 是正常的）

### 2. 🖥️ 基础设施快照
- 服务器：westb-13313 (connect.westb.seetacloud.com)，账户 root
- 工作目录：/root/autodl-tmp/simgate-modular-routing
- Python：conda 环境（aml-train 镜像），`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- GPU：2× RTX 5090 32GB (cuda:0, cuda:1)
- 关键脚本：episode_level_collection.py（数据收集）、death_decomposition.py（519行，就绪）、post_collection_analysis.sh、launch_plan002.sh (cuda:0)、launch_plan004b.sh (cuda:1)
- W&B：未配置；弹性 GPU：未启用
- 活跃进程：plan-001b-gpu0-v5 RUNNING（measure-melting-point 20eps + lifespan-longest-lived 补 ep19）
- Agent 队列：空，idle 1706s

### 3. 📊 当前状态
**刚做完**：D017 决策（C1 claim Tier B）、文献扫描（novelty confirmed，12篇无 direct competitor）、plan-012 预分析（30 tasks, r=0.989 确认核心假设）、find-non-living-thing 追加收集完成（40 eps，唯一 0% 死亡率 task）

**RUNNING**：plan-001b-gpu0-v5（GPU0，收集最后 2 tasks 数据）

**PENDING**：
- plan-001b-gpu1-freeze-chem：GPU1 应接管 freeze + chemistry-mix 各 20 eps（准备中）
- plan-001b-gpu1-rebalance：GPU 负载均衡方案（准备中）
- research-cf-pilot-gpu1：早期 pilot，等待审批但可能已过时（Plan C episode-level 已替代 fork-based）

**等待中**：Agent idle，无活跃 Worker，GPU1 可能空闲——下一个"你"第一件事检查 GPU1 是否在跑，没跑就立即派任务

### 4. 📋 待办（条件触发式）
- plan-001b-gpu0-v5 完成 → 检查数据完整性（所有 task 20 eps/modality）→ 如果全量就绪，启动 plan-012 death decomposition 全量分析
- GPU1 空闲 → 立即派 plan-001b-gpu1-freeze-chem 或 rebalance 任务，禁止空卡
- plan-001b 全部完成 → plan-012 (death decomposition, P0-CORE, 0 GPU) + plan-002 (router SFT, cuda:0, 8h) + plan-004 (explicit vs implicit, cuda:1, 12h) 可并行
- plan-012 结果出来 → 验证 D015 预分析结论是否在全量数据上 hold（r≥0.95 继续，否则评估 framing）
- Agent 提交 plan-001b revised 方案 → 审批时确认关联 plan-id + 数据 reuse 策略
- 审稿报告从 Group C 回来 → 读 review-report-action.skill.md，走 Holistic Pass + Per-Comment Action Matrix

### 5. 🎯 战略上下文
**核心结论链**：D005 (MVP PASS) → D008 (1-step labeling 失败, tie 98.2%) → D010 (Plan C episode-level) → D013 (framing pivot: death avoidance = ~99% routing signal) → D015 (30 tasks 预分析 r=0.989 确认) → D017 (C1 Tier B 锁定)

**论文 story (v3)**：LLM agent routing 的 routing signal 几乎完全来自 death avoidance（避免灾难性 -100 惩罚），non-death 场景下两种 modality 近似等效。贡献 = empirical finding + counterfactual methodology，不是 router 架构。

**投稿目标**：EMNLP 2026 ARR short paper (4 pages)，DDL 2026-05-25（剩 11 天）。关键路径：prescreening 收尾(~1h) → 001b 数据(~20h 双卡) → 012 分析(0h GPU) → 002+004 并行(~12h) → 写作(~3天) = 紧但可行。

**最容易判断错的事**：
1. research-cf-pilot-gpu1 是早期 fork-based pilot（D009），Plan C 已替代——不要按它的方案审批，可能需要清理
2. plan-004b 依赖 plan-002 Step 1 的 death_aware_labeling.py 输出，不能完全与 plan-002 并行
3. find-non-living-thing 是唯一 internal-preferred task（0% 死亡率），是 C1 claim 的关键 counter-example——Tier B claim 已 accommodate 它，不要忽略
4. 审稿阶段已启动（Group C review_chat_id 存在），但研究实验继续推进，不要因为在审稿就停实验


---
