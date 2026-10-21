# check n32 progress v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_n32_progress_v2_20260523T054158_result.json`
- **Structured JSON:** [`73b5d8444d044847c66f.json`](../../sessions/73/73b5d8444d044847c66f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

**进程状态**：运行中，已运行 ~13h28m
- PID 157197 (python run_mvp_pilot.py)，PID 157469 (VLLM::EngineCore)
- 仅使用 **GPU 3**（`CUDA_VISIBLE_DEVICES=3`），**不是** 4 卡并行

**进度**：**73%** — 881,344 / 1,204,736 prompts
- 已用时：13h26m
- 当前速度：~13-35 it/s（波动大），input ~3302 toks/s, output ~4922 toks/s

**GPU 利用率**：
| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 0% | 2 MiB / 32607 MiB |
| 1 | 0% | 2 MiB / 32607 MiB |
| 2 | 0% | 2 MiB / 32607 MiB |
| **3** | **77%** | **29844 MiB / 32607 MiB** |

**ETA**：按当前速率（~18.2 it/s 平均），剩余 323,392 prompts ≈ **~5h** 剩余，预计 **~18:30 (今天下午)** 完成。

**输出目录**：`output/fewnerd_pretrained_n32_seed42/` 当前为空，脚本应在全部推理完成后统一写入。

**注意**：之前提到的 shard0-3 日志是 05-22 18:23 的旧运行（PID 不同），与当前任务无关。当前是单 GPU 运行，总 prompt 数 1,204,736 = 9412 instances × 32 samples × 4（可能是 4 轮 temperature 或其他参数）。

---
