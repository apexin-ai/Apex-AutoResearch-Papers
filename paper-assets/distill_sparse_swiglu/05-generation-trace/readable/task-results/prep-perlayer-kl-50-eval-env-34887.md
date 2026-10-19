# prep perlayer kl 50 eval env 34887

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_perlayer_kl_50_eval_env_34887_20260522T035816_result.json`
- **Structured JSON:** [`1fdc0ca6adb51ede6d6d.json`](../../sessions/1f/1fdc0ca6adb51ede6d6d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

单向足够（34887 从 41718 拉取 checkpoint）。

---

**汇报：**

| 项目 | 状态 | 详情 |
|------|------|------|
| **SCP 连通性** | 单向可用 | 34887 → 41718 通过 `scp -P 41718 root@connect.westd.seetacloud.com:` 可达（已配置 SSH key）。反向未配置（不需要）。 |
| **Eval 代码** | 就绪 | `benchmark_eval.py` 存在 (17817B, May 18) |
| **Python 环境** | 就绪 | torch=2.8.0+cu128, cuda=True, gpus=2, transformers=5.8.1, lm_eval=0.4.12 |
| **磁盘空间** | 充足 | 根分区 8.4G 可用，数据盘 181G 可用。Checkpoint ~150MB 无压力 |
| **LLaMA-3.1-8B 缓存** | 完整 | `/root/autodl-tmp/models/llama-3.1-8b/` (15G) |
| **BoolQ/SuperGLUE 数据集** | 已缓存 | `super_glue` + `boolq` 均在 `.hf_cache/datasets/` 中 |

**SCP 命令（训练完成后用）：**
```bash
# 在 westd-34887 上执行
scp -P 41718 root@connect.westd.seetacloud.com:/root/distill_sparse_swiglu/checkpoints/&lt;checkpoint_file> /root/distill_sparse_swiglu/checkpoints/
```

无问题需要修复，环境已就绪。

---
