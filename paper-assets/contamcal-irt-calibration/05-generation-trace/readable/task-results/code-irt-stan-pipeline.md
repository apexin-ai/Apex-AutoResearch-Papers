# code irt stan pipeline

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_irt_stan_pipeline_20260514T004904_result.json`
- **Structured JSON:** [`d4842b09f1d30e56130d.json`](../../sessions/d4/d4842b09f1d30e56130d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。总结：

**已完成:**
1. **环境搭建**: CmdStanPy 1.3.0 + CmdStan 2.38.0 已安装
2. **Stan 模型部署**: `contam_irt_4pl_simple.stan` 和 `contam_irt_4pl.stan` 上传到 `/root/contamcal-irt-calibration/stan_models/`
3. **脚本编写**: `/root/contamcal-irt-calibration/exp006/run_irt_stan.py` — 支持 `--synthetic` 和 real-data 两种模式
4. **Synthetic validation 通过**: 
   - 0 divergent transitions, R-hat=1.006, ESS=1402
   - gamma posterior SD = 0.137（vs MLE 的 b_se=10000 问题已解决）
   - 采样耗时 ~62s（50 models × 100 items, 4 chains × 1000 samples）

**Real-data 运行命令:**
```bash
python /root/contamcal-irt-calibration/exp006/run_irt_stan.py \
  --eval-dir /root/autodl-tmp/exp001/eval_results/ \
  --stan-model /root/contamcal-irt-calibration/stan_models/contam_irt_4pl_simple.stan \
  --output-dir /root/autodl-tmp/exp006/irt_stan_results/ \
  --chains 4 --iter-sampling 1000 --adapt-delta 0.95
```

**待 real data 就绪时可直接运行**（当前 eval_results 目录中的模型子目录为空）。

---
