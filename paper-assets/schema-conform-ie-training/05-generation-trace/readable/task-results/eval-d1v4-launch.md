# eval d1v4 launch

**schema conform ie training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_d1v4_launch_20260513T104853_result.json`
- **Structured JSON:** [`a46af1449e31b8a2e87f.json`](../../sessions/a4/a46af1449e31b8a2e87f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

**1. D1 v4 训练** — 成功完成。500/500 steps, 耗时 4h01m。LoRA 已自动 merge 到 `/root/autodl-tmp/output/formal_D1_v4/merged/`（含 model.safetensors）。5 个 checkpoints (100-500) 均已保存。

**2. D1 v4 eval** — 已启动（tmux session `eval_d1v4`，CUDA_VISIBLE_DEVICES=1）。评估 scierc_test / crossner_politics / crossner_science 三个数据集，模型正在加载中。

**3. D2 ckpt400 eval** — scierc_test 544/551（99%），即将完成第一个数据集，后续还有 crossner_politics 和 crossner_science。完成后会自动接着跑 D2 final eval。

**4. GPU 状态**
- GPU 0: 59% util, 22GB — D2 eval
- GPU 1: D1 eval 刚启动，正在加载模型

---
