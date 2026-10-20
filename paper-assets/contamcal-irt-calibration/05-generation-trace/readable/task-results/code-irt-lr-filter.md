# code irt lr filter

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_irt_lr_filter_20260515T201053_result.json`
- **Structured JSON:** [`d625e7a31b1782216b9f.json`](../../sessions/d6/d625e7a31b1782216b9f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 变更摘要

### 方案选择
**方案 1（robust）**：从 `train_config.json` 读取 lr 值，实时过滤。

### 修改文件

**`run_irt_calibration.py`** (7 处修改):
1. **L63**: 新增 `get_train_lr(dirname, checkpoint_dir)` — 读 checkpoint 的 `train_config.json`，含 fallback（eval dir 有 v2 后缀但 checkpoint 无）
2. **L87-89**: `load_eval_results` 签名增加 `lr_filter=None, checkpoint_dir=None`
3. **L115-122**: seed filter 后增加 D076 lr filter 逻辑
4. **L221-225**: `load_pooled_eval_results` 签名增加 `lr_filter, lr_filter_scales, checkpoint_dir`
5. **L237-241**: pooled loop 中按 scale 选择性注入 lr filter
6. **L519-522**: 新增 `--checkpoint-dir` 和 `--lr-filter` CLI 参数
7. **L585-586**: main() Mode 2 传递 lr_filter/checkpoint_dir

**`run_pooled_4bench_irt.py`** (4 处修改):
1. **L14**: docstring 增加 D076 排除规则说明
2. **L52-55**: 新增常量 `CHECKPOINT_DIR`, `STANDARD_LR=5e-5`, `LR_FILTER_SCALES={"3B"}`
3. **L353-356**: `load_pooled_eval_results` 调用传入 lr filter 参数
4. **L370**: exclusions 列表增加 `D076_3B_lr_confound`

### 关键设计决策
- **lr filter 只对 3B 生效**：因为 0.5B/1.5B 全部使用 lr=2e-4（无 confound），全局过滤会清空这两个 scale
- `get_train_lr` 含 fallback：eval dir 命名 `d100_v2_s42` 对应 checkpoint `d100_s42`
- 未找到 `train_config.json` 的 checkpoint 被排除（保守策略）

---
