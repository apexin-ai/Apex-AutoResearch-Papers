# director / loop_10.md

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_10.md`
- **Structured JSON:** [`bfb24f1b70e5a1531b34.json`](../../sessions/bf/bfb24f1b70e5a1531b34.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: max_messages
updated: '2026-05-26T11:59:15+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：10894:cuda:0-3 + 34685:cuda:0-3，共 8 张，不得用其他设备
- 34685 禁止同时跑 CKA 分析 + 训练（IO 互斥，之前导致 10-17× 减速危机）
- v2 代码是唯一合法版本——v1 数据已确认有 bug（D050/D052），不得混用 v1/v2 数据做 ANOVA
- 用户自行提交论文（D058），不要代提交
- Plan B (ordinal interaction) 已确认（D055/D058），不要回退到 Plan A (crossover)

### 2. 🖥️ 基础设施快照
- **10894**: connect.westd.seetacloud.com, root, /root/occsafe_vla, RTX PRO 6000 98GB ×4, 磁盘 63%
- **34685**: connect.westd.seetacloud.com, root, /root/occsafe_vla, RTX PRO 6000 98GB ×4, 磁盘 41%（⚠️ 之前 2%，需确认）
- Python: 两台均 conda base（aml-train 镜像），`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- HF cache: /root/autodl-tmp/.hf_cache（两台）
- Cron 监控已设置（eval 完成自动回调），具体 cron ID 需重新查

### 3. 📊 当前状态
**关键问题**：Agent 连续 3 次 rotation 后 idle 16h，eval 结果和 Cell 2/4 v2 训练可能未被启动。首要任务是 SSH 确认 10894 和 34685 实际进程状态。

预期中的实验状态（需验证）：
- 10894:0 — reverse_cutoff_s2_v2 训练中（ETA ~May 27 06:40）
- 10894:1/2/3 — 3 个 s3 eval（mvp_occ_s3_v2_eval / full_occ_ln_s3_v2_eval / ablation_occ_detach_s3_v2_eval）应该已完成（ETA 原为 May 26 12:10 UTC）。**eval 后应启动 3 个 v2 训练但 Agent idle 期间可能没启动**
- 34685:0/1/2/3 — vanilla_v2_s1, vanilla_v2_s2, detach_ln_s3, cutoff_25k_s1_v2（ETA May 27 05:30-06:00）

Registry 中 PREPARING 状态（~10 个）：包括 full_occ_ln_v2_s0, full_occ_ln_v2_s1, detach_ln_v2_s0 等 Cell 2/4 v2 补训。

### 4. 📋 待办
- **立即**：SSH 10894 确认 cuda:1/2/3 实际状态 → 如 eval 已完成且 GPU 空闲 → 立即启动 full_occ_ln_v2_s0(cuda:1) + full_occ_ln_v2_s1(cuda:2) + detach_ln_v2_s0(cuda:3)
- **立即**：如 eval 结果文件已生成 → 收集 CAR 数据录入 registry
- reverse_cutoff_s2_v2 完成(10894:0) → 启动 detach_ln_v2_s1 (Cell 4, seed=43)
- 34685 训练完成(~May 27 05:30-06:00) → 逐个 eval（vanilla_v2_s1_eval, vanilla_v2_s2_eval, detach_ln_s3_eval, cutoff_25k_s1_v2_eval）
- 全 v2 factorial n=3 齐全 → 确认性 2×2 ANOVA（Gradient × Norm）
- 用户确认后 → 启动 Paper Agent（Intro/Method/Related Work 可先写，Results 后补）

### 5. 🎯 战略上下文
**核心结论**：Plan B — OCC auxiliary loss 对 VLA 无益（ordinal interaction，ALL OCC ≤ Vanilla）。论文转为 analysis/negative-result contribution：BN×gradient flow factorial study。

**v2 factorial 设计**（2×2 + vanilla baseline）：
- Cell 1: Full OCC BN (Grad ON + BN) — CAR ~0.700, v2 n=2→3
- Cell 2: Full OCC LN (Grad ON + LN) — v1 only, v2 补训中
- Cell 3: Detach BN (Grad OFF + BN) — CAR 0.757, v2 n=3 ✅
- Cell 4: Detach LN (Grad OFF + LN) — v1 only, v2 补训中
- Vanilla — CAR 0.768, v2 n=1→3

Partial ANOVA (v2 Cell 1 vs 3): Hedges' g=-1.023（大效应），p=0.422（不显著，功效低），方向一致。

**易错点**：
- v1 机制证据（gradient collapse, CKA degradation）已被推翻为 bug 产物（D056/D057），不要引用
- 当前可用机制证据仅有梯度正交性 (cosine≈0)
- 论文 deadline CoRL May 29，全 v2 数据预计 May 27 齐全，时间很紧
- Agent idle 问题：连续多次 rotation 后未执行任务，新 session 第一件事必须 SSH 确认实际 GPU 状态


---
