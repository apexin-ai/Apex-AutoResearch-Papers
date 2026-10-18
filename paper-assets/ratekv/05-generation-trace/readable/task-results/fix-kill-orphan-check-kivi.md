# fix kill orphan check kivi

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_kill_orphan_check_kivi_20260515T144123_result.json`
- **Structured JSON:** [`a7825411da388b44696d.json`](../../sessions/a7/a7825411da388b44696d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

**1. PID 340906 (Mistral hires 孤儿)** — 已 kill，确认死亡。

**2. PID 341441 (KIVI v2)** — 进程已退出，因为**实验已完成**。

**3. KIVI baseline v2 结果**：
| 配置 | PPL |
|------|-----|
| KIVI-4bit-g32-r128 (Qwen2.5-7B) | **9.8976** |
- 298938 tokens, 583 chunks, stride=512
- 结果已保存: `/root/ratekv/artifacts/kivi_baseline_qwen7b_v2_results.json`
- Registry 已更新为 DONE

**4. GPU 状态**：
| GPU | 型号 | 温度 | 功耗 | 显存 | Util |
|-----|------|------|------|------|------|
| 0 | RTX PRO 6000 Black (96GB) | 64°C | 118W/600W | 0MiB | 100% |
| 1 | RTX PRO 6000 Black (96GB) | 36°C | 36W/600W | 0MiB | 0% |

**GPU 0 异常**：显示 100% util 但 0MiB 显存且无进程。这是 kill 孤儿进程后的残留状态，通常会自行恢复。如果持续不降，可能需要 `nvidia-smi --gpu-reset -i 0`。

**5. tmux 会话**：仅 `yi15_9b_full_pipeline` 存活，无 KIVI 相关 session。

---
