# ops falcon3 eval offline fix

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_falcon3-eval-offline-fix_20260522T110903_result.json`
- **Structured JSON:** [`a3e51a06880b4c253d8b.json`](../../sessions/a3/a3e51a06880b4c253d8b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个 eval 全部正常运行，MMLU 推理进度约 31%（~4300/14042），速度稳定 ~37 it/s。

## 最终报告

### 1. 原始失败原因
原 eval 启动时未配置 AutoDL 代理（`source /etc/network_turbo`），导致 `httpx` 无法连接 HF Hub 下载数据集：
- `RuntimeError: Cannot send a request, as the client has been closed.`
- `[Errno 101] Network is unreachable`

### 2. 数据集缓存状态
已手动构建 HF Hub 格式缓存于 `/root/autodl-tmp/.hf_cache/hub/`：
- **MMLU** (`datasets--cais--mmlu`): test/validation/dev parquet 完整，auxiliary_train 为 dummy（99842 行，eval 不使用该 split）
- **ARC** (`datasets--allenai--ai2_arc`): test/validation/train parquet 完整

### 3. 重启的 3 个 eval

| exp_id | PID | GPU | 进度 | 速度 | GPU Util |
|--------|-----|-----|------|------|----------|
| `eval_falcon3_d000_s42_v2` | 627327 | cuda:0 | 4306/14042 (31%) | ~37 it/s | 91% |
| `eval_falcon3_d005_s42_v2` | 627474 | cuda:1 | 4378/14042 (31%) | ~37 it/s | 90% |
| `eval_falcon3_d025_s42_v2` | 627631 | cuda:2 | 4410/14042 (31%) | ~37 it/s | 89% |

GPU 显存：0/1/2 各 16825 MiB，GPU 3 为既有进程（55019 MiB）。

### 4. 预计完成时间
- MMLU 剩余 ~9700 items / 37 it/s ≈ **4.4 分钟**
- ARC-Challenge 约 1170 items，≈ **0.5 分钟**
- 总计约 **5 分钟后**全部完成

### 5. 异常
- `auxiliary_train` 为 dummy parquet（第一行重复 99842 次），不影响 eval（evaluate.py 只用 test split）
- GPU 3 上有既有进程占用 55019 MiB，与本次 eval 无关

---
