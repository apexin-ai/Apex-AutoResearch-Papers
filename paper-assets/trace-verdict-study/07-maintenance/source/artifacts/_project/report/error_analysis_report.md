# Qwen-7B Error Analysis Report

## 1. 各条件错误统计

| Condition | Total | Errors | Acc% | FP | FN | FP% | FN% |
|-----------|-------|--------|------|----|----|-----|-----|
| ae_only | 1190 | 1 | 99.9 | 0 | 1 | 0% | 100% |
| exception_only | 1190 | 2 | 99.8 | 0 | 2 | 0% | 100% |
| vota | 1190 | 7 | 99.4 | 0 | 7 | 0% | 100% |
| loop_only | 1190 | 171 | 85.6 | 61 | 110 | 35.7% | 64.3% |
| full_trace | 1190 | 217 | 81.8 | 103 | 114 | 47.5% | 52.5% |
| no_trace | 1190 | 296 | 75.1 | 90 | 206 | 30.4% | 69.6% |

Label distribution: pass=851 (71.5%), fail=339 (28.5%)

**关键发现**: exception-based 条件错误全部是 FN (pred=fail, label=pass)，零 FP。

## 2. 错误样本重叠矩阵 (Jaccard)

- full_trace ∩ no_trace: J=0.437 (最高)
- full_trace ∩ loop_only: J=0.416
- loop_only ∩ no_trace: J=0.394
- **exception_only 与其他条件零重叠**

## 3. 顽固错误 (>=4 条件)

| Sample | Problem | Label | Wrong in |
|--------|---------|-------|----------|
| 345 | MBPP/794 | pass | ae_only, full_trace, no_trace, vota |
| 540-543, 548-549 | MBPP/113 | pass | full_trace, loop_only, no_trace, vota |

最难问题: MBPP/284, MBPP/419, MBPP/443 — full_trace/loop_only/no_trace 全错，exception_only 全对。

## 4. Tier 对比

### full_trace 独有错误 (58个): 76% FP — more trace = more false positive
### loop_only 独有错误 (36个): 89% FN
### no_trace 独有错误 (119个): 82% FN

### FP/FN 质变
- Tier 1/2 (exception-based): 100% FN, 0% FP — 安全性保证
- full_trace: ~50/50 FP/FN — 噪声干扰

## 5. 论文启示

1. "Less is more": full_trace 独有错误 76% 是 FP，更多信息导致更多误报
2. Exception 信号决定性: 顽固问题在 exception_only 下全部做对
3. FP/FN 质变对 CI/CD 安全性意义重大
4. 信息选择性 (information selectivity) 叙事