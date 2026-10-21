# research paper readiness check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_paper-readiness-check_20260514T062052_result.json`
- **Structured JSON:** [`a0b623fbb00f7731cf89.json`](../../sessions/a0/a0b623fbb00f7731cf89.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕，以下是结构化评估报告。

---

# 论文数字就绪度评估报告

**项目**: exec-sim-repair-verifier | **目标**: EMNLP 2026 ARR May 25 | **剩余**: 11 天

---

## A. 已确定的数字（可直接写入论文）

### C1: Complexity-Dependent Reformulation Advantage

**Function-level（100% settled）**

| 指标 | 值 | 来源 |
|------|-----|------|
| CLS 4B 5-seed mean | 88.43±0.78% | multi-seed-core + cls-seed789 + cls-seed0 |
| CWM 4B 5-seed mean | 87.19±0.37% | cwm-baseline + cwm-seed123/456/789/0 |
| CLS-CWM 4B gap | +1.25pp (one-sided p=0.025) | 5-paired-clustered-bootstrap |
| CLS 8B 3-seed mean | 89.39% (42=90.48, 123=89.37, 456=88.31) | model-size-scaling-cls8b + cls8b-seed123/456 |
| CWM 8B 3-seed mean | 86.96% (42=87.67, 123=86.98, 456=86.24) | model-size-scaling-cwm8b + cwm8b-seed123/456 |
| CLS-CWM 8B gap | ~2.43pp | 上述 3 seed 对比 |
| 4B→8B CLS scaling | +2.07pp (seed42) | model-size-scaling-cls8b |
| 4B→8B CWM scaling | +0.16pp (seed42), CWM 碰天花板 | model-size-scaling-cwm8b |
| LLM Judge 8B zero-shot | 64.4% | llm-judge-8b-zeroshot |
| LLM Judge 32B zero-shot | 71.7% | llm-judge-32b-zeroshot |
| Fine-tuned 4B vs zero-shot gap | +24pp (vs 8B), +16.7pp (vs 32B) | 上述两项 |

### C2: Diagnostic Granularity At Equivalent Accuracy（100% settled）

| 指标 | 值 | 来源 |
|------|-----|------|
| TOST equivalence p-value | 0.0071 (±2pp margin) | 5-paired-clustered-bootstrap |
| Pooled gap (CLS vs TRAJ) | -0.40pp, 95% CI [-1.32, +0.52] | 同上 |
| ICC (block correlation) | 0.191, DEFF=3.97 | block-corr-empirical |
| Seeds 789/0 NF4 quantization | 需在论文中注明 | cls-seed789, cls-seed0 |

### C3: Accuracy-Utility Frontier（100% settled）

| 指标 | 值 | 来源 |
|------|-----|------|
| T=1 instances 占比 | 68.7%, per-test advantage ≈ 0 | oracle-f2p-stratified |
| T≥2 instances 占比 | 31.3%, advantage 显著 | 同上 |
| T=2 贡献整体优势占比 | 55.3% | 同上 |
| P2P regression rate | 1.04% mean / 0% median | p2p-regression-rate |
| Majority voting (K=3) | -0.69pp（negative） | per-test-majority-voting |
| Per-test fail precision/recall | 82.75% / 93.64% | per-test-precision-recall |
| Best mutation type | return_value (97.26%) | 同上 |
| Worst mutation type | off_by_one (82.56%) | 同上 |

### 辅助数据（settled）

| 指标 | 值 | 来源 |
|------|-----|------|
| 训练数据量 | 19,076 samples (52% pass / 48% fail) | mvp-b-data-prep |
| 5 种 mutation types | ✅ | 同上 |

---

## B. 待确定的数字（正在跑或未开始）

### 🔴 Critical Path（阻塞论文最终数字）

| 缺失项 | 状态 | ETA | 影响 Section |
|--------|------|-----|-------------|
| **CWM v12 全量 eval** | RUNNING ~25% | ~02:20 UTC May 15 (~20h) | Table 4 repo-level CLS-CWM gap 最终值 |
| **CWM seed123 全量 eval** | RUNNING ~25% | ~02:30 UTC May 15 (~20h) | repo-level paired bootstrap CI |
| **D063: val set checkpoint sweep** | 未开始，需修 eval 脚本 | 修完后 ~数小时 | **所有** repo-level CLS best checkpoint 可能变化 |

### 🟡 Nice-to-Have（增强论文但非必须）

| 缺失项 | 状态 | ETA | 影响 Section |
|--------|------|-----|-------------|
| 8B CWM repo-level training | RUNNING (GPU 2, PID 210568) | ~8-10h 训练 + eval | 2×2 scaling table, "CWM failure is scale-invariant" |
| 8B CLS seed123 repo-level training | RUNNING (GPU 3, PID 210652) | ~8-10h 训练 + eval | 8B multi-seed robustness |
| CWM unparseable + error mode 分析 | 未开始 | CWM eval 完成后 | Error analysis section |
| CLS/CWM error complementarity（oracle ensemble） | paper_framing 中提到 90.63% | 需确认数据来源 | Discussion |

---

## C. 方法论风险

### 🔴 D063 Val Set 修复（高风险）

**问题**: 所有 repo-level checkpoint sweep 在 test set (9784 samples) 上做 = cherry-picking。

**影响范围**:
- repo-level-cls-v5-conda: 当前 ckpt-600 (76.37%) 可能不是 val set 最佳
- repo-level-cls-seed123-home: 当前 ckpt-600 (80.73%) 可能变化
- repo-level-cls-8b-conda: 当前 ckpt-400 (84.52%) 可能变化
- CWM 同理（虽然 CWM eval 还没跑完 sweep）

**最坏情况**: val set 选出的 checkpoint 在 test set 上表现差几个百分点，但 CLS-CWM gap 方向性几乎不可能逆转（CWM ~58% vs CLS ~76-84%，gap >18pp）。

**建议**: 数字可能小幅调整，但 narrative 安全。论文中可先用当前数字写，D063 修复后替换。

### 🟡 CWM Eval 完成后的风险

CWM v12 running acc ~58.3%（2500+ samples），趋势稳定（波动 <0.3pp/百样本）。25% → 100% 大幅变化的可能性很低。但最终数字可能在 56-60% 范围内微调。

**对 narrative 影响**: CLS-CWM repo-level gap 预计 18-26pp，C1 "classification advantage scales with complexity" 结论稳固。

### 🟢 8B CWM 训练结果

若 8B CWM 也在 repo-level 表现差（预期如此，因为 token exhaustion 是结构性问题），则论文可声称 "CWM failure is scale-invariant"。若 8B CWM 意外表现好，需调整 narrative 但不影响 C1 核心结论（4B 层面差距已确认）。

---

## D. 可立即开始撰写的 Sections

### ✅ 不依赖任何 pending 数字

| Section | 理由 |
|---------|------|
| **Method** | 所有 formulation（CLS/CWM/TRAJ）、数据构建、训练设置已定义完毕 |
| **Function-level Results（全部）** | 5-seed CLS/CWM 对比、8B scaling、LLM judge baseline，数字 100% settled |
| **C2: Diagnostic Granularity** | TOST 等价检验完成，所有统计数字确定 |
| **C3: Oracle Frontier** | T 分层分析、P2P regression rate、block correlation 全部完成 |
| **Statistical Methodology** | clustered bootstrap、TOST、ICC/DEFF 方法已验证 |
| **Related Work** | 文献覆盖较充分（见 Section E） |
| **Introduction** | Story spine 已成型，可用 placeholder 处理 repo-level gap |

### 📝 可用 placeholder 先写

| Section | Placeholder 内容 |
|---------|-----------------|
| **Repo-level Results (Table 4)** | CLS 用当前数字，CWM 用 "~58% (preliminary)" |
| **Abstract headline** | repo-level gap 用 "[Z] percentage points" 占位 |
| **Error Analysis** | 待 CWM eval 完成后补充 unparseable/token budget 分析 |
| **Scaling Table (2×2)** | 8B CWM repo-level 待补 |

---

## E. 文献缺口

### literature_map.yaml 覆盖统计

| 类别 | 已有 | 缺口 |
|------|------|------|
| Execution Simulation | 5/5 | ✅ 无 |
| LLM Verification for Code | 5/5 | ✅ 无 |
| APR and SWE-bench | **7/8** | ❌ 缺 1 篇（类别标注 "gap 1"，未指明具体缺什么） |
| Code LLMs and Benchmarks | 6/6 | ✅ 无 |
| Task Reformulation NLP | **3/4** | ❌ 缺 1 篇（需一篇 classification vs generation 在其他 NLP 任务的系统性对比） |
| Statistical Methods | **2/3** | ❌ 缺 1 篇（可能需要 clustered bootstrap 的原始参考或 ICC/DEFF 的经典引用） |

**Related Work 写作评估**: 已有 28 篇 verified 文献，覆盖 6 个核心类别。Dream #5 审稿指出 "related work ≤7 refs 需 15+"，当前 28 篇足够支撑扩写。3 个 gap 需要补充但均非关键阻塞。

**建议补充方向**:
1. APR gap: 考虑补一篇最新 SWE-bench leaderboard 分析或 SWE-agent v2 等
2. Task Reformulation gap: 补一篇 extractive vs generative QA 的系统性对比（如 FiD 或 RAG 类工作）
3. Statistical gap: 补 ICC 原始论文（Shrout & Fleiss 1979）或 design effect 的经典教科书引用

---

## 总结

**论文写作可立即开始**: Method、Function-level Results、C2、C3、Related Work 不依赖任何 pending 实验。

**关键阻塞项**: CWM v12/seed123 全量 eval (~20h) + D063 val set 修复。两者完成后 repo-level 数字才能定稿，但 C1 gap 方向性（CLS >> CWM）已极度稳固。

**时间风险**: 11 天中 CWM eval 占 ~1 天，D063 修复 + val sweep 占 ~0.5-1 天，8B 训练+eval 占 ~1-1.5 天。写作窗口 ~7-8 天，足够。

---
