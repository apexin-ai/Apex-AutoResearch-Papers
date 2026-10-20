# infra check gpu processes

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check-gpu-processes_20260514T055731_result.json`
- **Structured JSON:** [`1927a37affbad079d2d3.json`](../../sessions/19/1927a37affbad079d2d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态汇报

| GPU | 显存占用 | 利用率 | PID | 实验名 | CUDA_VISIBLE_DEVICES |
|-----|---------|--------|-----|--------|---------------------|
| 0 | 44266 MiB / 97887 MiB | 97% | **79817** | bf16_importance_s020 | 0 |
| 0 | ↑ (同上) | ↑ | **80500** | bf16_importance_s030 | 0 |
| 1 | 26051 MiB / 97887 MiB | 63% | 79411 | bf16_importance_s015 | 1 |
| 2 | 31597 MiB / 97887 MiB | 97% | 77565 | v6_random_s030_r3 | 2 |
| 3 | 20899 MiB / 97887 MiB | 73% | 80212 | bf16_importance_s025 | 3 |

### 关键发现

**GPU 0 存在冲突**：`bf16_importance_s020`（PID 79817）和 `bf16_importance_s030`（PID 80500）都被分配到 `CUDA_VISIBLE_DEVICES=0`，两个进程共享同一张卡，合计占用 ~44GB 显存。

所有 5 个进程均存活（状态 `Ss+`）。`bf16_importance_s020` 正在正常推进，当前处理到第 19/50 个问题。尽管两个实验挤在 GPU 0 上没有 OOM，但 97% 利用率 + 71°C 温度说明负载很重，可能互相拖慢。

---
