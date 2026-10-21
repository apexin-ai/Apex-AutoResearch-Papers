# diagnose exp 009 crash v3

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_009_crash_v3_20260517T000217_result.json`
- **Structured JSON:** [`62eba5d2579e859c7e43.json`](../../sessions/62/62eba5d2579e859c7e43.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部正常运行：

- **GPU 0**: exp-008 (494 MiB)
- **GPU 1**: exp_009_10pct_v3 (6616 MiB) — 已开始 continued pretraining
- **GPU 2**: exp_009_30pct_v3 (3482 MiB) — 加载训练模型
- **GPU 3**: exp_009_50pct_v3 (3482 MiB) — 加载训练模型

## 总结

**Crash 原因**：不是网络问题，是 **CUDA OOM**。MMLU 5-shot 评估使用 `batch_size=8`，loglikelihood 计算时 logits 张量 (8×~2000×151936) 超出 24GB 显存。

**修复内容** (`scripts/exp009_dose_response.py`):
1. `batch_size=8` → `batch_size="auto:4"` — 自动找最大安全 batch size（smoke test 确认找到 64）
2. 移除 `simple_evaluate` 中重复的 `batch_size=8` 参数
3. 添加 `max_length=2048` 限制序列长度
4. 添加 `HF_DATASETS_OFFLINE=1`、`HF_HUB_OFFLINE=1`、`TRANSFORMERS_OFFLINE=1` 防止网络请求

3 个 v3 实验已在 GPU 1/2/3 上运行，预计 ~5h/GPU。

---
