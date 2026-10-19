# ops p0 log extraction

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_p0_log_extraction_20260513T153711_result.json`
- **Structured JSON:** [`7d392a0c8ef087250c7e.json`](../../sessions/7d/7d392a0c8ef087250c7e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集。以下是完整结果。

---

## m2_embed_verify (Qwen2.5-Coder-3B)
实际日志路径: `/root/runs/faith-evidence-ie/m2_embed_verify.log`
完成标记: "All 3 strategies completed at Wed May 13 21:22:26 CST 2026"

### random
| eval@N | val_loss | R@1 | R@5 | R@10 |
|--------|----------|-----|-----|------|
| 500 | 0.4834 | 0.5357 | 0.9808 | 1.0 |
| 1000 | 0.5451 | 0.5348 | 0.9765 | 1.0 |
| 1500 | 0.5827 | 0.5331 | 0.9747 | 1.0 |
| Final | 0.5978 | 0.5122 | 0.9826 | 1.0 |

**best_step: 500** (val_loss=0.4834)

### embedding_distance
| eval@N | val_loss | R@1 | R@5 | R@10 |
|--------|----------|-----|-----|------|
| 500 | 0.4603 | 0.5557 | 0.9808 | 1.0 |
| 1000 | 0.5237 | 0.5314 | 0.9756 | 1.0 |
| 1500 | 0.5817 | 0.5270 | 0.9739 | 1.0 |
| Final | 0.5935 | 0.5209 | 0.9826 | 1.0 |

**best_step: 500** (val_loss=0.4603)

### dataflow_aware
| eval@N | val_loss | R@1 | R@5 | R@10 |
|--------|----------|-----|-----|------|
| 500 | 0.5602 | 0.5436 | 0.9817 | 1.0 |
| 1000 | 0.5829 | 0.5584 | 0.9808 | 1.0 |
| 1500 | 0.6045 | 0.5375 | 0.9782 | 1.0 |
| Final | 0.6201 | 0.5287 | 0.9843 | 1.0 |

**best_step: 500** (val_loss=0.5602)

---

## plan_013_starcoder (StarCoder2-3B)
实际日志路径: `/root/runs/faith-evidence-ie/plan_013_starcoder.log`
完成标记: "All 3 strategies completed at Wed May 13 20:21:22 CST 2026"

### random
**训练日志中无 eval 输出。** 训练跑到 step 500 后直接 "Strategy random completed"，没有 `[eval@N]` 记录。

数据来源于独立评估脚本 `/tmp/eval_random_s42.log`：
| eval@N | val_loss | R@1 | R@5 | R@10 |
|--------|----------|-----|-----|------|
| best ckpt | 0.5113 | 0.4922 | 0.9800 | 1.0 |

（无多步 eval，仅对 `random_s42/best` checkpoint 做了一次完整评估，1148 val samples）

### embedding_distance
| eval@N | val_loss | R@1 | R@5 | R@10 |
|--------|----------|-----|-----|------|
| 500 | 0.5140 | 0.4800 | 0.9826 | 1.0 |
| 1000 | 0.4816 | 0.5078 | 0.9843 | 1.0 |
| 1500 | 0.4978 | 0.4930 | 0.9861 | 1.0 |
| Final | 0.5060 | 0.5174 | 0.9834 | 1.0 |

**best_step: 1000** (val_loss=0.4816)

### dataflow_aware
| eval@N | val_loss | R@1 | R@5 | R@10 |
|--------|----------|-----|-----|------|
| 500 | 0.5257 | 0.4756 | 0.9756 | 1.0 |
| 1000 | 0.5255 | 0.4869 | 0.9695 | 1.0 |
| 1500 | 0.5382 | 0.4782 | 0.9774 | 1.0 |
| Final | 0.5509 | 0.5078 | 0.9765 | 1.0 |

**best_step: 1000** (val_loss=0.5255)

---

## StarCoder random R@1=0.4922 溯源

| 项目 | 值 |
|------|---|
| 来源文件 | `/tmp/eval_random_s42.log` |
| 评估 checkpoint | `/root/autodl-tmp/structfuse/m2_starcoder_output/random_s42/best/model.pt` |
| 验证数据 | `/root/autodl-tmp/structfuse/m2_embed_verify_data/val.jsonl` (1148 samples) |
| 交叉验证 | `pilot_results_summary.md` 报告同一数字 (R@1=0.4922, val_loss=0.5113) |
| 可验证性 | **verifiable** — 独立 eval 脚本对 best checkpoint 执行完整评估，两个文件数字一致 |
| 注意 | 训练日志本身无 eval 输出（random 策略训练时未触发 eval callback），数字来自后补评估 |

---
