# ops status check westd29022

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_status_check_westd29022_20260518T172903_result.json`
- **Structured JSON:** [`4d122196626fb6ba10a6.json`](../../sessions/4d/4d122196626fb6ba10a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-29022 状态汇报

| GPU | 任务 | 进度 | 关键指标 | 预估完成 |
|-----|------|------|----------|----------|
| **cuda:0** | GRPO训练 `grpo_cka_only_20_extended_300` | **170/300** (57%) | loss=0.138, reward=0.267, ~117s/step | ~05:40 UTC |
| **cuda:1** | eval `math500_grpo_standard_20_fair` | **110/500** (22%) | Acc@100=0.3600, ~150s/sample | ~17:30 UTC (很慢) |
| **cuda:2** | eval `math500_sft_cka_only_20_v4` | **25/500** (5%) | 刚启动20min, ~43s/sample | ~07:30 UTC |
| **cuda:3** | eval `math500_dense_unpruned` | **428/500** (86%) | **Acc@400=0.7375**, ~35s/sample | **~02:10 UTC** (最快完成) |

### 详情

- **cuda:0**: 82°C/604W, 90.6GB VRAM。从 checkpoint-100 续训, 已到 step 170, 剩 130 步约 4.2h。
- **cuda:1**: 83°C/603W, 31.5GB VRAM。这个 eval 极慢，部分样本生成耗时 3-5 分钟（疑似模型生成超长序列）。110/500 已花 4.3h，剩余约 16h。
- **cuda:2**: 79°C/561W, 16.8GB VRAM。01:07 启动, 进度正常。
- **cuda:3**: 58°C/341W, 17.7GB VRAM。接近完成，约 40 分钟内出结果。Dense unpruned Acc@400 = 73.75%。

### 已完成结果文件
- `math500_grpo_unpruned.json` (May 18 12:54) — 仅此一个。

### 注意
cuda:1 的 `grpo_standard_20_fair` eval 速度异常慢（VRAM 占 31.5GB，远高于其他 eval 的 ~17GB），可能模型较大或生成长度未受限。按当前速度要到明天中午才能跑完。

---
