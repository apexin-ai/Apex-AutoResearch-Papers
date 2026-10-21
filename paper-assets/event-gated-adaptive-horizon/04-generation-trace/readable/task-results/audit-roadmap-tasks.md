# audit roadmap tasks

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_roadmap_tasks_20260525T134553_result.json`
- **Structured JSON:** [`dba16fa77afbbc15780e.json`](../../sessions/db/dba16fa77afbbc15780e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I have all the data needed. Here's the audit:

## ROADMAP 任务审计

### ROADMAP 状态本身已过时
ROADMAP 列出 exp_074/077/078/079 为运行中，但实际：
- exp_074 (008a Walker s3): **已完成** (success, eval 855.9)
- exp_079 (frozen dt_emb Walker s0): **已完成** (killed)
- exp_080/081 (008e_v3 Walker s1/s2): **运行中但未列入 ROADMAP**
- exp_077/078 (Cheetah baseline/008d): 仍运行中

ROADMAP 实验统计写 "155 个（78 success）"，report.md 写 "成功 79 / 共 153"，两者不一致。

---

### 可立即执行的任务

1. **ROADMAP 自身更新** — 将 exp_074/079 从 "运行中" 移除，加入 exp_080/081，统一实验计数
2. **exp_074 结果纳入论文** — 008a 现在有 4 seeds (mean eval 791, std 102.2, all civo_alert=0)。appendix Table complete_results 缺 008a_s3 行，需添加：`008a\_s3 & Unexposed emb & exp$^a$ & OFF & 15 & 855.9 @105K & --- & Healthy`
3. **exp_072 (008e_v3 s5) 纳入 appendix** — 008e_v3 现有 s1-s4 在 appendix 中，s5 (eval 853.1, NVE 0.61, healthy) 缺失
4. **008f 额外 seeds 纳入 appendix** — exp_071 (s3, eval 311.9) 和 exp_073 (s4, eval 289.3) 未在 appendix 表中
5. **plan_034 标记完成** — ROADMAP "完成后下一批" 仍列 plan_034 NVE threshold 分析，但 appendix 已包含完整 n=56 AUROC=0.990 分析，provenance 也引用了 plan_034 结果。应从待办移除
6. **Rebuttal Q&A 实验计数更新**（见下方详细列表）

### Blocked 任务（依赖在跑实验）

1. **plan_022 Cheetah causal control (dt_embed_dim=0)** — 依赖 exp_078 (Cheetah 008d) 确认 CIVO
2. **exp_077/078 完成后分析 + 更新论文** — 依赖 exp_077/078 完成
3. **exp_080/081 完成后更新 008e_v3 multi-seed 统计** — 依赖 exp_080 (s1)/081 (s2) 完成，完成后 008e_v3 将有 6+ seeds
4. **等待 Round 5 审稿结果** — 外部依赖
5. **Round 5 反馈 → 修正 → 数据锁定 (5/27)** — 依赖 Round 5
6. **ICML 投稿 (5/29)** — 依赖一切完成

---

### Rebuttal Q&A 更新需求

**Q4** (环境数量): 引用 "133 experiments across 43 configurations" → 应更新为当前计数 (~153 experiments)

**Q6** (NVE threshold): 引用 "In-sample AUROC 0.957 (n=30)" 和 "LOEO mean AUROC 0.988" → 论文正文已更新到 n=56 AUROC=0.990 F1=0.941。Rebuttal 应同步，或至少在 response 中引用最新数字

**Q7** (样本量): 引用 "133 experiments across 63 successful conditions" → 应更新为 ~153/79

**Q10** (环境多样性): 同 Q4，引用 "133 experiments" → 过时

**Q14** (Seed count 统计可靠性): 引用 "133 experiments, 63 success, 35 negative" → 过时。另外 "Fisher exact p=0.003: trained 7/7 onset" — 如果 Cheetah exp_078 确认 CIVO 则更新为 8/8 或更多

**Q15** (NVE threshold 敏感度): 引用 "In-sample AUROC=0.957, accuracy 27/30" → 论文已用 n=56 AUROC=0.990 53/56。Rebuttal 同步

**Q1** (Frozen diagnostic): 引用 "2/2 original validation + 3 additional seeds s3-s5" — exp_068 (008d repro s1) 现在提供第 6 个 trained seed 数据 (NVE 4.12, collapse)。可考虑补充

---

### Appendix 缺失

以下已完成实验 (conclusion=success) 不在 appendix Table complete_results 中：

| 缺失实验 | 配置 | 关键指标 |
|----------|------|---------|
| exp_074 (008a_s3) | Unexposed emb s3 | eval 855.9, no CIVO |
| exp_072 (008e_v3_s5) | Mitigation s5 | eval 853.1, NVE 0.61, healthy |
| exp_071 (008f_s3) | No dt_emb s3 | eval 311.9, NVE 0.4, healthy |
| exp_073 (008f_s4) | No dt_emb s4 | eval 289.3, NVE 0.76, healthy |
| exp_068 (008d repro s1) | Trained s1 repro | eval 39.1, NVE 4.12, collapse |
| exp_067 (frozen plan015) | Frozen s0 dedicated | eval 281.5, NVE 0.19, healthy |
| Cartpole exps (060-062) | 跨环境验证 | 未在 appendix 中出现 |

注：exp_066/066b (RSSM fidelity timeseries)、exp_064 (value distribution)、exp_065 (cosine) 是分析实验，内容已在 appendix 正文引用，无需加入训练结果表。

---

### 数据一致性问题

1. **实验总数不一致**：ROADMAP 写 155/78 success，report 写 153/79 success，rebuttal 写 133/63 success → 三处数字互不相同，需统一

2. **NVE 指标版本分歧**：
   - 论文正文 (methodology/analysis/conclusion)：n=56, AUROC=0.990, F1=0.941 ✓
   - Appendix §ROC figure caption：n=30, AUROC=0.957（ROC 图本身）
   - Appendix §Comprehensive validation 段落：n=56, AUROC=0.990 ✓
   - Provenance C047-C053：n=32, AUROC=0.961 ← **过时**，与论文正文 (0.990) 和 appendix (0.957/0.990) 均不一致
   - Rebuttal：n=30, AUROC=0.957 ← **过时**

3. **Provenance C004/C011/C018/C042**：仍引用旧的 "7/8 classification (n=8)" 和 "AUROC=0.933"。论文正文和 appendix 已更新到更大样本量，但这些 provenance 条目未同步

4. **Appendix cross-domain table (Tab cross_domain)**：Walker trained 列 "5/5"，但现在有 exp_068 (s1 repro) 和 exp_059 (s5) 等额外 seeds。如果论文声称 "7/7 onset"（rebuttal Q8/Q14），appendix 表格应反映完整 seed count

5. **008a seed count**：appendix 仅列 3 seeds (008a, 008a_s1, 008a_s2)。exp_074 完成后应为 4 seeds。provenance C023 引用 008a eval=777.7 只是 s0 数据，4-seed summary (mean 791, std 102.2) 可加强 C3 claim

---

### 优先级建议

**数据锁定 5/27 前必须完成（不依赖在跑实验）：**
1. 统一实验计数（ROADMAP/report/rebuttal 三处对齐）
2. Appendix table 补充 exp_074/072/071/073/068/067 行
3. Rebuttal Q&A 实验计数和 NVE 数字更新到最新
4. Provenance C047-C053 从 n=32/AUROC=0.961 更新到 n=56/AUROC=0.990
5. ROADMAP 更新运行状态

---
