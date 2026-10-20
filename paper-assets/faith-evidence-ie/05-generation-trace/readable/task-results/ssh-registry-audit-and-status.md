# ssh registry audit and status

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_registry-audit-and-status_20260521T234218_result.json`
- **Structured JSON:** [`2b42f2c93be12daf446a.json`](../../sessions/2b/2b42f2c93be12daf446a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集完毕。

---

## 任务 1: GPU 状态

| GPU | 显存占用 | PID | 进程 |
|-----|---------|-----|------|
| 0 | 6,071 / 97,887 MiB (6%) | 140534 | `freige.eval.test_inference` — **test_eval_1_7b_sft_s42** |
| 1 | 32,503 / 97,887 MiB (33%) | 125323 | `freige.eval.test_inference` — **test_eval_14b_sft_s42** |
| 2 | 94,453 / 97,887 MiB (97%) | 142872 | `freige.training.rsft_trainer` — **retrain_4b_rsft_ced_s42_v2** |
| 3 | 32,503 / 97,887 MiB (33%) | 143166 | `freige.eval.test_inference` — **test_eval_14b_sft_s42_no_evi** |

注意：PID 125323（GPU 1）与预期的 125321 略有出入，应为同一实验的子进程。

---

## 任务 2: Stale RUNNING 实验（全部 DEAD，进程已结束）

### 1. d140_1_7b_sft_s42_no_evi_2048_fix (PID 87382) — ✅ DEAD

| 指标 | 值 |
|------|-----|
| **F1** | **0.4436** |
| **ign_F1** | **0.4233** |
| precision | 0.4584 |
| recall | 0.4298 |
| ign_precision | 0.4297 |
| ign_recall | 0.4172 |
| tp | 5222 |
| pred_count | 11391 |
| gold_count | 12151 |
| evi_precision/recall/f1 | 0.0 / 0.0 / 0.0 |
| format_compliance_rate | 0.9848 |
| field_compliance_rate | 0.0 |
| n_predictions | 44566 |
| n_truncated | 507 |
| inference_time_seconds | 7438.2 |
| config: no_evidence=true, split=dev, seed=42, max_new_tokens=2048, model=Qwen3-1.7B, adapter=sft_output_qwen3_1_7b_bf16 |

### 2. d140_4b_sft_s42_no_evi_2048_fix (PID 88987) — ✅ DEAD

| 指标 | 值 |
|------|-----|
| **F1** | **0.4095** |
| **ign_F1** | **0.4016** |
| precision | 0.4062 |
| recall | 0.4128 |
| ign_precision | 0.3859 |
| ign_recall | 0.4185 |
| tp | 5016 |
| pred_count | 12349 |
| gold_count | 12151 |
| evi_precision/recall/f1 | 0.0 / 0.0 / 0.0 |
| format_compliance_rate | 0.9980 |
| field_compliance_rate | 0.0 |
| n_predictions | 25638 |
| n_truncated | 178 |
| inference_time_seconds | 7606.2 |
| config: no_evidence=true, split=dev, seed=42, model=Qwen3-4B, adapter=sft_output |

### 3. d140_8b_sft_s42_no_evi_2048_fix (PID 87302) — ✅ DEAD

| 指标 | 值 |
|------|-----|
| **F1** | **0.5227** |
| **ign_F1** | **0.5019** |
| precision | 0.5001 |
| recall | 0.5475 |
| ign_precision | 0.4716 |
| ign_recall | 0.5363 |
| tp | 6653 |
| pred_count | 13304 |
| gold_count | 12151 |
| evi_precision | 0.9063 |
| evi_recall | 0.0196 |
| evi_f1 | 0.0384 |
| edcr | 0.7051 |
| format_compliance_rate | 1.0 |
| field_compliance_rate | 0.0081 |
| n_predictions | 31119 |
| n_truncated | 260 |
| inference_time_seconds | 10900.5 |
| config: no_evidence=true, split=dev, seed=42, model=Qwen3-8B, adapter=sft_output_qwen3_8b_bf16 |

### 4. d140_4b_sft_s42_with_evi_2048 (PID 93402) — ✅ DEAD

| 指标 | 值 |
|------|-----|
| **F1** | **0.4033** |
| **ign_F1** | **0.3946** |
| precision | 0.3954 |
| recall | 0.4115 |
| ign_precision | 0.3748 |
| ign_recall | 0.4167 |
| tp | 5000 |
| pred_count | 12645 |
| gold_count | 12151 |
| **evi_precision** | **0.7823** |
| **evi_recall** | **0.7991** |
| **evi_f1** | **0.7906** |
| edcr | 0.7262 |
| evi_f1_joint | 0.3129 |
| format_compliance_rate | 0.9980 |
| field_compliance_rate | 0.7523 |
| n_predictions | 24682 |
| n_truncated | 243 |
| inference_time_seconds | 8887.1 |
| config: no_evidence=false, split=dev, seed=42, model=Qwen3-4B, adapter=sft_output |

### 5. test_eval_14b_rsft_s42 (PID 97434) — ✅ DEAD

无 `metrics.json`，但有 `test_summary.json`（test split，无 gold label 计算 metrics 的方式不同）：

| 指标 | 值 |
|------|-----|
| **F1** | **0.3849** |
| **ign_F1** | **0.3849** |
| precision | 0.4805 |
| recall | 0.3210 |
| tp | 5570 |
| pred_count | 11593 |
| gold_count | 17350 |
| **evi_precision** | **0.4684** |
| **evi_recall** | **0.8442** |
| **evi_f1** | **0.6025** |
| edcr | 0.7865 |
| evi_f1_joint | 0.2688 |
| format_compliance_rate | 0.998 |
| field_compliance_rate | 0.36 |
| n_documents | 500 |
| n_predictions | 15835 |
| n_truncated | 67 |
| inference_time_seconds | 19085.8 |
| config: split=test_revised, no_evidence=false, model=rsft_output_14b (Qwen3-14B RSFT) |

### 6. eval_llama_rsft_s42_no_evi_2048 (PID 95606) — ✅ DEAD

| 指标 | 值 |
|------|-----|
| **F1** | **0.5703** |
| **ign_F1** | **0.5559** |
| precision | 0.5673 |
| recall | 0.5734 |
| ign_precision | 0.5440 |
| ign_recall | 0.5684 |
| tp | 6967 |
| pred_count | 12282 |
| gold_count | 12151 |
| evi_precision | 1.0 |
| evi_recall | 0.0003 |
| evi_f1 | 0.0007 |
| format_compliance_rate | 0.9990 |
| field_compliance_rate | 0.0 |
| n_predictions | 24365 |
| n_truncated | 140 |
| inference_time_seconds | 15710.3 |
| config: no_evidence=true, split=dev, seed=42, model=rsft_output_llama_3_1_8b_k1 (Llama-3.1-8B RSFT) |

---

## 任务 3: 当前活跃实验

| 实验 | PID | 状态 | GPU | 说明 |
|------|-----|------|-----|------|
| test_eval_14b_sft_s42 | 125323 | **ALIVE** | GPU 1 (32.5GB) | 14B SFT test eval |
| test_eval_1_7b_sft_s42 | 140534 | **ALIVE** | GPU 0 (6.1GB) | 1.7B SFT test eval |
| retrain_4b_rsft_ced_s42_v2 | 142872 | **ALIVE** | GPU 2 (94.4GB) | 4B RSFT training, step 350/510, loss=0.626, token_acc=0.854 |
| test_eval_14b_sft_s42_no_evi | 143166 | **ALIVE** | GPU 3 (32.5GB) | 14B SFT no-evi test eval |

**retrain_4b_rsft_ced_s42_v2 训练进度**：
- 当前 step: 350 / 510 (68.6%)
- 最新 checkpoint: checkpoint-350 (saved 07:41)
- Loss: 0.6263
- Mean token accuracy: 0.8536
- Learning rate: 7.85e-6
- save_steps=50, 下一个 checkpoint 在 step 400

日志文件未在 `~/runs/faith-evidence-ie/` 找到（可能 nohup 输出到其他位置）。但进程全部活跃，从 GPU 占用和 trainer_state 看运行正常。

---

## 任务 4: 磁盘状态

```
/dev/md0  350G  251G  100G  72%  /root/autodl-tmp
```

剩余 100GB，暂无压力。

---
