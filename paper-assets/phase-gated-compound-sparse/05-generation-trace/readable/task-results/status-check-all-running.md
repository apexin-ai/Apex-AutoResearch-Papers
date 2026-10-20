# status check all running

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_check_all_running_20260514T173728_result.json`
- **Structured JSON:** [`02ba438286376f370227.json`](../../sessions/02/02ba438286376f370227.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data. Here's the status report:

---

## 实验状态报告（01:38 CST / 17:38 UTC, May 15）

### 1. c2_n500_deepseek (GPU 0+1) — RUNNING

| GPU | 条件 | 进度 | 速率 |
|-----|------|------|------|
| GPU0 (PID 130124) | importance s015 | **429/500** (85.8%) | ~40s/problem |
| GPU1 (PID 130263) | random s015 | **452/500** (90.4%) | ~40s/problem |

- 当前条件 (s015): 还在第 1/4 个 sparsity level
- 当前条件完成预估：GPU0 ~47min, GPU1 ~32min
- GPU 利用率：GPU0 77% / 33GB, GPU1 97% / 34GB
- **总剩余预估：~17h**（当前条件 + 3 个后续 sparsity: s020/s025/s030, 每个 ~5.5h）

### 2. c2_qw_n500 (GPU 2+3) — RUNNING

| GPU | 条件 | 进度 | 速率 |
|-----|------|------|------|
| GPU2 (PID 131864) | Qwen importance s015 | **322/500** (64.4%) | ~51s/problem |
| GPU3 (PID 132002) | Qwen random s015 | **329/500** (65.8%) | ~51s/problem |

- 当前条件 (s015): 第 1/4 个 sparsity level
- 当前条件完成预估：GPU2 ~2.5h, GPU3 ~2.4h
- GPU 利用率：GPU2 97% / 34GB, GPU3 92% / 35GB
- **总剩余预估：~24h**（Qwen 比 DeepSeek 慢 ~25%）
- 注：`n500_qw_imp_s020.log` 和 `n500_qw_rand_s020.log` 各 1306 字节（仅模型加载头），停留在 22:00——看起来是之前被杀的重复进程残留的日志，不是当前活跃任务

### 3. c3_llama (GPU 2+3) — NEARLY COMPLETE

| GPU | 条件 | 进度 | 速率 |
|-----|------|------|------|
| GPU2 (PID 149238) | importance s030 | **39/50** (78%) | ~1.5min/problem |
| GPU3 (PID 148980) | random s030 | **40/50** (80%) | ~1.5min/problem |

- 已完成条件：s015, s020, s025（各 175 行日志，末尾有 `Verdict: PASS`）
- 当前条件 s030：第 4/4，最后一个 sparsity level
- **预计 ~15-20 分钟内完成**
- 注：PID 已变更（原 138393 → 现 149238/148980），说明中间重启过
- 输出目录：`profiling_output_c3_llama_{importance,random}_s030/` 已创建但尚无文件（完成后写入）
- 已完成的输出：`profiling_output_c3_llama_{importance,random}_s0{15,20,25}/` 各有数据文件

### GPU 总览

| GPU | 占用 | 利用率 | 进程 |
|-----|------|--------|------|
| 0 | 33.4 / 97.9 GB | 77% | c2_n500_deepseek (importance) |
| 1 | 33.9 / 97.9 GB | 97% | c2_n500_deepseek (random) |
| 2 | 62.9 / 97.9 GB | 97% | c2_qw_n500 (34GB) + c3_llama (29GB) |
| 3 | 63.7 / 97.9 GB | 92% | c2_qw_n500 (35GB) + c3_llama (29GB) |

### 要点

- **c3_llama 即将完成**（~15min），完成后 GPU 2+3 各释放 ~29GB 显存
- c2_n500_deepseek 和 c2_qw_n500 都还在第 1/4 个 sparsity level，预计还需 17-24 小时
- 无死亡/僵尸进程残留（原重复 PID 132389/132392 已清理）

---
