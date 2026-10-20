# agent / loop_2.md

**redundancy compound sparsity 2** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_2.md`
- **Structured JSON:** [`fb4d6f2c36de44ccdd64.json`](../../sessions/fb/fb4d6f2c36de44ccdd64.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: idle_timeout
updated: '2026-05-12T17:30:17+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0, cuda:1 @ westd-16980，禁止用其他设备
- **gamma_sweep 是 FINAL GATE（D008）**：任一 gamma beat random ≥5% → continue；全部 fail → archive 整个项目。Gate 结果出来前禁止启动 Phase 1-5 实验
- inverted_ema_reasoning_v2 已被 Director 指令取消（D007），registry 仍为 PREPARING，需改 CANCELLED
- 10/10 实验全 negative，**禁止写 paper**，等 Director continue/archive 决策
- KeyDiff 用 pairwise O(B²) similarity，**不是** centroid comparison——不能作为 "centroid-based eviction 可行" 的证据（ROADMAP 已标注，不要回退）

### 2. 🖥️ 基础设施快照
- 服务器：westd-16980，2×RTX PRO 6000 96GB（cuda:0, cuda:1）
- 工作目录：`/root/carc/`
- Python：`/root/miniconda3/bin/python`（conda base 环境，`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- 模型：`/root/carc/models/DeepSeek-R1-Distill-Qwen-14B`
- 结果目录：`/root/carc/results/`（各实验 JSON 结果文件）
- 数据：WikiText-2（parquet cache）、MATH-500 embedded problems（脚本内置）
- 活跃进程：
  - `analysis_gamma_sweep` PID 40063, tmux session, GPU 0, 日志 `/root/carc/analysis_gamma_sweep.log`
  - GPU 1 空闲（待 analysis_heatmap 提交）
- Cron：reconcile 返回 0 条活跃 cron（gamma_sweep 可能无 cron 监控，需检查）

### 3. 📊 当前状态
**刚做完**：前 session 处理了 inverted_ema 双向证伪（D006→D007），更新 ROADMAP 为 final gate 状态。

**Registry 活跃实验**：
- `analysis_gamma_sweep` — RUNNING, GPU 0, 测试 8 个 gamma 值，已完成 gamma=0.1（PPL 8.17, 比 random 差 7%）。D003 数据预示高 gamma 也不乐观（ema_0.9 vs random 仅差 1.77%）
- `analysis_heatmap` — PREPARING（per-layer EMA 可视化，无论 continue/archive 都有用）
- `inverted_ema_reasoning_v2` — PREPARING（应标记 CANCELLED）
- `carc_generate_rope_test` — PREPARING（遗留，状态不明）

**运行中 Worker**：
- `worker_code_analysis_heatmap_20260512T172509` — 写 heatmap 代码
- `worker_research_keydiff_details_20260512T172753` — 调研 KeyDiff 细节

**等待中**：两个 Worker 的 `[WORKER DONE]` 回调

### 4. 📋 待办（条件触发式）
- gamma_sweep cron 回调 / 手动检查完成 → spawn worker 读结果 JSON → 判定 gate（任一 gamma beat random ≥5% → 向 Director 汇报 continue；全 fail → 汇报 archive）
- `worker_code_analysis_heatmap` 完成 → review 代码 → `submit_training_job` 到 GPU 1
- `worker_research_keydiff_details` 完成 → 更新 literature_map.yaml 中 KeyDiff 描述
- **立即**：将 `inverted_ema_reasoning_v2` registry 状态改为 CANCELLED
- **⚠️ gamma_sweep 无活跃 cron**（reconcile 返回 0）→ 需手动检查是否有 cron 在监控，若无则注册一个或安排 Worker 轮询

### 5. 🎯 战略上下文
**核心结论链**：D001（cross-axis MVP）→ D002（MVP FAIL, pivot to O(1) eviction）→ D003（sanity FAIL）→ D004（允许最后部署尝试）→ D005（EMA ≈ noisy recency）→ D006（pivot to inverted EMA）→ D007（inverted doubly negated）→ D008（gamma_sweep = final gate）

**关键数字**：recency baseline 仅比 full cache 差 0.09%（WikiText-2 32K），signal-based eviction 的天花板极低。EMA 双向证伪：evict-low ≈ random，evict-high 比 random 差 15%。

**易错点**：
- gamma_sweep 可能无 cron 监控（前 session 可能因 context limit 未注册），下一个 session 必须第一时间确认
- gamma_sweep 日志可能混入其他进程 OOM traceback（共享终端），分析时检查 PID 归属
- 不要把 D003 的 4K 结果和 D005 的 32K 结果混为一谈——context length 不同，PPL 数值不可直接比较
- 项目目标是 EMNLP 2026 ARR（DDL 2026-05-25），但 10 连 negative 下大概率 archive，不要提前写论文


---
