# experiment qwen3 1 7b no evidence sft

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_qwen3_1_7b_no_evidence_sft_20260516T072825_result.json`
- **Structured JSON:** [`74d4476ba389b0eefbc1.json`](../../sessions/74/74d4476ba389b0eefbc1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已提交完成。当前状态：

**实验**: `plan_006_qwen3_1_7b_no_evidence_sft`
- **状态**: QUEUED → 等待模型下载完成后自动启动训练
- **GPU**: cuda:2（已确认空闲 0 MiB）
- **模型下载**: Qwen3-1.7B 从 ModelScope CDN 下载中，~1MB/s，预计 ~55min
- **训练配置**: bf16 LoRA (rank=64, alpha=128), `--no_evidence`, `--no-quantize`, seed=42, 3 epochs
- **输出**: `/root/autodl-tmp/sft_output_qwen3_1_7b_no_evidence/`
- **日志**: `~/runs/faith-evidence-ie/plan_006_qwen3_1_7b_no_evidence_sft.log`
- **PID**: 316274（包装脚本，等下载 PID 316228 完成后启动训练）

包装脚本 `/tmp/download_and_train_1_7b.sh` 会自动：
1. 等待下载进程完成
2. 验证模型文件存在
3. 启动 `sft_trainer.py --no_evidence --no-quantize` 训练

下载完成 + 训练预计总计 ~1.5-2h。需要定期检查时告诉我。

---
