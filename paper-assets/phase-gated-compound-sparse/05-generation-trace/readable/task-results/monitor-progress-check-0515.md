# monitor progress check 0515

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_progress_check_0515_20260515T021653_result.json`
- **Structured JSON:** [`a55ad61e8d5a9baf8546.json`](../../sessions/a5/a55ad61e8d5a9baf8546.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

save_project_file 不支持此文件名。直接输出报告。

---

# Progress Check — 2026-05-15 10:18 UTC+8

## c2_n500_deepseek (cuda:0 + cuda:1)

| Condition   | Done | Total | Status     |
|-------------|------|-------|------------|
| imp_s015    | 500  | 500   | ✅ Complete |
| imp_s020    | 500  | 500   | ✅ Complete |
| imp_s025    | 386  | 500   | 🔄 Running |
| imp_s030    | —    | 500   | ⏳ Queued   |
| rand_s015   | 500  | 500   | ✅ Complete |
| rand_s020   | 500  | 500   | ✅ Complete |
| rand_s025   | 432  | 500   | 🔄 Running |
| rand_s030   | —    | 500   | ⏳ Queued   |

- **imp_s025** (GPU 0): rate ~1.9 prob/min → ETA ~11:18
- **rand_s025** (GPU 1): rate ~1.9 prob/min → ETA ~10:54
- **s030**: auto-starts after s025, ~4.4h each → DeepSeek 全部完成 ~**15:42**

## c2_qw_n500_r3 (cuda:2 + cuda:3)

| Condition   | Done | Total | Status     |
|-------------|------|-------|------------|
| imp_s015    | 500  | 500   | ✅ Complete |
| imp_s020    | 500  | 500   | ✅ Complete |
| imp_s025    | 500  | 500   | ✅ Complete |
| imp_s030    | 58   | 500   | 🔄 Running |
| rand_s015   | 500  | 500   | ✅ Complete |
| rand_s020   | 500  | 500   | ✅ Complete |
| rand_s025   | 500  | 500   | ✅ Complete |
| rand_s030   | 39   | 500   | 🔄 Running |

- **imp_s030** (GPU 2): rate ~2.3 prob/min → ETA ~13:28
- **rand_s030** (GPU 3): rate ~2.3 prob/min → ETA ~13:39
- Qwen 全部完成 ~**13:39**

## GPU Health

| GPU | Util | VRAM Used | VRAM Total |
|-----|------|-----------|------------|
| 0   | 80%  | 33.4 GiB  | 95.6 GiB  |
| 1   | 77%  | 33.9 GiB  | 95.6 GiB  |
| 2   | 76%  | 25.1 GiB  | 95.6 GiB  |
| 3   | 77%  | 25.7 GiB  | 95.6 GiB  |

## 风险/异常

无异常。Qwen 已进入最后一轮 s030，DeepSeek s025 接近尾声。**全部完成 ETA: ~15:42 UTC+8**，瓶颈在 DeepSeek s030（尚未启动）。

---
