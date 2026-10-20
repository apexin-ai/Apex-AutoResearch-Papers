# code prepare seed456 all methods

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare_seed456_all_methods_20260513T164443_result.json`
- **Structured JSON:** [`9d2260e6ba72591df93d.json`](../../sessions/9d/9d2260e6ba72591df93d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个脚本全部通过语法验证。

提交命令：

```
UNCURATED_CMD: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /root/div_cal_verify/env.sh && export TRANSFORMERS_OFFLINE=1 && cd /root/div_cal_verify && bash run_uncurated_seed456.sh 0"
RGDS_CMD: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /root/div_cal_verify/env.sh && export TRANSFORMERS_OFFLINE=1 && cd /root/div_cal_verify && bash run_rgds_seed456.sh 0"
EXT_CMD: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /root/div_cal_verify/env.sh && export TRANSFORMERS_OFFLINE=1 && cd /root/div_cal_verify && bash run_ext_seed456.sh 1"
```

GPU 排期：cuda:0 串行跑 uncurated→RGDS（~4h），cuda:1 跑 external_only（~2h），等 random_50 完成后提交。

---
