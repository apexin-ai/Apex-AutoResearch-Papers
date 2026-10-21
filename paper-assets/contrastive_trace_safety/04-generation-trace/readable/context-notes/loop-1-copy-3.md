# reviewer / loop_1.md

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`23a0e61d01eb8f3c613b.json`](../../sessions/23/23a0e61d01eb8f3c613b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-17T08:38:21+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 `autodl-rtx6000` 上 GPU 白名单未在 constraints.yaml 中明确（文件未创建），但 2× RTX PRO 6000 Blackwell (98GB each) 均可用
- Bootstrap 比较必须用 **matched window**（HS-optimal window 同时用于 text），这是跨模型一致的协议。不要用 HS-best-W vs text-best-W 做 bootstrap
- Bonferroni α 现在是 **0.0125**（4 模型），不再是 0.017（3 模型）。所有显著性判断必须用新阈值
- OT-7B 的 CP 定义必须与其他模型一致（= last safety label + 1），不能用 "first DKE" 替代

### 2. 🖥️ 基础设施快照
- 服务器：`autodl-rtx6000(root)`，工作目录 `/root/autodl-tmp/contrastive_trace_safety`
- Python：`/root/miniconda3/bin/python3.12`
- 模型缓存：`/root/autodl-tmp/.hf_cache/` 下有 R1-32B (62GB), QwQ-32B (62GB), R1-Qwen-7B (15GB), OpenThinker-7B (15GB)
- 数据集：`ishitakakkar-10/HarmThoughts`（HuggingFace）
- Hidden states：`artifacts/hidden_states/` (R1-8B 268), `hidden_states_r1_32b/` (100), `hidden_states_qwq_32b/` (96), `hidden_states_ot7b/` (228)
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/`
- 论文：`docs/paper/sections/*.tex`
- 活跃进程：OT-7B pipeline 已完成（PID 60094 应已退出）；无 RUNNING 实验

### 3. 📊 当前状态
**刚完成的审查：**
- exp_ot7b_full_pipeline (Path A) — OT-7B HS>Text 在 bal_acc(p=0.001) 和 FPR(p=0.007) 通过 Bonferroni。**但有 3 个写作问题需处理**：layer 0 异常、HS temporal gains 反转、precision 偏低 35.7%
- Path C (adaptive two-stage) — 改进 +1.3pp 在噪声范围内，已写入 appendix + discussion，不作为 core contribution
- Path B feasibility — 可行（1.5 天），但需 LLM API annotation（本地分类器已被否决 F1=0.59）
- R1-Distill-Qwen-7B — 已判定不可用（无 think tags, 0% jailbreak rate），被 OpenThinker-7B 替代

**Registry**: 18 experiments, all DONE。无 RUNNING/PREPARING。

**等待中**：Director 对以下项的决策：
- Path B 是否执行（LLM annotation 成本 $15-30，需 1.5 天）
- 论文 framing 更新（4 模型版本，Claim 1 temporal 需 qualify）
- Rebuttal 最终版（W1-W7 修改 + OT-7B 新数据）

### 4. 📋 待办（条件触发式）
- Director 批准 Path B 执行 → 审查 annotation validation（必须先在 100 条 held-out 上测 agreement ≥90%）→ 审查新 bootstrap 结果
- Paper Agent 提交新版论文（含 OT-7B）→ 做 Round 4 写作审查，重点：(a) Claim 1 temporal 是否 properly qualified for OT-7B 反转, (b) layer 0 discussion, (c) 4-model Bonferroni α=0.0125 是否全文更新, (d) Table 1/2 新增 OT-7B 行数据一致性
- 新 worker 完成 Holm-Bonferroni 计算 → 核实 step-down 顺序和 adjusted p-values
- 如果 Director 问 "是否降级回 Findings" → 评估：OT-7B 解决了 confound，但 Path C 未解决 novelty，Path B 未执行。3/3 结构问题只解决了 1 个

### 5. 🎯 战略上下文
**核心决策链**：D001→D005(MVP pass)→D014(claim重评)→D018(统计基础)→D022(三路扩展冲 Main)

**论文 4 个 core findings**：
1. Temporal context dominates（需 qualify：OT-7B HS probes 在 W>3 后下降）
2. Modality advantage is model-dependent：R1-8B ✓(p<0.001), OT-7B ✓(p=0.001), R1-32B directional(p=0.08), QwQ absent(p=0.83)
3. Negative results define boundaries（transfer/BOCPD/Mahalanobis all fail）
4. NEW: HS advantage is scale-dependent not architecture-dependent（2/2 小模型 pass Bonferroni，0/2 大模型 pass）

**最容易判断错的事**：
- OT-7B bootstrap FPR 比较用 W=3 for both。text 在 W=25 时 FPR=0.161 **低于** HS 的 0.188。如果审稿人问 "at text's optimal window"，HS FPR 优势消失。不要在论文中 claim "HS universally lower FPR"
- 论文 oracle section 说 "GRU +4.5 steps" 但 per-seed 数据（60/20/20 split）显示 GRU-multi mean=7.01。数字来自不同 evaluation protocol（70/30 vs 60/20/20），不是 bug 但需要 caption 说明
- exp_003 cross-transfer 用的是旧 layer indices（R1-32B layer 2, QwQ layer 1），在 exp_c2 correction 之前跑的。negative 结论 robust 但论文不能引用这些具体层号


---
