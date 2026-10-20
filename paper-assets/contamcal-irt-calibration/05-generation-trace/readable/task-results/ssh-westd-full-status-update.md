# ssh westd full status update

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd-full-status-update_20260519T052220_result.json`
- **Structured JSON:** [`fdaf2354644a06ff9402.json`](../../sessions/fd/fdaf2354644a06ff9402.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-29999 Full Status Report

**Server verified**: 4× NVIDIA RTX PRO 6000 Black, 97887 MiB each ✓

---

### GPU Overview (nvidia-smi)

| GPU | Memory | Util | Process PID | Status |
|-----|--------|------|-------------|--------|
| 0 | 0 / 97887 MiB | 0% | — | **IDLE** |
| 1 | 52087 / 97887 MiB | 79% | 110298 | Gemma d100 |
| 2 | 37195 / 97887 MiB | 62% | 106255 | OLMo-2 d005 v2 |
| 3 | 56709 / 97887 MiB | 60% | 103574 | Phi-4 d050 |

---

### 1. OLMo-2 d025 (cuda:0, PID 102091) — COMPLETED ✓

- **Process**: Dead (exited cleanly)
- **.done sentinel**: Exists (May 19 13:18)
- **Final metrics**:
  - Steps: **3384/3384** (100%)
  - train_loss: **0.9582**
  - mean_token_accuracy: **0.7732**
  - entropy: 0.9835
  - Runtime: **7420s (~2h04m)**
  - EXIT_CODE=0

---

### 2. OLMo-2 d005 v2 (cuda:2, PID 106250) — RUNNING

- **Process**: Alive (wrapper 106250, GPU child 106255)
- **Progress**: **2459/3177 (77.4%)**
- Latest loss: 0.8955, accuracy: 0.778
- **ETA**: ~25 min remaining (~2.1s/it)

---

### 3. Phi-4 d050 (cuda:3, PID 103574) — RUNNING

- **Process**: Alive (main + 32 torch compile workers)
- **Progress**: **2214/3642 (60.8%)**
- Latest loss: 1.149, accuracy: 0.735
- **ETA**: ~1h07m remaining (~2.8s/it)

---

### 4. Gemma d100 (cuda:1, PID 110293) — RUNNING (just started)

- **Process**: Alive (wrapper 110293, GPU child 110298)
- **Progress**: **50/4159 (1.2%)**
- Latest loss: 2.527, accuracy: 0.487 (warmup phase)
- **ETA**: ~3h05m remaining (~2.7s/it)

---

### 5. Gemma d050 — COMPLETED ✓ (previously finished)

- **.done sentinel**: Exists (May 19 13:11)
- **Final metrics**:
  - Steps: **3642/3642** (100%)
  - train_loss: **1.260**
  - mean_token_accuracy: **0.7239**
  - entropy: 1.155
  - Runtime: **10400s (~2h53m)**
  - EXIT_CODE=0

---

### Summary

| Experiment | Status | Progress | Loss | Accuracy |
|-----------|--------|----------|------|----------|
| OLMo-2 d025 | **DONE** | 100% | 0.958 | 0.773 |
| Gemma d050 | **DONE** | 100% | 1.260 | 0.724 |
| OLMo-2 d005 v2 | Running | 77% | 0.896 | 0.778 |
| Phi-4 d050 | Running | 61% | 1.149 | 0.735 |
| Gemma d100 | Running | 1% | 2.527 | 0.487 |

**GPU 0 is now free.** OLMo-2 d005 v2 should finish next (~25 min), then Phi-4 d050 (~1h), then Gemma d100 (~3h).

---
