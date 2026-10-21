# analysis stan diagnostic exp005

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_stan-diagnostic-exp005_20260513T225141_result.json`
- **Structured JSON:** [`738a870dbacd38b2a658.json`](../../sessions/73/738a870dbacd38b2a658.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 最终诊断结论

### 根因：磁盘配额耗尽（不是 Stan 数值问题）

**Simple model 崩溃 (retcode=1)**：ME model 先运行 95 分钟，在 /tmp 生成 ~1 GB CSV（9000 tau + 9000 log_lik × 4 chains），耗尽 3.9 GB tmpfs 空间。Simple model 写 CSV 时 disk quota exceeded → 全部 4 chains 返回 retcode=1。

**证据**：清理磁盘后，σ_e=0.1 + N=30 + inits 完美收敛：
| 测试 | σ_e | Rhat | gamma | 状态 |
|------|-----|------|-------|------|
| Test 1 | 0.3 | 1.007 | 0.458±0.095 | ✅ |
| Test 3 | 0.1 | 1.003 | 0.788±0.132 | ✅ |

**ME model Rhat=1.945** 是独立问题：10231 参数 vs 9000 观测，严重欠识别。用 `contam_irt_4pl_me_analytic.stan` 替换即可。

### 修复建议
1. **设置 `output_dir` 到非 tmpfs 位置**（或运行前清 /tmp）
2. **先跑 simple，再跑 ME**
3. **ME model 换用 analytic 版本**（消除 9000 tau 潜变量）
4. σ_e=0.1 和 0.3 都能收敛，无需裁剪范围

结果已保存到 `artifacts/exp005_noise_propagation/diagnostic_results.json`。

---
