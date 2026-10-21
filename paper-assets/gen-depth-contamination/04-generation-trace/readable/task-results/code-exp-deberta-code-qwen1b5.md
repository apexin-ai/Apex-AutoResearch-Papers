# code exp deberta code qwen1b5

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_deberta_code_qwen1b5_20260520T033440_result.json`
- **Structured JSON:** [`2796a35e7b1aad388641.json`](../../sessions/27/2796a35e7b1aad388641.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息收集完毕。汇总结果：

## 数据状况

- **路径**: `/root/autodl-tmp/gen-depth-contamination/data/exp_code_qwen1b5/`
- **文件**: depth_0.jsonl ~ depth_5.jsonl（6 个 depth），每个 5,500 samples，共 **33,000 samples**
- **格式**: `{"text": "...", "doc_id": "code_py_0"}` — 与 arXiv/C4 格式一致，可直接使用
- **OBD baseline**: `/root/autodl-tmp/gen-depth-contamination/results/exp_code_qwen1b5/pairwise_auc.json`
  - OBD K\*=2（0v1=0.9388, 1v2=0.7382, 2v3=0.53 < θ=0.60）

## 脚本分析

现有脚本（`run_deberta_arxiv.py`, `run_deberta_c4_1b5.py`）都是独立脚本，数据路径/结果目录/OBD路径全部硬编码。需要创建 `run_deberta_code.py`，基于 arXiv 模板修改以下配置：

| 参数 | 值 |
|------|-----|
| EXPERIMENTS | `{"code_qwen1b5": DATA_DIR / "exp_code_qwen1b5"}` |
| RESULTS_DIR | `ROOT / "results" / "exp_deberta_code_qwen1b5"` |
| OBD_MAP | `{"code_qwen1b5": ROOT / "results" / "exp_code_qwen1b5" / "pairwise_auc.json"}` |

其余超参（MAX_LEN=512, EPOCHS=3, BS=16, LR=2e-5, N_BOOT=10000, THETA=0.60）与 arXiv 完全一致。

## 需要先创建脚本

需要在服务器上创建 `/root/autodl-tmp/gen-depth-contamination/scripts/run_deberta_code.py`。脚本与 `run_deberta_arxiv.py` 完全相同，只改三个路径常量。

## 推荐启动命令

```bash
bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && CUDA_VISIBLE_DEVICES=2 python scripts/run_deberta_code.py'
```

使用 `CUDA_VISIBLE_DEVICES=2` 让脚本中的 `cuda:0` 映射到物理 GPU 2，无需修改脚本内部设备逻辑。

**下一步**: 需要主 Agent 先通过 `ssh_execute` 创建脚本文件，然后通过 `submit_training_job` 提交训练。

---
