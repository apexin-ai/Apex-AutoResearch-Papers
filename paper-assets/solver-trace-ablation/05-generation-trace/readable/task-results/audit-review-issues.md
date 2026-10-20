# audit review issues

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_review-issues_20260522T120904_result.json`
- **Structured JSON:** [`57e91efbe8757a504491.json`](../../sessions/57/57e91efbe8757a504491.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 未解决 Issues 完整列表

### CRITICAL（必须修复）— 13 个

| ID | 描述 | Status | 首次出现 | 最新出现 | 修复方向 |
|---|---|---|---|---|---|
| v17-R12-W1 | 单模型 (Qwen3-4B) 无法支撑通用性声明 | in_progress | R17 | R28 | 正文 claim 限缩到单模型范围 |
| v19-R12-W3 | ProofFOL p=0.10 被过度引用，same-task-family 非 cross-domain | in_progress | R19 | R29 | p=0.10 降级措辞，已改标题为 'within-FOL cross-dataset replication' |
| v17-R1-W9 | Seed 43 使用 T=0.7 sampling 评估而非 greedy | in_progress | R17 | R28 | 需 greedy re-eval 或排除 seed 43 |
| v27-R1-N4 | Seed 43 T=0.7 + checkpoints 已删除不可恢复 | in_progress | R27 | R28 | 排除 seed 43 改 N=2 报告，或标注 caveat |
| v22-R12-N1 | ISR vs Random N-H rate p=0.182 不显著，Goodhart claim 缺统计支撑 | in_progress | R22 | R28 | 弱化 causal claim，补充 effect size |
| v22-R12-N3 | Premise-count confound 使 ISR 3.2×→1.06× | in_progress | R22 | R28 | 正文前置 confound 讨论，考虑 normalized ISR |
| v23-R12-N1 | N=3 seeds 统计效力不足 | in_progress | R23 | R28 | 扩展 key condition 到 N=5，或 power analysis caveat |
| v23-R2-W3 | 与 Helff et al. (2026) IPT 对比不充分 | in_progress | R23 | R28 | 补系统对比表格 |
| v25-R12-N1 | 5-seed 与 3-seed 矛盾——N-H% 18 vs 6 | in_progress | R25 | R28 | seed-dependent 波动正文讨论 |
| v25-R12-N2 | Abstract/Intro 以 raw ISR 214× 为核心叙事 | in_progress | R25 | R28 | 替换为 matched ISR 或 effect size |
| v25-R2-N1 | Goodhart taxonomy 映射不严谨 | in_progress | R25 | R28 | 已部分解决（v27-R12-N2 放弃新术语），需检查残留 |
| v27-R12-N1 | STA 与 Helff 2026 IPT 概念同构，区分不充分 | in_progress | R27 | R28 | 补技术对比表格 |
| v27-R12-TAXONOMY | Taxonomy 分类规则 black box，不可复现 | in_progress | R27 | R28 | 补 confusion matrix + threshold sensitivity |
| v27-R2-W1 | ISR 对 TS 反向效果未在正文讨论 | open | R27 | R28 | 正文补 per-mode 诊断力差异讨论 |
| v28-R1-N1 | ISR 聚合 vs per-sample 诊断未分离 | open | R28 | R28 | §3 补 ISR 双重用途 + confound 影响 |

### WARNING（应修复）— 15 个

| ID | 描述 | Status | 最新 |
|---|---|---|---|
| v19-R1-W6 | Classifier recall 未知 + PG 审计仅 seed 42 | in_progress | R28 |
| v16-R1-W2 | LOO 独立性假设未量化偏差 | in_progress | R28 |
| v16-R1-W4 | ISR-as-reward 乘法耦合混淆 | in_progress | R28 |
| v22-R2-N1 | 方法论新颖性不足（LOO 是标准技术） | in_progress | R28 |
| v22-R1-W1 | ProofFOL genuine 用 coarser classifier | in_progress | R28 |
| v22-R1-W4 | Shuffled-ISR control N=46 效力有限 | in_progress | R27 |
| v22-R1-W5 | SFT PR confound 仅 100-step (n=32) 部分缓解 | in_progress | R28 |
| v23-R1-N3 | 乘法耦合需 constant-bonus control | in_progress | R27 |
| v23-R2-N1 | Case study 标题与通用声称 framing 矛盾 | in_progress | R28 |
| v25-R1-W5 | Table 1 exec-only 仅 seed 42 | in_progress | R27 |
| v25-VISUAL-W1 | Figure 3 色盲可读性差 | in_progress | R28 |
| v27-R1-N2 | CMH pseudo-replication | in_progress | R28 |
| v27-R1-W7 | Non-hacking rate classifier recall 跨条件不一致 | in_progress | R28 |
| v27-R2-W3 | Title 'Structural Degeneration' 概念跳跃 | in_progress | R28 |
| v27-R2-W4 | Taxonomy 验证 50 样本偏少 | in_progress | R28 |
| v27-R2-MR-PRM | ISR 与 PRM 概念联系未讨论 | open | R27 |
| v27-R1-W4 | 100-step checkpoint n=32 样本量不足 | open | R27 |
| v28-R1-M4 | 50% exec-only seeds 不收敛，影响未讨论 | open | R28 |
| v17-VISUAL-LAYOUT | Display items 分布不均 (pp5-6 纯文本) | in_progress | R28 |

### INFO（可选修复）— 10 个

| ID | 描述 | Status |
|---|---|---|
| v22-R2-W3 | 与 Kim et al. 区分不清 | open |
| v21-R1-N1 | 新增引用整合略机械 | open |
| v23-MR-SHAPLEY | 缺 Shapley values 引用 + LOO 选择 justify | open |
| v23-MR-PROSFI | 缺 PRoSFI + Interleaved Bonus 引用 | open |
| v25-MINOR-BIB | FOLIO bib 年份 mismatch | open |
| v27-R2-MR-PROOF-QUALITY | 缺 Proof quality metrics 先行工作引用 | open |
| v27-R2-W6 | Taxonomy 持久性/可迁移性存疑 | open |
| v27-R2-W7 | β 值消融仅两个点 | open |
| v27-R2-MR-MUTATION | 缺 ML mutation testing 引用 | in_progress |
| v28-R12-MR-INFLUENCE | 缺 influence functions 引用 | open |
| v28-VISUAL-APPENDIX | Appendix 末页大面积空白 | open |
| v17-VISUAL-FONT | Figure 内部文字偏小 | in_progress |

---

## DDL 前 (5/25) 必须 vs 可选

### 必须修复（影响审稿评分的 critical + 高频 warning）

| 优先级 | Issue 组 | 工作量 | 说明 |
|---|---|---|---|
| P0 | v17-R1-W9 + v27-R1-N4 (Seed 43) | **大** | 需决策：排除 seed 43 → 全文改 N=2 报告，或找到 greedy re-eval 方案。影响 Table 1 + 所有统计 |
| P0 | v25-R12-N2 + v22-R12-N3 (ISR 数值叙事) | **中** | Abstract/Intro 替换 raw 214× 为 matched 1.06×，前置 confound 讨论 |
| P0 | v28-R1-N1 (ISR 聚合 vs per-sample) | **中** | §3 补 1-2 段讨论 |
| P0 | v27-R12-N1 + v23-R2-W3 (STA vs IPT) | **中** | 补对比表格到 §2 或 Appendix |
| P1 | v17-R12-W1 (单模型 claim) | **小** | 扫描全文弱化通用性措辞 |
| P1 | v22-R12-N1 (p=0.182) | **小** | 弱化 Goodhart causal claim |
| P1 | v25-R2-N1 (Goodhart taxonomy) | **小** | 检查 v27-R12-N2 修复后残留 |
| P1 | v27-R12-TAXONOMY | **中** | Appendix 补分类规则 + validation |
| P1 | v27-R2-W1 (ISR per-mode 差异) | **小** | 正文补 1 段 |
| P1 | v23-R12-N1 (N=3 power) | **小** | 正文已有 caveat，强化措辞即可 |

### 可延后（不影响接收决定）

- 所有 INFO 级别
- 视觉排版类 (VISUAL-*)
- 缺失引用类 (MR-*)：补引用工作量小但不紧急
- v16-R1-W4, v23-R1-N3 (乘法耦合)：连续多轮未被单独提及

### 预估总工作量

- **P0 组**：~4-6 小时（Seed 43 决策最耗时）
- **P1 组**：~3-4 小时（多为文本修改）
- **可选组**：~2-3 小时

5/25 前完成 P0+P1 可行，建议先解决 Seed 43 决策（P0 最大阻塞项），其余为文本/framing 修改可并行推进。

---
