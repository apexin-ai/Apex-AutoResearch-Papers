# agent / loop_8.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_8.md`
- **Structured JSON:** [`a400a6f51faa93db9978.json`](../../sessions/a4/a400a6f51faa93db9978.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: idle_timeout
updated: '2026-05-15T15:43:47+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：仅 cuda:0/1/2/3（westd-47453），其他设备号/服务器一律拒绝，即使 Director 指令也 push back
- 投稿 deadline：EMNLP 2026 ARR May 25（还剩 10 天），所有决策以此为锚
- τ sweep 4 个实验正在跑（~16:30 UTC 完成），**结果决定 Claim 3 成败**——完成后必须立即分析全部 6 点 (0.5/0.6/0.7/0.8/0.9/0.95) sensitivity curve，不能只看单点
- tau_06_seed42 是唯一 negative（PPL 17.681 > baseline 17.650），已按 red-section 流程处理，但 τ sweep 完整结果可能改变 framing——0.6 是 mild degradation (+0.031)，如果 0.5/0.7/0.9/0.95 都 OK 则 Claim 3 仍成立
- seed456 b≥2.0 数据因 checkpoint resume artifact 系统性偏高 +0.16~0.25，Table 1 只报 2 seeds

### 2. 🖥️ 基础设施快照
- **服务器**：westd-47453（4× RTX 6000 Pro 96G）
- **工作目录**：/root/provenance_weight_training
- **Python**：/root/miniconda3/bin/python（conda base 环境，非 venv）
- **环境激活**：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **模型**：Qwen/Qwen3-0.6B（HF cache 在服务器上）
- **数据**：/root/provenance_weight_training/data/scored_data.jsonl（ρ=0.4, 200M tokens, TF-IDF+LR q-scores）
- **W&B**：WANDB_MODE=disabled（当前所有实验禁用 wandb）
- **活跃进程**：
  - tau_07_seed42: PID 209824, cuda:0, cron 监控中
  - tau_05_seed42: PID 205652, cuda:1, cron 监控中
  - tau_095_seed42: PID 215505, cuda:2（cron 应已注册，reconcile 只返回 2 个但实际 4 个在跑）
  - tau_09_seed42: PID 213283, cuda:3（同上）
- **GPU 预算**：已消耗 ~125h，剩余 ~55h；当前批 ~14.4h，排队 ~21.6h，余量 ~19h

### 3. 📊 当前状态
**刚完成**：nmin1_seed42 分析（PPL 17.789，n_min=1 ESS 约束失效确认）+ tau_06_seed42 negative 处理 + ess_only_seed42 分析（PPL 17.728，max-intervention 退化确认，D029）+ golden_ratio_seed42 分析（PPL 17.654，oracle 上界确认）

**正在跑**：τ sweep 4 个实验（tau=0.5/0.7/0.9/0.95），预计 ~16:30 UTC 完成。这是 Claim 3 的决定性数据。

**Registry 总览**：40 experiments — 27 success / 1 negative / 1 failed / 2 killed / 4 RUNNING / 4 PREPARING / 1 QUEUED

**等待中**：
- 4 个 τ sweep cron 回调（~16:30 UTC）
- Director 未有未决审批
- nmin4_seed42 / adaptive_v2 ×3 seeds 在 PREPARING，等 GPU 释放
- detector_modernbert QUEUED（P1 优先级）

### 4. 📋 待办（条件触发式）
- **τ sweep 4 个实验完成** → spawn worker 跑 post-hoc eval 全部 6 点 → 绘制 τ sensitivity curve (PPL vs τ) → 判断 Claim 3：如果 PPL variance < 0.05 across τ∈[0.5, 0.95] 则 "robust default" 成立；否则需缩小 claim 范围或重新 frame
- **τ sweep 分析完成** → 立即提交 nmin4_seed42（cuda:0）+ 排队中优先级最高的 ess_only_seed123（cuda:1）→ 两个一起跑
- **nmin4_seed42 完成** → 整合 n_min ablation 4 点数据 (n_min=1/2/3/4)，绘制 n_min sensitivity 图
- **ess_only_seed123 完成** → 与 ess_only_seed42 合并，Claim 1 多 seed 加固
- **全部 P0 消融完成** → 评估论文初稿启动条件（τ sweep + ess_only 多 seed + n_min 完整 ablation）
- **GPU 全部空闲但 P0 未完** → 立即铺 adaptive_v2 ×3 seeds 和 batchsize=8
- **Director 要求启动论文写作** → 先 read paper_framing.md + writing_plan.yaml，确认所有 claims 有实验支撑

### 5. 🎯 战略上下文
**核心框架**：Dual-constrained adaptive b* = inf{b ≥ 0 : α_eff(b) ≥ τ} s.t. ESS(b) ≥ n_min。最小干预准则替代 Drayson 的 grid search。

**决策链关键节点**：
- D023: α_eff 非 decorative，dual-constraint 框架恢复（修正 D021/D022 过度修正）
- D025: τ 降级为 empirical HP（不能 claim proportion-free 理论推导）
- D029: ESS-only PPL 17.728 > uniform 17.690 — max-intervention 退化确认，Key Risk #1 resolved
- D030/D031: n_min framing 调整为 "most consistent across seeds"（variance 优势），非 "optimal"

**Claim 强度排序**：Claim 2 ★★★★★（grid-match 已 3-seed 验证）> Claim 1 ★★★☆☆（dual-constraint 核心，需 ess_only 多 seed 加固）> Claim 3 ★★☆☆☆（τ sweep 结果待定）

**易踩的坑**：
1. tau_06 是 negative 但 mild (+0.031)——不要过度解读，等全 sweep 数据再判断
2. 论文用 ratio of means (89.9%) 而非 mean of ratios (91.0%)——aggregation 口径已决策（memory.md）
3. n_min 和 batch_size 耦合（batch_size=4 → n_min=max(2, 4//2)=2），n_min=3 的数据来自旧 adaptive 实验（D018 确认唯一差异=n_min）
4. Golden Ratio PPL=17.654 ≈ adaptive_fix 17.650——adaptive 已封顶 oracle 上界，后续消融聚焦 robustness 不是追更低 PPL
5. reconcile_crons 只返回 2 个 cron（tau_05/tau_07），但实际 4 个在跑——tau_09/tau_095 的 cron 可能需要检查是否正常注册


---
