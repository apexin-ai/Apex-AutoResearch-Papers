# reviewer / loop_1.md

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`c9b8871f762913ddf91a.json`](../../sessions/c9/c9b8871f762913ddf91a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-19T10:47:47+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 **westd-20861:cuda:0**（单卡 RTX PRO 6000 98GB）。项目 GPU 白名单只有 cuda:0。
- 磁盘总量 **30GB**，当前可用 ~15GB。Qwen 模型 (15GB) 和 Llama-3.1 (16GB) **无法共存**，必须顺序执行。
- 远程代码根目录 `/root/turn_residual_gating/`，本地 artifacts 在 `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/`。**两边可能有同名文件版本不一致**——断言"未改"前必须两边都读。
- UG (uniform) 的 "uniform" 含义是**无 turn conditioning**，不是"所有层共享同一 gate"。每层有独立 `UniformGateNetwork`。Registry 假说描述有误但尚未修正。

### 2. 🖥️ 基础设施快照
- **服务器**: westd-20861, 工作目录 `/root/turn_residual_gating/`
- **Python**: `/root/miniconda3/bin/python3.12`, conda env = base
- **Qwen 模型**: `/root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct` (15GB)
- **Llama-3.1 tokenizer**: `/root/.cache/modelscope/hub/models/LLM-Research/Meta-Llama-3___1-8B-Instruct/` (11MB, tokenizer only, 权重未下载)
- **训练数据**: `/root/turn_residual_gating/data/ultrachat_8k/` (HF 缓存已清，data 独立存在)
- **Eval 数据**: `data/standard_conversations.json` (5 convs) + `data/ultrachat_eval_sample.json` (~50 convs)
- **Checkpoints**: `runs/phase2_tg_s42_v7/`, `runs/phase2_ug_s42/`, `runs/phase2_lora_only_s42/` (训练中)
- **4way eval 脚本**: `scripts/run_4way_eval.sh` (8 runs: 4 models × 2 GAR variants)
- **活跃进程**: phase2_lora_only_s42 RUNNING on cuda:0, ~48% 完成 (gs~1450/3000)
- **HF token**: 未配置。Llama-3 通过 ModelScope 绕过 gated access。
- **无 W&B 配置**，不检查 W&B。

### 3. 📊 当前状态
刚完成 Route B 实验设计文档 (`artifacts/route_b_design.md`) 审查，提了 3 个问题：eval 数据源不一致 (standard_conv vs ultrachat_eval_sample)、§3.4 需要的 v7 中间 checkpoint 不存在 (只有 epoch 级)、缺少 PPL 对比。

**Registry**:
- `phase2_lora_only_s42`: **RUNNING**, gs~1450/3000 (~48%), 预计 ~3h 后完成。L_GAR ≈ 0（与 TG/UG 一致），gate 全 1.000。
- `phase2_ug_s42`: DONE, 未做 eval
- `phase2_tg_s42_v7`: DONE, eval 完成 (GAR-ours +0.35pp, GAR-Dongre +0.72pp)
- `phase2_lora_only_s42`: PREPARING → RUNNING (registry 已更新)

**等待中**:
- LoRA-only 训练完成 → 触发四路 eval
- Director 对 Route B 设计审查反馈的回复
- Director 对 Llama-3 磁盘方案 (A/B/C/D) 的决策

### 4. 📋 待办（条件触发式）
- **LoRA-only 训练完成通知** → 验证 checkpoint 完整性 + registry 更新 + GPU 释放 → 审查 eval 启动
- **四路 eval 完成** → 核心审查：四模型 GAR curve 是否趋同？TG vs LoRA-only 差值？→ 这是 Route A vs B 的 gate keeper
- **四路 eval: TG ≈ LoRA-only (差值 <0.5pp)** → Route B 确认，建议 Director 启动论文写作
- **四路 eval: TG > LoRA-only (差值 ≥1pp)** → Route A 仍有可能，建议 two-stage 实验
- **Director 决策 Llama-3 方案** → 如果选 B (顺序执行)，需等 Qwen 所有实验+eval 完成后清理
- **梯度冲突实验 (§3.1) 提交** → 审查 cosine similarity 和 magnitude ratio 结果
- **v7 中间 checkpoint 重训练** → 如果 Director 批准 route_b_design §3.4 方案 B (2h GPU 重训)

### 5. 🎯 战略上下文
**核心结论链**: Phase 1 GAR 衰减 70.8% (D001) → v1-v6 全 negative → v7 MSE 训练成功但推理仅 +0.35pp (D013) → 反向 turn conditioning 发现 (D014) → 30x train-eval GAR disconnect confirmed non-bug (D015) → Two-stage conditional plan (D016) → Two-route strategy adopted (D017)

**LoRA-only 训练已暗示结局**: L_GAR ≈ 0 意味着 LoRA 单独就能推训练 GAR 到 target，gating 在训练端冗余。推理端预计也将趋同（v7 推理效果本就极弱）。**Route B (negative result paper) 的概率 ≈ 80%+**。

**最容易判断错的事**:
1. **不要把 UG 的 per-layer variation 当异常** — 这是预期行为（每层独立 gate network），registry 的 `unexpected_per_layer_variation: true` 是错误标注
2. **不要因为训练 GAR=0.5 就认为方法有效** — 30x train-eval disconnect 是根本问题。训练 GAR 对所有三种配置都 ≈0.5，推理 GAR 才是判据
3. **eval 数据有两套**：standard_conversations (5 convs, v7 旧 eval 用的) 和 ultrachat_eval_sample (50 convs, 4way 脚本用的)。对比 v7 旧数据时注意数据源差异
4. **磁盘是硬约束**：30GB 盘放不下 Qwen+Llama，任何涉及 Llama 完整模型的实验都需要先删 Qwen


---
