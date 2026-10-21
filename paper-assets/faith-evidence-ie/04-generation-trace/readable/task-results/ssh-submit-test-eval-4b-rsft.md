# ssh submit test eval 4b rsft

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_submit-test-eval-4b-rsft_20260521T100059_result.json`
- **Structured JSON:** [`6a09e860d6a0d099be8a.json`](../../sessions/6a/6a09e860d6a0d099be8a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Fallback：4B RSFT s42 adapter 不存在。**

已确认的环境状态：
- `test_inference.py` 存在 ✓
- `test_revised.json` 在 `/root/autodl-tmp/data/re-docred-repo/data/test_revised.json` ✓（注意：不在 `docred/` 下）
- `SPLIT_FILENAMES` 支持 `test_revised` ✓
- cuda:1 空闲（0 MiB）✓
- SFT s42 adapter：`/root/autodl-tmp/sft_output` ✓
- Base model：`/root/autodl-tmp/models/Qwen3-4B` ✓

**缺失**：4B RSFT s42 adapter。旧路径 `rsft_output_r2b` 已被删除。服务器上现有的 RSFT adapter：

| 路径 | 说明 |
|------|------|
| `rsft_output_ced_s43` | CED-filtered, SFT seed 43 |
| `rsft_output_4b_sft_s44` | SFT seed 44 |
| `rsft_output_nli_large` | NLI large filtered |
| `rsft_output_random_k1` | random baseline |
| `rsft_output_14b` | 14B 模型 |

**建议**：
1. 如果训练数据 `rsft_filtered/rsft_train.jsonl` 仍可用，需要重新训练 4B RSFT s42
2. 或者指定一个现有 adapter（如 `rsft_output_ced_s43`）来跑 Re-DocRED test eval

---
