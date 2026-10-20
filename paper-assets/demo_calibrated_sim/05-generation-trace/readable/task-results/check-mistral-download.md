# check mistral download

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_mistral-download_20260512T225752_result.json`
- **Structured JSON:** [`aeeea05c51c861487359.json`](../../sessions/ae/aeeea05c51c861487359.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 检查结果

**Mistral-7B-Instruct-v0.3 已下载完成。**

- **路径**: `/root/autodl-tmp/models/Mistral-7B-Instruct-v0.3/`
- **总大小**: 14GB（符合 7B 模型预期）
- **文件完整性**: ✓
  - `config.json` ✓
  - `tokenizer.json` + `tokenizer.model` ✓
  - 3 个 safetensors 分片（4.9GB + 5.0GB + 4.5GB）✓
  - `generation_config.json`, `special_tokens_map.json`, `tokenizer_config.json` ✓
- **下载时间**: 2026-05-13 02:39 ~ 02:57

另外在 `/root/autodl-tmp/.hf_cache/hub/models--mistralai--Mistral-7B-Instruct-v0.3/` 有 HF cache 的 refs 目录（仅元数据，无实际 blob），实际模型文件在 `models/` 目录下。

`/root/democalib/` 下暂无 Mistral 相关的评估脚本。

---
