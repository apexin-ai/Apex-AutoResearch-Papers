# ops check 16639 full status

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-16639-full-status_20260519T202857_result.json`
- **Structured JSON:** [`ac316b0233330b7ebe6e.json`](../../sessions/ac/ac316b0233330b7ebe6e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-16639 实验状态汇总

### GPU 分配

| GPU | 显存占用 | GPU利用率 | 用途 |
|-----|---------|----------|------|
| 0 | 89921/97887 MiB | 0% | vLLM (port 8010) — exp-079 已完成，vLLM 空闲 |
| 1 | 0 MiB | 0% | **空闲**，无残留进程 |
| 2 | 89729/97887 MiB | 100% | vLLM (port 8012) — exp-077 运行中 |
| 3 | 90369/97887 MiB | 100% | vLLM (port 8013) — exp-078 运行中 |

### 实验状态

**exp-079 (ICG×LogiQA, cuda:0) — 已完成**
- SC: 0.4750 (95/200), ICG: 0.4700 (94/200), Delta: -0.0050
- 耗时 54.3 min，结果已保存到 `results.json`
- vLLM (port 8010) 仍在运行但空闲（0 reqs, 0% KV cache）

**exp-077 (κ generalization, cuda:2) — 运行中，~64% 完成**
- 进度: 131/204（日志显示 `[131/204] folio_130`）
- 最新日志时间: 04:29，正常推理中
- 尚未生成 `results.json`（只有 log 和 intermediates 目录）

**exp-078 (Debate×LogiQA, cuda:3) — 运行中，~47% 完成**
- 进度: 95/200（日志显示 `[95/200] Processing logiqa_094`）
- 已生成中间 `results.json`（211KB）
- ETA: ~111 min remaining（约还需 1.8 小时）

**exp-072b 残留 (cuda:1) — 无残留**
- GPU 1 显存 0 MiB，无计算进程

### tmux sessions
`exp077_vllm`, `exp077_run`, `vllm_logiqa`, `exp079_vllm` — 共 4 个。exp-078 是 nohup 后台启动的，没有独立 tmux session。

---
