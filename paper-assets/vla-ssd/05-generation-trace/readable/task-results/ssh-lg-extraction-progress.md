# ssh lg extraction progress

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_lg-extraction-progress_20260515T171527_result.json`
- **Structured JSON:** [`cec7761caca7bbe37285.json`](../../sessions/ce/cec7761caca7bbe37285.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## LIBERO-Goal 特征提取进度报告

### 进程状态
| 进程 | PID | 运行时间 | 内存(RSS) | CPU |
|------|-----|---------|-----------|-----|
| lg_extract_trained | 627256 | 30m27s | ~2.4GB | 987% |
| lg_extract_untrained | 627335 | 30m25s | ~2.3GB | 955% |

两个进程均存活，CPU 使用正常。

### GPU 使用
| GPU | 利用率 | 显存 |
|-----|--------|------|
| cuda:0 | 0% | 16,417 / 97,887 MiB |
| cuda:1 | 0% | 16,375 / 97,887 MiB |

GPU 利用率瞬时为 0%（推理是 burst 式的，snapshot 抓到空闲间隙），显存占用 ~16GB 正常。

### 提取进度

**Trained (cuda:0)**: **6/10 tasks 完成**，正在处理第 7 个 task
| 已完成 task | 文件大小 |
|------------|---------|
| open_the_middle_drawer_of_the_cabinet | 2.70 GB |
| open_the_top_drawer_and_put_the_bowl_inside | 3.92 GB |
| push_the_plate_to_the_front_of_the_stove | 2.94 GB |
| put_the_bowl_on_the_plate | 1.80 GB |
| put_the_bowl_on_the_stove | 1.95 GB |
| put_the_bowl_on_top_of_the_cabinet | 1.02 GB |

**Untrained (cuda:1)**: **5/10 tasks 完成**，正在处理第 6 个 task
| 已完成 task | 文件大小 |
|------------|---------|
| open_the_middle_drawer_of_the_cabinet | 2.71 GB |
| open_the_top_drawer_and_put_the_bowl_inside | 3.93 GB |
| push_the_plate_to_the_front_of_the_stove | 2.94 GB |
| put_the_bowl_on_the_plate | 1.80 GB |
| put_the_bowl_on_the_stove | 1.72 GB |

### 预估剩余时间
- 平均 ~5 min/task（30 min 完成 5-6 tasks）
- **Trained**: 剩余 4 tasks → ~20 min
- **Untrained**: 剩余 5 tasks → ~25 min

### DINO LIBERO-Goal 特征
`/root/autodl-tmp/vla-ssd/features/dinov2_libero_goal/` **不存在**，尚未开始提取。

### 异常
无异常。local_files_only 修复后两个进程均稳定运行，预计再 25-30 分钟全部完成。

---
