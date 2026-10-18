# code n4 reverse chain prep

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_n4_reverse_chain_prep_20260516T140408_result.json`
- **Structured JSON:** [`32ef144b66209fe78b03.json`](../../sessions/32/32ef144b66209fe78b03.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 全部通过。总结：

**脚本路径**: `/root/autodl-tmp/recursive_gen_depth_est/scripts/run_reverse_chain_pipeline.sh`

**Dry-run 结果**: 全部通过
- GPT-2 XL (1.5B): finetune ✓, generate ✓
- OLMo-1B: finetune ✓, generate ✓  
- Pythia-1.4B: finetune ✓, generate ✓
- 数据格式正确（jsonl, 含 text/depth 字段）

**模型状况**: 三个模型均已下载到 `/root/autodl-tmp/models/`，无需额外下载

**运行方式**: 
```bash
# 完整运行 (500 samples/depth, cuda:1)
bash scripts/run_reverse_chain_pipeline.sh

# 自定义样本数
NUM_SAMPLES=100 bash scripts/run_reverse_chain_pipeline.sh
```

**预估完整运行时间** (500 samples):
- 每个模型 finetune ~5-8 min, generate ~15-25 min
- 3 个模型 × (finetune + generate) ≈ 60-100 min
- 特征提取 + 分类器 ≈ 10-15 min
- **总计约 1.5-2 小时**

---
