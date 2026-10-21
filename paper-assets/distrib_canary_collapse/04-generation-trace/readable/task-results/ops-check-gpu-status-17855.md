# ops check gpu status 17855

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-gpu-status-17855_20260522T050824_result.json`
- **Structured JSON:** [`97080fda437180e65dbd.json`](../../sessions/97/97080fda437180e65dbd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-17855 实验状态汇总

### GPU 状态
| GPU | 利用率 | 显存占用 | 总显存 |
|-----|--------|----------|--------|
| 0 | **0%** | 14.3G | 95.6G |
| 1 | 96% | 13.9G | 95.6G |
| 2 | 94% | 13.9G | 95.6G |
| 3 | 94% | 14.1G | 95.6G |
| 4 | 89% | 13.9G | 95.6G |
| 5 | 97% | 13.9G | 95.6G |

### 实验进度

| 实验 | PID | GPU | 状态 | 进度 | 运行时间 |
|------|-----|-----|------|------|----------|
| **t25_a060_v3★** | 582540 | cuda:3 | **ALIVE** | gen_22 训练中 (22/25) | 4h07m |
| t25_a050_v3 | 582618 | cuda:0 | **ALIVE** | gen_21 训练中 (21/25) | 4h07m |
| t15_a075_s43 | 582768 | cuda:1 | **ALIVE** | gen_10 训练中 (10/15) | 4h07m |
| t10_a075_s43 | 586115 | cuda:2 | **ALIVE** | gen_9 训练中 (**9/10, 最后一个 gen**) | 3h42m |
| t20_a075_s43 | 603933 | cuda:4 | **ALIVE** | gen_2 训练中 (2/20) | 58m |
| t25_a045_s43 | 577236 | cuda:5 | **ALIVE** | gen_12 训练中 (12/25) | 4h49m |

### 要点
- 全部 6 个实验**进程存活**，正常运行
- **t10_a075_s43** 即将完成（最后 1 个 gen）
- **t25_a060_v3★** 和 **t25_a050_v3** 接近完成（剩余 3-4 个 gen）
- **t20_a075_s43** 刚启动约 1 小时，进度较早（2/20）
- GPU 0 利用率 0% 但 t25_a050_v3 (cuda:0) 进程存活——可能正在做非 GPU 操作（数据生成/保存阶段）

---
