# ops westd cuda2 launch sft standard math500

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_cuda2_launch_sft_standard_math500_20260518T221735_result.json`
- **Structured JSON:** [`56ce41fe89fe0a46cc52.json`](../../sessions/56/56ce41fe89fe0a46cc52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cuda:2 已成功启动，模型已加载到 GPU（12458MiB），正在加载 MATH 数据集。

## 汇总

**cuda:2 — eval_math500_sft_standard_20_2048** ✅ 已启动
- 模型：`sft_qwen_math_standard_20`（注：`sft_standard_20_westd` 缺权重，用了完整的 `sft_qwen_math_standard_20`）
- PID 33033, 12458MiB 占用
- 输出：`results/math500_sft_standard_20_2048.json`
- 日志：`results/math500_sft_standard_20_2048.log`

**其他 GPU 进度：**

| GPU | 实验 | 进度 | 备注 |
|-----|------|------|------|
| cuda:0 | eval_math500_dense_2048 | 运行中（17658MiB, 91%） | 无可定位的独立日志文件 |
| cuda:1 | eval_math500_grpo_standard_20_fair_v2 | ~41/500（8%），日志停更于 02:22 但 GPU 仍活跃（19251MiB, 99%） | tqdm 可能未 flush |
| cuda:3 | eval_math500_grpo_rasp_20_fair | **371/500（74%）**, 中间 Acc@300=0.2567, Acc@350=0.2429 | 预计还需 ~2-3h |

---
