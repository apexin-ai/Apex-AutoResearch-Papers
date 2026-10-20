# train sft qwen math westd

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_sft_qwen_math_westd_20260516T080740_result.json`
- **Structured JSON:** [`9d4fb31236e68b27f33b.json`](../../sessions/9d/9d4fb31236e68b27f33b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 SFT 实验均已成功启动训练：

| 实验 | GPU | 显存 | 速度 | 总步数 | 预计时间 |
|------|-----|------|------|--------|----------|
| sft_rasp_20_qwen_math | cuda:0 | 51GB (85%) | ~1.07 it/s | 2805 | ~44 min |
| sft_standard_20_qwen_math | cuda:1 | 51GB (81%) | ~1.04 it/s | 2805 | ~45 min |

完成事项：
- 修复了 `sft_recovery.py` 中 EOS token 断言（Qwen2.5 chat template 使用 `<|im_end|>` 而非 `<|endoftext|>`）
- Registry 两条实验已更新为 RUNNING
- 预计 ~45 分钟后训练完成

注意：之前 kill 了 cuda:0 上残留的 `eval_gsm8k.py --model_path sft_rasp_25` 进程（已跑近 2 小时），如需要可后续重跑。

---
