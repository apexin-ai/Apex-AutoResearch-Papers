# code plan a implementation

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_a_implementation_20260514T031920_result.json`
- **Structured JSON:** [`bb08fe68a2dc9b677fb6.json`](../../sessions/bb/bb08fe68a2dc9b677fb6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Seed0 r2 正在 synthetic data generation 阶段（10%），运行正常。

## 完成报告

### 改动摘要

**1. controller.py** — 完全重写
- 删除旧的 `CollapseAwareController`（velocity form + spectral rank 信号）
- 新增 `PIController`：位置式 PI，`u(k) = u_bias + Kp * e(k) + integral`
- 误差定义 `e = setpoint - y`（entropy 下降 → e > 0 → 增加 real data）
- 条件积分 anti-windup：输出饱和时停止积分
- `set_baseline(g0_entropy)`：自动计算 setpoint = g0_entropy * margin
- `from_config()` 类方法 + `ControllerConfig` dataclass 保留
- 默认参数：Kp=0.15, Ki=0.02, u_bias=0.5, w_min=0.1, w_max=0.9, margin=0.9

**2. controlled_pipeline.py** — 大幅重构
- 信号源从 spectral rank → n-gram entropy（100K generated tokens）
- spectral rank 保留为辅助记录指标
- 支持 5 种模式：`pure_synthetic`, `fixed_mix`, `threshold`, `pi_controller`, `pure_real`
- G0 训练后自动测量 baseline entropy → `controller.set_baseline()`
- PIController 实例跨 generation 保持状态（integral 累积）
- control_log.jsonl 记录：generation, segment, step, unigram_entropy, trigram_entropy, vocab_coverage, eff_rank, holdout_ppl, w, mode, controller_state
- 新增 CLI 参数：--mode, --w_fixed, --threshold, --kp, --ki, --u_bias, --setpoint_margin, --setpoint, --w_min, --w_max
- checkpoint_interval_tokens 默认改为 5M（与 v7 一致）

**3. run_plan_a.sh** — 新建
- 支持环境变量覆盖所有参数（MODE, SEED, KP, KI 等）
- 支持尾部额外参数传递 (`"$@"`)
- conda 环境自动激活

### Dry-run 结果

| 测试 | 结果 |
|------|------|
| PIController 基本功能 | PASSED — set_baseline/step/get_state 正确 |
| Anti-windup（y=0 极端 collapse） | PASSED — w=0.9 clamped，integral 不增长 |
| ControllerConfig → from_config | PASSED |
| reset() | PASSED — integral/step_count 归零，setpoint 保留 |
| controlled_pipeline.py --help | PASSED — 全部 19 个参数正确解析 |
| 全量 import 验证 | PASSED — PIController/MixedDataset/VALID_MODES 正常导入 |
| GPU dry-run | 跳过 — GPU 被 seed0 r2 占用 |

### 与设计文档的偏差

无实质性偏差。设计文档中 `run_plan_a.sh` 未包含 `--checkpoint_interval_tokens` 和 `--u_bias`/`--w_min`/`--w_max`，已补充。

---
