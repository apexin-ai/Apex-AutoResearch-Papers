# code fix signals 3B bugs

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_signals_3B_bugs_20260515T154509_result.json`
- **Structured JSON:** [`ebf0e0c24cd3d1daff20.json`](../../sessions/eb/ebf0e0c24cd3d1daff20.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复确认完毕。总结：

## 修复结果

### 文件修改
**`/root/contamcal-irt-calibration/exp002/compute_signals.py`，第 33 行**

```diff
- help="Reference model path for S2 Min-K%++ (auto-inferred if not set)")
+ help="Reference model path for S2 Min-K%%++ (auto-inferred if not set)")
```

### Bug 1（argparse 参数名）
`run_batch.py` 已经使用 `--signal`（单数），与 `compute_signals.py` 的 `--signal` 定义一致。**此 bug 在当前代码中已修复。**

但 `--ref-model-path` 的 help 字符串中 `Min-K%++` 的 `%` 未转义，导致 argparse 将 `%++ (` 解析为格式化指令，`--help` 直接崩溃（`ValueError: unsupported format character '(' at index 37`）。此问题现已修复（`%` → `%%`）。

### Bug 2（GPU 映射）
**不存在。** `run_batch.py` 通过 `env["CUDA_VISIBLE_DEVICES"]` 正确隔离 GPU，signals 模块全部使用 `"cuda"` / `model.device` / `device_map="auto"`，在 `CUDA_VISIBLE_DEVICES` 限定后自动映射到 `cuda:0`。

### 验证结果
- `compute_signals.py --help` ：通过（rc=0）
- `run_batch.py --help`：通过（rc=0）
- `run_batch.py --model-size 3B --print-only`：9 个子命令全部使用 `--signal all`，参数传递正确

---
