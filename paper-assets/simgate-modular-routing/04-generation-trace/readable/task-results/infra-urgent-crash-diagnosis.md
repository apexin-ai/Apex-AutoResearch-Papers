# infra urgent crash diagnosis

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_urgent-crash-diagnosis_20260513T184325_result.json`
- **Structured JSON:** [`5d16b4186b6166d2ba2e.json`](../../sessions/5d/5d16b4186b6166d2ba2e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**没有 crash，两个实验都在正常跑。** 进度慢是因为每个 episode/task 本身耗时长。

---

## Boil v3 (GPU 1)

| 项目 | 状态 |
|------|------|
| 进程 | PID 650426 存活，00:23 启动，VLLM PID 651246 (28GB) |
| 日志最后修改 | 02:43:56（刚刚，持续写入中） |
| 进度 | **17/20 episodes**（当前正在跑 Episode 17） |
| episodes.jsonl | 17 行 |
| 错误 | 无（grep error 结果为 0） |
| 速度 | ~8.3 min/episode（141 分钟完成 17 个），正常范围 |

## 预筛 (GPU 0)

| 项目 | 状态 |
|------|------|
| 进程 | PID 131653 存活（02:42 刚启动 grow-fruit），VLLM PID 132374 (28GB) |
| 日志最后修改 | 02:44:19（持续写入） |
| 进度 | **7 tasks 完成 + 1 running（grow-fruit）= 8/25** |
| 已完成 | chemistry-mix, chemistry-mix-paint-tertiary-color, find-animal, find-living-thing, find-non-living-thing, find-plant, freeze |
| 错误 | 无 |
| 速度 | ~20 min/task（每个 task 5 episodes x 30 steps） |

## 诊断结论

- GPU 0 利用率 0%、GPU 1 利用率 11% — 两张卡各跑各的，无争抢
- 进度看起来"停滞"是因为 ScienceWorld 每个 episode 需要多轮 LLM 推理（最多 30 步），单 episode 耗时 ~8 分钟
- 预估完成时间：boil v3 还剩 ~3 个 episode ≈ 25 分钟；预筛还剩 17 个 tasks ≈ 5-6 小时

---
