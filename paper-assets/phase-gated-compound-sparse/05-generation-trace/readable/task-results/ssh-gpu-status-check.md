# ssh gpu status check

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu-status-check_20260514T055604_result.json`
- **Structured JSON:** [`c332757f80dbf81c4a43.json`](../../sessions/c3/c332757f80dbf81c4a43.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU-PID 映射完成，汇总如下：

**GPU→PID 映射：**
- GPU 0: PID 79817 (bf16_importance_s015, 20890 MiB) + PID 80500 (bf16_importance_s030, 18462 MiB) — **两个实验共享**
- GPU 1: PID 79411 (bf16_importance_s020, 26042 MiB)
- GPU 2: PID 77565 (v6_random_s030_r3, 31588 MiB)
- GPU 3: PID 80212 (bf16_importance_s025, 20890 MiB)

---

| GPU | 显存 | 实验 | 进度 | 预计剩余 | 备注 |
|-----|------|------|------|---------|------|
| 0 | 39.4/97.9 GB (89%) | **bf16_importance_s015** | 21/50 | ~8 min | ⚠️ 与 s030 共享 GPU |
| 0 | _(同上)_ | **bf16_importance_s030** | 4/50 | ~15 min | ⚠️ 与 s015 共享 GPU |
| 1 | 26.1/97.9 GB (76%) | **bf16_importance_s020** | 18/50 | ~9 min | |
| 2 | 31.6/97.9 GB (76%) | **v6_random_s030_r3** | 41/50 | ~5 min | 最快完成 |
| 3 | 20.9/97.9 GB (79%) | **bf16_importance_s025** | 10/50 | ~8 min | |

**已完成/终止：**
- **v6_random_s025** — 50/50 已完成，Verdict: FAIL (EXIT_CODE=0)
- **mvp_v5_random_s020** — 已被 kill (EXIT_CODE=129/137)

**其他：**
- `huggingface-cli download Qwen/Qwen2.5-7B-Instruct` 仍在后台运行 (PID 58322)

**空闲 GPU：无** — 全部 4 张 GPU 都在使用，GPU 0 还跑了两个实验。v6_random_s030_r3 (~5 min 后) 完成后 GPU 2 将空闲。

---
