# data d129 complete table compilation

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_d129-complete-table-compilation_20260518T095828_result.json`
- **Structured JSON:** [`ff19d1f06483637d588a.json`](../../sessions/ff/ff19d1f06483637d588a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集完毕。现在编制完整表格。

---

## 完整 1.7B 3×3 Seed 数据

### 数据来源

| Run | 目录 | eval 文件 | classify 来源 |
|-----|------|-----------|---------------|
| ISR 0.1 s42 | w2_1.7b_isr_b01_s42 | eval_results.json | 本次 classify_h7.py |
| ISR 0.1 s43 | d129_1.7b_isr_b01_s43 | eval_results.jsonl | classify_results.json |
| ISR 0.1 s44 | d129_1.7b_isr_b01_s44 | eval_results.jsonl | classify_results.json + 手动 H9 audit |
| Random 0.1 s42 | w2_1.7b_random_b01_s42 | eval_results.json | 本次 classify_h7.py |
| Random 0.1 s43 | d129_1.7b_random_b01_s43 | eval_sta_results.json | classify_results.json |
| Random 0.1 s44 | d129_1.7b_random_b01_s44 | eval_sta_results.json | classify_results.json |
| ISR 0.3 s42 | w2_1.7b_isr_b03_s42 | eval_results.json | classify_h7_results.json |
| ISR 0.3 s43 | d129_1.7b_isr_b03_s43 | eval_greedy/results.jsonl | eval_greedy/classified.json |
| ISR 0.3 s44 | d129_1.7b_isr_b03_s44 | eval_greedy/results.jsonl | eval_greedy/classified.json |

---

### Per-seed 表

**%值均为 of n_proved（非 of n_total=100）**

| Condition | Seed | n_proved | PR | ISR* | H7 | H1 | H8 | Genuine | CI | S-Gen |
|-----------|------|----------|------|------|------|------|------|---------|------|-------|
| ISR 0.1 | s42 | 100 | 1.00 | 0.600 | 0 (0%) | 100 (100%) | 0 (0%) | 0 (0%) | 100 (100%) | 0 |
| ISR 0.1 | s43 | 60 | 0.60 | 0.750 | 60 (100%) | 0 (0%) | 0 (0%) | 0 (0%) | 60 (100%) | 0 |
| ISR 0.1 | s44 | 82 | 0.82 | 0.440 | 0 (0%) | 32 (39.0%) | 15 (18.3%) | 35 (42.7%) | 77 (93.9%) | 3 |
| Random 0.1 | s42 | 93 | 0.93 | 0.028 | 0 (0%) | 78 (83.9%) | 1 (1.1%) | 15 (16.1%) | 93 (100%) | 0 |
| Random 0.1 | s43 | 100 | 1.00 | 0.051 | 0 (0%) | 76 (76.0%) | 0 (0%) | 24 (24.0%) | 100 (100%) | 0 |
| Random 0.1 | s44 | 100 | 1.00 | 0.007 | 0 (0%) | 84 (84.0%) | 0 (0%) | 16 (16.0%) | 100 (100%) | 0 |
| ISR 0.3 | s42 | 17 | 0.17 | 0.182 | 0 (0%) | 12 (70.6%) | 0 (0%) | 5 (29.4%) | 1 (5.9%) | 5 |
| ISR 0.3 | s43 | 52 | 0.52 | 0.231 | 0 (0%) | 14 (26.9%) | 0 (0%) | 38 (73.1%) | 52 (100%) | 0 |
| ISR 0.3 | s44 | 92 | 0.92 | 0.236 | 0 (0%) | 1 (1.1%) | 1 (1.1%) | 90 (97.8%) | 92 (100%) | 0 |

---

### Pooled 表（mean±std across 3 seeds，std=sample std ddof=1）

| Condition | PR mean±std | ISR* mean±std | H1% pooled | H7% pooled | Genuine% pooled | CI% pooled | S-Gen pooled |
|-----------|-------------|---------------|------------|------------|-----------------|------------|--------------|
| ISR 0.1 | 0.81±0.20 | 0.597±0.155 | 132/242=54.5% | 60/242=24.8% | 35/242=14.5% | 237/242=97.9% | 3/242=1.2% |
| Random 0.1 | 0.98±0.04 | 0.029±0.022 | 238/293=81.2% | 0/293=0% | 55/293=18.8% | 293/293=100% | 0/293=0% |
| ISR 0.3 | 0.54±0.38 | 0.216±0.030 | 27/161=16.8% | 0/161=0% | 133/161=82.6% | 145/161=90.1% | 5/161=3.1% |

---

### H9 验证

**来源**: `worker_audit_d129-1_7b-isr-b01-s44-genuine` 的手动审查结果（保存于 `_result.json`）

ISR β=0.1 s44 的 35 个 "genuine"（escaped H1/H7/H8）的手动分类：

| 类别 | 数量 | 占 35 genuine |
|------|------|--------------|
| H9: Pure Conjunction (零步推理) | 16 | 46% |
| H9: Shallow Chain (1-hop + 合并) | 12 | 34% |
| Borderline Genuine (2-3 hop) | 5 | 14% |
| Weird/Degenerate (ISR=0) | 2 | 6% |

- H9 **不在** classify_h7.py 的检测范围内，是 worker 手动审查标注的
- H9 总计 28-30 个（取决于是否将 Degenerate 计入），占 genuine 的 80-86%
- 修正后 ISR b01 s44 真实 genuine = **5/82 = 6.1%**
- H9 机制：模型生成 `∀x(A→B1), ∀x(A→B2)...` 前提，合并为 `∀x(A→B1∧B2∧...)` 结论；每个前提都 "necessary"（ISR>0），但这只是 valid AND-introduction，无实质推理
- H9 逃过分类器：结论≠单个前提（非H1），需要前提（非H7），结论形如 `∀x(A→B∧C)` 而非裸 `B∧C`（非H8）
- **H9 仅审查了 ISR b01 s44 一个 run**，其余 8 个 run 未做 H9 audit

---

### 关键观察

1. **ISR β=0.1 方差极大**: 3 个 seed 的 hacking 模式完全不同（s42=H1 100%, s43=H7 100%, s44=H1+H8+H9混合）
2. **Random β=0.1 高度一致**: 3 个 seed 均以 H1 为主（76-84%），CI=100%
3. **ISR β=0.3 PR 方差极大** (0.17-0.92): 但 ISR* 稳定 (0.18-0.24)，genuine rate 随 PR 增长
4. **CI 普遍 ~100%**: 除 ISR b03 s42 (5.9%) 外，所有 run 几乎全部使用抽象谓词
5. **Strict genuine 近零**: 仅 ISR b03 s42 (5个) 和 ISR b01 s44 (3个) 有非零 strict_genuine

---
