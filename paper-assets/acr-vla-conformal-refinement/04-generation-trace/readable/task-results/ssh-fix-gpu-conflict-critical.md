# ssh fix gpu conflict critical

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix-gpu-conflict-critical_20260517T065801_result.json`
- **Structured JSON:** [`6ccd424e194084f0f45a.json`](../../sessions/6c/6ccd424e194084f0f45a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 最终报告

### GPU 进程状态（清理后）

**bjb1-18228** — 每卡单进程 ✓
| GPU | PID | 任务 | 内存 |
|-----|-----|------|------|
| cuda:0 | 474319 | (早期任务) | 2392 MiB |
| cuda:1 | 531970 | perdof_seed44 | 2392 MiB |
| cuda:2 | 587763 | obs_only_seed46 (14:51启动) | 5645 MiB |
| cuda:3 | 588037 | obs_only_seed47 (14:51启动) | 5645 MiB |

**bjb1-32546** — 每卡单进程 ✓
| GPU | PID | 内存 |
|-----|-----|------|
| cuda:0 | 319128 | 2856 MiB |
| cuda:1 | 295478 | 1887 MiB |
| cuda:2 | 309158 | 2392 MiB |
| cuda:3 | 322337 | 2820 MiB |
| cuda:4 | 393646 | 5645 MiB |
| cuda:5 | 319463 | 2392 MiB |

**bjb2-28827** — 每卡单进程 ✓
| GPU | PID | 内存 |
|-----|-----|------|
| cuda:0 | 224628 | 2856 MiB |
| cuda:1 | 222830 | 2856 MiB |
| cuda:2 | 363223 | 5645 MiB |
| cuda:3 | 242264 | 2856 MiB |
| cuda:4 | 272762 | 1923 MiB |
| cuda:5 | 326081 | 3785 MiB |

### seed46 数据完整性

- **JSON 文件**: 不存在（评估仍在进行中，尚未输出结果）
- **Log 文件**: 存在，16行，内容为模型加载和环境初始化。还没开始 rollout。
- **状态**: PID 587763 正在运行，刚完成初始化（加载 VLM + CRM + 10个 LIBERO task），即将开始 rollout

### 额外 kill 说明

除了用户指定的 590627/590833，我还发现并 kill 了同批次的另外两个冲突进程：
- **590637** (perdof_seed47 on cuda:2) — 与 587763 争 GPU
- **590906** (obs_only_seed46 副本 on cuda:3) — 与 588037 争 GPU

`perdof_seed47` 现在没有运行中的实例，如需要可重新提交到空闲 GPU。

---
