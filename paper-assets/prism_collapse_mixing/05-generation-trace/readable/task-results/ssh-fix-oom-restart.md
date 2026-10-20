# ssh fix oom restart

**prism collapse mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix-oom-restart_20260515T222338_result.json`
- **Structured JSON:** [`bbe94ec366d5dbea5e17.json`](../../sessions/bb/bbe94ec366d5dbea5e17.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

pipeline 通过 `subprocess.Popen` 调用 `compute_signals.py`。下次调用时（Gen 2+）会自动使用修复后的代码。

---

## 报告

### 1. 当前进程状态
- PID 200889/200890 存活，运行约 57 分钟
- dmesg 无权限读取（非 OOM killer 所致）
- GPU 显存各占 ~8.5GB / 97.9GB，利用率 0%（batch 间歇性）

### 2. Gen 1 信号完成度
- **未完成**，正在计算中
- seed42: ~87% (272/313 batches)
- seed137: ~79% (246/313 batches)
- 预计 10-15 分钟完成

### 3. compute_signals.py 修改详情

| 行号（新） | 修改内容 |
|---------|---------|
| 76-79 | **新增** forward hook：`model.gpt_neox.layers[-1].register_forward_hook()` 只捕获最后一层 hidden state |
| 86 | **移除** `output_hidden_states=True`（原先返回全部 25 层，浪费 ~24 层显存） |
| 89 | **改为** 从 hook dict 取 hidden state：`_last_hidden['val']` |
| 123-124 | **新增** 每 batch 后 `del out, logits, hidden, h_cpu` + `torch.cuda.empty_cache()` |
| 126 | **新增** 循环结束后 `_hook.remove()` |

**显存节省估算**：Pythia-410M batch_size=16 seq_len=256 时，24 层冗余 hidden states 约占 24 × 16 × 256 × 1024 × 2B ≈ 200MB/batch。加上 `empty_cache()` 防止碎片累积。

### 4. 是否重启
- **不需要重启**。当前进程即将完成 Gen 1 信号计算。
- Pipeline 通过 `subprocess.Popen` 调用 `compute_signals.py`，Gen 2+ 信号计算时自动使用修复后的新代码。
- 备份文件：`compute_signals.py.bak`

### 5. 新 PID
- 无需重启，PID 不变：200889 / 200890

---
