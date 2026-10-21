# ssh 5090c cuda3 pending exp

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_5090c_cuda3_pending_exp_20260521T181022_result.json`
- **Structured JSON:** [`7108cb4d86251ae66e34.json`](../../sessions/71/7108cb4d86251ae66e34.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已启动，模型正在加载到 cuda:3（15397 MiB）。

**状态总结：**
- **e2_fewnerd_s42** — 刚启动在 cuda:3，tmux session `e2_fewnerd_s42`，vLLM 正在加载 Qwen2.5-7B-Instruct
- **e2_fewnerd_s456** — 已有另一个 session `exp_e2_pretrained_fewnerd_s456` 在 cuda:2 上运行（30233 MiB）

E2 pretrained 实验完成情况：
| 数据集 | s42 | s123 | s456 |
|--------|-----|------|------|
| CoNLL | ✅ 3453 | ✅ 3453 | ✅ 3453 |
| SciERC | ✅ 551 | ✅ 551 | ✅ 551 |
| FewNERD | ⏳ 刚启动 | ✅ 37648 | ⏳ 另一session运行中 |

FewNERD s42 预计约 37k samples，需数小时完成。日志路径：`output/e2_pretrained_fewnerd_s42.log`

---
