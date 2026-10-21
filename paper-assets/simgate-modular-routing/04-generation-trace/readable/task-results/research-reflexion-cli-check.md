# research reflexion cli check

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_reflexion-cli-check_20260517T131334_result.json`
- **Structured JSON:** [`319765e2c11e8f4c1e33.json`](../../sessions/31/319765e2c11e8f4c1e33.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整信息如下：

## CLI 参数列表

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--tasks` | all 11 | 逗号分隔的 task 子集 |
| `--episodes-per-task` | 20 | 每 task episode 数 |
| `--max-trials` | 3 | 每 episode 最大 retry/reflexion 次数 |
| `--mode` | **必填** | `reflexion` 或 `retry` |
| `--model` | (未知默认) | vLLM 模型名 |
| `--api-base` | (未知默认) | vLLM OpenAI-compatible API base URL |
| `--output-dir` | `results/{mode}_baseline/` | 输出目录 |
| `--max-steps` | 30 | 每 episode 最大步数 |
| `--seed` | - | 随机种子 |
| `--dry-run` | flag | 只打印计划不执行 |

## 11 个 Task 完整列表

1. `chemistry-mix`
2. `find-animal`
3. `find-non-living-thing`
4. `freeze`
5. `grow-fruit`
6. `identify-life-stages-1`
7. `identify-life-stages-2`
8. `inclined-plane-determine-angle`
9. `lifespan-longest-lived`
10. `lifespan-longest-lived-then-shortest-lived`
11. `measure-melting-point-unknown-substance`

## 建议 Task 分割方案

按复杂度和预期耗时均衡拆分（长名称 task 通常步骤更多）：

**Port 8000 (6 tasks):**
- `chemistry-mix`
- `find-animal`
- `find-non-living-thing`
- `freeze`
- `grow-fruit`
- `identify-life-stages-1`

**Port 8001 (5 tasks):**
- `identify-life-stages-2`
- `inclined-plane-determine-angle`
- `lifespan-longest-lived`
- `lifespan-longest-lived-then-shortest-lived`
- `measure-melting-point-unknown-substance`

逻辑：后 5 个 task 名称更长、涉及多步科学推理（物理角度、多轮生命周期比较、熔点测量），预计单 episode 消耗 token 更多但 task 数少 1 个，总负载大致平衡。

---
