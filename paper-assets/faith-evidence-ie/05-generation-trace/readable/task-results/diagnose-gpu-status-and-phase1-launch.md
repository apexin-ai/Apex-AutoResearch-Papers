# diagnose gpu status and phase1 launch

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gpu-status-and-phase1-launch_20260521T035357_result.json`
- **Structured JSON:** [`479cb66ac29b7189d3bf.json`](../../sessions/47/479cb66ac29b7189d3bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

**GPU 状态**

| GPU | 显存占用 | 进程 | 状态 |
|-----|---------|------|------|
| cuda:0 | 18879 MiB | PID 70706 — LLaMA RSFT s42 with-evi@2048 | 运行 1h07m |
| cuda:1 | 32503 MiB | PID 70388 — 14B RSFT with-evi@2048 | 运行 1h08m |
| cuda:2 | 18879 MiB | PID 64391 — LLaMA SFT s43 with-evi@2048 | 运行 3h07m |
| cuda:3 | 6071 MiB | PID 74712 — **D140 1.7B no-evi@2048** | **刚启动** |

**s43 harvest**: 未完成，metrics.json 不存在，仍在运行。

**D140 Phase 1 启动**:
- **Phase 1b** (1.7B SFT s42 no-evi@2048): **已启动** on cuda:3, PID 74712, registry RUNNING
- **Phase 1a** (1.7B SFT s42 with-evi@2048): **等待 cuda:2** — s43 仍占用，待其完成后启动

---
