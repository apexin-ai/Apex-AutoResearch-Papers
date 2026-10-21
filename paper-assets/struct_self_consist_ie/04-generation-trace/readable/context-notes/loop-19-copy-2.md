# reviewer / loop_19.md

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_19.md`
- **Structured JSON:** [`840d2f1047c9df534901.json`](../../sessions/84/840d2f1047c9df534901.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 19
reason: max_wall_time
updated: '2026-05-24T01:32:05+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 autodl-5090，GPU 白名单需查 `execution.gpu_ids`（之前出过 cuda:0 越界事故）
- 论文 EMNLP 2026 主文严格 8 页限制，Limitations 不计页数但只写 3 点一小段
- ARR Responsible NLP Checklist 在 OpenReview form 里手动填，不放进论文 PDF
- Abstract 不超过 200 words
- 项目中存在两种 F1 metric（macro entity-type-averaged vs instance-averaged），混用会导致 ~2pp 系统性偏差——审查数值时务必确认 metric 定义

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090 (root)，工作目录 `/root/autodl-tmp/struct_self_consist_ie`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/`
- 论文源文件：`docs/paper/sections/*.tex`，主文件 `docs/paper/main.tex`
- Registry：`registry.yaml`（本地 workspace 根目录）
- 远程分析产出：`/root/autodl-tmp/struct_self_consist_ie/artifacts/multiseed_inverse_scaling/`（all_results.json 106KB, consistency_report.json 21KB）
- 无活跃训练进程（DDL 5/25，实验阶段已结束，处于提交前审查阶段）

### 3. 📊 当前状态
**所有标记过的 critical/warning 数值问题已全部解决：**
- ✅ α=0.161→0.121 (single_signal.tex:50)
- ✅ M1 LP Δ +0.09→+0.12 (experiments_main.tex:76)
- ✅ M2 degeneracy 31%→26% (experiments_main.tex:76)
- ✅ M3 SciERC degen 13.4%→12.2% (experiments_main.tex:91)
- ✅ U1 "+5-8pp at 80% coverage" 悬空 claim 删除 (experiments_main.tex:106)
- ✅ AUROC .749→.631, SJ 现为 SciERC 最佳 (experiments_main.tex:38,40)
- ✅ MV +0.61→+0.6 (experiments_main.tex:90, introduction.tex:11)
- ✅ Headroom 11.4→13.0pp (single_signal.tex L12,35,39,47)
- ✅ ARR checklist 3 处悬空 Ethics Statement 引用已删
- ✅ 匿名性检查通过，硬编码路径已修复

**未阻塞但需注意：**
- appendix tab:scale_comparison (L1606) 仍有 SciERC Greedy=.667, Hdr=11.4（不同 seed/metric，独立问题）
- SciERC construction +0.32pp vs 5-seed +1.11pp 差异：Worker 的 F1 metric 与论文不同（greedy ~65% vs ~66.7%），未升级 claim，保留原值
- R43 response letter 中 "SciERC FT +1.02pp" 与论文 +0.32pp 不一致（response letter 数据来源待追溯）
- BibTeX shinn2023reflexion 作者 "Edward Berman" 待人工验证

### 4. 📋 待办（条件触发式）
- Worker 提交论文 PDF → 检查最终编译是否 8 页、0 undefined refs、图表完整
- Director 发起 response letter 终稿审查 → 核对 SciERC +1.02pp 来源，建议改为 +0.32pp 或 +1.11pp（取决于 metric 统一结果）
- 新 Worker 修数值 → 独立交叉验证修改后的值与 registry/appendix 一致
- Director 问 SciERC construction 是否升级 → 建议：除非确认 Worker 的 F1 metric 与论文 "macro F1" 一致，否则保留 +0.32pp n.s.

### 5. 🎯 战略上下文
- **核心结论**：QE signals 预测质量 (AUROC 0.82) 但 selection <1pp；correlation-selection gap 由 degeneracy + LP compression + signal alignment collapse 共同造成；entity construction 在低 degeneracy 条件下有条件正向 (+1.40pp Few-NERD)
- **论文 story**：Discover → Diagnose → Construct (exploratory) 三阶段；R43 已将 causal→correlational、prescriptive→exploratory、四贡献→三贡献
- **最容易判断错的事**：
  1. 项目中有两种 F1 metric（差 ~2pp），看到数值不一致先查 metric 定义再下结论
  2. "31%" 是 constant-F1 degeneracy，"26.4%" 是 entity-set exact-match degeneracy——两种定义在不同表格中使用，不要混淆
  3. tab:multiseed 的 SciERC AUROC 与主表用的不是同一个计算方法（已修复，但说明项目中 metric 不统一是系统性问题）
  4. Inverse scaling "40/58" 是跨所有数据集/方法的统计，不要与 FewNERD 单数据集多 seed 的 ~24% 比例混淆


---
