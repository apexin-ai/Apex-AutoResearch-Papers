# diagnose cqa1 32758 failures

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_cqa1-32758-failures_20260526T092900_result.json`
- **Structured JSON:** [`c82c97e5935f254b4211.json`](../../sessions/c8/c82c97e5935f254b4211.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。所有数据已收集，以下是报告。

---

## 诊断报告：cqa1-32758 GPU 3/4/5 实验"失败"

### 结论：误报。三个实验全部在正常运行。

---

### 根因

**监控系统无法识别这三个实验，因为它们的启动方式不符合监控框架的约定。**

| 差异点 | GPU 0/1/2（被监控识别） | GPU 3/4/5（被误判死亡） |
|--------|------------------------|------------------------|
| tmux 名称 | `pi05-*-cqa1` | `pi05-obj-s44`, `pi05-long-s43/s44`（无 `-cqa1` 后缀） |
| 启动时间 | 14:52–14:57 UTC | 13:54–13:55 UTC（早 1 小时） |
| `/root/runs/` 日志 | 有对应 `.log` 文件 | 无 |
| sentinel 文件 | 无 | 无 |
| W&B | 无 | 无 |

监控系统在 `/root/runs/` 找不到日志、找不到 sentinel、找不到 W&B heartbeat → 判定 "process dead 5× with no sentinel/W&B"。

---

### GPU 3/4/5 进程状态（全部健康）

| GPU | PID | 运行时长 | CPU% | RSS | 状态 | 当前评估任务 |
|-----|------|---------|------|-----|------|------------|
| 3 | 197917 | 3h36m | 534% | 12GB | Rl+ | `object` benchmark, seed 44 — 正在跑 `pick_up_the_milk` |
| 4 | 198442 | 3h36m | 543% | 14GB | Rl+ | `long` benchmark, seed 43 — 正在跑 `LIVING_ROOM_SCENE5` |
| 5 | 199049 | 3h35m | 529% | 14GB | Rl+ | `long` benchmark, seed 44 — 正在跑 `LIVING_ROOM_SCENE5` |

三个进程的命令行均为 `python -u src/evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 ...`，参数正确，与 GPU 0/1/2 的实验同类型。

---

### GPU 0/1/2 实验状态（健康）

| GPU | PID | tmux | 当前评估任务 |
|-----|------|------|------------|
| 0 | 216649 | pi05-crm-k2-long-s44-cqa1 | tmux buffer 为空，但进程活跃 |
| 1 | 219043 | pi05-adaptive-object-s42-cqa1 | `object` benchmark |
| 2 | 219679 | pi05-adaptive-goal-s42-cqa1 | `goal` benchmark |

---

### 系统健康

- **GPU 温度**：38–51°C，全部正常
- **GPU 显存**：10.7–13.1 GB / 24.5 GB，余量充足
- **系统内存**：115GB / 1TB used，877GB available
- **磁盘**：根分区 14% used（26GB 可用）
- **dmesg**：容器内无权限读取，但内存充裕，不可能 OOM

---

### 是否可以在 GPU 3/4/5 上重跑？

**不可以，也不需要。** 三个实验仍在正常执行中。它们完成后会输出结果到：
- `logs/eval_object_adaptive_pi05_seed44.json`
- `logs/eval_long_adaptive_pi05_seed43.json`
- `logs/eval_long_adaptive_pi05_seed44.json`

如果强行重跑，需要先 kill 当前进程，会浪费已计算的 3.5 小时。

---

### 建议

1. **不做任何操作** — 让 6 个实验自然完成
2. **在监控系统中标记为 false positive** — 这三个实验是手动启动的，不走标准监控流程
3. **后续启动时统一命名规范** — tmux session 名加 `-cqa1` 后缀，stdout 重定向到 `/root/runs/acr-vla-conformal-refinement/`

---
