# eval pythia topk50 001

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_pythia_topk50_001_20260514T183056_result.json`
- **Structured JSON:** [`a2caf3a93ac7e15a63c8.json`](../../sessions/a2/a2caf3a93ac7e15a63c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Pipeline `pythia_topk50_001` 正在 cuda:0 上运行中：
- **depth-0 finetune**: 完成（loss=2.24, 268s）
- **depth-1 generate**: 进行中（1630/5000, top-k k=50）
- depth-2, depth-3: 待运行

已创建 eval 脚本 `scripts/run_eval_pythia_topk50.sh`，涵盖：
1. 代码污染检查（filter_code.py stats）
2. 特征提取（extract_features.py, GPU）
3. 4-class 分类（RF+LR）
4. 3-class d1/d2/d3 分类
5. 3-class 去除代码污染后分类

每 ~4.5 分钟轮询进度，pipeline 完成后立即启动 eval。

---
