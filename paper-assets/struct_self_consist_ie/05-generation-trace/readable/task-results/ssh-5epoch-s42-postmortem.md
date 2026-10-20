# ssh 5epoch s42 postmortem

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_5epoch_s42_postmortem_20260521T180111_result.json`
- **Structured JSON:** [`9fffae70655f8d18cdbc.json`](../../sessions/9f/9fffae70655f8d18cdbc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都仍在运行，尚未完成。

## 状态汇总

### exp_fewnerd_5epoch_s42
- **状态**: 运行中，1.2% (3592/301184 prompts)
- **预计剩余**: ~1h50m（当前速度 ~51 it/s, ~3850 toks/s input）
- **输出目录**: 已创建，但 samples.jsonl 尚未生成（推理未完成时不会写入）
- **启动时间**: 05-22 01:57

### exp_fewnerd_5epoch_s123
- **状态**: 运行中，1.0% (3048/301184 prompts)
- **预计剩余**: ~2h（当前速度 ~50 it/s, ~3300 toks/s input）
- **输出目录**: 已创建，但 samples.jsonl 尚未生成
- **启动时间**: 05-22 01:57

### GPU 状态
| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| 0 | 87% | 30.2/32.6 GB |
| 1 | 90% | 30.2/32.6 GB |
| 2 | 79% | 30.2/32.6 GB |
| 3 | 57% | 29.9/32.6 GB |

4 卡都在工作（seed=42 用 2 卡，seed=123 用 2 卡）。301184 = 37648 × 8（8 次 self-consistency 采样）。按当前速度，两个实验预计约 2 小时后完成。不更新 registry，不删除 cron。

---
