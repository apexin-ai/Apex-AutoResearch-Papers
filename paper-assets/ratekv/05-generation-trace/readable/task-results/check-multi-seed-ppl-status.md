# check multi seed ppl status

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_multi_seed_ppl_status_20260516T053102_result.json`
- **Structured JSON:** [`a51fc78ff9cb1bb3d20d.json`](../../sessions/a5/a51fc78ff9cb1bb3d20d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都在运行中，尚未完成。当前状态：

### 1. llama_multi_seed_ppl (PID 399378)
- **状态**: 运行中，已运行 1h53m
- **进度**: Seed 42 (1/3) — head profiling 160/256
- Baseline PPL: **8.0922**, Uniform 4-bit PPL: **8.4701** 已完成
- 仍在第一个 seed 的 profiling 阶段，后续还需 MCKP 求解 + PPL eval，再重复 seed 123/456

### 2. mistral_multi_seed_ppl_v2 (PID 401152)
- **状态**: 运行中，已运行 1h29m
- **进度**: Seed 42 (1/3) — head profiling 130/256
- Baseline PPL: **7.0352**, Uniform 4-bit PPL: **7.1308** 已完成
- 同样在第一个 seed 的 profiling 阶段

### 3. GPU 状态
| GPU | VRAM 占用 | 利用率 |
|-----|----------|--------|
| cuda:0 | 42791 MiB | 100% |
| cuda:1 | 41299 MiB | 100% |

### 4. 结果文件
`/root/ratekv/artifacts/` 下无 multi_seed 相关输出，尚未产出结果。

### 估算
每个 seed 需完成 256 head profiling + MCKP + PPL eval，共 3 个 seed。当前两个实验都刚完成第一个 seed 的 ~50-60% profiling。粗估还需 **3-5 小时**完成全部 3 seed。无需干预，进程正常运行中。

---
