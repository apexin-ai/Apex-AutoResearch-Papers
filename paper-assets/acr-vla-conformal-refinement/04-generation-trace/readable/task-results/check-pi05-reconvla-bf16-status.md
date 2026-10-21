# check pi05 reconvla bf16 status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_pi05-reconvla-bf16-status_20260524T211335_result.json`
- **Structured JSON:** [`4b3448922eb5de325af2.json`](../../sessions/4b/4b3448922eb5de325af2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry state machine doesn't allow direct PREPARING → DONE. I'll report the status as-is.

## 状态汇报

### 1. eval-pi05-reconvla-spatial-s42 — **CRASHED (OOM)**
- GPU 0 加载 PI05 模型时 CUDA OOM
- 崩溃原因：GPU 0 已被其他进程占用 14.3 GiB，剩余仅 26.8 MiB
- 当前 GPU 0 显存 3660/24564 MiB（崩溃进程已退出）
- 需要重新启动，指定空闲 GPU（如 cuda:1，当前 1 MiB 占用）或使用 bf16 加载

### 2. eval-pi05-reconvla-goal-s42 — **RUNNING (GPU 2)**
- GPU 2: 13516/24564 MiB, 20% util
- 进度：**task 2/10**
  - ✅ `open_the_middle_drawer_of_the_cabinet`: **90.0% (18/20)**
  - 🔄 `put_the_bowl_on_the_stove`: 5/5 so far (rollout 5/20)

### 3. eval-pi05-reconvla-object-s42 — **RUNNING (GPU 3)**
- GPU 3: 13624/24564 MiB, 21% util
- 进度：**task 1/10 完成，进入 task 2**
  - ✅ `pick_up_the_alphabet_soup_and_place_it_in_the_basket`: **80.0% (16/20)**

### 4. eval-pi05-reconvla-spatial-s42-bf16 — **未启动**
- 无日志文件（`find` 未找到任何 bf16 相关日志）
- 该实验从未实际运行

### GPU 总览 (bjb2-28827)
| GPU | 显存占用 | 状态 |
|-----|---------|------|
| 0 | 3660/24564 MiB | 空闲（spatial 已崩溃退出）|
| 1 | 1/24564 MiB | 空闲 |
| 2 | 13516/24564 MiB | goal 实验运行中 |
| 3 | 13624/24564 MiB | object 实验运行中 |
| 4 | 3660/24564 MiB | 其他进程 |
| 5 | 4253/24564 MiB | 其他进程 |

---
