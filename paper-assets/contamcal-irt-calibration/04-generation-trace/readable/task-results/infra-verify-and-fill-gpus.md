# infra verify and fill gpus

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_verify-and-fill-gpus_20260516T142018_result.json`
- **Structured JSON:** [`4d2b0b4a4ae2df2595cc.json`](../../sessions/4d/4d2b0b4a4ae2df2595cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证和修复工作完成。以下是完整报告：

---

## 报告

### 1. exp_002_signals_3B_d000_s123_cuda2 — **真失败，不是 false positive**

- 日志文件 `/root/runs/contamcal-irt-calibration/exp_002_signals_3B_d000_s123_cuda2.log` 不存在
- 输出目录 `/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d000_s123/` 不存在
- **但**：已有新 attempt 在 cuda:0 运行（PID 780943，已运行 1h36m），输出到 `Qwen2.5-3B_d000_s123_a32`，8/9 信号完成，s4_selfcritique_mmlu 进行中

### 2. cuda:1 PID 760236 (0.5B d100_s123) — **已成功完成**

- PID 760236 已退出
- 输出目录 `Qwen2.5-0.5B_d100_s123` 完整（9 signal + 3 merged = 12 files）
- cuda:1 现在在跑新任务：PID 780591，0.5B-Instruct signals（1h37m elapsed，mmlu 的 s1/s2 完成，s4 进行中）

### 3. cuda:4/5 确认仍在运行 ✓

### 4. cuda:2 和 cuda:3 — **无 3B s123 signals 可启动**

所有合法 3B s123 dosages 的 signals 已完成或在跑：

| Dosage | Alpha | Status |
|--------|-------|--------|
| d000_s123 | 32 ✓ | 运行中 cuda:0，差 s4_mmlu + mmlu merge |
| d005_s123 | 32 ✓ | **完成** |
| d025_s123 | 32 ✓ | **完成**（本次补了 mmlu merge） |
| d100_a32_s123 | 32 ✓ | **完成** |
| d100_s123 | **16** ✗ | C006 黑名单 |
| d000_v2_s123 | **16** ✗ | C006 黑名单 |

C007 优先级检查：0.5B s123（4/4 完成）、1.5B s123（4/4 完成），优先级条件满足。

### 本次执行的操作

1. **d025_s123 mmlu merge**：合并 14042 items → `signals_merged_mmlu.json`
2. **d000_s123_a32 部分 merge**：合并 arc_challenge（1172 items）和 gsm8k（1319 items）的 merged 文件。mmlu merge 需等 cuda:0 上 s4_mmlu 完成后再做

### 待办

- cuda:0 PID 780943 完成后，需手动 merge d000_s123_a32 的 mmlu（同样的 Python 一行命令）
- cuda:2、cuda:3 当前空闲，无 3B s123 signals 工作。可分配给其他任务

---
