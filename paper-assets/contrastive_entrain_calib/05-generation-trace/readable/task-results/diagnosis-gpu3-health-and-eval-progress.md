# diagnosis gpu3 health and eval progress

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_gpu3-health-and-eval-progress_20260521T074803_result.json`
- **Structured JSON:** [`cc70971ad38c379a769e.json`](../../sessions/cc/cc70971ad38c379a769e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。汇总如下：

---

## GPU 3 诊断：**CPU offload 导致卡慢，非硬件问题**

**根因**：accelerate 加载 LoRA 时显存不足，将 ~2.5GB 权重 offload 到 CPU。日志关键行：

```
[WARNING] accelerate.big_modeling: Some parameters are on the meta device because they were offloaded to the cpu.
no modules could be assigned to the following devices due to insufficient memory: - 0: 2489319424 bytes required
```

**表现**：GPU util 持续 0%，VRAM 仅 12922 MiB（其他三卡均 16884 MiB），CPU 占用 8095%。日志自 15:31:29 打出 "Running eval on 362 pairs..." 后 **20+ 分钟零进度**（0/362），推理完全跑在 CPU 上，速度预计慢 50-100x。

**结论**：不是硬件问题，是模型加载时 GPU 3 可用显存不足（可能残留了之前冲突进程的 CUDA context）。**建议 kill 500594 后重启**，确保 GPU 3 显存干净。

ECC: N/A（不支持），dmesg: 容器内无权限。

---

## 4 卡进度总览

| GPU | 任务 | 进度 | GPU Util | VRAM | 速率 | 预计完成 |
|-----|------|------|----------|------|------|----------|
| 0 | ckpt5000-v2 | **100/362 (27.6%)** | 45% | 16884 MiB | ~3.9/min | ~16:53 |
| 1 | ckpt6000 | **100/362 (27.6%)** | 41% | 16884 MiB | ~3.7/min | ~17:00 |
| 2 | ckpt6500 | **100/362 (27.6%)** | 45% | 16884 MiB | ~3.7/min | ~17:01 |
| 3 | ckpt7000-v2 | **0/362 (0%)** | 0% | 12922 MiB | N/A (CPU) | **无限期** |

GPU 0/1/2 均正常推进，约 1h 后（~17:00）完成。

---

## 已完成的 eval 结果（6 个）

`ckpt1000`, `ckpt2000`, `ckpt3000`, `ckpt4000`, `ckpt4500`, `ckpt5500`

---

**建议操作**：kill PID 500594 → 确认 `nvidia-smi --id=3` 显存释放 → 重提 ckpt7000-v2 eval。是否执行？

---
