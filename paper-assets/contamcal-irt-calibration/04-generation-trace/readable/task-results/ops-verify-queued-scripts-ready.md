# ops verify queued scripts ready

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-queued-scripts-ready_20260516T041841_result.json`
- **Structured JSON:** [`fef9ed960f26b9dfbfc1.json`](../../sessions/fe/fef9ed960f26b9dfbfc1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证完成。

---

## 脚本就绪状态报告

### 1. `run_3B_s42_signals.sh` ✅ READY

| 项目 | 状态 |
|------|------|
| 文件存在 & 可执行 (755) | ✅ |
| 覆盖范围: d000 + d005 + d100 × 3 benchmarks × s1/s2/s4 | ✅ (d025 已跳过，注释说已有 signals) |
| S3 排除 | ✅ 只跑 s1, s2, s4 |
| Skip logic | ✅ 检查输出文件是否存在 |
| Alpha=32 运行时校验 | ✅ 每个 dose 开始前 grep adapter_config.json |
| Checkpoint alpha 确认 | ✅ d000_s42=32, d005_s42=32, d100_a32_s42_v3=32 |

注意：d000_s42 和 d005_s42 名称在 C006 blocklist 中，但磁盘上实际 alpha=32（已重训）。输出目录加了 `_a32` 后缀区分。运行时校验是最终安全网。

### 2. `run_3B_d100_s123_gsm8k_arc_signals.sh` ✅ READY

| 项目 | 状态 |
|------|------|
| 文件存在 & 可执行 (755) | ✅ |
| Benchmarks: gsm8k + arc_challenge（mmlu 已在 cuda:4 跑） | ✅ |
| Signals: s1, s2, s4 / S3 排除 | ✅ |
| Skip logic | ✅ |
| Alpha=32 运行时校验 | ✅ |
| Checkpoint `Qwen2.5-3B_d100_a32_s123` alpha=32 | ✅ |
| REF model `Qwen2.5-3B_d000_s123` 存在 | ✅ |

### 3. `run_05B_s123_signals.sh` ✅ READY (有小问题)

| 项目 | 状态 |
|------|------|
| 文件存在 & 可执行 (755) | ✅ |
| 覆盖范围: d000 + d005 + d025 + d100 × 3 benchmarks × s1/s2/s4 | ✅ |
| S3 排除 | ✅ |
| Skip logic | ✅ |
| 4 个 checkpoint 全部存在 & alpha=32 | ✅ |
| Alpha=32 运行时校验 | ⚠️ **缺失** — 3B 脚本有但 0.5B 没有 |

⚠️ **风险**：虽然当前所有 0.5B checkpoint 确认 alpha=32，但缺少运行时校验与 3B 脚本不一致。不阻塞提交，但建议补上。

### 4. `rrf_aggregation.py` ✅ READY

| 项目 | 状态 |
|------|------|
| 文件存在，有 argparse (--help 可用) | ✅ |
| ALPHA16_BLOCKLIST 包含全部 5 个无效目录 | ✅ `Qwen2.5-3B_d000_s42`, `d000_v2_s42`, `d005_s42`, `d025_s42`, `d100_s42` |
| SKIP_PATTERNS = ["DEPRECATED"] | ✅ |
| 支持 --generate-exposure 模式输出 exp-006 所需格式 | ✅ |

### 5. `run_irt_calibration.py` ✅ READY

| 项目 | 状态 |
|------|------|
| 文件存在 | ✅ |
| CmdStan 2.38.0 已编译 | ✅ (`bin/stanc` 存在) |

---

## 总结

**5/5 全部 Ready。** 唯一建议：给 `run_05B_s123_signals.sh` 补上 alpha=32 运行时校验（与 3B 脚本一致的安全检查），当前不阻塞提交。

---
