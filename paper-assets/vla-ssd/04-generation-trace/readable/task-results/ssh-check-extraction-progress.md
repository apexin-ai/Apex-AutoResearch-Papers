# ssh check extraction progress

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-extraction-progress_20260515T210616_result.json`
- **Structured JSON:** [`bff5272e72e28e1ae017.json`](../../sessions/bf/bff5272e72e28e1ae017.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 进程状态
| PID | 任务 | 运行时间 | 状态 |
|-----|------|---------|------|
| 658056 | untrained_no_inst | 37min49s | **运行中** |
| 661030 | trained_no_inst | 4min00s | **运行中** |

### GPU 占用
| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| GPU 0 | 16,379 / 97,887 MiB | 0% |
| GPU 1 | 16,361 / 97,887 MiB | 0% |

GPU 利用率 0% 是特征提取的正常现象（瞬时采样，实际在批次间歇期）。

### no_inst 特征提取进度

**untrained_no_inst** (PID 658056, 已跑 ~38min)：已完成 **3/10** 个 task
| 文件 | 大小 |
|------|------|
| open_the_middle_drawer_of_the_cabinet.h5 | 2.8G |
| open_the_top_drawer_and_put_the_bowl_inside.h5 | 4.0G |
| push_the_plate_to_the_front_of_the_stove.h5 | 2.0G (正在写入) |

**trained_no_inst** (PID 661030, 已跑 ~4min)：已完成 **1/10** 个 task（正在写入中）
| 文件 | 大小 |
|------|------|
| open_the_middle_drawer_of_the_cabinet.h5 | 2.0G (正在写入，1.1GB 当前) |

文件大小范围 2.0G-4.0G，与 50 demos 预期的 ~2.9GB 量级吻合（不同 task 的 episode 长度不同导致差异）。

### 已有 with-instruction 特征目录
| 目录 | 文件数 | 状态 |
|------|--------|------|
| trained_libero_goal | 10 | **完整** |
| untrained_libero_goal | 10 | **完整** |
| dinov2_libero_goal | 10 | **完整**（目录名是 `dinov2_libero_goal`，不是 `dino_libero_goal`） |

### 预估剩余时间
- **untrained_no_inst**：38min 完成 3 个 task（~12.7min/task），剩余 7 个 → 预估还需 **~89min**（比之前预估慢不少）
- **trained_no_inst**：4min 完成约 1 个 task，剩余 9 个 → 预估还需 **~36min**（与之前预估接近）

untrained 比 trained 慢可能是因为 untrained 模型的特征提取吞吐量不同，或者早期 task 的 episode 更长。

---
