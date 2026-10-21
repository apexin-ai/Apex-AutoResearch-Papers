# reviewer / loop_12.md

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_12.md`
- **Structured JSON:** [`19606f1682690c261461.json`](../../sessions/19/19606f1682690c261461.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: max_wall_time
updated: '2026-05-16T17:20:54+00:00'
---

### 1. 🔴 硬约束 / 红线
- 两台服务器各 2 张 GPU（index 0/1），无 gpu_ids 白名单配置，但不能跨服务器混用进程
- 论文中 DR bound 值必须级联一致：abstract 用 dataset-specific（SciERC ≤0.09%, DocRED ≤0.20%），其余章节用合并上界（≤0.20%），±0.6pp F1 cost
- ft_ablation_analysis.md 刚修完 14 个数据错误（DocRED 表格行间 copy-paste），论文 FT ablation 表必须从 registry 逐格核对，不能从 analysis artifact 直接抄
- Mistral 仅参与 ZS 验证，不参与 FT composability——论文已有 clean 理由（§5.4 L12），不要加 Mistral FT 实验

### 2. 🖥️ 基础设施快照
- **westd-16980**: 2× RTX PRO 6000 Blackwell 98GB，`/root/schema_semantic_constrained_ie`，conda base (`/root/miniconda3/bin/python`)
- **westd-21461**: 同配置，同路径
- **全部 4 张 GPU 空闲**，54 个实验全部完成，无活跃进程
- 模型路径: Qwen FT `/root/autodl-tmp/checkpoints/qwen_lora_{scierc,docred}_merged`，Llama FT `/root/autodl-tmp/checkpoints/llama_lora_{scierc,docred}_merged`，Base Qwen `/root/autodl-tmp/models/Qwen3-8B-ms`
- Latency profiler: `/root/schema_semantic_constrained_ie/profile_latency.py`（已部署可用）
- 本地 workspace: `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/`
- 论文目录: `artifacts/_project/paper/`

### 3. 📊 当前状态
**刚完成**: Paper Round 4 审查（7/10）+ ft_ablation_analysis.md 数据修正审查（15 个字段已修正确认）+ 残余 DR error analysis 审查 + ROADMAP 审查。所有 54 个实验 DONE，registry 无 RUNNING/PREPARING。

**论文进度**: Round 4 = 7/10，连续两轮（R3/R4）无 CRITICAL/WARNING。待 Paper Agent 用完整 FT ablation 数据 + error analysis 做 final patch 后提交 Round 5。

**等待中**: Paper Agent Round 5 审查请求（预计很快）。

### 4. 📋 待办
- Paper Agent 提交 Round 5 → 按 §5.3 模板评分，重点核对 FT ablation 表格数据是否用了修正后的 registry 真值（尤其 Qwen DocRED grammar_only RV 必须为 0%，Llama unconstrained DR 必须为 0.49%）
- Round 5 Overall ≥8 且连续两轮无新 critical → 收敛信号，Paper Agent 停止迭代
- 如果 Agent 更新 appendix FT ablation table → 核对与 ft_ablation_analysis.md 修正后数据一致
- 如果 Director 要求引用审计 → Read `skills/global/reference-audit.skill.md` 后执行
- w8_ft_posthoc_baseline.qwen_docred.R_F1_constrained 仍为 "TBD"（应为 40.56）→ 如有人更新 registry 需确认

### 5. 🎯 战略上下文
**核心结论链**: DR violations 由 constraint tightness 驱动（非 ontology scale）→ Grammar 层消除 ET/RV 但不碰 DR → Semantic 层降 DR 41-72% → 两层协作 DR≤0.20%（FT regime）→ overhead ≤5.4% → composability 确认（FT+OntoCoDec 正交）

**易错点**:
1. SciERC FT unconstrained DR 是 1.95%（22/1128），registry 存了 1.9（四舍五入）和 0.0195（精确）两种格式——论文用 1.95%
2. DocRED latency benchmark 结果在 `/tmp/latency_benchmark_docred_results.json`（westd-16980），SciERC 在 `/tmp/latency_benchmark_results.json`——上一轮有 worker 混淆过这两个文件
3. CF 是 model-dependent：well-calibrated 模型（Qwen/Llama）S1 增加 CF，poorly-calibrated（Mistral）S1 降低 CF——不要简单说 "S1 increases CF"
4. Qwen DocRED FT full_s1 的 R-F1 在 all-set（40.56）和 excl-fail（42.23）差异大，论文用 all-set 为主
5. R² = 0.886 的 dual-factor pattern 基于 n=4，论文已加 caveat


---
