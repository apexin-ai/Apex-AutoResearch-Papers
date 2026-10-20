# agent / loop_1.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`3ae818cf997b67d733cb.json`](../../sessions/3a/3ae818cf997b67d733cb.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: idle_timeout
updated: '2026-05-13T18:33:23+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：只能用 westb-13313 上的 cuda:0 和 cuda:1（config gpu_ids）
- submit_on_allocated 命令必须自带环境激活：`source /root/miniconda3/bin/activate && ...`（aml-train 镜像用 conda，不存在 .venv）
- GPU 编号脚本内始终从 0 开始（`--gpu_id 0`），框架自动注入 CUDA_VISIBLE_DEVICES 映射物理卡
- mvp-p1-gpu0 的旧代码数据：always-internal/always-deterministic 有效，oracle 数据有 tie-break 偏差（D003/D004）。新代码 v3 数据干净
- DDL: EMNLP 2026 ARR short paper，2026-05-25（剩 12 天）

### 2. 🖥️ 基础设施快照
- 服务器：westb-13313，账号 root
- 工作目录：/root/autodl-tmp/simgate-modular-routing
- Python：/root/miniconda3/bin/python（conda base 环境）
- 模型：/root/autodl-tmp/models/Qwen/Qwen2___5-7B-Instruct/
- 数据：ScienceWorld API（实时交互，无静态数据集）
- 结果目录：/root/autodl-tmp/simgate-modular-routing/results/mvp/
- 日志目录：~/runs/simgate-modular-routing/
- W&B：CRON 提示 "W&B data available"，但 registry 里没有 wandb_run_id，Worker 分析中会提取
- 活跃进程：无（两个实验刚退出）
- Cron：reconcile 返回 0 active

### 3. 📊 当前状态
两个 Phase 1 实验刚完成（~15:15 UTC），都在 ANALYZING：

| exp_id | GPU | task types | 状态 |
|--------|-----|------------|------|
| mvp-p1-gpu1-v3 | cuda:1 | chemistry-mix-paint + grow-plant | ANALYZING，Worker 分析中 |
| mvp-p1-gpu0-vllm | cuda:0 | melt + change-state-of-matter | ANALYZING，Worker 分析中 |

等待中：
- **Worker 回调 ×2**：`worker_analysis_mvp-p1-gpu1-v3_20260513T151635` 和 `worker_analysis_mvp-p1-gpu0-vllm_20260513T151641`，它们正在 SSH 读日志提取 metrics
- 已向 Director 汇报"实验完成、分析中"，尚未汇报最终 metrics

历史数据点（旧代码 mvp-p1-gpu0）：boil 20ep → internal=-49.8, det=-19.7, oracle=-29.7（det 优于 internal 30.1 分）

### 4. 📋 待办
- 两个分析 Worker 回调到达 → 提取 5 个 task type 的 det vs internal 指标 → 按 MVP v3 标准判定（≥2/5 Pass，≥3/5 Conditional，<2/5 Fail）→ update_registry(conclusion=success/negative) → 刷新 report.md → 向 Director 汇报完整 MVP 判定
- MVP Pass → 进入 Research 阶段，统一代码重跑 strong tasks，开始论文 framing
- MVP Conditional Pass → 向 Director 汇报需收窄 claim，建议补跑 episodes 或换 task type
- MVP Fail → 按 red-section 产出 Framing 调整提案，禁止默默跑下一个实验
- 无论结果如何：两张 GPU 空闲，分析完成后立即安排下一批实验（GPU 空着 = 浪费）

### 5. 🎯 战略上下文
- 核心假设：确定性外部计算（环境模拟器）在规则驱动任务上优于纯 LLM 内部推理 → selective routing 有信号
- 早期发现（D004）：1-step lookahead 在稀疏 reward 下 95% 步骤 delta=0，oracle ≈ always-det 是预期行为。因此 primary metric 改为 det vs internal（不看 oracle）
- 决策链：D001(MVP 方案) → D002(Phase 0+1 修订) → D003(tie-break+death filter 修复) → D004(primary metric 改 det vs internal)
- 易错点：
  - 不要把旧代码 (mvp-p1-gpu0) 的 oracle 数据和新代码 v3 的 oracle 数据直接对比（tie-break 逻辑不同）
  - boil 的 30.1 分差距来自旧代码，新代码重跑可能不同
  - mvp-p1-signal (PREPARING) 是占位条目，实际拆成了 gpu0/gpu1 多个实验跑
  - GPU1 已重启 4 次（v1→vllm→v2→v3），前几次的 killed 记录是迭代过程不是事故


---
