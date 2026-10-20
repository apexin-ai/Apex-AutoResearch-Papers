# gpu d065 d066 docred status check

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_d065_d066_docred_status_check_20260520T030500_result.json`
- **Structured JSON:** [`0a8a7c42e4ee16b67496.json`](../../sessions/0a/0a8a7c42e4ee16b67496.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### westd-16980: d065 LLaMA greedy 4096 重跑

| GPU | 利用率 | VRAM | 任务 | 进度 |
|-----|--------|------|------|------|
| GPU0 | 90% | 18.3/97.9 GB | d065 LLaMA greedy **unc** 4096 | **379/998** (38%) |
| GPU1 | 87% | 18.3/97.9 GB | d065 LLaMA greedy **con** 4096 | **350/998** (35%) |

- 两个进程从 09:35 CST 开始运行，已跑 ~90 分钟
- 速度: unc ~4.2 docs/min, con ~4.0 docs/min
- **ETA**: unc ~13:30 CST (05:30 UTC), con ~14:20 CST (06:20 UTC)

**排队中**:
- `d065_cascade_qwen.sh` — 等两个 LLaMA 进程结束后跑 Qwen greedy unc+con (ETA 开始 ~14:20 CST)
- `d066_qwen_beam_sweep.sh` (PID 712981) — 等 LLaMA unc (PID 697390) 结束后启动

---

### westd-21461: d066 beam sweep + d067 seed variance

| GPU | 利用率 | VRAM | 任务 | 进度 |
|-----|--------|------|------|------|
| GPU0 | 92% | 37.8/97.9 GB | d067 qwen_docred seed123 unc **+ d066 DocRED beam1 unc** | 73/998 + 24/200 |
| GPU1 | 77% | 18.9/97.9 GB | d066 SciERC beam8 full_s1 | 55/551 (10%) |

**d065 在 21461 上已完成** — 无相关进程，GPU0 已释放给 d066/d067。

**d066 SciERC beam sweep (GPU1)** — 接近完成:
- beam1 unc/s1, beam2 unc/s1, beam4 unc/s1: 全部完成 (含 eval)
- beam8 unc: 完成 (551/551)
- beam8 s1: **55/551 (10%)** ← 当前运行，ETA ~11:40 CST

**d066 DocRED beam sweep v2 (GPU0)** — 刚开始:
- beam4 unc/s1: 已有 (200 docs, 之前跑的)
- beam1 unc: **24/200 (12%)** ← 当前运行
- 待跑: beam1 s1, beam2 unc, beam2 s1, beam8 unc, beam8 s1

**d067 seed variance (GPU0)**:
- qwen_scierc 2 seeds × 2 modes: 全部完成
- llama_scierc 2 seeds × 2 modes: 全部完成
- qwen_docred seed123 unc: **73/998 (7%)** ← 当前运行
- 待跑: qwen_docred seed123 s1, seed456 unc+s1, llama_docred 2 seeds × 2 modes

**注意**: GPU0 同时跑两个推理进程（37.8GB VRAM），互相竞争会拖慢速度。d067 qwen_docred 全量 998 docs 估计还需 ~6-7 小时。

---
