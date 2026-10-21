# reviewer / loop_10.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_10.md`
- **Structured JSON:** [`b3336e29b43b720b0d57.json`](../../sessions/b3/b3336e29b43b720b0d57.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: max_wall_time
updated: '2026-05-15T18:36:09+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 cuda:0 和 cuda:1（bjb1-45299 两张 RTX PRO 6000）。GPU 隔离模式：`CUDA_VISIBLE_DEVICES=N` + `--device cuda:0` 映射物理 GPU N 到逻辑 cuda:0。
- 015b 命令里写 `--device cuda:0` 但实际跑在物理 GPU 1——这不是越界，是隔离映射。不要误判。
- 008e_v3_s2 是 **non-CIVO**（fixed_dt=1，CIVO 通路结构性不可能）。D053 已定稿。不要把它重新标回 CIVO positive。
- NVE 诊断使用 **35K+ 窗口**。25K 处的高 NVE 值（如 008e_v3_s1=1.93）不算入分类。

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-45299(root)，工作目录 `/root/autodl-tmp/event-gated-adaptive-horizon`
- Python：`/root/miniconda3/bin/python`（conda base 环境，非 venv）
- 激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/`
- 论文源码：`{workspace}/docs/paper/`（main.tex + sections/）
- 活跃进程：009d (PID 149708, GPU 0, 4156 MiB)。GPU 1 完全空闲（015b 已退出，0 MiB）。
- W&B：未配置（本项目不检查 W&B）。

### 3. 📊 当前状态
**刚完成**：015b 完成审查（PASS）。数据与独立 SSH 读取完全一致。D049 进一步夯实（frozen dt_emb → gradient starvation，非 CIVO）。论文 D053/D054 修正（7/8, AUROC=0.933）已在 abstract/intro/results/conclusion/methodology 一致应用。fig2_nve_trajectory.py 审查完毕（两个 warning 已报告）。

**Registry 状态**：
- exp_009d_baseline_walker_s0: RUNNING, cuda:0, ~128K/500K, 118K eval=480.6（健康）
- exp_015b_frozen_dt_emb: ANALYZING（应为 DONE，registry 未更新，metrics 停在 92K）
- exp_016_sgs_walker_s1: QUEUED（GPU 1 空闲但未启动——**已提醒 Director 两次**）

**等待**：Director 响应 GPU 1 空闲 + exp_016 启动指令。

### 4. 📋 待办
- exp_016_sgs 启动 → 核实命令中 CUDA_VISIBLE_DEVICES=1、SGS flag（reward_dt_emb_detach）是否正确、GPU 边界合规
- 009d 持续推进 → 每 ~30K 检查一次 eval 趋势，确认 baseline 稳定
- 015b registry 更新为 DONE → 验证最终 metrics（95K=238.4, 105K=204.2）和 conclusion 正确入库
- fig2 如果更新（加 35K+ 窗口标注）→ 重新审查图表
- exp_016 出结果 → 审查 SGS 是否阻断 CIVO（预期 NVE<1.5x）；如果 SGS 失败 → framing 分支决策审查

### 5. 🎯 战略上下文
- **核心因果链（D049 定稿）**：Trained dt_emb 是 sustained CIVO 的必要条件。Frozen → gradient starvation（非 CIVO）。Removed (dim=0) → 完全阻断。
- **NVE 诊断力（D054 定稿）**：task_b2@1.5x(35K+) 7/8 accuracy, AUROC=0.933。1 FP = 008e_v3_s2（non-CIVO late collapse，D053）。论文措辞已从"perfect detection"修正为"sensitive but not perfectly specific"。
- **易错点**：(1) 008e_v3_s2 的 NVE=3.78 超阈值但不是 CIVO——它用 fixed_dt=1，CIVO 通路不存在，崩溃签名完全不同（entropy 上升、actor_loss 翻正 vs CIVO 的 entropy 锁死、actor_loss 深负）。(2) fig2 缺少 35K+ 窗口视觉标注，审稿人可能质疑为何忽略 25K 处超阈值点。(3) 015b 的 55K NVE=1.45x 接近但低于 1.5x 阈值——不要误读为"almost CIVO"，完整轨迹显示它快速自修正到 <0.5x。
- **管线关键路径**：exp_016_sgs 是论文 method section 核心（SGS 阻断 CIVO）。它不启动 = 论文无方法贡献。DDL 2026-05-29，剩 14 天。


---
