---
loop: 2
reason: idle_timeout
updated: '2026-05-21T11:17:02+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd-28034 GPU 分配：用于 eval 任务（exp-003 ckpt eval 系列），具体 GPU 编号按 `get_project_resource_usage` 白名单
- westd-29046 GPU 分配：cuda:0 = exp-003-s2 训练，cuda:1 = exp-003 训练。不可交叉占用
- DDL：EMNLP 2026 ARR May 25 cycle，距提交仅 4 天
- exp-003 和 exp-003-s2 是仅存的两个 RUNNING 训练，不可 kill——它们提供论文最终数据点
- 所有 eval 必须用 `eval_unified_preset.py`（D027 统一基线），不能用旧的 `eval_pipeline.py`

### 2. 🖥️ 基础设施快照
- **westd-29046**（2× A100 96GB）：
  - 工作目录：/root/contrastive_entrain_calib/
  - Python：/root/miniconda3/bin/python（conda base）
  - exp-003 训练：PID 70649, cuda:1, ~step 5900+
  - exp-003-s2 训练：PID 237432, cuda:0, ~step 1749+
  - Checkpoint 输出：/root/autodl-tmp/checkpoints/exp003/, /root/autodl-tmp/checkpoints/exp003_s2/
- **westd-28034**（4× A100 32GB）：
  - 同样路径结构，用于 eval 任务
  - 模型缓存：/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B
  - 数据：/root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl（362 pairs）
  - Eval 结果目录：/root/contrastive_entrain_calib/results/exp003_d027_eval/
- **Cron 活跃**：exp-003 和 exp-003-s2 各一个 cron 监控进程存活 + 自动提交 ckpt eval

### 3. 📊 当前状态
**刚发生的事**：收到 exp-003-eval-ckpt4500 完成回调（ANALYZING 状态）。已 spawn Worker（worker_analysis_exp-003-eval-ckpt4500_20260520T190452）去 westd-28034 读取结果并更新 registry，**Worker 尚未回调**。

**Registry 状态**：
- RUNNING：exp-003（R3-only GRPO 训练）、exp-003-s2（R3-only seed 2 训练）
- ANALYZING：exp-003-eval-ckpt4500（Worker 正在分析）
- PREPARING（4个）：exp-003-eval-ckpt3000、exp-003-eval-ckpt2000、vanilla-d027-reeval、exp-009-eval-ckpt500
- DONE：34 个（success 17, negative 13, killed 4）

**等待中**：
- Worker 回调：worker_analysis_exp-003-eval-ckpt4500 → 拿到结果后更新 registry + 汇报 Director
- Cron 自动：exp-003 后续 ckpt（6000~8000）会自动触发 eval pipeline
- exp-003-s2 后续 ckpt eval 也由 cron 自动触发

### 4. 📋 待办（条件触发式）
- Worker worker_analysis_exp-003-eval-ckpt4500 回调 → 读取分析结果，确认 plateau onset 判定，汇报 Director（含 [资源] 行）；若 SYCONScore ≈ 0.114 → plateau 从 step 4000 开始（确认），论文 R3-only 轨迹图数据完整度 +1
- exp-003 ckpt-6000/6500/.../8000 eval cron 回调 → 逐个分析，重点关注 plateau 是否延续到训练结束
- exp-003-s2 ckpt eval cron 回调 → 与 seed 1 对应 ckpt 交叉对比，验证 reproducibility
- exp-003 训练完成（~ckpt-8000，ETA May 21 ~18:00）→ 最终 eval → Results section 数据定稿
- exp-003-s2 训练完成 → seed 2 完整轨迹 → error bars 计算 → 论文补充
- PREPARING 的 4 个实验：等 GPU 空闲或 Director 分配后提交（优先级：vanilla-d027-reeval > exp-003-eval-ckpt3000/2000 > exp-009-eval-ckpt500）
- Paper Agent Results section 写作完成 → Intro/Framework D041 patch → May 22 全文 polish

### 5. 🎯 战略上下文
**核心论文 narrative（Scheme C dual-layer）**：
- Layer 1：d_syc 方向能判别 sycophancy（AUROC 0.82+）但所有基于它的 reward formulation 均失败
- Layer 2：ALL GRPO RL 方法都失败（包括不用 d_syc 的 R3-only 也 plateau below vanilla 0.134）；唯一成功的是 SFT（exp-004 ACT, SYCONScore 0.301 = +126%）
- Three-layer distinction（D042）：d_syc = harmful collapse > R3-only = partial recovery then plateau > SFT = self-recovery

**关键决策链**：D039 统一 eval 基线 → D040 kill exp-009 → D041 dual-layer narrative → D042 three-layer distinction → D043 claim 强度 Medium → D044 DDL May 25

**易错点**：
- 不要混淆旧 eval（eval_pipeline.py）和新 eval（eval_unified_preset.py / D027）的数据——只有 D027 数据可用于论文
- exp-003 R3-only 的 plateau SYCONScore=0.114 低于 vanilla 0.134，这是 **negative**（RL 比不训练还差），不是 success
- exp-004 是 SFT 不是 RL——论文 narrative 依赖这个区分，不可搞混
- Claim 强度已降至 Medium（D043），不要在论文中用 strong claim 措辞
- exp-003-s2 seed 2 的已有 eval（ckpt-500/1000/1500）全部 negative，与 seed 1 趋势一致
