# ops 14b progress check v2

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_14b_progress_check_v2_20260519T072028_result.json`
- **Structured JSON:** [`934ee795904e5a38088e.json`](../../sessions/93/934ee795904e5a38088e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

有参考实验数据了。完整 pipeline: d0 gen → 3×(LoRA+gen) → features → classify。参考实验每个 LoRA+gen 周期约 6h40m。

## 14B 实验进度

### nvidia-smi
```
Tue May 19 15:20:48 2026
+-----------------------------------------------------------------------------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
|   0  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:5A:00.0 Off |                  Off |
| N/A   59C    P0            306W /  600W |   32313MiB /  97887MiB |     94%      Default |
|   1  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:A8:00.0 Off |                  Off |
| N/A   59C    P0            308W /  600W |   32313MiB /  97887MiB |     97%      Default |
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|    0   N/A  N/A          776616      C   python                                32304MiB |
|    1   N/A  N/A          787051      C   python                                32304MiB |
+-----------------------------------------------------------------------------------------+
```

### qwen25_14b_temp09 (cuda:0)
- **当前阶段**: Phase 2 — 生成 d0 (unconditional, τ=0.9)
- **d0 进度**: 3827/5000 samples (76.5%)
- **已运行**: 4h22m (自 11:00 起)
- **整体进度**: ~16% (d0 gen 是 pipeline 的第一步；后续还有 3×LoRA finetune + 3×generation + feature extraction + classification)
- **ETA**: ~2026-05-20 13:00 (约 21h 后)
  - d0 剩余 ~1h20m
  - 3×(LoRA+gen) 参考耗时 ~20h（基于 qwen25_14b baseline 每周期 6h40m）
  - features + classify ~20min

### qwen25_14b_topk50 (cuda:1)
- **当前阶段**: Phase 2 — 生成 d0 (unconditional, top-k=50)
- **d0 进度**: 2700/5000 samples (54%)
- **已运行**: 2h23m (12:59 重启，首次 11:00 在 cuda:0 启动后被 Terminated)
- **整体进度**: ~9%
- **ETA**: ~2026-05-20 14:00 (约 22h 后)
  - d0 剩余 ~2h
  - 后续同 temp09

### 备注
- 两个实验的日志只通过 `tee` 记录了启动信息和权重加载进度条，生成过程的 tqdm 进度条用 `\r` 覆盖同行，不写入日志文件
- topk50 首次在 cuda:0 启动，因与 temp09 冲突被终止后于 12:59 在 cuda:1 重启
- 参考时间基于已完成的 `qwen25_14b` baseline 实验（d0→d3 总耗时约 26h）

---
