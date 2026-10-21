# fix exp 002 signals 3B gpu interface

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp_002_signals_3B_gpu_interface_20260515T150612_result.json`
- **Structured JSON:** [`9720b9e2f0577da19f02.json`](../../sessions/97/9720b9e2f0577da19f02.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**GPU 3 仍被 PID 576735 占用**（exp001 3B d025_s123 eval 进程，8976 MiB）。按 C002 约束不能提交。

汇总如下：

---

### 1. Kill 确认
PID 576030、576040 均已终止（kill -9，confirmed KILLED）。

### 2. compute_signals.py 新版 CLI 接口

| 参数 | 说明 |
|------|------|
| `--model-path` (required) | Base model 路径 |
| `--adapter-path` | LoRA adapter 路径（可选） |
| `--benchmark` (required) | mmlu/gsm8k/arc_challenge/humaneval |
| `--signal` (required) | s1/s2/s3/s4/all |
| `--output-dir` (required) | 输出目录 |
| `--sft-data-dir` | SFT 数据目录（S1 用） |
| `--ref-model-path` | 参考模型路径（S2 用） |
| `--k-percent` | Min-K% 选择（S2，默认 20） |
| `--original-eval-paths` | 原始 eval 路径（S3 用） |
| `--paraphrase-eval-paths` | 改写 eval 路径（S3 用） |
| `--cache-dir` | HF cache 目录 |
| `--batch-size` | 默认 8 |

**已移除的旧参数**: `--gpu`, `--signals`(复数), `--sft-data-path`, `--dry-run`, `--max-items`

### 3. run_batch.py 修改 Diff

**改动 1: 新增常量和函数**
```python
+ BASE_MODEL_ROOT = "/root/autodl-tmp/.hf_cache/Qwen"
+ def base_model_path(model_name: str) -> str:
+     return f"{BASE_MODEL_ROOT}/{model_name}"
```

**改动 2: build_task() 重写**
```diff
- "--model-path", ckpt,            # ← 旧：传 LoRA adapter 路径
+ "--model-path", base,            # ← 新：传 base model 路径
+ "--adapter-path", ckpt,          # ← 新增：LoRA adapter 单独传
- "--sft-data-path", sft,          # ← 旧：传文件路径
+ "--sft-data-dir", SFT_DATA_ROOT, # ← 新：传目录路径
- cmd.extend(["--gpu", str(gpu)])  # ← 移除：不再传 --gpu 给子脚本
- cmd.extend(["--signals"] + signals)  # ← 旧：多信号列表
+ "--signal", "all",               # ← 新：单参数
- cmd.append("--dry-run")          # ← 移除
- cmd.extend(["--max-items", ...]) # ← 移除
+ "gpu": gpu,                      # ← 新增：存入 task dict 供 env 使用
```

**改动 3: subprocess.run 通过 env 传递 GPU**
```diff
  try:
+     env = os.environ.copy()
+     if task.get("gpu") is not None:
+         env["CUDA_VISIBLE_DEVICES"] = str(task["gpu"])
      result = subprocess.run(
          task["cmd"],
          cwd="/root/contamcal-irt-calibration/exp002",
          capture_output=True, text=True, timeout=14400,
+         env=env,
      )
```

### 4. 提交阻塞

**GPU 3 当前被 PID 576735 占用**（exp001 evaluate.py，Qwen2.5-3B_d025_s123_aligned），8976 MiB。按 C002 约束，必须等该进程完成后才能提交 exp_002_signals_3B。

是否需要我轮询等待 GPU 3 释放后自动提交？

---
