# fix m2 full starcoder resume

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_m2_full_starcoder_resume_20260514T175326_result.json`
- **Structured JSON:** [`864714d6126c4cd28628.json`](../../sessions/86/864714d6126c4cd28628.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部通过。

## 结果汇总

### random_s42 checkpoint 验证
| 目录 | model.pt | 状态 |
|------|----------|------|
| `best_by_val_loss/` | 5.7GB | OK |
| `best_by_recall_at_1/` | 5.7GB | OK |

### Resume 脚本
**路径**: `/root/structfuse/run_m2_full_starcoder_resume.sh`

**8 runs 配置**:

| # | Run | Strategy | Seed | Epochs |
|---|-----|----------|------|--------|
| 1 | random_s43 | random | 43 | 2 |
| 2 | random_s44 | random | 44 | 2 |
| 3 | embedding_distance_s42 | embedding_distance | 42 | 3 |
| 4 | embedding_distance_s43 | embedding_distance | 43 | 2 |
| 5 | embedding_distance_s44 | embedding_distance | 44 | 2 |
| 6 | dataflow_aware_s42 | dataflow_aware | 42 | 3 |
| 7 | dataflow_aware_s43 | dataflow_aware | 43 | 2 |
| 8 | dataflow_aware_s44 | dataflow_aware | 44 | 2 |

### 验证结果
- 语法检查: `SYNTAX_OK`
- `train.py --help`: 正常加载，参数匹配
- 所有 seed 42/43/44 数据文件已就绪

### 时间估算
random_s42 是 3 epochs × 11308 samples / batch 8 ≈ 4242 steps，耗时约 ~23.6h（20s/step）。

| Epochs | 预估 steps/run | 预估时间/run |
|--------|----------------|-------------|
| 3 epochs (s42) | ~4242 | ~23.6h |
| 2 epochs (s43) | ~2808 | ~15.6h |
| 2 epochs (s44) | ~2816 | ~15.6h |

- 2 个 3-epoch runs: ~47.2h
- 6 个 2-epoch runs: ~93.6h
- **总计 ≈ 141h (~5.9 天)**

---
