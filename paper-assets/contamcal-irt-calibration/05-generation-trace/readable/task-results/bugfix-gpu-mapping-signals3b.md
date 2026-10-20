# bugfix gpu mapping signals3B

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_bugfix_gpu-mapping-signals3B_20260515T152702_result.json`
- **Structured JSON:** [`53a0792bccb0d9f61485.json`](../../sessions/53/53a0792bccb0d9f61485.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

排查完成。总结：

---

## 1. Bug 根因

**`compute_signals.py.bak:135`**（事发时的活跃版本）：
```python
if args.gpu:
    os.environ["CUDA_VISIBLE_DEVICES"] = args.gpu
```

调用链：
1. 父 shell 设 `CUDA_VISIBLE_DEVICES=3`（预期用物理 GPU 3）
2. `run_batch.py` 旧版 build_task 把 `--gpu 0` 作为 cmd arg 传给 subprocess
3. `compute_signals.py`（旧版）解析 `--gpu 0` 后，用 `os.environ["CUDA_VISIBLE_DEVICES"] = "0"` **覆盖**了继承的 `"3"` 为 `"0"`
4. 之后 `import torch` → PyTorch 看到 `CUDA_VISIBLE_DEVICES=0` → 跑在物理 GPU 0

## 2. 修复状态

**run_batch.py 和 compute_signals.py 已在之前被更新修复。** 当前代码：

- `run_batch.py:201-208` — 通过 `env=` 参数传 `CUDA_VISIBLE_DEVICES`，不再传 `--gpu` 给子进程：
  ```python
  env = os.environ.copy()
  if task.get("gpu") is not None:
      env["CUDA_VISIBLE_DEVICES"] = str(task["gpu"])
  result = subprocess.run(task["cmd"], ..., env=env)
  ```
- `compute_signals.py`（新版）— 无 `--gpu` 参数，无 `CUDA_VISIBLE_DEVICES` 覆写，接口已适配（`--signal all`, `--sft-data-dir`, `--adapter-path`）

**残留风险**：3 个独立 signal 脚本的 `__main__` 块仍有同样模式（`signal_embedding.py:174`, `signal_minkpp.py:216`, `signal_selfcritique.py:249`），但这些仅在独立运行时触发，主路径不受影响。

## 3. signals_3B 进程状态

PID 576040 已死，无存活子进程。

## 4. 是否需要 git commit + sync

代码已修复且在服务器上是最新的。如果本地仓库也有这份代码，需要确认本地是否同步了最新版。是否需要我检查本地仓库状态并 commit？

---
