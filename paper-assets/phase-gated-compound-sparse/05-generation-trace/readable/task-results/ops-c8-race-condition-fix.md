# ops c8 race condition fix

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_c8_race_condition_fix_20260516T042414_result.json`
- **Structured JSON:** [`88f29e1bb261876ca9eb.json`](../../sessions/88/88f29e1bb261876ca9eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就位。汇报：

---

## 诊断结果

| 项目 | 状态 |
|------|------|
| GPU 0 s025 (PID 315057) | 运行中，16/250，~1.06 min/题，预计 ~16:30 完成 |
| 主脚本 Round 1 s015 (GPU 2) | 47/250，~1.32 min/题 |
| 主脚本 Round 1 s020 (GPU 3) | 47/250，~1.32 min/题，Round 1 预计 ~16:51 完成 |
| s025 输出目录 | profiling 代码只在最后写文件，运行期间目录为空 |
| `profiling_results.json` | 原本不存在 → **已有竞争窗口** |

**时间窗口**: GPU 0 预计比 Round 2 早 ~21 分钟完成，但单题方差极大（11秒~5分钟），不够安全。

## 执行方案

**方案 A 不可行**：bash 函数在脚本启动时已加载到内存，修改文件不会影响 `run_one` 函数的行为。

**实际执行**：Sentinel + Guardian 方案

1. **Sentinel 已创建** — `profiling_output_c8_llama_importance_s025/profiling_results.json`（227 bytes）。Round 2 的 skip 检查 `[ -f "$outdir/profiling_results.json" ]` 会命中，跳过 s025。

2. **GPU 0 覆盖** — Python 代码用 `open(out_path, "w")` 写文件（line 537），完成后会覆盖 sentinel 为真实数据。

3. **Guardian 后台进程** (PID 316993) — 每 2 分钟检查 GPU 0 是否存活。GPU 0 退出后：
   - 若 sentinel 被覆盖（真实数据）→ 正常结束
   - 若 sentinel 仍在（GPU 0 失败）→ 删除 sentinel，允许未来重跑

监控日志：`/tmp/c8_guardian.log`

---
