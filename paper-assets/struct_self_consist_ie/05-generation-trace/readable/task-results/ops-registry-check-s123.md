# ops registry check s123

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_registry-check-s123_20260524T081851_result.json`
- **Structured JSON:** [`51023027f54886ea0c0a.json`](../../sessions/51/51023027f54886ea0c0a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**Registry 状态已修正为 RUNNING。**

实验 `exp_fewnerd_mf4v2_s123_v4` 之前在 registry 中存在但 conclusion 为 `killed`（来自之前 v3 的记录），filter 查询时未返回是因为状态不匹配。现已更新为 RUNNING。

**服务器进程状态**：
- 主进程 PID 273294：`run_mvp_pilot.py` seed=123，已运行 ~2 小时，CPU 35%
- vLLM 子进程 PID 273638：占用 GPU cuda:0，30588 MiB 显存，CPU 99%
- 在 tmux session 中运行，进程树完整

**注意**：tee 未成功写入 `train.log`（输出目录在 tee 启动时可能尚未创建），`output/fewnerd_mf4v2_seed123_v4/` 目录当前为空。实验结果（`samples.jsonl`）应在推理完成后生成。

---
