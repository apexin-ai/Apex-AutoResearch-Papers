# director / loop_1.md

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`0ee7fa84359ebd810aec.json`](../../sessions/0e/0ee7fa84359ebd810aec.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-15T14:10:48+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只允许 westd-34887 的 cuda:0 和 cuda:1（constraint C001）
- 服务器是 AutoDL 实例，外部网络操作前必须 `source /root/distill_sparse_swiglu/setup_env.sh`（含 network_turbo + SSL 证书 + HF_HUB_DISABLE_XET=1）
- conda 环境（aml-train 镜像），不要创建 venv，pip 在 `/root/miniconda3/bin/pip`
- 校准数据已从 SlimPajama 改为 WikiText-103（D002），SlimPajama 在 AutoDL 下不可访问
- KL 训练必须启用 gradient checkpointing（8B 模型端到端反向传播无 checkpointing 会 OOM ~88GB/95GB）

### 2. 🖥️ 基础设施快照
- 服务器：westd-34887 (connect.westd.seetacloud.com)，账号 root
- GPU：2× RTX PRO 6000 Blackwell (98GB, compute cap 12.0)
- 工作目录：`/root/distill_sparse_swiglu/`（src/train.py, src/evaluate.py, src/losses.py, src/predictor.py, src/data_utils.py）
- Python：`/root/miniconda3/bin/python`，PyTorch 2.8.0+cu128, transformers 5.8.1
- 模型：`/root/autodl-tmp/models/llama-3.1-8b/`（Llama 3.1 8B, 16.1GB, 4 shards, 验证通过）
- HF cache：`/root/autodl-tmp/.hf_cache`
- 环境初始化脚本：`/root/distill_sparse_swiglu/setup_env.sh`
- Checkpoints：`/root/distill_sparse_swiglu/checkpoints/mvp_bce_s42/`, `s123/`, `s456/`（各 145MB）
- 活跃进程：两卡可能均空闲（quicktest 刚部署，需确认）

### 3. 📊 当前状态
**BCE 3-seed 全部完成**（训练+评估）：
- mvp_bce_s42: sparse PPL=44.21, dense=27.96
- mvp_bce_s123: sparse PPL=44.83, dense=28.38
- mvp_bce_s456: sparse PPL=42.54, dense=28.14
- Mean sparse PPL = 43.86 ± 1.18, sparsity = 0.498

**KL 系列连续失败**，正在修复：
- mvp_kl_s42: DONE/negative — 稀疏性坍塌至 0%（reg_weight=0.1 被 KL loss 压制）
- kl_lagrangian_quicktest: DONE/negative — Lagrangian lambda 爬升追不上 KL（KL~418 vs constraint~1.2）
- **kl_normalized_quicktest: PREPARING** — KL 除以 seq_len 归一化（KL ~0.27 at step 1），Lagrangian (lambda_init=1.0, ×2.0/25步, cap=1000)。代码已就绪，应该即将提交或刚提交到 cuda:0
- 我还要求 Agent 在 cuda:1 并行跑一个 seq_len-only 归一化变体作为 hedge，但不确定是否已执行

**待处理**：
- mvp_kl_s123/s456 原始版本待取消（固定 reg_weight 已知坍塌）
- evaluate.py 曾被修改过导致 dense PPL 不一致（6.12 vs ~28），Reviewer 标记为 CRITICAL，要求统一评估版本

### 4. 📋 待办（条件触发式）
- kl_normalized_quicktest 完成 → 检查 200 步后 sparsity 是否稳定在 0.45-0.55：
  - sparsity ∈ [0.45, 0.55] → 跑完整 1000 步 × 3 seeds，然后用统一 evaluate.py 评估
  - sparsity < 0.3 → 方案 C 失败，退到方案 A（BCE warm-start + KL finetune）
- KL 3-seed eval 全部完成 → 对比 3-seed 均值：KL ppl < BCE ppl 差距 ≥ 0.3 → MVP PASS → complete_mvp() + 启动 post-MVP（paper_framing.md → experiment_plan.yaml → dream_simulate）
- KL ≈ BCE 或 BCE 更优 → MVP FAIL，评估 pivot（方案 A 作为最后诊断，或放弃 KL 方向）
- 所有 eval 必须用同一 evaluate.py 版本跑，确保 dense baseline 一致（~28 packed chunks 或 ~6 sliding window，选一个统一）

### 5. 🎯 战略上下文
- **项目核心**：验证 KL-divergence 能否训练出比 BCE 更好的 SwiGLU 激活稀疏性预测器（EMNLP 2026 ARR，DDL 5/25，仅剩 10 天）
- **决策链**：D001（MVP 设计）→ D002（校准数据改 WikiText-103）→ D003（KL 坍塌改 Lagrangian）→ D004（Lagrangian 不够改归一化）
- **最容易判断错的事**：
  1. KL 连续失败不等于方向错误——核心问题是梯度尺度不匹配（KL sum 跨 128k vocab vs constraint 跨 14336 neurons），归一化后应该可行
  2. BCE eval 报的 dense PPL ~28 偏高（packed chunks 而非 sliding window），绝对值不可与文献对比，但 KL/BCE 相对对比仍然有效——前提是统一评估方法
  3. BCE sparse PPL ~44 对应 +56% 增幅看似很大，但 Agent 认为 1000 步训练不充分（文献 predictor 充分训练后 1-5% 增幅），这是 MVP 快速验证而非最终结果
  4. Post-MVP skeleton 已在 ROADMAP：Phase 1 四条件 ablation → Phase 2 SPON 组合 → Phase 3 评估扩展 → Phase 4 论文
  5. Reviewer 之前指出 IDEA_BRIEF 的 core 级实验（STE baseline, iso-compute 对比）在 experiment_plan.yaml 展开时不能降级


---
