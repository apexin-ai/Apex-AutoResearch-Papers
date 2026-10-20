# diagnose urgent cuda2 cuda3 check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_urgent-cuda2-cuda3-check_20260523T074929_result.json`
- **Structured JSON:** [`ab70f9ef502620a8ed4a.json`](../../sessions/ab/ab70f9ef502620a8ed4a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 产出汇总

### GPU 状态
| GPU | 利用率 | 显存 | 状态 |
|-----|--------|------|------|
| 0 | 94% | 27.2/97.9 GB | PID 231549 运行中 |
| 1 | 92% | 32.5/97.9 GB | PID 194682 运行中 |
| 2 | 0% | 0 GB | **空闲 → 已提交 DPO 3ep** |
| 3 | 0% | 0 GB | **空闲 → 已提交 1.7B no-evi** |

### 1. 1.7B s43 with-evi ✅ DONE
- **ign_f1 = 28.70%** (s42 = 29.33%, Δ = -0.63pp)
- Registry → DONE/success

### 2. 1.7B s43 no-evi → 已提交
- PID **234597**, cuda:3, `--no_evidence` 已传
- 预计 ~6h (1.7B batch_size=1 单卡)

### 3. DPO rebuilt 1ep eval ✅ DONE
- **ign_f1 = 32.23%** (原始 38.9% → **下降 6.67pp**)
- rel_f1 = 33.38%
- Registry → DONE/success
- 注：重建 eval 显著低于原始，可能原始 eval 用了不同 protocol (truncation/max_new_tokens)

### 4. DPO 3ep 训练 → 已提交
- PID **234741**, cuda:2, timeout 2h
- 超参与 1ep 完全一致，仅 num_epochs=3
- wandb: freige-dpo / dpo_rebuilt_3ep

---
