# ops check yi mistral progress

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_yi_mistral_progress_20260515T180004_result.json`
- **Structured JSON:** [`f1dda630c89c7870a661.json`](../../sessions/f1/f1dda630c89c7870a661.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### Yi/Mistral downstream eval (PID 356698)
- **运行时间**: 12 分钟
- **GPU**: cuda:0, RTX PRO 6000 Black, 18856MiB / 97887MiB, 利用率 100%
- **当前进度**: Yi-1.5-9B 第 2/3 个配置 (Uniform 4-bit), loglikelihood 52% (26446/51065), ~56 it/s

| 任务 | 状态 |
|------|------|
| Yi baseline (bf16) | ✅ 完成 — `{arc: 0.5265, hella: 0.5912, piqa: 0.7949, wino: 0.7332}` |
| Yi uniform 4-bit | 🔄 52% |
| Yi MCKP k=2 | ⏳ 等待 |
| Mistral baseline | ⏳ 等待 |
| Mistral uniform | ⏳ 等待 |
| Mistral MCKP k=2 | ⏳ 等待 |

**完成度**: 1/6 任务完成，第 2 个进行中
**预估剩余**: ~35-40 分钟（当前任务 ~5 min + Yi MCKP ~10 min + Mistral 3 个任务 ~24 min，Mistral-7B 比 Yi-9B 略快）

### Phi-3-medium-128k-instruct 下载 (PID 351296)
- **运行时间**: ~80 分钟（自 00:41 开始）
- **进度**: 6 个 safetensors 分片中 1 个完成（model-00005, 4.5GB），5 个下载中（.cache/ 目录 6.3GB incomplete 文件）
- **已下载**: ~10.8GB / ~27.5GB ≈ **39%**
- **速率**: ~2.3 MB/s（HuggingFace 直连，未走 ModelScope）
- **预估剩余**: ~2 小时

### 磁盘空间
- `/root/autodl-tmp/`: 48GB 可用 / 250GB 总量 (81% 已用)
- Phi-3 下载完成后还需 ~17GB，剩余空间充足

### 其他进程
- PID 353520: `run_llama_downstream_eval.py` 也在 cuda:0 上运行（18024MiB）
- PID 357568: CodeLlama-7b-hf 通过 ModelScope 下载中

---
