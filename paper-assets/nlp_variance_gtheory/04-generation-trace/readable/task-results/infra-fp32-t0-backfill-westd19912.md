# infra fp32 t0 backfill westd19912

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_fp32_t0_backfill_westd19912_20260521T205613_result.json`
- **Structured JSON:** [`5fe9275ed3368451fb0c.json`](../../sessions/5f/5fe9275ed3368451fb0c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

补跑完成，验证通过：

| 指标 | 数值 |
|------|------|
| 补跑条件数 | 100 (condition_id 1297-1396) |
| 补跑行数 | 20,000 |
| 合并后总行数 | **259,200** (= 1,296 conditions × 200 items) |
| 唯一 condition_id | **1,296** (无缺失，无重复) |
| 每条件 items | 全部 200，无异常 |
| 补跑精度 | 全部 float32 × temperature=0.0 |
| 补跑准确率 | 71.38%（与其他条件一致） |
| 合并后总准确率 | 68.39% |
| 运行时间 | ~10 分钟 |
| GPU | westd-19912 GPU 0 (RTX PRO 6000 Blackwell) |
| PID | 75785（已完成） |

数据位置：
- westd-32570: `results/exp001_llama/llama_fp32_t0_backfill.jsonl`（已传输，与原 4 个 shard 并列）
- westd-19912: `results/exp001_llama/llama_fp32_t0_backfill.jsonl`（原始产出）

已清理临时 SSH 密钥。

---
