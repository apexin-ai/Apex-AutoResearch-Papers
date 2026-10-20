# infra cleanup and bootstrap ci

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_cleanup-and-bootstrap-ci_20260521T215950_result.json`
- **Structured JSON:** [`f2be8827783aaf805494.json`](../../sessions/f2/f2be8827783aaf805494.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务均完成。

---

## 产出

### 任务 1: GPU 清理对比

| GPU | 清理前 | 清理后 | 说明 |
|-----|--------|--------|------|
| 0 | 84,225 MiB | 0 MiB | vLLM Mistral:8000 已 kill |
| 1 | 83,565 MiB | 0 MiB | vLLM Qwen3:8001 已 kill |
| 2 | 0 MiB | 0 MiB | 无变化 |
| 3 | 89,811 MiB | 89,811 MiB | Mistral:8004 保留 |

已 kill 进程：ModelScope 下载 (427876, 427984)、vLLM 8000 (412708, 412714)、vLLM 8001 (413553, 413558)。释放约 168 GB 显存。

### 任务 2: Bootstrap CI 结果

| 指标 | 值 |
|------|-----|
| Point estimate | ρ = **-1.000**, p = 0.000 |
| Bootstrap 95% CI | **[-1.000, -1.000]** |
| Mean ρ | **-1.000** |
| Proportion ρ < 0 | **1.000** |
| Valid bootstrap samples | 9,982 / 10,000 |

5 个模型的 κ 和 Δ 呈完美单调递减关系（κ 严格递增时 Δ 严格递减），因此 Spearman ρ = -1.000。所有非退化 bootstrap 样本均保持该完美负相关，CI 退化为点。18 个无效样本是 bootstrap 抽到常数输入导致的 NaN。

---
