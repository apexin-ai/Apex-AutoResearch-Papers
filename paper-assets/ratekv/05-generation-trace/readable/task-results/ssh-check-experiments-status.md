# ssh check experiments status

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-experiments-status_20260514T183858_result.json`
- **Structured JSON:** [`137b704bc940edd2ebfd.json`](../../sessions/13/137b704bc940edd2ebfd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### 1. qwen_hires_float32_d048 — **ALIVE**
- PID 247429，运行 9 分 19 秒，状态 `Ss+`
- 日志显示：模型已加载，正在执行 Step 1 (High-resolution quantization profiling)
- 输出文件 `qwen_hires_results.json` 尚未生成
- 已有前次 float32 验证文件：`qwen_float32_profiles.json`（28 层 × 4 heads，baseline PPL=10.77）

### 2. yi15_9b_full_pipeline — **DEAD (crashed)**
- PID 229912 / 233153 均已不存在
- 退出时间：2026-05-14T14:51:26Z，exit code=0（wrapper 层面）
- **实际崩溃于 Phase 5**：`ImportError: cannot import name 'solve_ratequant_greedy' from 'solver'`
- Phase 1-4 完成，Phase 4 输出了 heterogeneity 指标（top5_concentration=0.6274）
- 但 `yi15_full_results.json` 存在（应为**更早一次成功运行**的结果），关键指标：

| 指标 | 值 |
|------|-----|
| baseline wikitext2 PPL | 7.016 |
| MCKP wikitext2 PPL | 7.313 |
| uniform 4-bit PPL | 7.217 |
| MCKP vs uniform | **-0.096 (FAIL)** |
| top5_concentration | 0.4934 |
| best_k | 2 (PPL=7.221) |
| verdict | **FAIL** |

### 3. GPU

| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 100% | 35,427 / 97,887 MiB |
| 1 | **0% (idle)** | 0 / 97,887 MiB |

### 4. 磁盘

| 挂载点 | 大小 | 已用 | 可用 | 使用率 |
|--------|------|------|------|--------|
| /root/autodl-tmp | 250G | 150G | 101G | 60% |
| / (overlay) | 30G | 17G | 14G | 55% |

---

**需要关注**：yi15 最新一次运行因 `solver.py` 中缺少 `solve_ratequant_greedy` 函数而崩溃，GPU 1 当前空闲。如需重跑需先修复 solver 的导入问题。

---
