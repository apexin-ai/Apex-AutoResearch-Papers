# ops cqa1 full status

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1_full_status_20260520T001139_result.json`
- **Structured JSON:** [`e9a1cd7e00209f064cf6.json`](../../sessions/e9/e9a1cd7e00209f064cf6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### 1. GPU 状态

| GPU | PID | 任务 | 显存 | Util |
|-----|-----|------|------|------|
| 0 | 994858 | **eval m16_seed44** (刚启动) | 3459 MiB | 18% |
| 1 | 818806 | eval m128_seed43 | 3461 MiB | 1% |
| 2 | 819552 | eval m16_seed43 | 3459 MiB | 1% |
| 3 | — | **空闲** | 1 MiB | 0% |

### 2. Eval 结果

两个 eval 均在运行中，尚无结果 JSON：

- **m128_seed43**: Ep 180/500 (36%), 运行 1h13m，最近 30 ep 窗口 SR ≈ 26.7% (8/30)
- **m16_seed43**: Ep 160/500 (32%), 运行 1h12m，最近 30 ep 窗口 SR ≈ 50% (15/30)

预计两者均还需 ~2h 完成。

### 3. m16_seed44

- 无 `_v3` 训练日志，但 `checkpoints/smart_compress_m16_seed44/checkpoint.pt` 已存在
- 已提交 eval 到 GPU 0（PID 994858），正在运行，Ep 2/500

### 4. GPU 3 安排

**无待跑任务。** 所有 smart_compress checkpoint（m16/m32/m64/m96/m128 × seed43/seed44）均已有 eval 结果或正在 eval 中。不存在 m128_seed44 checkpoint。GPU 3 当前空闲。

### 5. 最终 nvidia-smi

GPU 0/1/2 各跑一个 eval（各占 ~3.5GB），GPU 3 空闲。3 个 eval 并行运行中。

---
