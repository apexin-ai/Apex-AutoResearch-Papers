# ops disk cleanup d060

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk_cleanup_d060_20260518T070223_result.json`
- **Structured JSON:** [`d78427d47ea6760f9dcf.json`](../../sessions/d7/d78427d47ea6760f9dcf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总如下：

---

## 1. 6.9B 模型下载状态：**完成**

- `model-00001-of-00002.safetensors` (9.3G) + `model-00002-of-00002.safetensors` (3.7G) = 13G
- Tokenizer 验证通过 (vocab=50277)
- 路径：`/root/autodl-tmp/.hf_cache/pythia-6.9b-local/`

## 2. 磁盘空间

| | 清理前 | 清理后 |
|---|---|---|
| 可用空间 | 87G | 138G |
| 已用 | 164G | 113G |
| **释放** | | **~51G** |

## 3. 清理明细

| 目录 | 清理内容 | 释放空间 |
|---|---|---|
| `pythia14b_wiki_a100_s42` | gen_6-9 checkpoint (4×5.3G) + synthetic_data | ~21.2G |
| `pythia1b_c4_a100_s43` | gen_1-9 checkpoint (9×3.8G) + synthetic_data | ~34.2G |
| 其余 generalize + alpha_sweep | synthetic_data (均很小) | ~0.2G |
| gpt2m v1/v2、a025、MVP | 不存在，无需清理 | 0 |

保留完整：所有 `metrics.json`、`gen_10/checkpoint`、`all_metrics.json`、`analysis/` 目录。两个活跃实验（gpt2m cuda:0, pythia-1.4b s43 cuda:1）未触碰。

## 4. Checkpoint 自动清理建议

`iterative_train.py` 第 272-276 行每个 gen 结束时无条件保存 checkpoint，无自动清理逻辑。可在第 276 行后加：

```python
# Auto-cleanup: keep gen_0 + last 2 checkpoints
if gen >= 3:
    old_ckpt = os.path.join(args.output_dir, f"gen_{gen-2}", "checkpoint")
    if os.path.isdir(old_ckpt):
        shutil.rmtree(old_ckpt)
```

对于 6.9B (~14G/checkpoint)，这能在训练中自动节省 ~100G。改动简单（3 行），但由于当前两个实验正在跑，建议下次启动新实验前再加入，避免影响正在运行的进程。

---
