# ssh fix gpu and launch both

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix-gpu-and-launch-both_20260518T220013_result.json`
- **Structured JSON:** [`c78831186749388d4636.json`](../../sessions/c7/c78831186749388d4636.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都在正常运行。

## 报告

| 项目 | Condition A (Prompt Ablation) | Condition B (Filter Ablation) |
|------|------|------|
| **GPU** | GPU 0 (RTX 5090, 29628 MiB) | GPU 1 (RTX 5090, 29508 MiB) |
| **vLLM PID** | 170164 (in-process) | 169577 (API server, port 8001) |
| **tmux session** | `grounding-prompt-ablation` | `grounding-filter-ablation` |
| **状态** | 正在跑 `chemistry-mix` ep 0/20，vLLM 推理中 (~2700 toks/s input) | 正在跑 `chemistry-mix` Ep 1/20，API 请求正常 200 OK |

**修复内容**：
- `run_grounding_filter_wrapper.sh`: `CUDA_VISIBLE_DEVICES` 0→1, port 8000→8001, 所有 localhost URL 同步更新
- Prompt ablation 无需修改，`LLMAgent` 通过 `gpu_id=0` + `setdefault("CUDA_VISIBLE_DEVICES", "0")` 正确绑定 GPU 0

**nvidia-smi 确认**：两张卡均 ~90% GPU-Util，各自独立运行 vLLM EngineCore。

---
