# fix d010 controller logdet

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_d010_controller_logdet_20260517T062835_result.json`
- **Structured JSON:** [`65be37c4c40ee1ccd67b.json`](../../sessions/65/65be37c4c40ee1ccd67b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

---

## 修改摘要

### `src/controller.py`
- `__init__`: 新增 `signal="log_det"` 参数；`tau` 默认值 `0.02` → `0.005`
- `update(S_t)` → `update(spectral_metrics)`: 接收 dict，用 `self.signal` 键取值（含 `eff_rank` → `effective_rank` 映射）
- `get_state()` 增加 `signal` 字段

### `src/config.py`
- `controller_tau` 默认值 `0.02` → `0.005`
- 新增 `controller_signal: str = "log_det"`

### `src/pipeline.py`
- Controller 初始化增加 `signal=config.controller_signal`
- adaptive 模式下 `controller.update()` 改为传递 `{"effective_rank": ..., "log_det": ...}` dict

### `run_phase1.py`
- 新增 `--signal {log_det,eff_rank}` 参数（default=log_det）
- `--tau` 默认值 `0.02` → `0.005`
- `config.controller_signal = args.signal`
- summary 和 print 输出包含 signal 信息

### 清理
- `/root/autodl-tmp/spectral_collapse_ews/checkpoints_phase1/adaptive_seed42/` 已删除
- `results/phase1_adaptive_seed42_results.json` 已删除

### GPU 状态
- GPU 0: 65.9GB 占用（其他实验）
- **GPU 1: 已释放（0 MiB），可用**

---
