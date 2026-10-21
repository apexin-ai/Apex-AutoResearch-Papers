# code fix signals 3B bugs

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_signals_3B_bugs_20260515T155108_result.json`
- **Structured JSON:** [`937c2808d0c98d0d3e1e.json`](../../sessions/93/937c2808d0c98d0d3e1e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已提交 `6b9ebd9`。

## 结果报告

**(1) argparse 参数名**：已一致。`run_batch.py` 第 102 行传 `--signal all`，`compute_signals.py` 接收 `--signal {s1,s2,s3,s4,all}`。旧版 `.bak` 用 `--signals`（复数 + nargs="+"），导致 task 2-12 全部 rc=2。当前源码已修复。

**(2) CUDA_VISIBLE_DEVICES 传递**：正确。
- `run_batch.py` 第 203 行通过 `subprocess.run(env=...)` 注入 `CUDA_VISIBLE_DEVICES`
- `compute_signals.py` 无 `--gpu` 参数，不会覆盖环境变量（旧版 `.bak` 第 134-135 行会 `os.environ["CUDA_VISIBLE_DEVICES"] = args.gpu`）
- 所有模型加载用 `device_map="auto"` 或 `device="cuda"`，无硬编码 GPU ID
- 信号模块中张量通过 `model.device` 跟随模型设备，正确

**额外操作**：清理了 stale `.pyc` 缓存（旧版 `run_batch.py` 编译产物含 `--signals`）。

---
