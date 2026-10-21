# ssh check 5090 finished exps

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_5090_finished_exps_20260521T122748_result.json`
- **Structured JSON:** [`fa13d83a070c869f4a57.json`](../../sessions/fa/fa13d83a070c869f4a57.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验**仍在运行**，只是 PID 变了（被重新启动过）：

| 实验 | 原 PID | 当前 PID | GPU | 进度 | 状态 |
|------|--------|----------|-----|------|------|
| **exp_fewnerd_mf4v2_s42** | 13177 (已消失) | 26531 + 27074 (vLLM) | cuda:1 (30844/32607 MiB, 92%) | **77%** (28891/37648) | 运行中 |
| **exp_fewnerd_mf4v2_s123** | 13035 (已消失) | 26663 + 27228 (vLLM) | cuda:2 (30642/32607 MiB, 93%) | **70%** (26385/37648) | 运行中 |

两个实验都在 18:21 重启，已跑约 2 小时，推理速度 ~5750 toks/s input / ~3075 toks/s output。output 目录目前为空（samples.jsonl 在全部完成后才写入）。

另外 4 块 GPU 全部被占用，还有两个其他实验在跑：
- **cuda:0**: fewnerd_n16_s42 (PID 32118, N=16 实验)
- **cuda:3**: exp_e2_pretrained_fewnerd (PID 8411, pretrained Qwen2.5-7B 基线)

按当前速度估算：s42 剩余 ~23% 约需 4-5 分钟，s123 剩余 ~30% 约需 6-7 分钟。

---
