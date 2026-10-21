# debug exp002 gsm8k arc fail

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_exp002-gsm8k-arc-fail_20260514T112502_result.json`
- **Structured JSON:** [`2754d222daf55a1b3744.json`](../../sessions/27/2754d222daf55a1b3744.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部清楚了。

## 诊断结论

**根因**: `signal_minkpp.py:96` 的 bfloat16→numpy 转换 bug：
```python
# 旧代码（失败）
return token_log_probs[0].cpu().numpy()
# 修复后
return token_log_probs[0].cpu().float().numpy()
```

模型以 `torch.bfloat16` 加载，`bfloat16` 张量不能直接 `.numpy()`。numpy 不支持 bfloat16 dtype。

**时间线**:
1. **第一次 batch run**（`/tmp/exp002_signals_05B.log`，18:32 开始）：旧代码，**全部 9 个 task 都失败**（不只是 gsm8k/arc）。embedding 阶段成功（用 sentence-transformers，不涉及 LLM logprobs），但 minkpp 阶段全挂。
2. **代码已被修复**（当前服务器上的 `signal_minkpp.py` 已有 `.float()`）。
3. **第二次 batch run**（PID 353388，`run_05B.log`，18:46 开始）：用修复后的代码。**task 1/9 (d000/mmlu) 正在运行中**，已完成 embedding 和 minkpp，当前在 selfcritique 阶段（mmlu 有 ~14K items 需要逐条 generation，很慢）。

**当前状态**: 修复后的 batch run 运行正常，只是 selfcritique on MMLU 耗时长（已跑 ~41 分钟）。不需要额外干预，让它继续跑完即可。

**产出文件当前状态**:
- `d000/signal_minkpp_mmlu.json`（18:55）- 当前 run 产出，minkpp 已过 ✓
- `d000/signal_embedding_*.json` - 三个 benchmark 都有（第一轮 run 产出）
- `d005/signal_embedding_mmlu.json` - 第一轮 run 产出

需要我做什么操作吗？比如验证 selfcritique 是否也有类似的 bfloat16 问题、估算剩余时间等？

---
