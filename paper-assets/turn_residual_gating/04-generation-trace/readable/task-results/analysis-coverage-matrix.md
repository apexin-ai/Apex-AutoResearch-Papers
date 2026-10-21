# analysis coverage matrix

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_coverage_matrix_20260522T045012_result.json`
- **Structured JSON:** [`55bdd0b859f4db39e526.json`](../../sessions/55/55bdd0b859f4db39e526.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 覆盖率矩阵报告

### Claims × Experiments 矩阵

| Claim | 实验 | 状态 | 覆盖判定 |
|-------|------|------|----------|
| **C1** GAR衰减真实严重 | plan_001 GAR诊断 | ✅ DONE | **Fully covered** |
| **C2** 训练有效/推理失败(30x gap) | plan_002 v7训练 | ✅ DONE | **Partially covered** |
| | plan_008 Held-out eval | ✅ DONE | |
| | plan_019 Multi-seed (s=123) | ⏳ planned | ← gap: 无方差估计 |
| **C3** 失败机制因果分析 | plan_006 梯度冲突分析 | ✅ DONE | **Partially covered** |
| | plan_007 Attention heatmap | ✅ DONE | |
| | plan_018 PCGrad因果排除 | ✅ DONE | |
| | plan_013 Llama梯度冲突 | ⏳ planned | ← gap: 跨模型验证 |
| | plan_022 λ_GAR sensitivity | ⏳ planned (P2) | ← nice-to-have |
| | plan_023 v8b Scheduled Sampling | ❌ failed | |
| **C4** Gating零增量贡献 | plan_003 UG ablation | ✅ DONE | **Partially covered** |
| | plan_004 LoRA-only ablation | ✅ DONE | |
| | plan_005 4-way eval | ✅ DONE | |
| | plan_008 Held-out eval | ✅ DONE | |
| | plan_015 Bootstrap CI | ⚠️ orphaned (有结果) | ← 需注册 |
| | plan_020 扩展eval集(200 conv) | ⏳ planned (P1) | ← nice-to-have |
| **C5** 跨模型验证(Llama) | plan_009 Llama Phase1 GAR | ⏳ planned | **Uncovered** |
| | plan_010 Llama TG训练 | ⏳ planned | |
| | plan_011 Llama LoRA-only | 🔄 RUNNING | |
| | plan_012 Llama 3-way eval | ⏳ planned | |

### Reviewer Weakness 覆盖

| Weakness | 实验 | 状态 |
|----------|------|------|
| W3 下游任务 | plan_014 instruction retention | ⏳ planned (P2) |
| W7 单seed | plan_015 Bootstrap CI | ⚠️ orphaned (结果已产出，CI包含0) |
| W8 Exposure-bias mitigation | plan_016 v8 SS | ❌ failed (killed) |
| | plan_023 v8b SS fixed | ❌ failed |
| R4 Code-paper公式一致性 | plan_017 代码审计 | ⚠️ orphaned (结果已产出，公式已修正) |

### 汇总

| 覆盖等级 | Claims |
|----------|--------|
| **Fully covered** | C1 |
| **Partially covered** (核心实验已完成，加固实验待做) | C2, C3, C4 |
| **Uncovered** (0/4 完成，仅1个RUNNING) | **C5** |

### 关键 Gaps

1. **C5 跨模型验证 — 最高优先级 gap。** paper_framing 明确标注为 MUST-HAVE（不含→Findings 3.0紧绷）。4个实验中0个完成，plan_011 (LoRA-only) 正在运行，plan_009/010/012 尚未开始。**阻塞论文投稿。**

2. **plan_015 / plan_017 orphaned 状态。** 两个实验实际已产出有效结果（Bootstrap CI 确认 zero benefit; 公式不一致已定位），但 registry 状态为 orphaned，需要更新为 DONE 以反映真实覆盖。

3. **C2 multi-seed (plan_019) 未开始。** Dream review W7 标为"严重"，目前只有 bootstrap CI (plan_015) 部分缓解。effect size 极端 (30x) 可能允许单 seed，但至少需要在论文中论证。

4. **W8 exposure-bias mitigation 两次失败。** plan_016 被 kill，plan_023 也 failed。论文只能以 Discussion 中的 future work 处理此方向，无法升级为 "diagnosis + remedy"。

5. **W3 下游任务 (plan_014) 未开始 (P2)。** GAR 作为唯一代理指标的弱点未实验缓解。

### 建议优先级

1. **立即**: 推进 C5 Llama 实验链 (plan_009→010→012)，这是唯一阻塞投稿的 gap
2. **短期**: 修复 plan_015/017 的 orphaned 状态，使覆盖率矩阵准确
3. **如有 GPU 余量**: plan_019 (multi-seed) 或 plan_014 (downstream task) 择一执行

---
