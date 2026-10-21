# reviewer / loop_2.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_2.md`
- **Structured JSON:** [`9bb2892f40d5f1864cf5.json`](../../sessions/9b/9bb2892f40d5f1864cf5.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-14T13:23:30+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 cuda:0, cuda:1（C001 约束）。之前所有实验均遵守，但 GRASPrune config.py 默认 cuda:0，后续运行时必须确认不与 MVP 冲突
- **绝不能在主 conda base 环境运行 `pip install -r /root/GRASPrune/requirements.txt`**——会把 torch 从 2.10.0+cu128 降级到 2.7.0，破坏运行中的 MVP 实验
- AutoDL 网络：HF 下载需 `source /etc/network_turbo` + `HF_HUB_DISABLE_XET=1`；当前 eval 进程用的是本地缓存的 GSM8K，不依赖网络

### 2. 🖥️ 基础设施快照
- 服务器：`westb-23072(root)`，工作目录 `/root/recovery_aware_struct_prune`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- 模型：`/root/autodl-tmp/models/DeepSeek-R1-Distill-Qwen-7B`（下载进程 PID 138527 可能仍在跑）
- 剪枝模型：`/root/recovery_aware_struct_prune/models/pruned_standard_35` + `models/pruned_rasp_35`
- GRASPrune 代码：`/root/GRASPrune/`（已修改 data.py 添加 GSM8K 支持，无独立 venv）
- 数据集缓存：`/root/.cache/huggingface/datasets/openai___gsm8k/`
- HF cache：`/root/autodl-tmp/.hf_cache`
- 活跃进程：MVP pipeline tmux session `mvp_rasp_pipeline_v2`（PID 170769），内含两个并行 eval 进程 PID 170786（standard, cuda:0）+ PID 170787（rasp, cuda:1）
- 日志：`/root/recovery_aware_struct_prune/logs/mvp_resume_v3_20260514_161229.log`
- wandb：未配置（report_to="none"）

### 3. 📊 当前状态
**刚完成**：审查了 GRASPrune 代码部署 + 环境校准两个 worker，已向 Director 发送两份报告。

**RUNNING 实验**：
- `mvp_rasp_pipeline_v2`：Step 3.5 GSM8K eval，~40% 完成（standard ~530/1319, rasp ~552/1319），预计 ~18:30-18:50 UTC 完成 eval。之后自动进入 Step 4 GRPO RLVR recovery（~12-15h）。

**历史**：`mvp_rasp_pipeline`（v1）已 DONE/failed（GQA 约束违规，已修复后变为 v2）。

**等待中**：无 pending worker 回调。Director 未就 GRASPrune rescale WikiText2 硬编码问题做出决策。

### 4. 📋 待办
- MVP eval 完成（~18:50 UTC）→ 检查 post-prune accuracy 数字是否合理（pruned 模型 GSM8K 预期 <20%），确认 Step 4 GRPO 自动启动
- GRPO recovery 启动后 → 核实 GPU 利用率、learning rate、KL 系数等超参是否合理，检查 loss 曲线前 100 步是否正常下降
- GRPO 完成（预计 +12-15h）→ 核实 post-recovery accuracy，检查 recoverability Δ_acc 是否 >0，核实 Step 7 correlation analysis 的 Spearman ρ 是否 ≥0.4（MVP PASS 标准）
- 新 worker_done 通知到达 → 按 audit-checklist 审查
- GRASPrune 实际运行前 → 核实是否创建了隔离环境，是否避开了 requirements.txt 整体安装
- Director 要求章节写作审查 → 按 §5 模式执行对抗审查，特别注意 experiments.tex 的 [TBD] 占位符是否已填充

### 5. 🎯 战略上下文
- **核心假设**：CKA functional overlap F(h) 预测 RLVR 下的结构可恢复性。MVP 判据：Spearman ρ(F(h), activation_shift) ≥ 0.4
- **RASP 评分公式**：S(h) = I(h) × (1-F(h))^α，α=1.0。高 overlap 结构被优先剪枝（与传统 "冗余即可删" 的直觉一致，但理由不同——RASP 认为它们的功能可被 RLVR 重新分配）
- **35% sparsity 下剪枝全落在 MLP**：全局 importance ranking 自然保留所有 attention GQA groups，只剪 MLP intermediate channels。这意味着 attention-level CKA overlap 对 MVP 结果影响为零——correlation analysis 仅看 MLP 层
- **易错点**：
  1. activation shift proxy 度量的是 **retained neighbor 在 pruned vs recovered 模型间的变化**，不是 pruned structure 本身的变化。之前论文描述就写错过一次
  2. GRASPrune baseline 的 rescale 阶段硬编码 WikiText2，即使门训练改用 GSM8K。这不一定是 bug（原始设计如此），但论文需要说明
  3. 不要信 registry notes 里的进度数字——那是最后一次 worker 更新的快照，可能已过时。必须 ssh_read_only 独立核实
  4. experiments.tex 有大量 [TBD] 占位符（GRPO 超参、MLP 剪枝组数等），需 MVP 完成后填充


---
