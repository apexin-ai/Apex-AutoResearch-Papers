# experiment deberta finetune owa restart

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_deberta-finetune-owa-restart_20260522T161722_result.json`
- **Structured JSON:** [`7949b52c635345febb05.json`](../../sessions/79/7949b52c635345febb05.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 0 占用 14.3GB，利用率 97%。训练正常运行。

## 汇报

| 项目 | 值 |
|------|-----|
| **训练集** | 69,810 条（HF `tasksource/proofwriter` train split → `depth-5` config 过滤） |
| **数据来源** | HF depth-5 config，全部为 OWA 数据 |
| **标签分布** | True=19,932, False=19,932, Unknown=29,946 |
| **验证集** | 600 条（`proofwriter_full.json`） |
| **Total steps** | 5,455（1,091 steps/epoch × 5 epochs） |
| **速度** | ~1.2s/step |
| **预计训练时间** | ~110 min 全量；early stopping 可能 ~66 min |
| **PID** | 643576 |
| **初始 loss** | 日志中 step 50 才打第一个 loss（logging_steps=50），暂未可见 |
| **数据泄露检查** | 通过 — `remove_overlap()` 未发现 train/val 重叠样本 |
| **GPU** | cuda:0, 14.3GB/98GB, 97% utilization |

**注意**：脚本的 OWA 过滤逻辑有 bug — 检查 `config` 列是否含 "OWA"，但该列值为 `depth-0`/`depth-5` 等不含 "OWA"，导致 fallback 到全量。好在全量数据本身就都是 OWA，最终靠 `--depth-filter depth-5` 正确过滤到了 69,810 条。

---
