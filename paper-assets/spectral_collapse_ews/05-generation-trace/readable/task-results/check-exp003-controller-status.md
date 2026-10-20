# check exp003 controller status

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp003_controller_status_20260517T102242_result.json`
- **Structured JSON:** [`8e92a97eadde18c1149e.json`](../../sessions/8e/8e92a97eadde18c1149e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_003 状态汇报

### 进度
- **当前**: Gen 2，正在生成合成数据 **19840/50000** (~39.7%)
- 进程 PID 88156 存活，日志持续写入（2634 行）
- 已完成: Gen 0 (baseline eval) + Gen 1 (生成 → 训练 → eval)

### Controller 触发状态
- Controller 已初始化: `signal=log_det, tau=0.005, k=1.0, r_min=0.2, r_max=0.8`
- **Gen 1 mixing ratio = 0.5000**（默认 50/50，controller 未触发调整）
- Gen 2 尚在生成阶段，还没到 mixing 决策点

### Spectral Metrics 趋势

| Gen | eff_rank | ppl | distinct4 |
|-----|----------|------|-----------|
| 0 (baseline) | 417.55 | 9.55 | 0.7414 |
| 1 | 479.49 (+14.8%) | 10.01 (+4.8%) | 0.7108 (-4.1%) |

eff_rank 上升说明频谱尚未开始坍缩，ppl 和 distinct4 有轻微退化但幅度很小。log_det 信号大概率未达到 tau=0.005 阈值，因此 controller 维持默认 ratio。Gen 2 完成 eval 后是关键观察点——如果累积退化触发阈值，mixing ratio 将开始偏移。

### 错误
无任何 error/exception/traceback/OOM。

### 磁盘
- `/` (root): 84% (剩余 5.1G) — 偏紧，注意监控
- `/root/autodl-tmp`: 48% (剩余 132G) — 充足

---
