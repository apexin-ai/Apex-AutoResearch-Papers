# agent / loop_27.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_27.md`
- **Structured JSON:** [`3ceea4e5c6adf9e33e0f.json`](../../sessions/3c/3ceea4e5c6adf9e33e0f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 27
reason: idle_timeout
updated: '2026-05-28T22:50:44+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-51268 cuda:0 和 cuda:1，严禁使用其他 GPU
- bjb1-45299 宕机不可用，不要尝试连接
- 数据锁定 (D171) 生效中：所有实验数据和论文数值冻结，仅允许 prose polish + 格式调整，禁止修改任何数值/统计/表格/图表数据
- NVE CIVO 检测阈值 τ=2.0（D165），分析时用 2.0 不是 1.5
- exp_walker_008f_s0 和 exp_walker_no_dt_emb_s0 是不同 registry 条目但同一类实验（后者 killed），不要混淆
- Cheetah 008a 系列历史上多次 killed/failed（exp_095/096/098/099/102/103），当前命名为 exp_cheetah_008a_s0/s1，不要用旧命名
- `read_registry` 工具有缓存问题——exp_walker_no_dt_emb_s1 在工具中显示 RUNNING，但原始 YAML 已是 DONE/success。遇到状态不一致时以 registry.yaml 原始文件为准

### 2. 🖥️ 基础设施快照
- 服务器：westd-51268，2× RTX PRO 6000 Blackwell 96GB
- 工作目录：/root/autodl-tmp/event-gated-adaptive-horizon
- Python：/root/miniconda3/bin/python（conda base 环境，不是 venv）
- 环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- EGL 变量：MUJOCO_GL=egl, PYOPENGL_PLATFORM=egl, MUJOCO_EGL_DEVICE_ID={gpu_index}
- W&B：已配置
- 活跃进程：无（全部实验已完成）
- Cron：无活跃 cron（reconcile_crons 返回 0）

### 3. 📊 当前状态
Loop #27 session-start 完成。确认所有实验已结束，无 RUNNING/PREPARING：
- exp_cheetah_008a_s0: DONE/success, NVE=0.584 (C3 Cheetah s0 ✅)
- exp_walker_008f_s0: DONE/success, NVE=0.996 (C2 Walker no_dt_emb s0 ✅)
- exp_walker_no_dt_emb_s1: DONE/success, NVE=0.703 (C2 additional seed ✅)

已向 Director 汇报当前状态。无 Worker 运行，无 Director 决策待处理。
实验统计：208 个（103 success / 43 negative / 21 failed / 40 killed）。两块 GPU 空闲。

### 4. 📋 待办
- 用户决定 CoRL 2026 → 当前版本已就绪，确认提交流程
- 用户决定转 ICML/NeurIPS → Agent 已准备切换清单（ROADMAP 记录），执行 venue 切换
- Director 要求启动 Paper Agent 整合最终结果 → spawn worker 执行
- 若用户要求新实验（数据锁定后不应发生）→ push back，引用 D171

### 5. 🎯 战略上下文
- 核心发现：DreamerV3 的 trained dt_embedding 驱动 CIVO（Conditioning-Induced Value Overestimation），是 multi-joint locomotion 特异性现象。Frozen/removed dt_emb 可稳健阻止
- C2（causal control）和 C3（cross-env）证据链已闭合（D170）
- C6 已 CONFIRMED（4/4 deterministic mitigation）
- Hopper 结论：gate mechanism failure，不是 dt_emb-driven CIVO（D162）
- **关键阻塞**：Round 7 审稿指出 CoRL venue fit 是反复出现的 evidence 问题（Round 1/3/7），写作无法修复。切 ICML 可同时消除 W-MF2 + W-MF6 两个 desk-reject 条件。等待用户 venue 决策
- 论文 43 页（CoRL 格式，正文 8 页达标），venue-independent 修复全部完成并 Reviewer 验证通过
- 易错：CoRL DDL 是 5/28 12:00 UTC（北京时间 20:00），过期则 CoRL 选项自动失效


---
