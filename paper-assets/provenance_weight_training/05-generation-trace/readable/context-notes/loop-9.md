# director / loop_9.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_9.md`
- **Structured JSON:** [`22aa2cb7aada89ed533f.json`](../../sessions/22/22aa2cb7aada89ed533f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_messages
updated: '2026-05-15T18:32:04+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 cuda:0/1/2/3（4 卡），不得使用白名单外 GPU
- τ sweep 的 success/negative 判据已统一：PPL < uniform mean (17.694) = success，不要再改标准
- D031 的 "std=0.032 vs 0.009" n_min variance 叙事已禁止（memory 已记录），汇总文件不得使用旧数字
- paper_framing.md 中 "τ 不敏感（0.6-0.9 均可工作）" 已被数据否定（τ=0.9 negative），等 τ=0.95 齐后必须 reframe

### 2. 🖥️ 基础设施快照
- 服务器：通过 list_ssh_hosts 获取（本 session 未直接 SSH，Agent 在操作）
- 项目 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/`
- 模型：Qwen3-0.6B，数据：FineWeb subset 132M+ tokens，40% 污染
- 活跃进程（Agent 最后报告）：
  - cuda:0: ess_only_seed123 (PID 233872)
  - cuda:1: nmin4_seed42 (PID 225265, ETA ~5.9h, b*=0 全程=uniform)
  - cuda:2: tau_095_seed42 (PID 215505, 94% 完成, ETA ~14min from 17:14 UTC)
  - cuda:3: ess_only_seed456 (PID 233952)
- τ sweep 分析脚本已部署到服务器，6 组齐后自动出图

### 3. 📊 当前状态
**刚做完**：处理 τ sweep 5/6 结果 + Reviewer 的 Claim 3 挑战分析 + 确定 reframe 方向

**τ sweep 已完成 5/6**：

| τ | PPL | ΔPPL vs uniform | b* mean | conclusion |
|---|-----|-----------------|---------|------------|
| 0.50 | 17.688 | −0.006 | 0.39 | success |
| 0.60 | 17.681 | −0.013 | 0.59 | success |
| 0.70 | 17.679 | −0.015 | 0.89 | success |
| 0.80 | 17.653 | −0.041 | 1.40 | success |
| 0.90 | 17.712 | +0.018 | 2.36 | negative |
| 0.95 | — | — | — | RUNNING ~即将完成 |

**其他 RUNNING**：ess_only_seed123/456（~3.5h），nmin4_seed42（~5.9h）

**等待中**：Agent 在处理我发的 Claim 3 reframe 预告 + registry 确认指令

### 4. 📋 待办
- τ=0.95 eval 完成 → 确认 PPL > 17.712（预期 over-correction 更严重，b* 极高）→ 6 组齐后跑分析脚本出图（τ vs PPL + τ vs b*）
- 6 点 τ sweep 完整 → **更新 paper_framing.md Claim 3**：从 "τ insensitive" 改为 "wide safe range [0.5,0.8] + principled default τ=0.8 + b* monotonic mechanism as core insight"
- ess_only_seed123/456 完成 → eval → 与 adaptive_fix 对比 → 验证 Claim 1 核心（min-intervention > max-intervention）。这是 P0——如果 ess_only ≈ adaptive，α_eff 的独立价值被削弱
- nmin4_seed42 完成 → eval → 预期 PPL ≈ uniform（b*=0 全程）→ 补齐 n_min sensitivity 4 点（1/2/3/4）
- 上述全部完成 → 考虑 dream_simulate(review_mode="full") 验证 reframed story

### 5. 🎯 战略上下文
**核心决策链**：MVP PASS (D019) → τ 代码修复 (D021) → α_eff 理论审计 (D023) → τ 理论降级为 empirical HP (D025) → τ sweep 显示 narrow optimum (D032+Reviewer)

**Claim 3 reframe 是当前最重要的待办**。Reviewer 说 τ=0.8 是 narrow optimum；Agent 说 [0.5,0.8] 是 wide safe range。两者都有道理——关键是 τ=0.5 只捕获最大改善的 15%。新 framing 不能说 "insensitive"，要说 "safe range + principled default + clear mechanism"。

**ess_only 是最大风险点**：如果 ess_only PPL ≈ adaptive_fix，Claim 1（dual constraint > ESS-only）不成立，需要降级为 "dual 不劣于 ESS-only 且有理论 motivation"。paper_framing.md Key Risks 第 1 条已有分级应对方案。

**易错点**：
- 不要把 τ sweep 的 "success"（beats uniform）误解为 "接近最优"——τ=0.5 的 success 含金量远低于 τ=0.8
- nmin4 结果（b*=0 退化）是预期行为，不是 bug——n_min=batch_size 使 ESS 约束永远 binding
- 汇总文件已用统一 eval 数字重新生成，不要引用旧版数字


---
