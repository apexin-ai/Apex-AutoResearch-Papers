# diagnose all running experiments r2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_all-running-experiments-r2_20260521T232506_result.json`
- **Structured JSON:** [`a0b506955d5e39449b9a.json`](../../sessions/a0/a0b506955d5e39449b9a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 服务器诊断 rtx5090-4x — 2026-05-22

### GPU 状态
| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| 0 | 53% | 6,071 / 97,887 MiB |
| 1 | 91% | 32,503 / 97,887 MiB |
| 2 | 99% | 94,453 / 97,887 MiB |
| 3 | 91% | 32,503 / 97,887 MiB |

### 实验状态
| exp_id | GPU | PID | 运行时间 | 实际状态 | 进度 | ETA |
|--------|-----|-----|----------|----------|------|-----|
| retrain_4b_rsft_ced_s42_v2 | cuda:2 | 142867 | 11min | **RUNNING** | 143/510 (28%) | ~28min |
| test_eval_14b_sft_s42 | cuda:1 | 125321 | 4h53m | **RUNNING** | 427/500 (85%) | ~63min |
| test_eval_1_7b_sft_s42 | cuda:0 | 140534 | 35min | **RUNNING** | 未知（无日志） | 未知 |
| test_eval_14b_sft_s42_no_evi | cuda:3 | 143161 | 11min | **RUNNING** | 16/500 (3%) | ~3.8h |

### 详情

**retrain_4b_rsft_ced_s42_v2** — 训练正常进行中。已保存 checkpoint-50 和 checkpoint-100（adapter_model.safetensors 528MB）。最新日志 step 100 指标：loss=0.629, token_accuracy=0.854, lr=1.98e-5。总 510 步（3 epochs），当前 ~4.5s/step。

**test_eval_14b_sft_s42** — 推理 427/500，约 45-52s/doc。输出目录仅有 log.txt（34KB），尚无 metrics.json（应在全部完成后写入）。

**test_eval_1_7b_sft_s42** — 进程存活，GPU 0 显存 6GB 符合 1.7B 模型。但输出目录为空且无日志文件重定向（命令未用 nohup 包装），无法判断进度。

**test_eval_14b_sft_s42_no_evi** — 刚启动 11 分钟，模型加载完毕，推理 16/500，~28-35s/doc。已确认传了 `--no_evidence` 参数。

### 异常
- **1.7B eval 无可观测性**：PID 140534 未重定向日志，输出目录空，无法判断是否正常推理中。建议等待或检查 stdout 输出。
- 无已完成实验，4 个全部仍在运行中。

---
