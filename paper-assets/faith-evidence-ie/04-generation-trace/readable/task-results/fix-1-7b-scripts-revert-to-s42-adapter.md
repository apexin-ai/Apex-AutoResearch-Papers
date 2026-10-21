# fix 1 7b scripts revert to s42 adapter

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_1_7b_scripts_revert_to_s42_adapter_20260519T042711_result.json`
- **Structured JSON:** [`c9339485a5a44e712f09.json`](../../sessions/c9/c9339485a5a44e712f09.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报如下：

**1. 脚本恢复 ✓**
- `train_1_7b_s43.sh`: `--sft_adapter /root/autodl-tmp/sft_output_qwen3_1_7b_bf16`
- `train_1_7b_s44.sh`: `--sft_adapter /root/autodl-tmp/sft_output_qwen3_1_7b_bf16`
- 已从错误的 `_seed43`/`_seed44` 后缀恢复为 s42 共享 adapter

**2. s42 SFT adapter 存在 ✓**
- `/root/autodl-tmp/sft_output_qwen3_1_7b_bf16/adapter_model.safetensors` (279MB)

**3. 离线环境变量 ✓**
- 两个脚本均已有 `HF_HUB_OFFLINE=1`、`TRANSFORMERS_OFFLINE=1`、`HF_HOME`

**4. GPU 状态 — 无法提交 s43**

| GPU | 占用 | 任务 |
|-----|------|------|
| cuda:0 | 1.5GB | d112_ced_score (22500/24216, ~5 min 剩余) |
| cuda:1 | 16.1GB | plan017_14b_sft (6/144, ~2.5h 剩余) |
| cuda:2 | 17.3GB | plan017_14b_sft |
| cuda:3 | 18.9GB | plan019_8b_rsft_s44_eval (197/247, ~40 min 剩余) |

**8B eval ETA: ~13:08 UTC（约 40 分钟后）。** cuda:3 释放后可提交 s43。cuda:0 也将在 ~5 min 后释放，但 1.7B RSFT 通常需要更多显存，需确认是否够用。

---
