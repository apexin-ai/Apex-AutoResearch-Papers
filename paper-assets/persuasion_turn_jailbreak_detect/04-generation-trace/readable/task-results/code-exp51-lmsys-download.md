# code exp51 lmsys download

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp51_lmsys_download_20260522T090002_result.json`
- **Structured JSON:** [`a2d5dc828b84f7aa898e.json`](../../sessions/a2/a2d5dc828b84f7aa898e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇报：

**数据集**: HuggingFaceH4/ultrachat_200k（公开，无 gate），通过 hf-mirror.com 下载
- LMSYS-Chat-1M 因 gated repo + 无 HF token 无法使用
- 服务器无法直连 HuggingFace，通过国内镜像解决

**筛选条件**: ≥3 轮用户消息、英文、无 jailbreak 关键词、长度 ≤20k 字符。从 762 条中筛出 500 候选，随机抽取 200 条。

**统计**:
| 指标 | 值 |
|------|-----|
| 总条数 | 200 |
| 平均轮数 | 3.6 |
| 最短/最长 | 3 / 7 |
| 中位数 | 3 |
| 轮数分布 | 3轮:102, 4轮:80, 5轮:10, 6轮:5, 7轮:3 |

**文件路径**:
- `/root/persuasion_turn_jailbreak_detect/data/lmsys_benign_200.json` — 200 条 eval 用
- `/root/persuasion_turn_jailbreak_detect/data/lmsys_benign_10_adapt.json` — 10 条 adaptation 用

**格式验证**: 字段与现有 `wildchat_benign_226.jsonl` 完全一致（`conversation_id`, `source`, `label`, `turns`, `num_turns`, `metadata`, `attack_type`）。

---
