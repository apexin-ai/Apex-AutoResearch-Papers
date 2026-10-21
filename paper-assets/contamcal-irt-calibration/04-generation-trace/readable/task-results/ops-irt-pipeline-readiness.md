# ops irt pipeline readiness

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_irt-pipeline-readiness_20260516T040502_result.json`
- **Structured JSON:** [`2a4b56701852c21a0fc6.json`](../../sessions/2a/2a4b56701852c21a0fc6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：exp-006 IRT pipeline **READY**

所有 6 项检查通过：

| 组件 | 状态 |
|------|------|
| **Stan 模型** | 5 个 .stan + 已编译二进制，主模型 `contam_irt_4pl_simple.stan` 含 4PL+γ 参数化 |
| **CmdStan** | v2.38.0 已安装，cmdstanpy 已在 conda base 环境 |
| **IRT fitting 脚本** | `run_exp006.py` 端到端 pipeline，支持 `--dry-run` / `--skip-stan` |
| **7 Baselines** | B0-B6 全部实现（baselines.py），统一 `fit()` 接口 |
| **Dry-run** | `dryrun_full.json` 已有完整输出（含 Stan MCMC，max_rhat≈1.003） |
| **RRF→IRT 格式** | exp003 `exposure_aggregated.json` (`{bench: [floats]}`) 可直接传入 `--exposure-file`，零适配 |

**关于 per-benchmark γ_k**：Stan 模型定义单一 `real gamma`，per-benchmark γ_k 通过 pipeline 对每个 benchmark 独立拟合实现。

报告已写入 `artifacts/exp006_readiness_report.md`。

---
