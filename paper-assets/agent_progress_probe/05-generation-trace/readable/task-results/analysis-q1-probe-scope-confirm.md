# analysis q1 probe scope confirm

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_q1-probe-scope-confirm_20260516T051751_result.json`
- **Structured JSON:** [`559e74a7515c5c1a350e.json`](../../sessions/55/559e74a7515c5c1a350e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the confirmation report:

---

## Q1 确认报告

### 1. Probe "All" vs "Conf≥2" 为何相同 (0.598)

**原因：Probe cross-agent eval 的数据文件本身就只包含 conf≥2 windows。**

- Probe 评估使用的是 `embeddings_fixed_conf2.pt`（43,366 个 OH windows，全部 conf≥2）
- 对该文件做 trajectory-level split，test split 为 N=6,122
- Table 1 中 "All" 和 "Conf≥2" 列评估的是**完全相同的 6,122 个 windows**
- "All" 并不是指全部 143K OH windows，而是 eval 文件中的全部 windows（本身已经是 conf≥2）

如果真的在全部 143K OH windows 上评估 probe，macro_f1 = 0.530（来自 `cross_agent_results.json`），远低于 0.598。

### 2. Probe OH test split 详情

| 指标 | 值 |
|------|-----|
| N | 6,122 |
| Stagnation | 1,179 (19.3%) |
| Progress | 4,943 (80.7%) |
| Confidence | 全部 ≥ 2 (来源文件: `embeddings_fixed_conf2.pt`) |
| Split 方式 | Trajectory-level, seed=42 |

### 3. GB Matched-Scope Metrics (同一 6,122 test split)

| 指标 | GB | Probe (zero-shot) |
|------|-----|-----|
| macro_f1 | **0.9923** | 0.5984 |
| f1_stag | **0.9876** | 0.3074 |
| f1_prog | **0.9971** | 0.8895 |

### 4. Gap (GB − Probe)

| 指标 | Gap |
|------|------|
| macro_f1 | **+39.39pp** |
| f1_stag | +68.02pp |
| f1_prog | +10.76pp |

Paired bootstrap (from `bootstrap_table2_matched.json`): delta=+39.44pp, 95% CI=[37.86, 41.04], p=0.0

### 结论

审稿人的怀疑是正确的：Probe "All" 列不是在全部 OH windows 上的评估，而是与 "Conf≥2" 列指向同一子集。Table 1 中 Probe 行需要修正——要么补充真正的 "All" 数字 (0.530)，要么在表注中说�� Probe 的 eval scope 是 conf≥2。

---
