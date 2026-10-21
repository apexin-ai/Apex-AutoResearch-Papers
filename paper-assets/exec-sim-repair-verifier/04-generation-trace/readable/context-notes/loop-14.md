# director / loop_14.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_14.md`
- **Structured JSON:** [`a1da8ab8218a32c44e5c.json`](../../sessions/a1/a1da8ab8218a32c44e5c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 14
reason: max_messages
updated: '2026-05-15T16:41:28+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 分配须严格遵守 `execution.gpu_ids` 白名单，当前项目用 `get_project_status` 确认可用卡号再派任务
- 论文已进入审稿阶段（review_chat_id: `oc_0ae20ec1ce60f9c0589d629648584eff`），格式/投稿材料由 Group C 负责，Research Director 不介入
- rank ablation 不升级为独立 claim（前轮审稿已决策），仅作 supplementary evidence

### 2. 🖥️ 基础设施快照
- 本地 workspace: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/`
- 论文源码: `docs/paper/` 下 `.tex` 文件，最近 commit `ab4698f` 修正了 Qwen3 citation key
- 远程服务器/GPU/conda 等信息需通过 `get_project_status` + `get_resource_inventory` + `load_project_config` 获取，本轮未深入探查
- 活跃进程: 无 RUNNING 实验（Agent idle 27s，队列空）

### 3. 📊 当前状态
- 刚处理完 Reviewer 对 rank ablation 可视化的审查报告：**PASS**，3 个 info 级建议
- 可操作项：baseline (r16 α32) 的 F1/EM 在 LaTeX 表格中为 "---"，可从 cwm-baseline seed=42 实验补全（非阻塞，优先级低）
- Agent 队列空闲，无 RUNNING/PREPARING 实验
- Reviewer 刚被 RESET（连续 4 次 RESET_REVIEWER 后最终 RESET_BOTH 生效）

### 4. 📋 待办
- 接手后 → `get_project_status` + `director_get_project_overview` 刷新全局状态
- 如需补全 baseline F1/EM → 派 Agent 从 cwm-baseline seed=42 结果中提取，更新 LaTeX 表格
- 审稿报告回传时（`[审稿报告]` 前缀）→ 严格按报告末尾强制处理协议执行，先 Holistic Pass 再逐条 Action Matrix
- GPU 空闲时 → 检查 `experiment_plan.yaml` 是否有待跑实验，保持 GPU 不空转

### 5. 🎯 战略上下文
- 项目处于审稿阶段，实验主体已完成，当前重点是响应审稿反馈 + 补充 evidence
- 论文 framing 详见 `paper_framing.md`，实验计划见 `experiment_plan.yaml`，决策链见 `decisions.yaml`
- 易错点：收到审稿报告不能"已知悉"式回复，必须走 `review-report-action` skill 的完整流程
- Reviewer 刚重置，新 Reviewer session 启动后会自动初始化，不需要手动干预


---
