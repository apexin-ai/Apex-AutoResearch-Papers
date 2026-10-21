# research check paper agent figure progress

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_check-paper-agent-figure-progress_20260515T215752_result.json`
- **Structured JSON:** [`a8a785811f3f5076b9c4.json`](../../sessions/a8/a8a785811f3f5076b9c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the assessment.

---

## 论文图表完成度清单

### Figures

| ID | 描述 | 位置 | PDF 存在 | TeX 引用 | 状态 |
|---|---|---|---|---|---|
| fig1_reformulation | 三种验证范式概念图 | `artifacts/figures/paper/fig1_reformulation.pdf` | ✓ | main.tex L41 | **已完成** |
| fig2_scaling_gap | CLS vs CWM 4B→8B scaling | `artifacts/figures/paper/fig2_scaling_gap.pdf` | ✓ | main.tex L52 | **已完成** |
| fig3_oracle_stratified | Oracle per-test advantage by F2P T | `artifacts/figures/paper/fig3_oracle_stratified.pdf` | ✓ | main.tex L59 | **已完成** |

注：writing_plan 中的 `fig2_gap_amplification`（3-bar 复杂度递增图）已生成 PDF，但论文实际改用了 `fig2_scaling_gap`（4B→8B 对比图）。gap_amplification 版本在 artifacts 中备用但未引用。

### Tables

| ID | 描述 | 位置 | 状态 | 备注 |
|---|---|---|---|---|
| tab1_main_results | 函数级主结果 (5 seeds) | experiments.tex L25-44 | **已完成** | |
| tab2_scaling | 4B→8B scaling (3 seeds) | experiments.tex L54-71 | **已完成** | |
| tab3_oracle | Oracle accuracy-utility frontier | experiments.tex L89-108 | **已完成** | |
| tab4_repo_level | Repo-level 对比 | experiments.tex L118-140 | **80% — 缺 CWM 8B** | CWM 8B 行全 `---`，训练中 |
| tab5_rank_ablation | LoRA rank 消融 | experiments.tex L180-195 | **已完成** | 回应 R1-N3 新增 |

### Rank32 ablation 数据整合状态

- `cwm-rank32-ablation-v2`: acc=87.00%, Δ=-0.51pp → **已写入 tab:rank_ablation**
- `cwm-rank32-alpha64-ablation`: acc=87.04%, Δ=-0.47pp → **已写入 tab:rank_ablation**
- 数据锁定在 `artifacts/rank_ablation_data.json`，含 seq_length ablation
- 注：这两个实验在 registry 中查询返回空（count=0），但数据文件和 tex 表格均已就绪。registry 可能未注册或 ID 不匹配。

### Tex 文件状态

| Section | 文件 | 字数 (估) | 状态 |
|---|---|---|---|
| abstract | abstract.tex | ~200 | 已写 |
| introduction | introduction.tex | ~900 | 已写 |
| method | method.tex | ~1000 | 已写 |
| experiments | experiments.tex | ~2800 | 已写（含 rank ablation + relaxed matching + seq_length 消融） |
| related_work | related_work.tex | ~600 | 已写 |
| conclusion | conclusion.tex | ~400 | 已写 |
| main.tex | main.tex | 框架 | 已完成，可编译 (main.pdf 358KB) |

---

## 评估结论

**Step 2 图表阶段：95% 完成。** 所有 3 张 figure 和 5 张 table 已生成并嵌入 tex。唯一缺口是 tab4_repo_level 中 CWM 8B 行（训练 57%，ETA May 16 05:30 UTC）。

## 下一步推进建议

**紧急 P0（阻塞投稿）：**
1. **CWM 8B repo-level eval** — 训练完成后立即 eval，填入 tab4 CWM 8B 行。这是完成 8B-8B same-size 对比的唯一阻塞项。
2. **Review issues 修复** — `review_issues.yaml` 中 13 个 issue 仍 in_progress（2 critical, 8 warning, 3 info）。最紧急的：
   - R1-N1: 切换主表为 8B-8B 对比（D096 已决策，Paper Agent 写入中）
   - R2-W4: 标题 "Scales" → "Succeeds"/"Persists"
   - R2-W6: Related Work 补 LEVER/CodeT 引用
   - R1-M4: Method 明确 unparseable → majority 策略
   - R2-M2: 移除内部编号 "D088 protocol"

**P1（质量提升）：**
3. 将 `fig2_gap_amplification`（含 repo-level 25.59pp bar）替换或补充当前 fig2_scaling_gap — 原始 gap amplification 图更直观展示 complexity-dependent advantage 的核心 claim
4. Registry 注册缺失的 rank32 ablation 实验条目

**Paper Agent session 状态：** 从 artifacts 时间戳看（最新 19:49），session 今天还在活跃。实验 tex 和 figures 在持续更新中。如果 session 已停止，需要重新派单的任务是：**CWM 8B eval 后更新 tab4 + 批量修复 review_issues 中的 paper-assigned items**。

---
