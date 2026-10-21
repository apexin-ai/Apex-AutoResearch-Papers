# monitor exp 003 controller

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp_003_controller_20260517T104400_result.json`
- **Structured JSON:** [`dc4a5bea2c654c430a59.json`](../../sessions/dc/dc4a5bea2c654c430a59.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_003 (Phase 1 Adaptive D010) 状态报告

### 进程状态
- **PID 88156**: 存活，运行时间 4h12m
- **参数**: `signal=log_det, tau=0.005, k=1.0, r_min=0.2, r_max=0.8`

### 当前进度
- **当前 Generation**: 2/10（正在生成合成数据，28160/50000 = 56%）
- 已完成: Gen 0 (baseline evaluation) + Gen 1 (训练+评估)

### Spectral Metrics

| Generation | eff_rank | log_det | ppl | distinct4 | mix_ratio | train_loss |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 (baseline) | 417.55 | 2366.68 | 9.55 | 0.7414 | — | — |
| 1 | 479.49 | 2356.68 | 10.01 | 0.7108 | **0.5** | 1.983 |

### Controller 触发状态: 尚未触发

Gen 1 的 `mix_ratio = 0.5`（等于 base_rate），controller 未触发。这是预期行为：Gen 1 是第一个训练代，controller 需要至少一代的 log_det 历史才能计算 delta。

**关键观察**：log_det 从 Gen 0→Gen 1 已经下降了约 10 点（2366.68 → 2356.68），同时 ppl 上升、distinct4 下降。这些都是早期退化信号。**Gen 2 是验证 controller 是否正确触发的关键代**——如果 D010 修正有效，Gen 2 的 mix_ratio 应该 > 0.5。

### 注意事项
- 日志中没有 `controller`, `triggered`, `delta`, `S_ema` 等字段的输出——代码可能没有打印 controller 决策的详细日志，只在结果 JSON 中记录 `mix_ratio`
- Gen 2 样本生成还需约 20 分钟完成，之后进入 data mixing 阶段，届时才能看到 Gen 2 的 mix_ratio
- 结果 JSON 路径: `/root/spectral_collapse_ews/results/phase1_adaptive_seed42_results.json`

### 时间估计
Gen 1 从生成到评估完成约 1945 行日志（~2h），Gen 2 开始于 line 1947，目前 sample generation 56%。预计 Gen 2 完成还需约 1.5h，Gen 3+ 的 controller 触发验证约需 6-8h。

---
