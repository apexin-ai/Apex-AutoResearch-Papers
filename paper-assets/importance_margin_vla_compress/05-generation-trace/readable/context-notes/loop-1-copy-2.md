# agent / loop_1.md

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`7b92ed8594a87dd3405d.json`](../../sessions/7b/7b92ed8594a87dd3405d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: idle_timeout
updated: '2026-05-15T17:56:57+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：只能用 westd-27271 的 cuda:0 和 cuda:1，其他设备号禁止
- conda 环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，不要假设 .venv 存在
- 训练必须用 `submit_training_job`，禁止 nohup
- 脚本内 `--gpu 0` = 分配到的第一块卡（框架自动注入 CUDA_VISIBLE_DEVICES）

### 2. 🖥️ 基础设施快照
- 服务器：westd-27271，2× RTX PRO 6000 96GB
- 工作目录：/root/autodl-tmp/importance_margin_vla_compress
- Python：/root/miniconda3/bin/python（conda base 环境）
- 数据集：lerobot/aloha_sim_insertion_scripted_image（50 eps, 14D, 1 cam → 64 tokens, 20000 samples）
- 日志目录：~/runs/importance_margin_vla_compress/
- 配置目录：/root/autodl-tmp/importance_margin_vla_compress/configs/（baseline.yaml, imm_anchor.yaml）
- 活跃进程：mvp_imm_anchor_v2 (PID 26092, cuda:1, tmux 管理, cron 监控中)
- mvp_baseline_v2 进程已退出，cuda:0 空闲

### 3. 📊 当前状态
收到 mvp_baseline_v2 cron 回调（进程正常退出，ANALYZING）。已派 Worker `worker_analysis_mvp_baseline_v2_20260515T145527` 去 SSH 读日志 + 查 W&B 指标 + 检查 checkpoint，**Worker 尚未回调**。

Registry 状态：
- `mvp_baseline_v2` — ANALYZING，等 Worker 分析结果后转 DONE
- `mvp_imm_anchor_v2` — RUNNING (cuda:1, PID 26092)，训练中，有 cron 监控
- `mvp_baseline` / `mvp_imm_anchor` — DONE(failed)，第一轮因代码/环境问题失败，已修复后重跑为 v2

等待中：
1. Worker `analysis:mvp_baseline_v2` 回调 → 需要根据分析结果更新 registry、report.md、汇报 Director
2. mvp_imm_anchor_v2 cron 回调 → 同样流程分析 IMM 实验结果
3. 两个实验都完成后 → 对比 baseline vs IMM，评估 MVP gate criteria

### 4. 📋 待办
- Worker analysis:mvp_baseline_v2 回调 → 读 Worker 产出，更新 registry(conclusion/metrics/checkpoint_path)，更新 report.md；如果 baseline 成功则记录参考指标，等 IMM 实验完成后再一起评估 gate
- mvp_imm_anchor_v2 cron 回调（进程退出）→ 派 Worker 分析 IMM 实验日志+W&B → 更新 registry
- baseline + IMM 都完成 → 对比 gate criteria（Δ_k ≥2x, topk_preservation ≥10pp, success 不降 >5pp, L·ε/Δ_k ratio ↓≥30%）→ 汇报 Director PASS/FAIL
- 如果 MVP gate FAIL → 按 kill path 搜索 δ∈{0.1,0.3,0.5}, λ∈{0.1,0.5,1.0} 超参网格
- 如果 MVP gate PASS → 进入 research 阶段，扩展数据集/模型

### 5. 🎯 战略上下文
- 核心方向：IMM（Importance Margin Maximization）使 VLA visual token compression 在对抗扰动下保持 top-k 选择稳定性
- 第一轮 mvp_baseline + mvp_imm_anchor 都 failed（代码/环境问题），v2 是修复后的重跑
- mvp_baseline_v2 是纯 baseline（无 IMM），作用是建立 action loss 和 margin 指标的参考值
- mvp_imm_anchor_v2 是 IMM 训练（delta=0.3, lambda=0.5），需要与 baseline 对比来判断 IMM 是否有效
- 易错点：baseline 的 conclusion 判断标准是"训练正常完成且 loss 收敛"即为 success，不需要满足 gate criteria（gate criteria 是 baseline vs IMM 的对比标准）
- 决策链：D001(MVP方案) → D002(Reviewer warnings) → D003(gate量化) → D004(k=96条件) → D005(数据集换为aloha_sim_insertion)


---
