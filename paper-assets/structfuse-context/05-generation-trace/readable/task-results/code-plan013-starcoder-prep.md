# code plan013 starcoder prep

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan013-starcoder-prep_20260513T051012_result.json`
- **Structured JSON:** [`1336e6d8215825572c3a.json`](../../sessions/13/1336e6d8215825572c3a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已正常启动。

## 汇总

| 项目 | 结果 |
|------|------|
| **StarCoder2 路径** | `/root/autodl-tmp/models/bigcode/starcoder2-3b/bigcode/starcoder2-3b/` |
| **兼容性** | 完全兼容。AutoModel 加载正常，hidden_size=3072（vs Qwen 2048），projection 自动适配，LoRA targets (q_proj/v_proj) 存在。3030.4M 参数。|
| **数据生成** | **跳过** — extraction-dir/repos-dir 已从服务器删除，无法重新 mine。直接复用 `m2_embed_verify_data`（3282×3 train + 1148 val），作为更干净的对照实验（唯一变量=encoder 架构）。|
| **train.py 参数** | `--num-epochs`（设 2）、`--eval-steps 500`。无 early stopping 支持。|
| **代码修改** | 无。contrastive_model.py 已是 encoder-agnostic 的。|
| **训练状态** | PID 20005，tmux session `plan_013_starcoder`，cuda:0 占用 38GB/98GB，GPU 利用率 100%。random 策略已开始 Epoch 1。|

---
