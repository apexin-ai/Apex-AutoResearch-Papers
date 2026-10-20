# diagnostic cuda5 check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnostic_cuda5_check_20260516T110844_result.json`
- **Structured JSON:** [`5e474f28c14b6561b2fc.json`](../../sessions/5e/5e474f28c14b6561b2fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**进程状态：活着，正常推进，未卡死。**

### GPU 5 状态
- 利用率 26%，显存 2067 MiB — 正常工作中

### 当前任务
正在计算 `Qwen2.5-0.5B_d100_s123` 的 **s4 self-critique (MMLU)**：
- 进度：chunk [7000:8000]，batch 77/500（~1.07s/it）
- 已完成 ~7154 / 14042 items（~51%）
- 预计此信号剩余 ~60 分钟

### 各 adapter 完成度

| Adapter | 状态 |
|---------|------|
| d005_s123 | ✅ 全部完成 (s1+s2+s4+merged × 3 benchmarks) |
| d025_s123 | ✅ 全部完成 |
| d000_s123 | 🟡 缺 s4_gsm8k、merged_gsm8k |
| d100_s123 | 🟡 进行中 — 缺 s4_mmlu(当前)、s2_gsm8k、s4_gsm8k、merged_mmlu、merged_gsm8k |

### 为什么跑了 8+ 小时
不是卡死。s4 self-critique 对 MMLU（14042 items）在 0.5B 模型上需要 ~2h/adapter，脚本遍历 4 个 adapter × 3 个 benchmark × 4 个 signal，总计算量预期 10-12 小时。

### 预计剩余时间
约 2-3 小时（d100 mmlu s4 完成后还需 d000/d100 的 gsm8k s4 + merge）。

---
