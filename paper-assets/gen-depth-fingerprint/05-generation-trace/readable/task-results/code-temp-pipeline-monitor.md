# code temp pipeline monitor

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_temp-pipeline-monitor_20260518T152959_result.json`
- **Structured JSON:** [`ac31e4ddeec70dbbf79a.json`](../../sessions/ac/ac31e4ddeec70dbbf79a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

监控脚本已部署并正常运行。

**当前状态：**

| Target | 数据目录 | 当前 seeds | 目标 | GPU | 状态 |
|--------|----------|-----------|------|-----|------|
| olmo_t05 | olmo-2-1b-t05 | 276/990 | GPU 2 | 生成中 |
| qwen06_t05 | qwen3-0.6b-t05 | 189/990 | GPU 3 | 生成中 |
| olmo_t09 | olmo-2-1b-t09 | 0/990 | GPU 2 | 等待 t05 完成 |
| qwen06_t09 | qwen3-0.6b-t09 | 0/990 | GPU 3 | 等待 t05 完成 |

**产出：**
1. `/root/gen-depth-fingerprint/scripts/monitor_temp_pipeline.py` — 已部署
2. `tmux session temp_monitor` — 运行中，每 120s 检查一次
3. 当 seeds >= 990 时自动触发：
   - Feature extraction（`extract_features.py`，Pythia-410M ref model）→ `data/features_{model}-t{temp}.csv`
   - LOGO classification（binary F1 + 3-class F1 + bootstrap CI + Spearman ρ）→ `results/temp_{model}_t{temp}_eval.json`
4. GPU 调度：olmo 用 GPU 2，qwen 用 GPU 3；同 GPU 内 t=0.5 必须完成后才触发 t=0.9

---
