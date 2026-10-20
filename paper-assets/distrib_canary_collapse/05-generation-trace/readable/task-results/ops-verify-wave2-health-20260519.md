# ops verify wave2 health 20260519

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify_wave2_health_20260519_20260519T100551_result.json`
- **Structured JSON:** [`d8dcf44d1b71ff7a7c68.json`](../../sessions/d8/d8dcf44d1b71ff7a7c68.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| GPU | exp_id | PID alive | Gen | Speed | Issues |
|-----|--------|-----------|-----|-------|--------|
| 0 | alpha_sweep_a025_s42_fp32 | Yes | 5/10 (step 2891/5000, 58%) | ~7.67 it/s | None |
| 2 | padding_robustness_a100_s42_fp32 | Yes | 0 (baseline, just started) | — | No right-padding warnings |
| 3 | alpha_sweep_a025_s43_fp32 | **Dead** | — | — | **Crashed: HF hub OSError** |
| 4 | alpha_sweep_a025_s44_fp32 | **Dead** | — | — | **Crashed: HF hub OSError** |
| 5 | alpha_sweep_a075_s42_fp32 | Yes | 0 (baseline, just started) | — | None |

**GPU 使用情况:**
- GPU 0: 14237 MiB, 94% — active (a025_s42)
- GPU 1: 34801 MiB, 71% — 有其他进程占用（非本批实验）
- GPU 2: 7451 MiB, 68% — active (padding_robustness)
- GPU 3: 0 MiB, 0% — **空闲**
- GPU 4: 0 MiB, 0% — **空闲**
- GPU 5: 7453 MiB, 69% — active (a075_s42)

**问题汇总:**

`alpha_sweep_a025_s43_fp32` 和 `alpha_sweep_a025_s44_fp32` 均在模型加载阶段崩溃，根因相同：`RuntimeError: Cannot send a request, as the client has been closed.` → HuggingFace Hub 连接失败，导致无法下载 `EleutherAI/pythia-410m` 的 config.json。可能是两个进程同时发起 HF 请求时发生了 httpx client 竞争。需要重启这两个实验（GPU 3、4 空闲可用）。

---
