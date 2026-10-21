# ops westd start sft v3 and prep seed5 reeval

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_start_sft_v3_and_prep_seed5_reeval_20260522T101004_result.json`
- **Structured JSON:** [`73e3dd865424b741a455.json`](../../sessions/73/73e3dd865424b741a455.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

SFT baseline v3 已成功加载模型到 GPU 3（90649 MiB 显存占用），checkpoint shards 加载完毕。

### 产出汇总

**1. SFT baseline v3（GPU 3）**
- 状态：✅ 已启动，模型加载完成
- Session: `ragen_eval_gpu3`（created 18:11:47）
- GPU 3 显存: 90649 MiB
- 日志: `/root/autodl-tmp/logs/ragen_sft_baseline_ood_v3.log`
- 关键参数: `seed.val=321`, `enable_response_mask=False`, `model=qwen3_exp021_ragen_sft_v4`

**2. seed5 v2 config**
- 状态：✅ 已创建
- 路径: `config/_alfworld_exp029_seed5_ood_eval_v2.yaml`
- 修改: `seed.val: 321`, `experiment_name: seed5-step10-ood-eval-v2`, `enable_response_mask: False`（已为 False，无需改）
- 未启动，等 GPU 空闲

**3. 4 GPU 状态**

| GPU | 利用率 | 显存 | 任务 |
|-----|--------|------|------|
| 0 | 100% | 90467 MiB | ragen_eval_gpu0 |
| 1 | 100% | 90467 MiB | ragen_eval_gpu1 |
| 2 | 0% | 90467 MiB | ragen_eval_gpu2 |
| 3 | 0% | 90649 MiB | SFT baseline v3（刚启动，模型已加载） |

---
