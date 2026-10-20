# infra gpu cleanup and status

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu-cleanup-and-status_20260523T105353_result.json`
- **Structured JSON:** [`a2a4a73174be324c644a.json`](../../sessions/a2/a2a4a73174be324c644a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据齐全。汇总如下：

---

## GPU 清理

- PID 681007 (vLLM EngineCore, cuda:3): **已 kill**
- cuda:3 显存释放: 88239 MiB → **0 MiB**（释放 ~86 GB）

## 重复实验状态

| 实验 | 16639 进度 | 30973 进度 | 14391 进度 | 备注 |
|------|-----------|-----------|-----------|------|
| qwen25_pw_seed789 | **n=358** (running) | n=251 (running, \_v3) | — | 16639 领先 |
| llama8b_pw_seed789 | **n=303** (running) | n=238 (running, \_v2) | — | 16639 领先 |
| llama8b_pw_seed456 | n=98 (running) | **n=242** (running, \_v2) | — | 30973 领先 |
| llama8b_pw_seed123 | **n=600 ✅** | — | n=359 (running) | 16639 已完成，14391 冗余 |
| qwen25_pw_seed456 | n=478 ⚠️ | — | — | **无活跃进程**，疑似 crash（原 vLLM port 8005 在 cuda:3，已被 kill） |
| llama8b_pw_seed42 | n=223 | — | **n=600 ✅** | 14391 已完成 |

**当前 GPU 占用：**
- westd-16639: cuda:0/1/2 活跃（97%），cuda:3 **已空闲**
- westd-30973: cuda:0/1/2 活跃（96-97%）
- westd-14391: cuda:0 活跃（100%）

## 已完成实验结果 (n=600, ProofWriter)

| 实验 | n | SC% | SICA% | Δ(pp) | p (McNemar) | disc: SC→ | disc: SICA→ | 来源 |
|------|---|-----|-------|-------|-------------|-----------|------------|------|
| llama8b_pw_seed42 | 600 | 72.33 | 66.67 | **-5.67** | 0.0001 | 52 | 18 | 14391 |
| llama8b_pw_seed123 | 600 | 71.33 | 64.17 | **-7.17** | 0.0000 | 67 | 24 | 16639 |
| qwen25_pw_seed123 | 600 | 72.33 | 71.17 | -1.17 | 0.3105 | 21 | 14 | 16639 |
| mistral_pw_seed42 | 600 | 40.00 | 36.67 | **-3.33** | 0.0022 | 30 | 10 | 16639 |
| mistral_pw_seed123 | 600 | 40.83 | 37.50 | **-3.33** | 0.0091 | 37 | 17 | 16639 |
| mistral_pw_seed456 | 600 | 39.83 | 38.67 | -1.17 | 0.3817 | 27 | 20 | 16639 |
| mistral_pw_seed789 | 600 | 38.83 | 37.17 | -1.67 | 0.1742 | 27 | 17 | 16639 |

## 已完成实验结果 (n=204, FOLIO)

| 实验 | n | SC% | SICA% | Δ(pp) | p | 来源 |
|------|---|-----|-------|-------|---|------|
| llama8b_folio_s123 | 204 | 67.16 | 63.73 | -3.43 | 0.0654 | 16639 |
| llama8b_folio_s456 | 204 | 61.76 | 61.27 | -0.49 | 1.0000 | 16639 |
| llama8b_folio_s789 | 204 | 67.16 | 68.14 | **+0.98** | 0.7266 | 16639 |
| mistral_folio_s123 | 204 | 57.84 | 57.84 | 0.00 | 1.0000 | 16639 |
| mistral_folio_s456 | 204 | 28.92 | 27.94 | -0.98 | 0.6250 | 16639 |
| mistral_folio_s789 | 204 | 59.31 | 56.86 | -2.45 | 0.2668 | 16639 |
| qwen25_folio_s123 | 204 | 74.51 | 73.04 | -1.47 | 0.3750 | 16639 |
| qwen25_folio_s456 | 204 | 74.02 | 74.02 | 0.00 | 1.0000 | 16639 |
| qwen25_folio_s789 | 204 | 74.02 | 72.55 | -1.47 | 0.3750 | 16639 |

**关键发现：SICA 在所有模型/数据集上一致 ≤ SC，LLaMA 上差距最大且显著（p<0.001）。** qwen25_pw_seed456 实验疑似因 cuda:3 vLLM 问题中断（n=478），需决定是否在 cuda:3 上重启。

---
