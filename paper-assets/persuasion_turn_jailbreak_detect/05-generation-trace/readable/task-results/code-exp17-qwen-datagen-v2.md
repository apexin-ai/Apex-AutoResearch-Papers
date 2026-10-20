# code exp17 qwen datagen v2

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp17-qwen-datagen-v2_20260519T151849_result.json`
- **Structured JSON:** [`d4b2c23179a30b56a2a0.json`](../../sessions/d4/d4b2c23179a30b56a2a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 张 GPU 全部在使用：
- GPU 0: Llama jailbreak gen (exp16)
- GPU 1: Llama benign gen (exp16)  
- GPU 2: **Qwen3-8B jailbreak gen (exp17)** — 19GB
- GPU 3: **Qwen3-8B benign gen (exp17)** — 19GB

汇报：

**脚本**: `scripts/generate_crescendo_expanded.py` (598行)
- 基于 Llama 版脚本改造，适配 Qwen3-8B（`enable_thinking=False` 禁用思考模式）
- 30 个新 harmful goals + 25 个新 benign scenarios，全部不与原始数据重复
- 支持 `--mode jailbreak/benign`、`--num_conversations`、断点续传
- 输出格式与现有数据一致（`conversation_id`, `label`, `source`, `strategy_sequence`, `metadata`）
- `conversation_id` 格式: `crescendo_exp_XXXX`

**Dry-run**: 2 条 jailbreak 对话验证通过，每条约 105 秒

**已提交 jobs**:
| Job | exp_id | GPU | 输出文件 |
|-----|--------|-----|---------|
| Jailbreak 250 | `exp17_qwen_jailbreak_gen` | cuda:2 | `data/expanded_conversations/crescendo_jailbreak_expanded.jsonl` |
| Benign 250 | `exp17_qwen_benign_gen` | cuda:3 | `data/expanded_conversations/crescendo_benign_expanded.jsonl` |

**预计完成时间**: 约 7-8 小时（每条对话 ~105 秒 × 250 条）

---
