# research data source unification

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_data-source-unification_20260514T080027_result.json`
- **Structured JSON:** [`4c814ac98626b126b7c8.json`](../../sessions/4c/4c814ac98626b126b7c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部任务完成。总结如下：

---

## 产出 1: 权威数据源确认

**文件**: `results/death_decomposition_report.json` (westb-13313)

| 指标 | 权威值 |
|------|--------|
| n_tasks | 30 |
| n_episodes | 249 |
| Δ_full | +38.33 |
| Δ_nd | +0.48 |
| DAF | 0.9875 (98.75%) |
| Pearson r | 0.9864 |
| p-value | < 0.0001 |
| Labels | det:102 / int:1 / no:146 |
| Signal source | death_asymmetry:93 / score_comparison:10 / tied_alive:117 / both_dead:29 |

**find-non-living-thing 修正**: n=5, Δ=-6.80 (internal-preferred), NOT n=40/Δ=+9.58

## 产出 2: paper_framing.md ✅ 已更新

所有数字统一到 30 tasks / 249 eps 权威源，末尾新增 Data Provenance Note。

## 产出 3: paper_provenance.yaml ✅ 已修复

修复内容:
- C003: value 0.99 → 0.9875
- C006: Δ_full 37.9→38.33, Δ_nd 0.2→0.48
- **C010: r=0.989 → 0.9864** (解决 C010 vs C053 不一致)
- **C053: r=0.986 → 0.9864** (现在与 C010 一致)
- C015/C028: 标签分布精确化 (102/1/146 out of 249)
- C024: 所有值精确化
- C031: 新增 93/102=91.2% 量化
- C035: value 0.99 → 0.9875
- 全部 claim 添加 source 字段指向 report.json
- version 11→12, 新增 `data_authority` 和 `numbers_unified` 元数据

## 产出 4: 仍引用旧数字的文件清单

| 文件 | 旧数字 | 优先级 |
|------|--------|--------|
| **artifacts/paper_data_tables.md** | 全部旧数字 (29.60, 2.84, 90.41%, 0.9698, find-non-living-thing n=40/+9.58) | P0 — 论文直接引用 |
| **ROADMAP.md** | 11 tasks/245 eps, 所有旧指标, find-non-living-thing +9.58 | P0 |
| **memory.md** | 245 eps, 29.60, 2.84, 90.41%, 0.9698 | P1 |
| **report.md** | "194 episodes / 11 tasks" (plan-003-baseline) | P1 |
| **artifacts/_project/paper/paper_outline.md** | 29.60, 2.84, 90.41% | P1 |
| **artifacts/_project/report/number_consistency_audit.md** | 多处旧数字 | P2 — 审计文件本身需重写 |
| **artifacts/manifest.yaml** | 245 eps, find-non-living-thing 40eps/+9.58 | P2 |
| **registry.yaml** | 245 eps, 90.41%, 0.9698 等 | P2 |
| **decisions.yaml** | D018/D019 中引用旧 intermediate 数字 | P3 — 历史记录，不宜修改 |
| **task_context/agent.md** | 11 tasks/245 eps | P3 |

**decisions.yaml 不建议修改** — 它记录的是当时的决策依据，修改历史记录会掩盖认知演进过程。

---
