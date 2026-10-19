# diagnose mvp A 005

**crosscoder behavioral circuit transplant** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_mvp-A-005_20260510T160242_result.json`
- **Structured JSON:** [`aacfcd6c6d0e6b22af81.json`](../../sessions/aa/aacfcd6c6d0e6b22af81.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。以下是完整结果汇报：

---

## mvp-A-005 实验结果：NEGATIVE

**方法**: TopK Crosscoder (K=50, n_features=2048, 纯 MSE 损失无 L1)  
**运行时间**: 83s  
**L0**: 精确 = 50（TopK 硬约束）

### Gate 结果总表

| Gate | 指标 | 实际值 | 阈值 | 结果 |
|------|------|--------|------|------|
| Gate 1 (Training) | MSE reduction | 41.5% (0.290→0.169) | >50% | **FAIL** |
| Gate 2 (Features) | ratio>3 features | 90 | ≥1 | **PASS** |
| Gate 3 (Shift) | shift_ratio | 0.187 | ≥0.5 | **FAIL** |
| Gate 4 (PPL) | ppl_ratio | 1.072 | ≤1.05 | **FAIL** |
| Gate 5 DA | improvement | -0.011 | ≥0.10 | **FAIL** |
| Gate 5 non-DA | degradation | 0.025 | ≤0.03 | **PASS** |

### Part 2: Bias Injection（20 配置全部 FAIL）

5 个特征 (362, 313, 1768, 169, 828) × 4 个 α (0.5, 1.0, 2.0, 5.0)，无一通过所有 gates。核心矛盾：
- **低 α** (0.5-1.0): G4(PPL) pass 但 G3(shift) 和 G5(DA) 都远不够
- **高 α** (5.0): G3 接近 0.5 阈值但 G4 爆炸 (1.2-1.4)，且 G5 DA 反而更差

### 关键发现

1. **TopK 确实产生了更多 donor-exclusive features**（90 个 vs mvp-A-001 的 22 个），Gate 2 轻松通过
2. **但 rank-1 surgery 和 bias injection 仍然无法产生有益的行为变化** — DA improvement 始终为负（手术让 DA tokens 变差而非变好）
3. **shift 和 behavior 之间存在根本性 tradeoff**：增大 scale/α 可以移动激活，但同时破坏模型（PPL 上升 + DA 恶化）

### 假设验证

- **H1 (TopK 产生更好特征用于手术)**: 部分验证 — 特征质量确实更好，但无法转化为有效行为移植
- **H3 (bias injection 作为替代手术方式)**: 未验证 — 20 个配置全部失败

### MVP 系列总结

mvp-A-001 到 mvp-A-005 共 4 次正式实验（A-002v2 被 kill），结论一致：**crosscoder 可以找到 donor-exclusive features，但现有的手术方式（rank-1 weight surgery / residual bias injection）无法将这些特征有效移植到 target 模型中产生行为改善。** 瓶颈不在特征发现，而在手术/注入机制本身。

---
