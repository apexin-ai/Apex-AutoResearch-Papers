# run quick probe k8

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_quick-probe-k8_20260516T141413_result.json`
- **Structured JSON:** [`0e908a739f16cdbf9329.json`](../../sessions/0e/0e908a739f16cdbf9329.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

启动成功。

**总结：**

1. **硬编码检查**：无阻塞性硬编码。`generate.py`/`score.py`/`pipeline.py` 全部动态读取 `config.K_CANDIDATES`。`curate.py` 的 `no_curation(n, k=4)` 默认值不影响（pipeline 显式传参）。

2. **`run_quick_probe_k8.py` 已创建**，关键修改：
   - `config.K_CANDIDATES = 8`
   - `config.NUM_GENERATIONS = 3`
   - `CONDITION_ID = 10`（避免复用 K=4 的 checkpoint）
   - `CUDA_VISIBLE_DEVICES=0`

3. **已启动**：
   - tmux session: `quick_probe_k8`
   - PID: 506647
   - 日志: `/root/autodl-tmp/carr/outputs/quick_probe_k8.log`
   - 状态: Generation 0/2 正在生成 8 candidates/prompt（已完成 16/2000）

预计每代 ~2x K=4 时间，总计 4-7h 完成 3 代。

---
