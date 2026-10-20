# director / loop_6.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_6.md`
- **Structured JSON:** [`974a5ffeb4db85f40a9f.json`](../../sessions/97/974a5ffeb4db85f40a9f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_messages
updated: '2026-05-15T19:39:19+00:00'
---

### 1. 🔴 硬约束 / 红线
- 需要先通过 `get_project_status` 和 `load_project_config` 确认本项目当前分配的 GPU 设备号，不要假设任何 cuda 设备
- 项目已进入审稿阶段（review_chat_id: `oc_0b622d6038b969b96148ee8a163a1a0c`），研究侧继续推进实验，但不参与论文格式/投稿材料准备
- ideas.md 和 constraints.yaml 尚未创建（标记 ⚠️），首次使用时需初始化

### 2. 🖥️ 基础设施快照
- 本轮 session 未执行 SSH 探查，服务器/工作目录/Python 路径/模型路径等需要通过 `load_project_config(section="execution")` + `list_ssh_hosts` + `get_resource_inventory` 重新获取
- 活跃进程/tmux/cron 状态未知，需 BOOT 后立即查询

### 3. 📊 当前状态
- 本轮 session 38 条消息 / 3h18min，Main Agent 仅 2 条消息后 idle 180min 触发 RESET
- 未在本轮执行任何实验审批或方向决策
- 具体 registry 状态（RUNNING/PREPARING 实验）需通过 `director_get_project_overview` + `auto_build_report_facts` 刷新
- 无等待中的 Worker 回调或 Director 决策

### 4. 📋 待办
- BOOT 启动 → `get_project_status` + `director_get_project_overview` + `get_resource_inventory` 全面摸底
- 确认 GPU 分配 → 检查是否有空闲 GPU 未被占用，有则立即派实验
- 审稿报告到达 → 按 `review-report-action` skill 处理（Holistic Pass → Action Matrix）
- Main Agent 重置完成 → 根据项目状态派发下一批任务

### 5. 🎯 战略上下文
- 项目名 simgate-modular-routing，核心方向/claims 见 `paper_framing.md`，实验计划见 `experiment_plan.yaml`
- 已进入审稿阶段，研究侧应继续铺 ablation / 扩展实验，GPU 不能空等
- 本轮 session 实际产出很少（Main Agent 几乎未工作），下一个"你"需要重新评估项目全貌后立即推进
- 易错点：不要因为"审稿阶段"就停下实验——审稿期间 GPU 必须持续跑，这是 L1 红线


---
