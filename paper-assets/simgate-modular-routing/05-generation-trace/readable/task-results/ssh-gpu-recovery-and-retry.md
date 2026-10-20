# ssh gpu recovery and retry

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu-recovery-and-retry_20260518T053604_result.json`
- **Structured JSON:** [`f44b80853bb72ca12dce.json`](../../sessions/f4/f44b80853bb72ca12dce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

| 检查项 | 状态 |
|--------|------|
| **GPU 恢复** | **未恢复。** `nvidia-smi` 是 0 字节空文件，`/dev/nvidia*` 设备不存在，PyTorch 报 `CUDA available: False, GPU count: 0`。驱动仍未加载。 |
| **已保存数据** | **完好。** 26 个 episode JSON 全部存在（chemistry-mix 20/20, find-animal 6/20）+ `retry_dose_response_analysis.json` |
| **Crafter 文件** | **完好。** `crafter_pilot/` 目录及所有文件（heuristic_agent.py, v8, episode_runner, llm_agent 等）均在 |
| **dry-run** | **无法执行**，GPU 不可用，vLLM 无法启动 |
| **全量实验** | **不可提交**，需等 GPU 恢复 |

**结论**: westb-14838 的 GPU 驱动仍然挂掉。数据和代码完好无损，不存在丢失风险。需要等待平台方（AutoDL/SeetaCloud）修复驱动，或者考虑将实验迁移到 westb-13313 执行。

---
