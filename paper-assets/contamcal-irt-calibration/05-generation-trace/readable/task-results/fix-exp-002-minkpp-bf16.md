# fix exp 002 minkpp bf16

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp-002-minkpp-bf16_20260514T124528_result.json`
- **Structured JSON:** [`d2134019f64b2ef2be1e.json`](../../sessions/d2/d2134019f64b2ef2be1e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 checkpoint 都在。重启命令：

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp002 && python run_batch.py --model-size 0.5B --gpu 0 2>&1 | tee run_05B.log
```

## 修复总结

**修改的文件：**

1. **`signal_minkpp.py:96`** — `.float()` 修复已在文件中（非本次修改）
2. **`compute_signals.py`** — 新增 `_load_cached_signal()` 函数（lines 191-198），为 embedding/minkpp/selfcritique 三个信号加了 per-signal 缓存跳过逻辑。已计算的 signal JSON 存在则直接加载，不重复计算
3. **`run_batch.py:208`** — `timeout` 从 7200 (2h) 增加到 14400 (4h)，解决 MMLU selfcritique 超时问题

**根因**：不是 bfloat16 bug（已修复），是 run_batch.py 的 2h timeout 导致 MMLU 的 selfcritique 计算（14k items × generate）超时被杀。

**需要重跑的信号**：所有 selfcritique + 部分 minkpp + d005/d100 的多数信号。per-signal cache 会自动跳过 embedding/minkpp 已完成的部分，大幅缩短重跑时间。

请用上面的命令在 tmux `exp002_05B` 中重启。

---
