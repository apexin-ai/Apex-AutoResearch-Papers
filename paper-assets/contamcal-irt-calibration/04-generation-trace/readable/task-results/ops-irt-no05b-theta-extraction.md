# ops irt no05b theta extraction

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_irt_no05b_theta_extraction_20260517T085345_result.json`
- **Structured JSON:** [`49016bfb130d29b81462.json`](../../sessions/49/49016bfb130d29b81462.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本正常运行中。第一个域 (STEM_Math, 1190 items) 预计约 5 分钟完成。

**状态汇总：**

1. **Stan CSV 已被清理** — `fit_stan_model()` 未指定 `output_dir`，CmdStanPy 用临时目录并在对象回收后删除。`/tmp` 中残留的 CSV 均不完整（仅 1-2 行数据）。

2. **已启动重跑脚本** `extract_theta_no05b.py` (PID 970486)：
   - 使用完全相同的 Stan 模型、数据、seed (42)、配置 (4 chains × 1000 samples)
   - 对所有 8 域 + pooled 重新拟合
   - 提取完整 theta posterior (mean, SD, 95% CI)
   - 计算 Δθ = mean(θ_3B) - mean(θ_1.5B) 及其 95% CI
   - 输出保存到 `/root/autodl-tmp/exp006/mmlu_domain_irt_no05B/theta_results.json`

3. **预计完成时间**：约 50 分钟（各域 fit_time 为 80-525 秒）

需要我稍后回来检查结果吗？

---
