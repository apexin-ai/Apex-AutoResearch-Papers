# diag dcol deberta 003

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_dcol_deberta_003_20260515T020544_result.json`
- **Structured JSON:** [`b72ec3fa14287336d919.json`](../../sessions/b7/b72ec3fa14287336d919.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成，结果如下：

---

## 诊断结果

### 根因

**GPU 竞争，非僵尸进程。** PID 239543 在 dcol_003 运行期间占用了物理 cuda:1 上 **57.35 GiB** 显存。dcol_003 自身使用 ~37 GiB，两者合计 ~94 GiB，撑满了 95 GiB 的 GPU。当 dcol_003 在 batch 440 附近尝试分配 512 MiB 时触发 OOM。

PID 239543 现已死亡，无法追溯其来源（比 gpt2xl_topk50_001 的 PID 233355 晚启动，不是它）。可能是之前某次实验的残留进程。

日志中的 `EXIT_CODE=129` = SIGHUP，说明 dcol_003 进程被信号终止。

### cuda:1 当前状态

**已清空可用。** GPU 1 显存占用 0 MiB。

```
GPU 0: 15629 MiB / 97887 MiB  ← gpt2xl_topk50_001 (PID 233355) 在跑
GPU 1:     0 MiB / 97887 MiB  ← 空闲，可以立即重跑
```

tmux 里只有 `gpt2xl_topk50_001` 一个 session，没有残留。

### dcol_trainer.py GPU 设置

**正确。** 第 376 行：
```python
device = torch.device(f"cuda:{args.gpu}" if torch.cuda.is_available() else "cpu")
```
通过 `--gpu 0` + 环境变量 `CUDA_VISIBLE_DEVICES=1` 隔离，torch 的 `cuda:0` 映射到物理 GPU 1。代码没有硬编码 GPU ID 的问题。

### v4 建议

1. **直接重跑即可** — cuda:1 现在空闲，dcol_003 单独运行只需 ~37 GiB，95 GiB GPU 绑绑有余
2. **启动前加 GPU 预检** — 在 launch script 里加一行检查目标 GPU 是否有其他进程占用，避免再次撞上 GPU 竞争：
   ```bash
   nvidia-smi --query-compute-apps=pid,used_memory --format=csv,noheader -i 1 | grep -q . && echo "WARNING: GPU 1 occupied" && exit 1
   ```
3. **可选安全余量** — 如果担心显存波动，可以把 `batch_size` 从 32 降到 24，或加 `--gradient_checkpointing`，但当前配置在独占 GPU 时完全够用，非必须

---
