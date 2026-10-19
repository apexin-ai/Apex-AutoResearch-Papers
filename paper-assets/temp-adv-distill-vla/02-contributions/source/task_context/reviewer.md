---
loop: 1
reason: max_wall_time
updated: '2026-05-15T09:55:51+00:00'
---

### 1. 🔴 硬约束 / 红线
- 训练进程只用 cuda:1（通过 `CUDA_VISIBLE_DEVICES=1 --device cuda:0` 映射）。之前所有实验均遵守，但项目 `execution.gpu_ids` 白名单未在 constraints.yaml 中显式定义——首次 SSH 时务必用 `nvidia-smi` 确认哪些 GPU 属于本项目
- 数据盘 `/root/autodl-tmp/`（250GB），根分区 30GB。模型、checkpoint、HF cache 必须放数据盘
- OpenVLA 模型下载 shard 1 曾因 3 个并发写者损坏——后续下载必须单进程，完成后验证 safetensors 完整性
- AutoDL 实例重启后 SSH 端口会变，连接失败不要重试，提示 Director 查新端口

### 2. 🖥️ 基础设施快照
- 服务器：`westd-34887(root)`，工作目录 `/root/temp-adv-distill-vla`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- 数据集：`/root/temp-adv-distill-vla/data/libero/libero_object/`（10 tasks × 50 demos）
- VIP 特征缓存：`/root/temp-adv-distill-vla/artifacts/vip_features_all/`（10 个 .pt 文件）
- MLP checkpoint：`/root/temp-adv-distill-vla/artifacts/mlp_checkpoints/`（10 per-task + 1 multitask）
- IQL checkpoints：`artifacts/iql_checkpoints/`（scale=1）、`iql_checkpoints_scaled/`（scale=100）、`iql_checkpoints_scaled1000/`（scale=1000）
- OpenVLA 模型：`/root/autodl-tmp/models/openvla-7b-finetuned-libero-spatial/`（shard 1 下载状态未最终确认，上次检查时 curl 在跑但 worker 已 done）
- HF cache：`/root/autodl-tmp/.hf_cache/`
- 无 wandb 配置，无活跃训练进程（截至最后一次 ps aux）

### 3. 📊 当前状态
**Gate 2 全面失败，等 Director kill/pivot 决策。**

我刚完成的审查：
- `phase1_iql_vip` (scale=1): DONE/negative — AUROC 0.506（random，value collapse）
- `phase1_iql_vip_scaled` (scale=100): PREPARING 但实验已完成 — AUROC **0.480**（比 random 还差，反相关）
- `phase1_delta_progress`: PREPARING 但实验已完成 — AUROC 0.533（Δprogress 无信号）
- `phase0_feature_val`: PREPARING — Gate 1 通过 via fallback (b) MLP R²=0.985

Registry 状态滞后：phase1_iql_vip_scaled 和 phase1_delta_progress 的 metrics/conclusion 已填但 status 仍为 PREPARING。

**无活跃 Worker/Cron。等 Director 对 kill/pivot 做最终决策。**

### 4. 📋 待办
- Director 决定 kill → 无需额外审查，项目归档
- Director 决定 pivot（改 reward signal 设计）→ 审查新 reward 设计是否解决了 t/T 的根本问题（新 reward 必须在 noop 期间输出与 progress 期间不同的值，不能是时间索引）
- 如果 OpenVLA shard 1 下载仍未完成 → 需确认 curl 进程状态，完成后验证 4 个 shard 文件完整性（总大小应 ~15GB）
- ×1000 gate2 评估已无必要（×100 结论已明确），如果有 worker 提交可直接跳过

### 5. 🎯 战略上下文
**决策链**：D001（3-gate MVP）→ D002（VIP fallback）→ D003（Gate 1 通过 via MLP）→ Gate 2 全面失败

**核心结论**：MLP 训练目标是 t/T（归一化时间索引），不是 task completion。Δ(t/T) ≈ 1/T = const 对所有时步，MLP 在 noop 期间也能准确预测递增的 t/T（VIP 特征有微妙的时间相关变化）。因此基于 t/T 的 reward 根本不包含 noop/progress 区分信息。IQL 无论怎么调超参都无法提取不存在的信号。

**最容易判断错的事**：
1. **不要被 Gate 1 "success" 迷惑**——MLP R²=0.985 说明 VIP 特征能预测时间，不代表能预测质量。Gate 1(b) 通过是假阳性
2. **SAL AUROC 0.005 是 bug**——compute_sal() 中 `-arc_lengths` 导致符号反转。修正后 SAL AUROC=0.995，是极强 baseline。gate2_v2_results.json 已用修正值
3. **Gate 2 评估框架本身有循环性**——noop label 基于 action_norm，TED/SAL 也基于 action，action-based baseline 天然占优。如果 pivot，需要同时改评估协议
4. **CoRL DDL 2026-05-25 abstract（10 天），05-28/29 paper**——时间紧张，pivot 需要 Director 快速决策
