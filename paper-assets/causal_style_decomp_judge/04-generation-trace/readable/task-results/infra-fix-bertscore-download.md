# infra fix bertscore download

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_fix_bertscore_download_20260520T121845_result.json`
- **Structured JSON:** [`bb1c36ca09f3233d853d.json`](../../sessions/bb/bb1c36ca09f3233d853d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

BERTScore 完全正常工作！

**结果汇总**:
- 旧下载进程已 kill
- 通过 ModelScope CDN 下载 `microsoft/deberta-xlarge-mnli` 到 HF cache（~5.5 分钟 vs HuggingFace 代理 20+ 分钟）
- 修复了 tokenizer_config.json 缺少 `model_max_length` 导致的 OverflowError
- BERTScore 验证通过：P=0.9230 R=0.9496 F1=0.9361
- 需要设置 `TRANSFORMERS_OFFLINE=1` 和 `HF_HOME=/root/autodl-tmp/.hf_cache` 才能正常使用（避免连接 HF 超时）

---
