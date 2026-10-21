# fix deberta code cuda3 prep

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_deberta_code_cuda3_prep_20260520T052907_result.json`
- **Structured JSON:** [`7911efe2d075808316dd.json`](../../sessions/79/7911efe2d075808316dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Summary:

**GPU 状态**
| GPU | Memory Used | Status |
|-----|-------------|--------|
| 0 | 0 MiB | idle |
| 1 | 0 MiB | idle |
| 2 | 3257 MiB | OLMo SF-4 running |
| **3** | **0 MiB** | **空闲，可用** |

**清理完成**
- tmux session `exp_deberta_code_qwen1b5` 已 kill
- `results/exp_deberta_code_qwen1b5/` 已删除

**OOM 修复**（3 处改动）
- 新增 `EVAL_BS = 8`（line 45）
- val DataLoader 改用 `EVAL_BS`（line 98）
- eval 前加 `torch.cuda.empty_cache()`（line 122, 131）
- 语法验证通过

**推荐重启命令**（CUDA_VISIBLE_DEVICES=3）:
```bash
CUDA_VISIBLE_DEVICES=3 bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 python scripts/run_deberta_code.py'
```

---
