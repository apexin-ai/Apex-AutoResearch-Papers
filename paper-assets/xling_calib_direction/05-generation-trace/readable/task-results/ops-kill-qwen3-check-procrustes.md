# ops kill qwen3 check procrustes

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_qwen3_check_procrustes_20260521T013311_result.json`
- **Structured JSON:** [`4f2892f94fb353dab586.json`](../../sessions/4f/4f2892f94fb353dab586.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。摘要：

1. **Qwen3**: PID 36611 已 kill，模型文件和 HF cache 已清理干净
2. **Llama4**: 下载已停止，7/14 shard 已下载（43G），**无活跃下载进程** — 需要重启下载
3. **磁盘**: 350G 中用了 131G，剩余 220G (38%)
4. **Procrustes sensitivity**: `linproj_procrustes_sensitivity.csv` 完整，281 行 = 8 layers × 5 langs × 7 n_pairs，无重复无截断
5. **额外发现**: `probing_controls_v2.py` (PID 47972) 正在运行，CPU 89.8%

产出已写入 `artifacts/kill_qwen3_status.md`。

---
