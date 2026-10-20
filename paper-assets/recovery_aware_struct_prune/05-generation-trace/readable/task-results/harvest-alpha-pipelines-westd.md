# harvest alpha pipelines westd

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_alpha_pipelines_westd_20260522T084914_result.json`
- **Structured JSON:** [`65d969c752d3b717b9fd.json`](../../sessions/65/65d969c752d3b717b9fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完毕。

```
== GPU 状态 ==
GPU 0: 19251 MiB, 98% util (非 α 管线任务)
GPU 1: 17651 MiB, 95% util (非 α 管线任务)
GPU 2: 7257 MiB,  5% util  ← α=2.0 SFT eval 刚启动
GPU 3: 12765 MiB, 93% util ← α=0.5 SFT eval 进行中

== α=0.5 (GPU 3, CUDA_VISIBLE_DEVICES=3) ==
GRPO训练: ✅ 完成 (100/100 steps, 15:22:57)
GRPO eval: ✅ 完成 accuracy=61.18% (807/1319), 16:32:50完成
SFT eval:  🔄 进行中 ~350/1319 (~27%), running acc=62.57%, 预计~17:30完成
  └─ SFT模型加载自 sft_rasp_alpha0p5_20, 16:32:57启动
C1 Δ = GRPO - SFT = 待SFT eval完成

== α=2.0 (GPU 2, CUDA_VISIBLE_DEVICES=2) ==
GRPO训练: ✅ 完成 (100/100 steps, 15:22:34)
GRPO eval: ✅ 完成 accuracy=66.11% (872/1319), 16:47:47完成
SFT eval:  🔄 进行中 ~7/1319 (<1%), 刚启动 16:49:32, 预计~18:10完成
  └─ SFT模型加载自 sft_rasp_alpha2p0_20

== Checkpoint 存在性 ==
grpo_rasp_alpha0p5_20: ✅ 存在 (model.safetensors 12.3GB + checkpoint-100/)
grpo_rasp_alpha2p0_20: ✅ 存在 (model.safetensors 12.3GB + checkpoint-100/)
sft_rasp_alpha0p5_20:  ✅ 存在
sft_rasp_alpha2p0_20:  ✅ 存在

== 已落盘结果文件 ==
eval_gsm8k_grpo_alpha0p5_20.json ✅ (.done sentinel存在)
eval_gsm8k_grpo_alpha2p0_20.json ✅ (.done sentinel存在)
eval_gsm8k_sft_alpha0p5_20.json  ❌ 未生成（eval进行中）
eval_gsm8k_sft_alpha2p0_20.json  ❌ 未生成（eval进行中）

== wandb ==
α=0.5 GRPO: grpo_sft_rasp_alpha0p5_20 (run 0fh1firj)
α=2.0 GRPO: grpo_sft_rasp_alpha2p0_20 (run 2b2x9kmb)
```

两个 α 管线的 GRPO 阶段全部完成，SFT eval 正在自动跑。α=0.5 SFT eval 约 30 分钟后完成，α=2.0 约 80 分钟后完成。GPU 0/1 在跑非 α 管线任务。

---
