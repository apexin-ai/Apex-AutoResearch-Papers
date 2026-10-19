# ops training results collection

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_training-results-collection_20260513T102734_result.json`
- **Structured JSON:** [`c4cb71290811e3989bf5.json`](../../sessions/c4/c4cb71290811e3989bf5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总完成。结果如下：

## 已收集的 best checkpoint eval metrics

### Qwen2.5-Coder-3B (m2_embed_verify)

| Strategy | Status | Best step | val_loss | R@1 | R@5 | R@10 |
|----------|--------|-----------|----------|-----|-----|------|
| random | **completed** | 500 | 0.4834 | 0.5357 | 0.9808 | 1.0 |
| embedding | running (step ~1200) | 500 | 0.4603 | **0.5557** | 0.9808 | 1.0 |
| dataflow | pending | — | — | — | — | — |

### StarCoder2-3B (plan_013_starcoder)

| Strategy | Status | Best step | val_loss | R@1 | R@5 | R@10 |
|----------|--------|-----------|----------|-----|-----|------|
| random | **completed** | ~500 | — (日志未捕获) | — | — | — |
| embedding | **completed** | 1000 | 0.4816 | 0.5078 | 0.9843 | 1.0 |
| dataflow | running (step ~500) | ~500 | — (best 已保存，指标未刷出) | — | — | — |

### 关键发现
- **Qwen embedding 策略 R@1=0.5557 最优**，比 random (+2pp)、比 StarCoder embedding (+4.8pp)
- R@5 和 R@10 近饱和（~0.98 和 1.0），差异主要在 R@1
- 所有 run 的 best 都在 step 500，之后 val_loss 持续上升（过拟合）
- StarCoder random 的 eval 指标因 stdout 缓冲未写入日志，需训练脚本补 `flush=True`

### 缺失数据
- StarCoder random：best checkpoint 已保存但 eval 指标丢失
- StarCoder dataflow：eval@500 已执行（best 模型 18:13 保存），等日志刷出
- Qwen embedding / dataflow：仍在训练中

汇总文件已写入 `bjb1-42106:/root/structfuse/results/`，artifact 已注册。

---
