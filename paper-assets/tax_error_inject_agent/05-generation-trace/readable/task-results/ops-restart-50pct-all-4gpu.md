# ops restart 50pct all 4gpu

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_restart-50pct-all-4gpu_20260515T235629_result.json`
- **Structured JSON:** [`3e539ceaeb420ff4b044.json`](../../sessions/3e/3e539ceaeb420ff4b044.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个训练全部启动成功。

| GPU | exp_id | 数据集 | seed | 显存 |
|-----|--------|--------|------|------|
| cuda:0 | v4-taxei-fixed-inject50-s1-r2 | taxei inject50 | 1 | 30619 MiB / 99% |
| cuda:1 | v4-random-fixed-inject50-s1-r2 | random inject50 | 1 | 30619 MiB / 99% |
| cuda:2 | v4-taxei-fixed-inject50-s7 | taxei inject50 | 7 | 27245 MiB / 87% |
| cuda:3 | v4-random-fixed-inject50-s7 | random inject50 | 7 | 27293 MiB / 99% |

**修正点**：项目路径从 `/root/tax_error_inject_agent` 改为 `/root/autodl-tmp/tax_error_inject_agent`（原路径不存在）。s1 重试用 `-r2` 后缀（原实验已 DONE/failed）。

每 15 分钟自动检查训练状态。

---
