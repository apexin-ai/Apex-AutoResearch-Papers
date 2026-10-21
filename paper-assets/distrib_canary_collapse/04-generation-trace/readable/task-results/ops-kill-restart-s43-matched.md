# ops kill restart s43 matched

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-restart-s43-matched_20260522T201845_result.json`
- **Structured JSON:** [`bce53df99d1bddd1577e.json`](../../sessions/bc/bce53df99d1bddd1577e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部确认完毕。

## s42 实际参数（从 cmdline/config.json 提取）

```
--model_name &lt;local_path>/EleutherAI/pythia-1.4b-deduped
--data_dir data/wikitext103_5k
--synthetic_ratio &lt;varies>
--num_generations 10
--steps_per_gen 5000
--seed 42
--batch_size 4
--max_length 512
--lr 5e-5
--gen_max_new_tokens 256
--gen_batch_size 8          ← s43 旧版错用默认值 16
--top_p 0.95
--optim adamw_torch
--gradient_checkpointing    ← s43 旧版缺失
```

## Kill 结果

- PID 717612 (17855, a075_s43): 已自行退出（EXIT_CODE=1，模型路径缺失）
- PID 717753 (17855, a060_s43): 已自行退出（同上）
- PID 821294 (19828, a050_s43): 已自行退出（同上）

s43 旧版根本没跑起来——用了裸 HF ID `EleutherAI/pythia-1.4b-deduped` 而非本地缓存路径。

## 磁盘清理（待确认）

**17855 剩余 27GB**，可删除的中间 checkpoint：

| 目录 | gen | 大小 |
|------|-----|------|
| t10_a045_s42_fp32_14b | gen_5/checkpoint | 5.3G |
| t10_a045_s42_fp32_14b | gen_6/checkpoint | 5.3G |
| t15_a045_s42_fp32_14b | gen_6/checkpoint | 5.3G |
| t15_a045_s42_fp32_14b | gen_7/checkpoint | 5.3G |
| t15_a050_s42_fp32_14b | gen_8/checkpoint | 5.3G |
| t15_a050_s42_fp32_14b | gen_9/checkpoint | 5.3G |
| t15_a060_s42_fp32_14b | gen_8/checkpoint | 5.3G |
| t15_a060_s42_fp32_14b | gen_9/checkpoint | 5.3G |
| **合计** | | **~42G** |

⚠️ t10_a045 和 t15 系列的 checkpoint 是它们最近的 resume 点。如果这些实验仍在运行或未完成，删除会影响断点续训。确认后再删。

## 重启结果

| 实验 | Server:GPU | New PID | cmdline 验证 | GPU 占用 |
|------|-----------|---------|-------------|---------|
| t10_a075_s43 | 17855:cuda:2 | 719178 | `--gen_batch_size 8 --gradient_checkpointing` ✓ | 10293 MiB ✓ |
| t10_a060_s43 | 17855:cuda:3 | 719252 | `--gen_batch_size 8 --gradient_checkpointing` ✓ | 10293 MiB ✓ |
| t10_a050_s43 | 19828:cuda:1 | 822048 | `--gen_batch_size 8 --gradient_checkpointing` ✓ | 10293 MiB ✓ |

3 个实验均已进入 Generation 0 (baseline) 阶段。

## 参数匹配确认

s43 vs s42 diff（仅以下字段不同）：
- `--seed`: 42 → 43
- `--output_dir`: `results/phase_diagram/t10_aXXX_s42_fp32_14b` → `results/scale/14b_t10_aXXX_s43_fp32`
- `--synthetic_ratio`: 各自对应（0.75/0.60/0.50）

其余参数完全一致，包括关键的 `--gen_batch_size 8`。

---
