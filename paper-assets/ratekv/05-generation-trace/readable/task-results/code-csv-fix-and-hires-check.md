# code csv fix and hires check

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_csv_fix_and_hires_check_20260514T040119_result.json`
- **Structured JSON:** [`5127d1c640beab536238.json`](../../sessions/51/5127d1c640beab536238.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务都完成了。

---

### 任务 1：CSV 修复 ✓

exp_e_hires_profile 行已更新：
- `uniform_ppl`: 15.4454 → **11.345**
- `mckp_vs_uniform`: 5.8764 → **1.776**
- 新增 `eval_note` 列，exp_e 填 "uniform from exp_c bf16 retest"，其他行留空

---

### 任务 2：双卡 hires 进程状态

| 进程 | PID | 状态 | 运行时间 | GPU 显存 | 进度 |
|------|-----|------|---------|---------|------|
| Llama hires | 171900 | **存活** | 1h36m | 29,480 MiB | 398/768 heads (52%) |
| Mistral hires | 173653 | **存活** | 1h20m | 27,850 MiB | 111/256 heads (43%) |

- **Llama**：当前在 L16H4，ETA 未显示（按速率估计还需约 1.5h）
- **Mistral**：当前在 L13H6，ETA ~96 min

两个进程都正常运行，GPU 各自独占一张卡。

---
