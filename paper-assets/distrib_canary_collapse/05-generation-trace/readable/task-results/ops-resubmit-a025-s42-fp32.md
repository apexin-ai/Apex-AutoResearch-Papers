# ops resubmit a025 s42 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_resubmit_a025_s42_fp32_20260519T075734_result.json`
- **Structured JSON:** [`5d9dc16ff5a1aee5e32e.json`](../../sessions/5d/5d9dc16ff5a1aee5e32e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已成功启动：

- **PID**: 109870（python 主进程）
- **GPU 0 显存**: 6525 MiB / 97887 MiB
- **状态**: 已加载 pythia-410m 模型，进入 Generation 0 (baseline)
- **无 right-padding 警告**
- **tmux session**: `alpha_sweep_a025_s42_fp32` 正常运行

根因：之前直接调用 `python` 但未激活 conda 环境，导致 PATH 中找不到 python。修复方式：与其他实验一致，先 `source conda.sh && conda activate base` 再运行。

---
