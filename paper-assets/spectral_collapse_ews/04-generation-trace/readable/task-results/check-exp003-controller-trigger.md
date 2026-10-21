# check exp003 controller trigger

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp003_controller_trigger_20260517T103941_result.json`
- **Structured JSON:** [`71eff853659f10b6f32e.json`](../../sessions/71/71eff853659f10b6f32e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_003 状态汇总

### 进度
- **当前：Gen 2/10，数据生成阶段** — 已生成 26240/50000 样本（~52%）
- Gen 0（pretrained baseline）：已完成
- Gen 1：已完成（生成 50000 样本 + 训练 + 评估）
- Gen 2：正在生成合成数据，尚未进入训练

### 已完成代的指标

| Gen | effective_rank | log_det | perplexity | mix_ratio |
|-----|---------------|---------|------------|-----------|
| 0 | 417.55 | 2366.68 | 9.55 | — (baseline) |
| 1 | 479.49 | 2356.68 | 10.01 | **0.5** |

### Controller 触发判断
⚠️ **Controller 尚未触发。** Gen 1 的 mix_ratio = 0.5（即 base_rate），且日志中没有任何 "mix_ratio" / "controller" / "trigger" 相关输出。Gen 2 还在生成数据阶段，controller 判断逻辑还没执行到。

需要等 Gen 2 完成训练+评估后，看 Gen 3 的 mix_ratio 是否偏离 0.5 才能判断 controller 是否响应了 log_det 下降信号（Gen 0→1 log_det 从 2366.68 降到 2356.68，降幅 ~10，τ=0.005 阈值下这个信号是否足够触发取决于具体实现）。

### GPU 状态
- GPU 0: 61°C, 305W/600W, 65.9GB/97.9GB VRAM, 61% util — 运行 exp_003
- GPU 1: 62°C, 258W/600W, 23.7GB/97.9GB VRAM, 87% util — 有其他进程

### 预估
Gen 1 生成 50000 样本用了约 1775 行日志，Gen 2 目前在第 2849 行生成到 26240。按当前速度，Gen 2 数据生成还需约 30-40 分钟，之后还有训练+评估。**预计 Gen 3 的 controller 判断结果最快 2-3 小时后可见。**

---
