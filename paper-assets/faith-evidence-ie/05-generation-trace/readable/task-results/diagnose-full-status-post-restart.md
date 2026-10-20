# diagnose full status post restart

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_full-status-post-restart_20260522T020954_result.json`
- **Structured JSON:** [`76047b5e4267e103e3b0.json`](../../sessions/76/76047b5e4267e103e3b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

1.7B SFT 在 497/500，输出目录仍为空（结果在推理全部完成后才写入）。报告当前状态：

---

## GPU 状态
| GPU | 显存占用 | 利用率 | PID | 实验 |
|-----|----------|--------|-----|------|
| 0 | 6,071 / 97,887 MiB | 51% | 140534 | test_eval_1_7b_sft_s42 |
| 1 | 6,071 / 97,887 MiB | 49% | 147596 | test_eval_1_7b_sft_s42_no_evi |
| 2 | 19,599 / 97,887 MiB | 88% | 152873 | test_eval_8b_sft_s42_no_evi |
| 3 | 32,503 / 97,887 MiB | 91% | 143166 | test_eval_14b_sft_s42_no_evi |

## 实验结果
| 状态 | 实验 | 进度 | 速度 | ETA |
|------|------|------|------|-----|
| [RUNNING] | test_eval_1_7b_sft_s42 | **497/500 (99.4%)** | ~27s/it | **~1-2 min** |
| [RUNNING] | test_eval_1_7b_sft_s42_no_evi | 260/500 (52%) | ~27s/it | ~1h48m |
| [RUNNING] | test_eval_8b_sft_s42_no_evi | 56/500 (11.2%) | ~32s/it | ~3h57m |
| [RUNNING] | test_eval_14b_sft_s42_no_evi | 274/500 (54.8%) | ~40s/it | ~2h31m |

服务重启后 4 个进程全部存活，均在正常推理。

## 8B no-evi 验证
- 参数正确: ✅ (`python -m freige.eval.test_inference --model_path .../Qwen3-8B --sft_adapter .../sft_output_qwen3_8b_bf16 ... --split test_revised --no_evidence`)
- adapter: ✅ (698MB, `/root/autodl-tmp/sft_output_qwen3_8b_bf16/adapter_model.safetensors`)
- --no_evidence: ✅
- --max_new_tokens 2048: ✅
- CUDA_VISIBLE_DEVICES=2: ✅

## Registry 更新
- 无需更新 — 4 个实验均仍在 RUNNING，无已完成实验。

## 备注
- test_eval_1_7b_sft_s42 即将完成（差 3 个 doc），完成后需要立即收集 test_summary.json 并更新 registry
- 日志路径：该实验日志在 `/tmp/test_eval_1_7b_sft_s42.log`（非标准路径），registry 中未记录 log_path

---
