# analysis mmlu domain gamma

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mmlu_domain_gamma_20260516T073016_result.json`
- **Structured JSON:** [`dce01df5eb3d3946f8ee.json`](../../sessions/dc/dce01df5eb3d3946f8ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 成功。结果：

- **脚本路径**: `/root/contamcal-irt-calibration/exp006/run_mmlu_domain_gamma.py`
- **8 个 domain**: STEM_Math(1190), STEM_Science(1397), STEM_CS_Eng(557), Medical(1640), Humanities(2816), Social_Sciences(3077), Business_Law(2482), Other(883)
- **全部 14042 items 映射到 domain，无遗漏**
- **8 个 1.5B 模型**: 4 dosage levels (0/5/25/100) × 2 seeds (42/123)
- **Stan 配置**: 2PL+γ, 4 chains × 1000w + 1000s, adapt_delta=0.95

**预计运行时间**: ~62 分钟总计（Humanities/Social_Sciences/Business_Law 因 >2000 items 会被 subsample 到 2000，实际每个 domain ~3-10 min）。

用法：
```bash
# 全量运行
python3 exp006/run_mmlu_domain_gamma.py

# 只跑某几个 domain
python3 exp006/run_mmlu_domain_gamma.py --domains STEM_Math Medical

# 包含 para 变体（16 models）
python3 exp006/run_mmlu_domain_gamma.py --include-para
```

---
