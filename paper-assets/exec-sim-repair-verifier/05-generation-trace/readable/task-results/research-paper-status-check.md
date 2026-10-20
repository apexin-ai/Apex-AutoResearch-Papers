# research paper status check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_paper-status-check_20260515T221247_result.json`
- **Structured JSON:** [`78cbe3cd439edae664b2.json`](../../sessions/78/78cbe3cd439edae664b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 论文写作状态报告

### 1. writing_plan.yaml 状态

| 章节 | 预算 | 实际词数 | 状态 |
|------|------|---------|------|
| abstract | 200w | ~243w | **完成** |
| introduction | 1000w | ~551w | **完成** |
| method | 1000w | ~671w | **完成** |
| experiments | 2800w | ~1884w | **完成** |
| related_work | 600w | ~381w | **完成** |
| conclusion | 400w | ~341w | **完成** |
| **合计** | **6000w** | **~4071w** | 在 8 页限内 |

所有章节均已完成 full draft，总字数 ~4071（含 LaTeX 命令），实际正文约 3200-3500 词，符合 8 页限制。

### 2. .tex 文件完成度

| 文件 | 内容 |
|------|------|
| `main.tex` | 主文件，所有 section 已 include，3 个 figure 已放置 |
| `abstract.tex` | 完整，覆盖全部 3 个 claims + 关键数字 |
| `introduction.tex` | 完整，3 个贡献点 itemized，引用充分 |
| `method.tex` | 完整，4 个 subsection（formulations, failure modes, oracle framework），公式 (1)-(3) |
| `experiments.tex` | 最充实，7 个 subsection + 5 个 table + 8 段 analysis，含 LoRA rank ablation |
| `related_work.tex` | 完整，5 段覆盖 execution sim / verification / learned verifiers / APR / NLP reformulation |
| `conclusion.tex` | 完整，limitations 和 future work 均有 |
| `references.bib` | 27 条，覆盖所有 citation clusters |

`paper/method.tex` 是早期草稿（更详细，~9KB），`docs/paper/method.tex` 是精简后的正式版本（~4.5KB）。

### 3. 图表产出

**Figures（均已生成 PDF+PNG）:**
- `fig1_reformulation` — 三种 formulation 概念图 ✅
- `fig2_gap_amplification` / `fig2_scaling_gap` — CLS vs CWM scaling gap ✅
- `fig3_oracle_stratified` — Oracle per-test advantage by T ✅
- `rank_ablation_chart` — LoRA rank 消融图（supplementary）✅

**Tables（在 experiments.tex 内）:**
- Table 1: Function-level main results (CLS/CWM/TRAJ/ZS) ✅
- Table 2: Model-size scaling 4B→8B ✅
- Table 3: Oracle accuracy-utility frontier ✅
- Table 4: Repo-level results ✅（CWM 8B 行仍为 `---`）
- Table 5: LoRA rank ablation ✅

### 4. 整体完成度：**~85%**

Full draft 已完成，但有关键 gaps：

**实验缺口（blocking）：**
- CWM 8B repo-level 训练中（ETA May 16 05:30），完成后需 eval 填入 Table 4，解锁 8B-8B direct comparison
- D096 已决策切换主表为 8B-8B 对比（双 seed gap 更稳健：25.48/26.51pp），需改写 abstract/intro/experiments 中的 primary claim

**Review Round 1 未解决的 issues（12 项 in_progress）：**
- **Critical:** R1-N1（单 seed 问题，已有 8B-8B 修复方案）、R1-N2（CWM 8B 缺失）
- **Warning:** TOST margin justification、scaling argument 弱化措辞、mutation type distribution shift 分析、relaxed matching 写入论文、ecological validity 讨论、per-test diagnostic 贡献降级、first author 核查、NF4 seed 标注
- **Info:** "below chance level" 措辞

### 5. 下一步最紧急任务（按优先级）

1. **等 CWM 8B 训练完成 → eval → 填 Table 4**（blocking，ETA ~14h）
2. **按 D096 决策改写 primary claim 为 8B-8B**（abstract/intro/experiments 中替换 25.59pp 单 seed → 双 seed 25.48/26.51pp）
3. **批量处理 Round 1 review issues**：relaxed matching 写入 analysis、TOST margin justification、scaling argument 措辞弱化、limitations 增加 synthetic-to-real 讨论
4. **LaTeX 编译检查**：确认页数、figure placement、reference 格式
5. **Final proof**：数字一致性（registry vs tex）、bib first author 核查剩余项

---
