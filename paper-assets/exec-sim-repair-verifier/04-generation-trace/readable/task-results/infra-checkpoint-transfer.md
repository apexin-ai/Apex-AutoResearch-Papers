# infra checkpoint transfer

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_checkpoint-transfer_20260512T083441_result.json`
- **Structured JSON:** [`2994ef5ab46a78ef01f2.json`](../../sessions/29/2994ef5ab46a78ef01f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 传输报告

**方案 A（直接 SCP）成功。**

### 验证结果

```
LoRA r=16, alpha=32, target={'k_proj', 'q_proj', 'o_proj', 'v_proj'}
CHECKPOINT_OK
```

### 文件校验（11/11 匹配）

| 文件 | 大小 | 状态 |
|------|------|------|
| adapter_model.safetensors | 47,224,624 | ✓ |
| tokenizer.json | 11,422,654 | ✓ |
| vocab.json | 2,776,833 | ✓ |
| merges.txt | 1,671,853 | ✓ |
| tokenizer_config.json | 5,431 | ✓ |
| training_args.bin | 5,841 | ✓ |
| README.md | 5,180 | ✓ |
| chat_template.jinja | 4,168 | ✓ |
| adapter_config.json | 1,043 | ✓ |
| added_tokens.json | 707 | ✓ |
| special_tokens_map.json | 613 | ✓ |

Checkpoint 路径：`/home/sonny/exec-sim-repair-verifier/checkpoints/best/`（已修复嵌套目录问题）。seetacloud cuda:2/3 可以跑 majority-voting 和 block-corr-empirical 实验了。

---
