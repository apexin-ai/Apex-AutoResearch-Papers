# reviewer / loop_14.md

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_14.md`
- **Structured JSON:** [`feeade756f78665414c1.json`](../../sessions/fe/feeade756f78665414c1.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 14
reason: max_wall_time
updated: '2026-05-17T08:28:31+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0-3 on autodl-5090。exp_028 当前占 cuda:0。
- 论文 tex 只能改 `docs/paper/sections/`，禁止动 `artifacts/_project/paper/`（C001 约束）
- Degeneracy 定义已统一为 **Constant F1, gold-filtered**（D123）。任何新分析必须用此定义，不能用 KeySet 或 all-data 变体。旧值 58%/21%/10% 已废弃，新值 47.4%/17.8%/13.8%。
- Figure 3 的 per-type points 定义不变（Few-NERD entity-type-level），但 dataset-level blue circles x 轴必须用新值。

### 2. 🖥️ 基础设施快照
- 服务器：`autodl-5090(root)`，工作目录 `/root/autodl-tmp/struct_self_consist_ie`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/`
- 模型路径：`checkpoints/qwen3-8b-fewnerd-5epoch-lora`（训练中）、`qwen3-8b-fewnerd-exp021-merged`（3-epoch 已完成）
- 数据：`data/fewnerd_uie_train`（131k）、`data/fewnerd_n16_subset`（5000 instances for inference）
- 活跃进程：PID 371545 (exp_028 训练, cuda:0, step ~50/41180, ETA ~2026-05-18 05:30 UTC)
- W&B：未配置（本项目不用 wandb）
- 分析输出：`output/r17_analyses/` (lp_compression_comparison.json, p2_supplementary.json)

### 3. 📊 当前状态
**刚完成**：D123 framing revision 整合一致性核实（PASS），W2 rank=8 LP 分析���实（LP 未被压缩，true differentiator = within-instance ρ），P2 补充分析核实（Q3/Q4/Q6），degeneracy 定义不一致 CRITICAL 发现 → 已修复。

**RUNNING**：exp_028_fewnerd_5epoch（训练中，ETA ~18h）

**等待中**：
- exp_028 训练完成 → LoRA merge → inference → degeneracy + LP selection 分析
- Figure 3 重绘（Main Agent 负责）
- Paper Batch 3（Q3/Q4 整合 + epoch confound 预留）

### 4. 📋 待办
- exp_028 训练完成通知 → 审查 merge + inference 设置是否用 Constant F1 gold-filtered 定义
- exp_028 分析结果出来 → 核实 degeneracy 值：若 ≤15% → 大利好，确认 narrative；若 >20% → 检查 Paper Agent 是否启用"training convergence modulates degeneracy"预案
- Figure 3 重绘完成 → 验证 x 轴 dataset-level points = (47.4, 17.8, 13.8)，per-type points 不变，Spearman ρ=-0.881 不应变（只有 dataset-level 3 points 移动，per-type 8 points 不变）
- Paper Batch 3 完成 → 核实 Q3 (29% neg ρ) 放入 MBR 段、Q4 (partial correlation) 放入 per-type 讨论
- Missing references（特别是 "Byerly & Khashabi 2024"）→ 如果 WebSearch 确认���存在则必须删除

### 5. 🎯 战略上下文
**核心叙事（D123 后）**：LP selection 需要 TWO jointly necessary conditions — low degeneracy (<~15%) AND adequate LP-quality alignment (ρ>~0.3)。LoRA-rank ablation 是关键证据：degen 降到 7.2% 但 ρ≈0.24 → LP 仍 fails。Few-NERD 满足双条件 → LP 成功。

**易错点**：
1. 不要把 paired subset 值 (11.1%→4.5%) 与 dataset-level 值 (13.8%) 混淆——前者是 4,351 matched instances 的 within-comparison
2. W2 worker 报告的 degeneracy 用的是 KeySet(t,T,s,e) 定义——不能直接引用其绝对值，只有相对结论（rank=8 LP 未被压缩）有效
3. R2 的核心 concern 是 excitement/novelty 而非 correctness——Practical Guidance + actionable decision rule 只能微调 R2 score，不能翻转
4. 投稿策略：坚持 Main track，commitment form 选 "willing for Findings fallback"。不要主动降级。
5. exp_028 是双刃剑：如果 5-epoch degeneracy 大幅升高，说明 3-epoch 的低 degeneracy 部分源自 under-training——但可 reframe 为 "practitioners can control degeneracy via training epochs"


---
