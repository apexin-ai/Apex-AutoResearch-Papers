# ops check sft status

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-sft-status_20260515T000539_result.json`
- **Structured JSON:** [`a216411b5da48c316761.json`](../../sessions/a2/a216411b5da48c316761.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 SFT 训练都在**正常运行中**，未卡住。

## 状态汇总

| 任务 | GPU | PID | 进度 | 速度 | 预计剩余 |
|------|-----|-----|------|------|---------|
| sft_rasp_20 | cuda:0 (76%, 51.6GB) | 249582 | **859/1870 (46%)** | ~1.07s/it | ~18 min |
| sft_standard_20 | cuda:1 (0%*, 51.6GB) | 249660 | **853/1870 (46%)** | ~1.08s/it | ~18 min |

\* GPU1 瞬时利用率为 0% 是因为 nvidia-smi 采样恰好在两个 batch 之间，显存占用和日志进度确认正常运行。

## 关键信息

- **启动时间**：两者均在 07:47-07:50 CST (即 23:47 UTC 05-14) 加载模型并开始训练，与提交时间吻合
- **数据集**：HF Hub 不可达，但成功使用了本地缓存的 GSM8K (7473 samples)
- **Checkpoint**：两个输出目录目前为空——checkpoint 尚未保存（可能在训练结束时才写入）
- **总训练时间**：1870 steps * ~1.07s ≈ 33 分钟，预计 **~08:23 CST (00:23 UTC)** 前完成

---
