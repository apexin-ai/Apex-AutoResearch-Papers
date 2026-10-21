# analysis coverage matrix audit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_coverage_matrix_audit_20260514T041621_result.json`
- **Structured JSON:** [`c44678171fdf7cd938f2.json`](../../sessions/c4/c44678171fdf7cd938f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完成。下面是完整的覆盖矩阵审计和就绪度评估。

---

## Claim × Experiment 覆盖矩阵

### C1: Calibration Claim（4PL+γ IRT 恢复真实性能）

| 实验 | 优先级 | 状态 | 详情 |
|------|--------|------|------|
| **exp-001** SFT injection | P0 | 🟡 部分完成 | 0% 基线: 3 scale × 2 seed ✅; d5% 0.5B ✅, 1.5B 🔄; d100% 0.5B ✅, 1.5B 🔄; **d25%/d50% 未启动**; 3B 污染版未启动; eval 大量失败/重试中 |
| **exp-004** simulation sweep | P0 | 🟡 可能完成 | 本地运行完成(03:41)但 SSH 检查失败5次,状态卡在 RUNNING,需验证结果 |
| **exp-006** IRT calibration + baselines | P0 | 🔴 未启动 | **主结果表**, blocked on exp-003 |
| **exp-015** QC-only d100 | P1 | ⚪ orphaned | 未启动 |
| **exp-007** 7B scale bridging | P1 | ⚪ 未启动 | blocked on exp-001 |
| **exp-014** multi-family | P1 | ⚪ 未启动 | rebuttal 备用 |
| **exp-012** 72B observational | P2 | ⚪ 未启动 | blocked on exp-006 |

**C1 就绪度: 🔴 红色** — 0个实验完成, 主结果实验(exp-006)距启动还差2步依赖

---

### C2: Signal Survival & Aggregation Claim（信号退化 + RRF 融合）

| 实验 | 优先级 | 状态 | 详情 |
|------|--------|------|------|
| **exp-002** signal pipeline | P0 | 🔴 未启动 | blocked on exp-001 eval 完成 |
| **exp-003** RRF ablation | P0 | 🔴 未启动 | blocked on exp-002 |
| **exp-008** signal survival | P0 | 🔴 未启动 | blocked on exp-002; **C2 "cliff-like" 核心证据** |
| **exp-009** RL case study | P1 | ⚪ 未启动 | blocked on exp-006 + exp-008 |
| **exp-013** closed-weight 2-signal | P2 | ⚪ 未启动 | blocked on exp-003 |

**C2 就绪度: 🔴 红色** — 0个实验启动, 全链未开工

---

### C3: Identifiability & Uncertainty Claim

| 实验 | 优先级 | 状态 | 详情 |
|------|--------|------|------|
| **exp-004** simulation sweep | P0 | 🟡 可能完成 | 同C1, 待验证 |
| **exp-005** noise propagation | P0 | 🔴 v1/v2 失败, v3 运行中 | v2 部分结果: simple model 收敛(γ=0.458, bias 6.8%), ME model 严重欠识别(10231参数 vs 9000观测); v3 用解析 ME 降至1231参数 |
| exp-006 (also supports C3) | P0 | 🔴 未启动 | 同C1 |

**C3 就绪度: 🟡 黄色** — MVP 验证通过(γ bias <8%), exp-004 可能完成, 但 exp-005 ME model 仍不稳定

---

## 关键依赖链分析

```
exp-001 (SFT) ──→ exp-002 (signals) ──→ exp-003 (RRF) ──→ exp-006 (主结果)
    │                    │                                       ↑
    │                    └──→ exp-008 (signal survival)          │
    │                                                            │
    └──→ exp-004 (simulation) ──→ exp-005 (noise) ──────────────┘
```

**瓶颈**: exp-001 eval 尚未全部完成 → exp-002 无法启动 → 整条链停滞

---

## 已有实际成果盘点

| 成果 | 支撑 Claim |
|------|-----------|
| MVP γ 恢复: bias 6.8%, θ corr 0.943, 即使 confounding (r=0.38) 仍通过 | C1, C3 |
| 0% baseline SFT: 3 scale × 2 seed 全部成功 | C1 基础设施 |
| d5% 0.5B SFT 成功, d100% 0.5B SFT 成功 | C1 部分 |
| 2 个 eval 完成: 0.5B clean (MMLU=41.8%), 1.5B clean (MMLU=57.5%) | C1 部分 |
| exp-005 v2 部分: simple model σ_e=0.3 收敛 | C3 部分 |

---

## 风险清单（按严重程度）

### 🔴 致命风险

1. **exp-006 (主结果表) 未启动, 依赖链深度 = 3**: exp-001 eval → exp-002 → exp-003 → exp-006。即使每步只需2天, 也需6天以上, 加上论文写作, 11天极其紧张。

2. **exp-008 (signal survival, C2 核心证据) 未启动**: paper_framing 将其提升为 Core Contribution 2, Dream review 称其"most genuinely novel finding", 但实验甚至没开始。

3. **exp-001 eval 大面积失败**: 44 个 registry 条目中 16 个 failed/killed, 主要集中在 eval 阶段（GPU 冲突、OOM、路径错误、--gpu 参数 bug）。Eval 是 exp-002 的前置条件。

4. **缺失 dosage 级别**: d25%, d50% 完全未启动, 但 dose-response 单调性是 5 个评估指标之一, 需要至少 3 个剂量点才有意义。

### 🟡 重要风险

5. **exp-004 状态不明**: 日志显示完成但 registry 仍是 RUNNING (SSH 检查失败), 需要手动验证结果质量。

6. **exp-005 ME model 反复失败**: 即使 v3 的解析 ME 成功, C3 的 "measurement error propagation" claim 只有模拟数据支撑, 没有真实数据验证 (blocked on exp-006)。

7. **论文写作零进度**: paper_framing 中列出 5 个必需 figure, 35+ 引用, Fisher Information 推导——全部未开始, 且 "zero figures" 被 Dream review 标记为 serious deficiency。

8. **3B 模型 eval 全部失败**: exp_001_eval_3B 的 4 次尝试全失败/running, 3B 是声称的最大 controlled scale。

### ⚪ 次要风险

9. **exp-007 (7B) / exp-014 (multi-family)** 未启动, 但 paper 已将 multi-family 降级为 rebuttal-ready。
10. **HumanEval 已降级到 appendix** (QC pass 仅 16%), 合理但减少了 benchmark 覆盖。

---

## 建议：优先级排序

### 必须立即做（今天）

1. **验证 exp-004 结果** — SSH 连接服务器, 检查 `/root/contamcal-irt-calibration` 下 exp-004 输出, 确认 144-condition sweep 是否完成
2. **修复 exp-001 eval 失败** — 根治 --gpu 参数 bug 和路径问题, 清理 GPU 上的僵尸进程, 批量重跑失败的 eval
3. **加速 exp-001 SFT 训练** — d25%/d50% 训练数据准备 + 提交; 1.5B/3B 的 d5%/d100% 完成

### 关键路径加速（Day 1-3）

4. **exp-001 eval 完成 → 立即启动 exp-002** — signal pipeline 是最大瓶颈, 即使只有部分 model 的 eval 也可以先跑
5. **exp-005 v3 验证** — 确认解析 ME model 是否收敛
6. **Fisher Information 推导** — CPU 工作, 可并行, Dream review 标记为 critical gap

### 降级策略（若时间不足）

7. **最小可投稿版本**: 如果 exp-002/003/006 链无法完成, 考虑:
   - 将 paper 范围缩小到 "simulation + MVP + signal analysis" (C3 + 部分 C2)
   - 用 MVP 数据代替完整 exp-006 主结果, 明确标注 "preliminary"
   - 或放弃 ARR May, 目标改为 AAAI 2027 (Jul-Aug deadline)

8. **剂量简化**: 如果 d25%/d50% 来不及, 用 {0%, 5%, 100%} 三点也能做基本的 dose-response 分析, 但单调性论证较弱

---

## 总结

**整体就绪度: 🔴 红色 — 严重落后**

11天内投稿需要: (1) 完成 exp-001 全部训练+eval, (2) 跑完 exp-002→003→006 全链, (3) 跑 exp-008, (4) 写完论文含 5 个 figure + 推导。以当前进度（1.5天产出 14 个成功实验 + 16 个失败）, 按最乐观估计需要 8-10 天纯实验 + 3-5 天写作, **ARR May 25 极难达成**。

建议立即评估是否切换到 AAAI 2027 (deadline ~Jul/Aug 2026), 或者确定一个 minimal viable paper scope 用 3 剂量 + 部分 baselines 勉强投稿。

---
