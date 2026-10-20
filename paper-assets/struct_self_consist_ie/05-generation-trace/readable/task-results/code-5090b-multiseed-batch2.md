# code 5090b multiseed batch2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_5090b_multiseed_batch2_20260518T192212_result.json`
- **Structured JSON:** [`592173fad74a143e0b22.json`](../../sessions/59/592173fad74a143e0b22.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个推理任务都在运行。汇报如下：

## 汇报

### 已启动的推理任务

| GPU | 任务 | 状态 | 备注 |
|-----|------|------|------|
| cuda:0 | FewNERD seed=456 | ✅ 已启动 | PID=16662, 30224MiB, 正在渲染 prompts |
| cuda:3 | FewNERD seed=123 | 🔄 运行中 | 14% (42,680/301,184), ~1.7h 剩余 |

### 无需启动的任务

- **SciERC seed=456**: 已完成（`output/exp_scierc_seed456/`，551 instances, n=8, 含 report.json + full_signal_analysis.json）

### 说明

- 推理脚本是 `code/run_mvp_pilot.py`（非 `inference_n16.py`），实际 n_samples=8（非 16）
- FewNERD 测试集有 37,648 instances × 8 samples = 301,184 prompts，单 GPU 预计 ~2 小时
- cuda:1 和 cuda:2 仍空闲
- tmux 未安装，使用 nohup 后台运行，日志在 `/tmp/infer_gpu0_fewnerd_s456.log`

---
