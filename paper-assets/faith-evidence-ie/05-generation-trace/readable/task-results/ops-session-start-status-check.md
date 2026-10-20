# ops session start status check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_session_start_status_check_20260519T171939_result.json`
- **Structured JSON:** [`04d8d1ad1de2715edfe4.json`](../../sessions/04/04d8d1ad1de2715edfe4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态
| GPU | 利用率 | 显存 | 占用进程 |
|-----|--------|------|---------|
| cuda:0 | 0% | 0 / 32607 MiB | **空闲** |
| cuda:1 | 46% | 11347 / 32607 MiB | PID 706339 (d112_rsft_no_evidence_eval_r3) |
| cuda:2 | 0% | 0 / 32607 MiB | **空闲** |
| cuda:3 | 55% | 6635 / 32607 MiB | PID 702845 (plan019_1_7b_rsft_no_evidence_eval_2048) |

## 实验进程状态
- **d112_rsft_no_evidence_eval_r3** (PID 706326): ALIVE, 运行 1h33m, 进度 149/247 batches (60%), ~40s/it → **预计还需 ~65min**
- **plan019_1_7b_rsft_no_evidence_eval_2048** (PID 702837): ALIVE, 运行 2h30m, 进度 116/247 batches (47%), ~78s/it → **预计还需 ~2h48m**
- **d112_rsft_s44_ced_score** (PID 604576): **DEAD** (已完成)

## 8B RSFT No-Evidence Eval R2 Metrics (已完成 ✓)
| 指标 | 值 |
|------|-----|
| F1 | 0.5530 |
| Ign-F1 | 0.5336 |
| Evi-F1(DREEAM/joint) | 0.0411 |
| Evi-F1(TP-only) | 0.0652 |
| EDCR | 0.6207 |
| Precision | 0.5324 |
| Recall | 0.5753 |
| Evi Precision | 0.8219 |
| Evi Recall | 0.0340 |
| Format OK | 985/985 (100%) |
| Truncated | 310/985 |
| Predictions | 20605 |
| `no_evidence: true` | ✓ 参数正确 |
| 推理耗时 | 11475s (~3h11m) |

注：field_compliance_rate 仅 3.0%（30/985 doc 有有效 evidence 字段），说明 no-evidence 模型确实几乎不输出 evidence，符合预期。

## 旧实验状态
- **d112_rsft_s44_generate**: **完成** — 4 shards, 共 24216 条 (6048+6048+6048+6072)
- **d112_rsft_s44_ced_score**: **完成** — 24216 条评分, 3014 条入选训练集 (12.4% selection rate), mean F1=0.676, mean CED=0.676
- **seed_llama_rsft_k1_s43**: **完成** — checkpoint-1100, checkpoint-1107 + adapter 文件已生成

## 1.7B No-Evidence 2048 进度
116/247 batches (47%), ~78s/it, 已运行 2h30m, **预计还需 ~2h48m** (ETA ~约 02:20 UTC)

## 可用 GPU 汇总
**cuda:0 和 cuda:2 完全空闲**，可立即提交新任务。

---
