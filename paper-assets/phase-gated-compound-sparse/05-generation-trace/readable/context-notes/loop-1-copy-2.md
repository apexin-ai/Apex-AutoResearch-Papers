# agent / loop_1.md

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`8a2cb1ab470c8c2b4004.json`](../../sessions/8a/8a2cb1ab470c8c2b4004.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: idle_timeout
updated: '2026-05-13T23:01:19+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单: westd-22162 cuda:0, cuda:1, cuda:2, cuda:3（4× H20-NVLink 96GB，非 RTX 6000 Pro——ROADMAP 标题未更新但 D005 已确认换卡）
- GPU 编号始终从 0 开始（框架自动注入 CUDA_VISIBLE_DEVICES）
- westd-22162 用 conda base 环境，不是 venv：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型路径固定 `/root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B`，不要改
- EMNLP 2026 ARR 截稿 **2026-05-25**（距今 12 天），所有决策以此为锚

### 2. 🖥️ 基础设施快照
- 服务器: westd-22162，4× H20-NVLink 96GB
- 工作目录: `/root/autodl-tmp/pacs/`
- Python: `/root/miniconda3/bin/python`（conda base）
- 模型: `/root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B`（28 layers, 28 heads, 4 KV heads, hidden 3584）
- 数据: `/root/autodl-tmp/pacs/data/math500.json`（分层 5×10=50, seed=42）
- Profiling 输出: `/root/autodl-tmp/pacs/profiling_output/`
- 日志: `~/runs/phase-gated-compound-sparse/mvp_interaction_index_profiling.log`
- 活跃进程: 无（实验已退出，PID 7436 已完成）
- Cron: reconcile 后无活跃 cron

### 3. 📊 当前状态
MVP M1 实验 `mvp_interaction_index_profiling` 刚完成（0.54h），状态 ANALYZING。

**我做了什么：**
1. Session 初始化（read_registry + reconcile_crons + report.md + ROADMAP）
2. 派 Worker 1 分析实验结果（读日志+profiling_output、提取 II 数值、判断 pass/fail）— `worker_analysis_mvp_interaction_index_profiling_20260513T195650`
3. 派 Worker 2 预检 M2/M4 代码就绪度 — `worker_research_m2_m4_code_readiness_20260513T195814`
4. 向 Director 汇报实验完成，说明下一步 pass/fail 分叉

**等待中：**
- 两个 Worker 均未回调，结果未知
- Director 无待决策项（等 MVP 结论后再决策）

### 4. 📋 待办
- Worker 1（分析）回调 → 读取 artifacts/mvp_ii_analysis.md → 提取 conclusion（pass/fail）→ update_registry(status=DONE, conclusion=...) → 刷新 report.md
- MVP pass → 立即铺 M2（per-phase grid search, 4 GPU ~8h）+ M4（kernel integration, 2 GPU, 可与 M2 并行）→ 向 Director 汇报并申请审批
- MVP fail → 按 red-section skill 产出 Framing 调整提案（Pivot A: phase-agnostic compound vs single-axis / Pivot B: empirical characterization）→ 向 Director 汇报，**禁止默默跑下一个实验**
- Worker 2（代码就绪度）回调 → 读取 artifacts/m2_m4_code_readiness.md → 了解需要补什么代码，提前派 Worker 写代码
- 4 GPU 全部空闲 → MVP 结论出来前合理等待，结论出来后必须立即全部用上

### 5. 🎯 战略上下文
- 项目核心: PACS — learned compound controller 联合协调 attention sparsity + KV cache retention，以推理阶段为条件。Novelty 锚点是 **phase-dependent interaction direction reversal**（不同 phase 的 II 符号/幅度不同）
- MVP pass 标准（OR）：任一 phase 对 II 95% CI 不重叠 ∨ 符号反转。这是整个项目的 go/no-go gate
- D005 确认 GPU 实际为 H20-NVLink（非 RTX 6000 Pro），D006 确认架构为 Blackwell sm_100+。MVP profiling 不受影响，但 M4 kernel 需注意 sm_100 兼容性
- Throughput 策略：开发/accuracy 用当前 H20，最终 throughput benchmark 短租 H100（M5 阶段申请）
- 关键路径：M1→M2→M3→M5→M5+→M6b→论文。M4∥M2，M6a∥M5
- 易踩坑：ROADMAP 写的"RTX 6000 Pro"已过时（实际是 H20），不要被误导。submit_on_allocated 命令必须自带 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`


---
