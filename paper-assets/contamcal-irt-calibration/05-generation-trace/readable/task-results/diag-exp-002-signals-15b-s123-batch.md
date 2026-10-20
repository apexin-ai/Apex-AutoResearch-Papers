# diag exp 002 signals 15B s123 batch

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp_002_signals_15B_s123_batch_20260516T130518_result.json`
- **Structured JSON:** [`d07810fb56e065882ee3.json`](../../sessions/d0/d07810fb56e065882ee3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论：**误报**，实验实际已全部成功完成

### faiss 错误：非关键路径，无影响

日志中出现 60 次 `ModuleNotFoundError("No module named 'faiss.swigfaiss_avx512_spr'")`，但这是 **faiss 的标准降级行为**——先尝试 AVX512-SPR，失败后立即 fallback 到 AVX512 并成功加载：

```
Loading faiss with AVX512-SPR support.
Could not load library with AVX512-SPR support due to: ModuleNotFoundError(...)
Loading faiss with AVX512 support.
Successfully loaded faiss with AVX512 support.  ← 每次都成功
```

### 真实退出原因：bash 语法错误（非 Python 错误）

日志末尾：
```
PASS: Qwen2.5-1.5B_d100_s123×arc_challenge   ← 最后一个任务正常完成
run_15B_s123_signals.sh: line 39: continue: only meaningful in a `for', `while', or `until' loop
run_15B_s123_signals.sh: line 40: syntax error near unexpected token `fi'
EXIT_CODE=2
```

所有 12 个 (model × benchmark) 组合都输出了 PASS（12 PASS, 0 FAIL），但脚本在最后一个任务完成后因 bash 语法错误崩溃（EXIT_CODE=2），没有打印 `===BATCH_COMPLETE_15B_S123===` 汇总行。CRON 检测到非零退出码就报了 failure。

注意：当前磁盘上的脚本 (`/root/contamcal-irt-calibration/exp002/run_15B_s123_signals.sh`) 语法是正确的，说明脚本在运行后被修复过，但执行时用的是旧版本。

### 输出完整性：4 个 contamination level × 3 benchmarks × 3 signals 全部到位

| 目录 | 信号文件 | merged 文件 | 状态 |
|------|---------|-------------|------|
| `Qwen2.5-1.5B_d000_s123` | 9 (s1/s2/s4 × mmlu/gsm8k/arc) | 3 | ✅ 完整 |
| `Qwen2.5-1.5B_d005_s123` | 9 | 3 | ✅ 完整 |
| `Qwen2.5-1.5B_d025_s123` | 9 | 3 | ✅ 完整 |
| `Qwen2.5-1.5B_d100_s123` | 9 | 3 | ✅ 完整 |

### 当前 GPU 状态

| GPU | 显存 | 利用率 | 进程 |
|-----|------|--------|------|
| 0 | 6919/24564 MiB | 61% | PID 780943 (python) |
| 1 | 2197/24564 MiB | 30% | PID 780591 (python) |
| 2 | 空闲 | 0% | — |
| 3 | 6791/24564 MiB | 67% | PID 764460 (python3) |
| 4 | 空闲 | 0% | — |
| 5 | 空闲 | 0% | — |

### 结论

**不需要重跑。** registry 标记 `conclusion=success` 是正确的（输出完整）。CRON 报 failure 是因为 bash EXIT_CODE=2，但那是脚本语法 bug，发生在所有计算完成之后。faiss 的 ModuleNotFoundError 是无害的 fallback 日志。

---
