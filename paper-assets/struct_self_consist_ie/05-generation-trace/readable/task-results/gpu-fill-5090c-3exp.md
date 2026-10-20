# gpu fill 5090c 3exp

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_fill_5090c_3exp_20260521T101551_result.json`
- **Structured JSON:** [`236b27270c51cce180b5.json`](../../sessions/23/236b27270c51cce180b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

| GPU | 实验 | 状态 |
|-----|------|------|
| cuda:0 | FewNERD N16 s456 v2（已有） | 运行中，未动 |
| cuda:1 | `exp_conll_mf4_v2_s42` — CoNLL MF4 v2 seed=42, qwen3-8b-conll2003-merged | RUNNING, 已在处理 (6% prompts) |
| cuda:2 | **跳过** — 14B Instruct 模型不存在 | — |
| cuda:3 | `exp_e2_pretrained_fewnerd_s123` — FewNERD E2 pretrained seed=123, Qwen2.5-7B-Instruct | RUNNING, 渲染 prompts 中 (23%) |

**实验 2（14B CoNLL v2）跳过原因**：`Qwen2.5-14B-Instruct` 模型未下载完成（仅有 `.locks` 目录，无实际权重文件）。服务器上有 14B fine-tuned 版本（`qwen25-14b-fewnerd-merged-final`）但不是 Instruct 原始模型。如需此实验，需先从 ModelScope 下载 14B Instruct（约 28GB，耗时较长）。

日志路径：
- `/tmp/exp_conll_mf4_v2_s42.log`
- `/tmp/exp_e2_pretrained_fewnerd_s123.log`

---
