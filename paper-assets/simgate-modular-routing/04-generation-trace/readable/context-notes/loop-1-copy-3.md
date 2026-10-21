# reviewer / loop_1.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`ba225b1f2e086c227e87.json`](../../sessions/ba/ba225b1f2e086c227e87.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-13T19:18:41+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0 和 cuda:1（westb-13313 只有 2 张 RTX 5090 32GB）
- SSH 只能用 `westb-13313` host（`autodl-simgate` 的 SSH key 不存在，连不上）
- Reviewer 角色是**只读**——不执行实验、不修改文件、不写代码。唯一输出渠道是 `reviewer_post_to_director`
- plan-011 keyword list 已 pre-register 在 `src/rule_based_keywords.json`，实验开始后禁止修改（防 p-hacking）
- Boil v3 数据是 v3 代码产出；MVP boil 是旧代码（>= tie-break + 全模式 death filter），两者不能直接混用

### 2. 🖥️ 基础设施快照
- 服务器：connect.westb.seetacloud.com:13313 (root)，2× RTX 5090 32GB
- 工作目录：`/root/autodl-tmp/simgate-modular-routing`
- Python：conda base (`/root/miniconda3/bin/python`)，vLLM 0.18.1 + torch 2.10.0（已 patch TritonTemplate duplicate bug）
- 模型：`/root/autodl-tmp/models/Qwen/Qwen2___5-7B-Instruct/`（agent backbone）；router 用 Qwen3-1.7B（plan-002 时下载）
- 数据盘：`/root/autodl-tmp/` 250GB，已用 15GB
- 活跃进程：GPU0 预筛 PID 649681（9/25 tasks done）；GPU1 **空闲**（boil v3 已完成）
- 已就绪脚本：`src/episode_level_collection.py`, `src/collect_trajectories.py`, `src/router_sft_train.py`, `src/rule_based_routing.py`, `src/death_aware_labeling.py`, `src/signal_prescreening.py`

### 3. 📊 当前状态
**我是 Reviewer，刚完成以下审查链：**
- MVP Phase 1 PASS（4/5 significant，det-int +30-40）→ D005
- Dream 审稿（best 4/6, median 3/6, worst 2/6）→ tool-use 定位 + rule-based baseline + death decomposition 修入 plan
- 1-step tie rate 98.2% CRITICAL → D008，1-step labeling 废弃
- Action divergence 73% + fork cost 78h → D010，Plan C (episode-level labeling) 采用
- Death decomposition：non-death Δ(D-I) 为负（-0.4 to -4.5）→ det 全部优势来自 death avoidance
- MVP post-process：750 SFT triples 100% det labels，0% internal → CRITICAL posted
- find-non-living-thing：唯一 internal-preferred task，但仅 1/5 episodes internal wins（30 steps）

**Registry 活跃：**
- `research-prescreening-gpu0` RUNNING（9/25 tasks，~6h 剩余）
- `research-boil-v3-gpu1` 刚完成（ANALYZING），20 eps done：internal -44.7, det -9.3, oracle +3.8
- `mvp-p1-gpu1-v3` 仍卡在 ANALYZING（Agent 一直没更新为 DONE）

### 4. 📋 待办（条件触发式）
- GPU1 空闲 + Agent 派任务 → 审查是否在 gpu_ids 白名单内，检查 CUDA_VISIBLE_DEVICES
- 预筛完成（25/25）→ 审查 signal type 分布，**重点看 internal-preferred tasks 数量**。如果 < 3 个，internal labels 严重不足，router 将退化为 always-det，需要 post to Director
- plan-001b 启动 → 审查 task list 是否包含 internal-preferred tasks（必须包含！否则 100% det labels）
- plan-001b 完成 → 审查 label 分布。Internal labels < 15% → severity critical
- Boil v3 registry 更新 → 核实 metrics 与日志一致（internal -44.7, det -9.3, oracle +3.8）；与 MVP boil 对比注意代码版本差异
- Any roadmap_updated → 读 ROADMAP + experiment_plan，审查方向合理性
- Any paper/chapter 审查请求 → 按 section 5 章节审查流程，含合规检查

### 5. 🎯 战略上下文
**决策链**：D001(MVP 方案) → D002(Reviewer 修订) → D003(tie-break fix) → D004(primary metric 改 det-int) → D005(MVP PASS) → D006(W1-W5 修订) → D007(Dream 处理) → D008(1-step labeling 废弃) → D009(pilot+全量两阶段) → D010(Plan C episode-level)

**最容易判断错的事**：
1. **不要被 "4/5 significant" 的 MVP 结果迷惑**——这个信号 100% 来自 death avoidance。Non-death delta 是负的。Selective routing 的增量价值极小（0.4-4.5 分），plan-003 是生死判决。
2. **Plan C label 不平衡是结构性的**，不是 bug——death-risk tasks 天然产出 100% det labels。唯一的 internal label 来源是 non-death / internal-preferred tasks。如果预筛只找到 1 个 internal-preferred task (find-non-living-thing)，router 训练数据将极度不平衡。**这是当前最大风险。**
3. **Oracle > det 的 gap (+10-17) 不能直接用作 "selective routing 有价值" 的证据**——oracle 在 sparse reward 下有已知退化（>tie-break 偏向 always-det），oracle 数据只能作为 supplementary。
4. **melt 和 change-state-of-matter-of 共享相同 environment variations**——论文中不能作为独立 task types 报告，应合并为 "state-change tasks"。
5. **ROADMAP GPU 类型已更正为 RTX 5090 32GB**（不是之前的 RTX PRO 6000 96GB），但 GPU 预算单位是 RTX 5090 wall-clock hours。


---
