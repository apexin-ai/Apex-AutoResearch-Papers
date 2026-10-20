# code batch continuation fix

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_batch_continuation_fix_20260512T204158_result.json`
- **Structured JSON:** [`22cd69b714f1506baf85.json`](../../sessions/22/22cd69b714f1506baf85.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 汇报

### 1. 代码 diff
替换了 `run_pipeline.py` L181-200 的 continuation 分支：
- **旧代码**：逐条 for 循环，每条 doc 单独 `model.generate()`，batch_size 实际为 1
- **新代码**：batch generation with left-padding，用 tokenizer batch encode + 一次 `model.generate()`，与 rewrite 分支结构对齐

本地和远程文件已同步修改，远程已备份为 `.bak3`。

### 2. Continuation batch dry-run
- **通过**，100 docs × 2 depths，总耗时 **1m32s**（含模型加载、seed data、feature extraction、analysis）
- 生成阶段：~29s/depth（7 batches × ~4.25s/batch），batch_size=16 无 OOM

### 3. 时间推算：5000 docs × 5 depths
| 阶段 | 估算 |
|------|------|
| 生成（5 depths） | 5 × (313 batches × 4.25s) ≈ **111 min** |
| Feature extraction（6 depths） | 6 × ~350s ≈ **35 min** |
| Analysis | ~5 min |
| **合计** | **~2h51m** |

**在 6h 预算内，余量充足。**

### 4. Rewrite 回归
- **通过**，10 docs × 1 depth，32s 完成，pipeline 未报错

### 5. 生成文本质量对比（抽样 doc_id=0）
- **depth_0（原文）**: "The woman who died after falling from a bridge over the A21 has been identified as a Sevenoaks mum. Marta Kendle, 37, fell from the Gracious Lane bridge..."
- **depth_1（batch continuation）**: "and a memorial fund was set up to help the family. Mrs Kendle's mother Lydia said: 'My daughter Marta was a lovely person who would smile when she saw anyone...'"

语义连贯，从原文前半段自然续写，质量正常。batch 模式与逐条模式的唯一差异是 left-padding 对齐 + 统一 max_new_tokens=256（不再按原文长度动态调整），生成内容风格一致。

### 6. 遇到的问题
- SSH 30s 超时：改用 nohup 后台执行 + 轮询解决
- `python3` 在 conda 环境外不可用：需先 `conda activate base`

---
