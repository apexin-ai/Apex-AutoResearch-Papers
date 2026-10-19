# eval collect 28034 results v2

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_collect-28034-results-v2_20260519T174252_result.json`
- **Structured JSON:** [`0543e5fa4b2138c639fb.json`](../../sessions/05/0543e5fa4b2138c639fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完毕。汇总：

## exp-004 完整 eval 结果（已入 registry）

| Checkpoint | ToF | NoF | SYCONScore | Eval 耗时 |
|---|---|---|---|---|
| **ckpt-500** | 0.094 | 0.890 | 0.170 | 2269s |
| **ckpt-2000** | 0.149 | 0.879 | 0.255 | 1930s |
| **ckpt-8000** | 0.182 | 0.867 | **0.301** | 1663s |

趋势：SYCONScore 随 step 单调递增（ToF 提升主导，NoF 小幅下降）。最佳 checkpoint-8000。

**文件路径（westd-28034）：**
- Eval 结果：`/root/contrastive_entrain_calib/results/exp004_unified_eval/`
- 训练 checkpoints（16个，500-8000）：`/root/contrastive_entrain_calib/outputs/exp-004-act-baseline/`
- 训练日志：`/root/contrastive_entrain_calib/outputs/exp-004-act-baseline/train_log.jsonl`

## 附带确认

- **exp-016**：unified reeval D027 结果已补入 registry（所有 alpha 的 ToF/NoF/SYCONScore）。alpha=5 SYCONScore=0.054 < vanilla 0.134，确认 negative 结论。
- **vanilla baseline**：registry 中已有结果（ToF=0.111, NoF=0.923, SYCONScore=0.197），标注了 "missing regex postprocess"，28034 上未发现 regex 后处理版本。

---
