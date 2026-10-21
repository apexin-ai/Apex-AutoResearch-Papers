# infra urgent multiseed status gpu

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_urgent-multiseed-status-gpu_20260522T103547_result.json`
- **Structured JSON:** [`38a53b9ab00aaffc3e5f.json`](../../sessions/38/38a53b9ab00aaffc3e5f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 全面状态报告

### 1. GPU 利用率 (westd-16639)

| GPU | 型号 | 利用率 | VRAM |
|-----|------|--------|------|
| 0 | RTX PRO 6000 Blackwell | **98%** | 90.2/97.9 GB |
| 1 | RTX PRO 6000 Blackwell | **98%** | 90.2/97.9 GB |
| 2 | RTX PRO 6000 Blackwell | **96%** | 90.2/97.9 GB |
| 3 | RTX PRO 6000 Blackwell | **0%** | 90.2/97.9 GB (idle) |

GPU 3 有 vLLM (Mistral port 8004) 加载但无实验使用，处于空闲。

### 2. 进程状态 — 全部运行中

| PID | 角色 | 状态 |
|-----|------|------|
| 510872 | cuda:1 Qwen FOLIO master | RUNNING |
| 552333 | cuda:0 Qwen PW master | RUNNING |
| 510987 | cuda:2 Mistral PW master | RUNNING |
| 555317 | Guard (kill_cuda1_after_folio) | RUNNING |

Guard log 最新：18:35 显示 folio seed789 进度 171/204，约 2 files/min。

### 3. 文件进度

**Qwen2.5 FOLIO** (expected: 204)
| Seed | 进度 | 状态 |
|------|------|------|
| 123 | 204/204 | **DONE** |
| 456 | 204/204 | **DONE** |
| 789 | ~173/204 | RUNNING (~15min remaining) |

**Mistral PW** (expected: 600)
| Seed | 进度 | 状态 |
|------|------|------|
| 42 | 600/600 | **DONE** |
| 123 | 261/600 (43%) | RUNNING |
| 456 | — | NOT STARTED |
| 789 | — | NOT STARTED |

**Qwen2.5 PW** (expected: 600)
| Seed | 进度 | 状态 |
|------|------|------|
| 123 | ~322/600 (54%) | RUNNING |
| 456 | — | NOT STARTED |
| 789 | — | NOT STARTED |

### 4. 已完成 seed 准确率

| Condition | Seed | SC | SICA | Δ(SICA-SC) |
|-----------|------|----|------|------------|
| qwen25_folio | 123 | **74.51%** (152/204) | **73.04%** (149/204) | **-1.47pp** |
| qwen25_folio | 456 | **74.02%** (151/204) | **74.02%** (151/204) | **+0.00pp** |
| mistral_pw | 42 | **40.00%** | **36.67%** | **-3.33pp** |

Partial (in-progress):
- mistral_pw seed123 (261/600): SC=39.08%, SICA=37.55%, Δ=-1.53pp

### 5. vLLM 进程

| Port | Model | GPU | 状态 |
|------|-------|-----|------|
| 8002 | Qwen2.5-14B | cuda:1 | Active (folio seed789) |
| 8003 | Mistral-7B | cuda:2 | Active (mistral_pw seed123) |
| 8004 | Mistral-7B | cuda:3 | **IDLE** — 无实验使用 |
| 8005 | Qwen2.5-14B | cuda:0 | Active (qwen25_pw seed123) |

### 6. westd-25068

**Authentication failed.** 仍然无法连接。

---
