# check o3 and gpu status

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_o3-and-gpu-status_20260524T061626_result.json`
- **Structured JSON:** [`8153a240fadb562f75c2.json`](../../sessions/81/8153a240fadb562f75c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## o3 数据

SC 是按 **n_valid=196** 算的，不是 n_questions=204。8 个问题的 traces 全部提取失败，被排除。

| 指标 | 值 |
|------|-----|
| n_questions | 204 |
| **n_valid** | **196** |
| SC 正确数 | 162 |
| **SC%** | **162/196 = 82.65%** ✓ 整数吻合 |
| SICA | 82.65%（delta_pp=0.0，cross-model 没改变任何答案） |
| n_err (n_sica_wrong) | 34 |
| 来源文件 | `results/exp_d135_frontier_scb/o3/results.json` |

结论：82.65% 是精确的，问题出在 n 应该用 196 而非 204。

## GPU 状态

| GPU | 状态 | 详情 |
|-----|------|------|
| cuda:0 | **occupied** | VLLM::EngineCore, 88430 MiB / 97887 MiB, 100% util |
| cuda:1 | **free** | 0 MiB, 0% util |
| cuda:2 | **occupied** | VLLM::EngineCore, 88430 MiB / 97887 MiB, 100% util |
| cuda:3 | **occupied** | VLLM::EngineCore, 88430 MiB / 97887 MiB, 100% util |

cuda:0/2/3 各跑一个 vLLM 引擎（3 张 H200 占满），cuda:1 完全空闲可用。

---
