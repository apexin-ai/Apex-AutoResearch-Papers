# reviewer / loop_3.md

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_3.md`
- **Structured JSON:** [`29eb3fa474b43d1c91f4.json`](../../sessions/29/29eb3fa474b43d1c91f4.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_wall_time
updated: '2026-05-21T19:41:32+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只用 GPU 0（CUDA_VISIBLE_DEVICES=0），服务器 westd-20861 只有 1 张卡（NVIDIA RTX PRO 6000 Blackwell, 98GB）
- v8b_ss_s123 eval 脚本已就绪但未执行（`scripts/eval_v8b_ss_s123.sh`），需等 v7 训练完或确认 VRAM 够并行
- M020 nGAR 混淆已修正——**绝不能**在论文中使用 "normalization artifact" 叙事（AR nGAR=0.493 vs TF nGAR=11.88，gap 24.1×，不是 "aligns"）
- 论文 instruction retention 数据：β=3（不是β=5），18 prompts（不是N=50）——commit e4522a3 已修复，但后续编辑要防回退

### 2. 🖥️ 基础设施快照
- 服务器：westd-20861，工作目录 `/root/turn_residual_gating`
- Python：`/root/miniconda3/bin/python3.12`，conda base 环境
- Qwen 模型：`/root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct`
- Llama 模型：`/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B-Instruct`
- 数据：`data/ultrachat_8k`（训练）、`data/ultrachat_eval_heldout.json`（eval, 50 convs）
- 活跃进程：v7_tg_s123 PID 245634（train_phase2.py, GPU 0, ~2min elapsed at last check 15:17 UTC）
- 无 W&B 配置（本项目不用 W&B，不检查）

### 3. 📊 当前状态
**刚完成**：v8b_ss_s123 训练完成审查（PASS，所有指标与 s42 偏差 <15%），v8b/v7 eval 脚本审查（PASS）
**RUNNING**：v7_tg_s123（Epoch 0 Step ~150 at 15:17 UTC，预计 ~6-7h 完成，即 ~21:00-22:00 UTC）
**待执行**：
- `scripts/eval_v8b_ss_s123.sh`（v8b eval，需 GPU）
- `scripts/eval_v7_tg_s123.sh`（v7+v8b 联合 eval，v7 训练完后执行）
**Registry 状态**：v7_tg_s123 RUNNING，v8b_ss_s123 DONE（仅训练指标，无 eval），其余 30 个 DONE/INVALIDATED

### 4. 📋 待办
- v7_tg_s123 训练完成 → 审查训练 final metrics（与 v7 s42 对比：final_loss ~1.04, gate_mean ~0.95, gate_std ~0.06）
- v8b_ss_s123 eval 结果出现 → **核心审查**：model-gen GAR-ours 与 s42 的 0.318 对比，gap ratio 是否在 [1.2×, 2.5×]（s42=1.57×），PPL <1.6。这是 C7 seed robustness claim 的关键数据
- v7_tg_s123 eval 结果出现 → 审查 TF-AR gap ratio（s42=32×），确认标准 TG 的 exposure bias 跨 seed 复现
- Agent 若更新论文加入 multi-seed 数据 → Mode B 审查：数字一致性、claim 强度是否从 "single seed" 升级
- 如发现 s123 gap ratio 与 s42 偏差 >50% → 立即 CRITICAL 报 Director

### 5. 🎯 战略上下文
**核心结论链**：ThreadGate 训练成功（TF GAR=0.50）但 AR GAR 坍塌（0.015-0.025），gap 20-33×。原因是 exposure bias（不是 gating 失败、不是梯度冲突）。证据：(1) PCGrad 无效排除梯度冲突，(2) β-steering 恢复 GAR 证明 attention misallocation，(3) scheduled sampling 压缩 gap 到 1.57×，(4) Llama 跨模型复现 12.5× gap。

**易踩坑**：
- nGAR vs raw GAR：TF 和 AR 的 normalization factor 不同（TF ~24.6, AR ~12.7），不能直接对比 nGAR 跨 TF/AR。论文用 raw GAR 报主结果是正确的
- v8b s42 是从 epoch_0 resume 的（2 个 epoch），s123 是 from scratch（3 个 epoch），wall clock 不可直接对比
- GAR-Dongre 在标准 TG（v7）下 gap 几乎为零（Qwen 1.28×, Llama 1.002×），但在 SS（v8b）下 Dongre 值异常高（~0.38），"Dongre uniformly low" 只适用于非 SS 训练
- 论文 Limitations 已按 EMNLP 规则精简（3 个点），不要再加长


---
