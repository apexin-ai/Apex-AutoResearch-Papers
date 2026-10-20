# ops check dpo 1ep and bf16 source

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-dpo-1ep-and-bf16-source_20260515T225719_result.json`
- **Structured JSON:** [`b7ea9c2a4a5d6f9525ad.json`](../../sessions/b7/b7ea9c2a4a5d6f9525ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### A: DPO 1ep eval 状态

**正在运行，约 50% 完成。**

- 第一次 (r1) OOM 失败——被提交到 GPU 0（PID 258508 占用 ~28GB），全部 batch 都 OOM。
- 第二次 (r2) 在 cuda:3 上运行中：PID 262080，已运行 ~59 min，显存 14468 MiB。
- 进度：**31/62 batches (50%)**，~113s/it，预计还需 ~58 min 完成。
- 输出目录 `dpo_ced_1ep_fixed/` 已创建但为空，尚无结果。
- cuda:3 上还跑着另一个 eval（PID 261622, rsft_s44, 15282 MiB），两个进程共享该卡。

### B: rel_f1=0.4549 来源

**0.4549 来自 checkpoint-100，不是 checkpoint-70。**

| 项目 | ckpt-100 (0.4549) | ckpt-70 (0.4341) |
|------|-------------------|-------------------|
| 路径 | `grpo_ced_g8_bf16/checkpoint-100` | `grpo_ced_g8_bf16/checkpoint-70` |
| F1 | 0.4549 | 0.4341 |
| Evi-F1 | 0.8086 | 0.8099 |
| EDCR | 0.6318 | 0.6685 |
| eval 配置 | batch=16, seed=42, no quantize, full dev (985 docs) | 完全相同 |

**差异原因：纯粹是 checkpoint 不同。** eval 条件完全一致（同 batch_size、同 seed、同数据集全量、无量化）。plan_009 报告的 0.4549 用的是 step-100，plan_011 用的是 step-70。

训练轨迹：step30=0.434 → step50=0.428 → step70=0.434 → step80=0.446 → step100=0.455，step 70 之后持续爬升。

---
