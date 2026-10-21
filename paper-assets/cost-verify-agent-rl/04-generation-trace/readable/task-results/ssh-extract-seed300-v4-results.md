# ssh extract seed300 v4 results

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_extract_seed300_v4_results_20260522T220927_result.json`
- **Structured JSON:** [`e2adf872720ab39b4813.json`](../../sessions/e2/e2adf872720ab39b4813.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## seed300 v4 OOD Eval 结果

### 核心指标

| 指标 | 值 |
|------|-----|
| **OOD pass@1** | **10.45% (14/134)** |
| OOD success | 10.45% |
| action_is_valid | 65.4% |
| action_is_effective | 99.3% |
| manager_invalid_action | 0.66% |
| avg num_actions | 45.2 |
| validation generation time | 1485s (~25min) |

### pass@k scaling（reward=10 per success）

| k | best@k mean | 近似 coverage |
|---|-------------|---------------|
| 1 | 1.04 | ~10% |
| 2 | 1.81 | ~18% |
| 4 | 3.31 | ~33% |
| 8 | 5.69 | ~57% |
| 16 | 8.31 | ~83% |
| 32 | 9.77 | ~98% |
| 64 | 9.99 | ~100% |

### 完成状态
评估**正常完成**。有一个 wandb BrokenPipeError 但仅影响日志上传，不影响结果。

### bjb1 GPU 状态
| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| cuda:0 | 0 MiB / 97887 MiB | 0% |
| cuda:1 | 0 MiB / 97887 MiB | 0% |

**两卡均空闲。** 但有 6 个 ray::TaskRunner 进程和 4 个 wandb-core defunct 僵尸进程残留，GPU 已释放。

### 关键结论

**v3 的 0% OOD 是 config artifact（enable_think=false），不是真实能力。** v4 修正 enable_think=true 后，seed300 OOD 从 0% 跃升至 **10.45% (14/134)**。seed300 不属于"healthy-but-zero-OOD"模式，它具备 OOD 泛化能力。pass@k 曲线表明 coverage 随采样次数快速增长（k=32 时已接近 98%）。

---
