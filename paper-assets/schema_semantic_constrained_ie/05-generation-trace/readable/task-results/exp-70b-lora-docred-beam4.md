# exp 70b lora docred beam4

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_70b-lora-docred-beam4_20260522T170455_result.json`
- **Structured JSON:** [`34cbca30546927b0fe13.json`](../../sessions/34/34cbca30546927b0fe13.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已启动并配置完成：

- **实验**: `eval_70b_lora_docred_200_beam4_s1`
- **服务器**: westd-21461, GPU1 (CUDA_VISIBLE_DEVICES=1)
- **PID**: 70638
- **配置**: 70B AWQ+LoRA, DocRED 200-doc, beam k=4, full_s1
- **预计时长**: ~1.8h（32s/sample）
- **修复**: PEFT `awq.py` 和 `tuners_utils.py` 已 patch 以支持 AwqMarlinLinear + LoRA（原始文件备份为 `.bak`）
- **Registry**: RUNNING，parent = eval_70b_lora_docred_200_s1_constrained
- **Cron**: 每 12 分钟监控进度

---
