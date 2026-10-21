# ops cwm seqlen audit

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cwm-seqlen-audit_20260524T020958_result.json`
- **Structured JSON:** [`a9a91eb7e69b7977bcfb.json`](../../sessions/a9/a9a91eb7e69b7977bcfb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。汇总如下：

---

```
seq_length 审计结果：

┌─────────────────────────────────────────────────────────────────────────┐
│ Table 2 使用的已完成 eval                                                │
├──────────────┬────────────┬──────────────────┬─────────────────────────┤
│ Seed         │ Checkpoint │ max_seq_length   │ 来源                    │
├──────────────┼────────────┼──────────────────┼─────────────────────────┤
│ s123 ckpt6633│ ckpt-6633  │ 8192             │ eval_repo_cwm.json      │
│              │            │                  │ + eval_qwen_cwm_s123.sh │
├──────────────┼────────────┼──────────────────┼─────────────────────────┤
│ s456 ckpt6633│ ckpt-6633  │ 8192             │ eval_repo_cwm.json      │
│              │            │                  │ + eval_qwen_cwm_s456.sh │
├──────────────┼────────────┼──────────────────┼─────────────────────────┤
│ s42 (Table 2)│ 不明       │ 不明             │ 反推 accuracy≈65.18%，  │
│              │            │                  │ 不匹配任何已知 eval     │
└──────────────┴────────────┴──────────────────┴─────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ 当前正在运行的 s42 eval（GPU 3）                                        │
├──────────────┬────────────┬──────────────────┬─────────────────────────┤
│ s42 ckpt6100 │ ckpt-6100  │ **4096**         │ /proc/272025/cmdline    │
│              │            │                  │ running_acc=69.5%       │
└──────────────┴────────────┴──────────────────┴─────────────────────────┘

eval_repo_cwm.py 默认值: 8192 (line 362)
```

**结论：不一致，存在三重混杂**

1. **seq_length 不一致**: s42 ckpt6100 eval 用 4096，s123/s456 ckpt6633 eval 用 8192
2. **checkpoint 不一致**: s42 用 ckpt-6100（来自 `checkpoints_repo_cwm_8b_conda/`），s123/s456 用 ckpt-6633（来自各自的训练目录）。s42 训练目录没有 ckpt-6633，s123/s456 训练目录没有 ckpt-6100
3. **Table 2 当前值存疑**: 66.48 ± 1.15 反推 s42 ≈ 65.18%，但这既不等于当前 ckpt6100 eval 的 ~69.5%，也不等于 ckpt400+seq4096 eval 的 64.36%，来源无法追溯

**不能混合计算均值**。如果要用当前 s42 ckpt6100 结果（seq=4096, ~69.5%）与 s123/s456（seq=8192），需要用一致的 seq_length 重新评估。

---
