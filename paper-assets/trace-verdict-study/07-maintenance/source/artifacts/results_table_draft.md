# Results Table Draft — trace-verdict-study

> Generated: 2026-05-15 | Target: EMNLP 2026 ARR (deadline May 25)

## Table 1: Main Results — Test Verdict Prediction (Qwen2.5-Coder-7B-Instruct)

All models fine-tuned on 4,720 training samples, evaluated on 1,190 test samples. Majority baseline accuracy: 71.5%.

| Condition | Accuracy | 95% CI | Δ vs No-Trace | Pass F1 | Fail F1 |
|-----------|----------|--------|---------------|---------|---------|
| No-Trace (v5) | 75.1% | [72.8, 77.5] | — | 0.813 | 0.627 |
| Full-Trace (v5) | 81.8% | [79.7, 83.9] | +6.6pp | 0.870 | 0.690 |
| **VOTA (v5)** | **99.2%** | [98.6, 99.7] | **+24.0pp** | **0.994** | **0.986** |

All three conditions use v5 code version (unified chat template handling). Bootstrap CIs from 10K resamples.

### Lift vs No-Trace (Bootstrap 95% CI)

| Comparison | Lift | 95% CI |
|------------|------|--------|
| Full-Trace vs No-Trace | +6.6pp | [+4.4, +9.0] |
| VOTA vs No-Trace | +24.3pp | [+21.8, +26.8] |
| VOTA vs Full-Trace | +17.7pp | [+15.5, +19.8] |

All paired CIs from bootstrap paired comparison (10K resamples). All differences statistically significant (p < 0.001).

## Table 2: Ablation Studies (Pending)

| Condition | Accuracy | Status | Plan ID | Purpose |
|-----------|----------|--------|---------|---------|
| **VOTA w/o actual/expected** | **99.4%** [98.9, 99.8] | **✅ DONE** | plan_001 | actual/expected 冗余，VOTA 效果来自 trace 行为模式理解 |
| **Full-Trace + label-only loss** | **86.2%** [84.4, 88.1] | **✅ DONE** | plan_002 | gradient dilution 确认：+4.4pp over full_trace(81.8%)，但仍 -13pp vs VOTA |
| **VOTA exception_only** | **99.83%** [CI pending] | **✅ DONE** | plan_003a | [ERROR] 事件是主驱动因素（≥VOTA full 99.2%），vs no_trace +24.7pp [22.3, 27.1] |
| **VOTA loop_only** | **85.6%** [83.5, 87.6] | **✅ DONE** | plan_003b | loop compression 单独贡献：> full_trace +3.9pp [1.8, 6.0]，但远低于 exception_only (-14.2pp) |
| VOTA ae_only | — | **RUNNING** (cuda:1) | plan_003c | 88% fallback 污染，结果→Appendix |
| Trace length ablation (4 lengths) | — | planned | plan_006 | accuracy vs trace length 曲线 |

## Table 3: Planned Generalization Experiments

| Experiment | Status | Plan ID | Purpose |
|------------|--------|---------|---------|
| DeepSeek-Coder-6.7B 复现 | planned | plan_004 | 多模型验证 |
| 第二 verdict task (DebugBench/Defects4J) | planned | plan_005 | 多任务验证 |
| Seed robustness (3 seeds) | planned | plan_008 | 结果稳定性 |
| Calibration analysis (ECE) | planned | plan_007 | 校准质量分析 |

## Training Details

| Condition | Train Loss | Eval Loss | Wall Clock | GPU-hours |
|-----------|-----------|-----------|------------|-----------|
| No-Trace (v4) | 0.180 | 0.645 | 21 min | 0.35 |
| Full-Trace (v5) | — | — | 131 min | 2.18 |
| VOTA (v5) | 0.050 | 0.087 | 141 min | 2.35 |

---

## 写作就绪度评估

### 可以立即开始写的 Sections

| Section | 就绪度 | 说明 |
|---------|--------|------|
| **Abstract** | 80% | 主结果已有（75.1→81.8→99.2 gradient）；待 ablation 结果决定最终措辞 |
| **Introduction** | 90% | Story spine 已定（paper_framing.md），三条件 gradient 已确立，可立即写 |
| **Related Work** | 95% | 已有 literature positioning（DCSH、TracePile、TRACED），与实验结果无关，可立即写完 |
| **Method (§3)** | 95% | VOTA 设计、数据构造、训练流程均已确定，可完整写出 |
| **Experimental Setup (§4.1-4.2)** | 95% | 模型、数据、超参、评估指标均已确定 |
| **Main Results (§4.3)** | **100%** | Table 1 定稿：三条件 v5 统一，所有 paired CI 已计算 |

### 需要等实验结果的 Sections

| Section | 就绪度 | 阻塞项 |
|---------|--------|--------|
| **Ablation Study (§4.4)** | 85% | plan_001 ✅, plan_002 ✅, plan_003a ✅, plan_003b ✅; 仅剩 ae_only (→Appendix) |
| **Analysis/Discussion (§5)** | 80% | 组件层级已建立: exception >>> loop > ae; 等 ae_only 确认 |
| **Conclusion** | 75% | 主结论可写：exception 是 minimal sufficient signal; 等 ae_only 补全 |

### 关键依赖链

```
plan_001 结果 (今天)
  ├── 决定 Claim 1 framing（strong vs adjusted）
  ├── 解锁 Ablation Study section
  ├── 解锁 plan_003 (component ablation)
  └── 影响 Abstract/Conclusion 措辞

plan_002 结果 (今天)
  ├── 决定 Claim 2 强度（gradient dilution 是否成立）
  └── 影响 full_trace 讨论

no_trace_v5 补跑 (plan_001 完成后, ~20min)
  ├── 统一三条件代码版本
  └── 重算所有 lift CI
```

### 建议写作优先级

1. **今天可以写**: Related Work → Method → Experimental Setup → Introduction draft
2. **plan_001/002 出结果后**: Main Results 定稿 → Ablation Study → Analysis
3. **最后**: Abstract → Conclusion（需要所有结果确认后才能定稿）
