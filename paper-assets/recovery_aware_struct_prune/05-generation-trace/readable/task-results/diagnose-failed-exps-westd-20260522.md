# diagnose failed exps westd 20260522

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_failed_exps_westd_20260522_20260522T111900_result.json`
- **Structured JSON:** [`49a4ae236daefc3186fe.json`](../../sessions/49/49a4ae236daefc3186fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。汇报如下：

---

## 诊断结果

### 实验 1: pipeline_depth_first_20

**失败根因**: **训练实际已完成，不是真正失败。** 监控系统误判。

三个阶段全部成功产出：
- `pruned_depth_first_20/` — 剪枝完成 (May 22 18:23)，含 `pruning_metadata.pt`
- `sft_depth_first_20/` — SFT 完成 (May 22 18:47)
- `grpo_depth_first_20/` — GRPO 100步完成 (May 22 19:06)，W&B run `immasi23`，checkpoint-100 完整

**缺失**: eval 步骤未执行。没有找到 `pipeline_depth_first_20.log`，说明 pipeline 不是通过标准日志机制启动的，导致监控系统找不到 sentinel/W&B。

**需要做的**: 只需跑 eval（GSM8K / MATH500），训练无需重跑。

---

### 实验 2: grpo_random_20_seed123

**失败根因**: **训练实际已完成，不是真正失败。** 监控系统误判。

- GRPO 100步全部完成 (May 22 19:01)，W&B run `1silchcm`
- 完整模型 (~12GB) 和 10 个 completion parquet 文件都在
- `sft_random_20` 源模型在 westd-32935 上存在

**缺失**: eval 步骤未执行。

**需要做的**: 只需跑 eval，训练无需重跑。

---

### 关键环境问题

| 条件 | 状态 |
|------|------|
| westb-23072 磁盘 | **100% 满** (250G/250G，仅剩 3.3MB) — 无法在此运行任何实验 |
| westb-23072 `sft_random_20` | **不存在** |
| westd-32935 磁盘 | 98% (15G 剩余) — eval 应该够用（不产生大文件） |
| westd-32935 GPU | cuda:0 空闲，cuda:1/2/3 被占用 |
| westb-23072 GPU | cuda:0 空闲，cuda:1 被占用 |

---

### 重跑建议

**不需要重跑训练**，只需在 westd-32935:cuda:0 上跑两个 eval：

**Eval 1 — depth_first_20 GRPO 模型 (GSM8K)**:
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_depth_first_20 --output_path results/eval_grpo_depth_first_20.json --max_samples 1319 --seed 42 --dtype bfloat16
```

**Eval 2 — random_20_seed123 GRPO 模型 (GSM8K)**:
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123 --output_path results/eval_grpo_random_20_seed123.json --max_samples 1319 --seed 42 --dtype bfloat16
```

两个 eval 需要串行跑（共用 cuda:0），每个约 20-30 分钟。也可以考虑跑 MATH500 eval（如果实验计划需要）。westb-23072 因磁盘满无法使用，建议先清理空间。

---
