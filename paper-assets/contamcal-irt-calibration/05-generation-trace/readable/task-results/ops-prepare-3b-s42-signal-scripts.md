# ops prepare 3B s42 signal scripts

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prepare-3B-s42-signal-scripts_20260516T035751_result.json`
- **Structured JSON:** [`ecdfdc75d30b409234b7.json`](../../sessions/ec/ecdfdc75d30b409234b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本创建完成，语法检查通过。

## 汇总

### Eval results 路径映射

| 剂量 | Checkpoint (alpha=32 ✓) | Eval 输出 | Signal 输出 |
|------|------------------------|-----------|-------------|
| d000 | `Qwen2.5-3B_d000_s42` | `Qwen2.5-3B_d000_s42_a32_aligned` (运行中, GPU 1) | `Qwen2.5-3B_d000_s42_a32` |
| d005 | `Qwen2.5-3B_d005_s42` | `Qwen2.5-3B_d005_s42_a32_aligned` (运行中, GPU 2) | `Qwen2.5-3B_d005_s42_a32` |
| d025 | `Qwen2.5-3B_d025_v3_s42` | `Qwen2.5-3B_d025_v3_s42_para_aligned` (运行中, GPU 0) | `Qwen2.5-3B_d025_v3_s42` — **已完整** (s1/s2/s4 × 3 bench) |
| d100 | `Qwen2.5-3B_d100_a32_s42_v3` | `Qwen2.5-3B_d100_a32_s42_aligned` (运行中, GPU 3) | `Qwen2.5-3B_d100_a32_s42_v3` |

### 脚本详情
- **路径**: `/root/contamcal-irt-calibration/exp002/run_3B_s42_signals.sh`
- **信号**: s1 (embedding_shift) + s2 (min-k++) + s4 (self_critique)，**不含 s3**
- **剂量**: d000, d005, d100（d025 已跳过）
- **总任务**: 3 doses × 3 benchmarks × 3 signals = 27 runs
- **安全措施**: 启动前验证 adapter alpha=32；skip-if-done 逐文件检查
- 语法 `bash -n` 通过

### d025 merged 状态
整个 `signals/` 目录下不存在任何 merged 文件（不只 d025），merged 不是当前 signals 流程的一部分。

### 注意
`Qwen2.5-3B_d000_s42` 和 `Qwen2.5-3B_d005_s42` 虽然目录名在 C006 黑名单中，但实际 `adapter_config.json` 已更新为 alpha=32，是原地重训的结果。脚本中有运行时 alpha 验证作为双重保险。

---
