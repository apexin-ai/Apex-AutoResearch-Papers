# diagnose dev eval status and codalab verify

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_dev-eval-status-and-codalab-verify_20260522T055058_result.json`
- **Structured JSON:** [`2d88166a40f164ff9901.json`](../../sessions/2d/2d88166a40f164ff9901.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

## 任务 1: dev_eval_4b_rsft_ced_s42_v2 状态

**仍在运行。** PID 161216 存活，已运行 ~2 小时，进度 341/985（~35%）。cuda:0 占用 9.6GB、56% 利用率，正常推理中。输出目录已创建但尚无结果文件（推理完成后写入）。按当前速度（平均 ~20s/doc），预计还需 ~3.5 小时完成。

## 任务 3: CodaLab dry-run 格式验证

**全部 12 个提交文件格式 OK。** 所有文件均包含必需键 `h_idx, t_idx, r, title`（外加 `evidence`）：

| 文件 | triples 数 |
|------|-----------|
| 14b_rsft_s42 | 11,235 |
| 14b_sft_s42 | 14,423 |
| 14b_sft_s42_no_evi | 15,563 |
| 1.7b_rsft_s42 | 7,793 |
| 1.7b_sft_s42 | 8,020 |
| 1.7b_sft_s42_no_evi | 6,144 |
| 4b_rsft_s42_v2 | 9,630 |
| 4b_sft_s42 | 10,609 |
| 8b_rsft_s42 | 8,049 |
| 8b_sft_s42 | 8,678 |
| llama_rsft_s42 | 9,641 |
| llama_sft_s42 | 9,502 |

（注：用户消息中未包含任务 2 的内容。）

---
