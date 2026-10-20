# check cross model output

**svs formal verification** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_cross_model_output_20260514T113949_result.json`
- **Structured JSON:** [`0dfad14b73e5ceff74c4.json`](../../sessions/0d/0dfad14b73e5ceff74c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

**脚本状态：已完成** (19:37:10 结束，pipeline_status=success，无错误)

**配置：**
- Chain 生成：Qwen2.5-14B-Instruct (本地 vLLM)
- 形式化/分解：DeepSeek V3.2 API
- 数据集：ProofWriter depth-5，5 题，每题 4 条 chain

**总体指标：**
- 形式化率：94.5% (257/272)
- SVS 正确：2/5，SC 正确：2/5

**逐题结果：**

| 问题 | Gold | SVS | SC | 形式化率 | IC scores | Z3 SAT | 耗时 |
|------|------|-----|----|----------|-----------|--------|------|
| pw_1309 | False | Unknown ✗ | Unknown ✗ | 91% | 0.2, 0.86, 1.0, 0.54 | 2/4 | 637s |
| pw_228 | True | True ✓ | True ✓ | 91% | 0.91, 0.91, 0.92, 0.91 | 4/4 | 461s |
| pw_51 | Unknown | False ✗ | Unknown ✓ | 100% | 0.87, 0.97, 0.89, 0.90 | 0/4 | 564s |
| pw_1518 | False | Unknown ✗ | Unknown ✗ | 83% | 0.63, 0.77, 0.67, 0.62 | 0/4 | 358s |
| pw_563 | True | True ✓ | Unknown ✗ | 100% | 1.0, 1.0, 1.0, 1.0 | 4/4 | 349s |

**关键观察：**
- SVS 在 pw_563 上胜过 SC（SVS 正确答 True，SC 错答 Unknown），验证了 cross-chain 一致性检查的价值
- 两个 gold=False 的题目 SVS 和 SC 都答错（均为 Unknown），说明否定推理仍是瓶颈
- pw_51 中 SVS 被高 group_score 的错误 chain 误导（False chain score=1.22 > Unknown chains score=1.01），SC 的多数投票反而更稳健
- 产出文件：`/root/autodl-tmp/svs_formal_verification/outputs_dryrun/cross_model_dry_run.json`

---
