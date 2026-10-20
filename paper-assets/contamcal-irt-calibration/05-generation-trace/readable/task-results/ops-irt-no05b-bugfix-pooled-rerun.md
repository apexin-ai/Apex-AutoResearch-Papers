# ops irt no05b bugfix pooled rerun

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_irt_no05b_bugfix_pooled_rerun_20260517T083303_result.json`
- **Structured JSON:** [`adf00796fa3dfe29c408.json`](../../sessions/ad/adf00796fa3dfe29c408.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果：

**Pooled γ 结果：**
- **Mean**: 0.1072
- **95% CI**: [-0.401, 0.625]
- **PPP**: 0.208
- **Rhat**: 1.0068, ESS=1157, 0 divergences

**修复内容：**
1. 添加 `_ppp_float()` 辅助函数处理 ppp 可能为 dict 的情况
2. 修复 4 处 `ppp` 作为 float 使用的 bug（line 246, 270, 414 对应位置）
3. 添加 `--pooled-only` 参数，从磁盘加载已有 domain 结果，仅重跑 pooled MCMC
4. 备份已保存为 `run_mmlu_domain_gamma_no05b.py.bak`

---
