# ops prepare eval scripts batch

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prepare-eval-scripts-batch_20260514T210801_result.json`
- **Structured JSON:** [`1d7b82339d928dd2e3b3.json`](../../sessions/1d/1d7b82339d928dd2e3b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**报告：**

| 项目 | 结果 |
|------|------|
| 脚本 1 | `/root/autodl-tmp/scripts/eval_lr5e6_ckpt40.sh` ✓ 已写入 |
| 脚本 2 | `/root/autodl-tmp/scripts/eval_lr5e6_rp_ckpt20.sh` ✓ 已写入 |
| ckpt-40 (`grpo_ced_lr5e6`) | 存在，adapter_model.safetensors 252MB |
| ckpt-20 (`grpo_ced_lr5e6_rp`) | 存在，adapter_model.safetensors 252MB |
| rp_r2 当前进度 | **step 27/200** (~13.5%)，约 1h 已跑，预估还需 ~5h25m |
| 语法验证 | 两个脚本均 SYNTAX_OK |

注意：rp_r2 训练日志有多次 KL divergence 极端值警告（最高 39B），目前标记为 monitoring only 未中断训练。

---
