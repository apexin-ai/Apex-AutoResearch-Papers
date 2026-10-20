# ops s43 fix restart final

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_s43-fix-restart-final_20260522T202204_result.json`
- **Structured JSON:** [`eb03d48a23294f196dde.json`](../../sessions/eb/eb03d48a23294f196dde.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。汇报结果：

## s42 实际参数（从 PID 679204 cmdline 提取）
```
--model_name /root/autodl-tmp/.ms_cache/EleutherAI/pythia-1.4b-deduped
--data_dir data/wikitext103_5k
--synthetic_ratio &lt;per-experiment>
--num_generations 10
--steps_per_gen 5000
--seed 42
--batch_size 4
--max_length 512
--lr 5e-5
--gen_max_new_tokens 256
--gen_batch_size 8
--top_p 0.95
--optim adamw_torch
--gradient_checkpointing
```

## 磁盘清理
- 17855 清理前: 88% (43GB 剩余)
- 17855 清理后: 88% (43GB 剩余) — checkpoint 已被之前清理过，phase_diagram_14b 不存在
- 19828: 54% (116GB 剩余) — 空间充足，无需清理

## 模型路径确认
- 17855: `/root/autodl-tmp/.ms_cache/EleutherAI/pythia-1.4b-deduped` ✓
- 19828: `/root/autodl-tmp/.hf_cache/EleutherAI/pythia-1.4b-deduped` ✓

## 重启结果

s43 实验已由另一个 Worker 在 04:23 UTC 正确启动，两个 bug 均已修复。

| 实验 | Server:GPU | PID | gen_batch_size | local_model | GPU 占用 |
|------|-----------|-----|---------------|-------------|---------|
| t10_a075_s43 | 17855:cuda:2 | 719178 | ✓ OK | ✓ ms_cache | 11236 MiB |
| t10_a060_s43 | 17855:cuda:3 | 719252 | ✓ OK | ✓ ms_cache | 11236 MiB |
| t10_a050_s43 | 19828:cuda:1 | 822048 | ✓ OK | ✓ hf_cache | 11236 MiB |

## s42 vs s43 参数 diff
仅 `--seed`（42→43）、`--output_dir`（路径不同）、`--model_name` 路径（19828 用 hf_cache vs 17855 用 ms_cache）不同。其余参数完全一致。✓

输出目录尚未创建（Gen 0 baseline 计算中），GPU 显存从 10293→11236 MiB 递增，进程状态 Rl+，一切正常运行。

---
