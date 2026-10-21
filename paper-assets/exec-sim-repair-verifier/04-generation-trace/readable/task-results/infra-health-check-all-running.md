# infra health check all running

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_health-check-all-running_20260512T112406_result.json`
- **Structured JSON:** [`1088ba18f72bae51de98.json`](../../sessions/10/1088ba18f72bae51de98.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

| 实验 | 服务器 | 状态 | 运行时长 | 说明 |
|------|--------|------|----------|------|
| cls-seed789 | home-1x5090 | **已完成** | - | EXIT_CODE=0, 所有检查 PASS (Accuracy gap +37.2pp) |
| cls-seed0 | seetacloud | **存活** | 21m24s | 训练中 372/1434 steps (26%), ~3.37s/it, ETA ~60min |
| repo-level-cls | seetacloud | **已崩溃** | - | EXIT_CODE=1, `KeyError: 'sample_weight'` |
| repo-level-cwm | seetacloud | **已崩溃** | - | EXIT_CODE=1, `KeyError: 'sample_weight'` |

### GPU 利用率 (seetacloud 4×5090)

| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 0% | 0 / 32607 MiB |
| 1 | 81% | 24795 / 32607 MiB |
| 2 | 0% | 0 / 32607 MiB |
| 3 | 0% | 0 / 32607 MiB |

只有 GPU 1 在工作（cls-seed0）。repo-level-cls 和 repo-level-cwm 都因 `KeyError: 'sample_weight'` 崩溃，需要修复数据集中的 `sample_weight` 字段后重跑。

---
