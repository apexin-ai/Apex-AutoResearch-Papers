# ops westd 34887 disk cleanup

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-34887-disk-cleanup_20260518T034843_result.json`
- **Structured JSON:** [`108a4d82d802442ab6c4.json`](../../sessions/10/108a4d82d802442ab6c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 清理结果

**磁盘变化**: 81% → 51%，可用空间 5.8G → 15G，释放 ~9.2G

剩余约 0.8G 差距因 overlay 文件系统限制（底层镜像文件删除不释放空间），在不破坏环境和其他项目的前提下已无更多安全可清理内容。

**清理明细：**

| 类别 | 释放空间 | 具体内容 |
|------|---------|---------|
| 失败/killed/negative 实验 checkpoint | ~3.5G | steps_curve_s42, bce_comp_staged_s42, kl_normalized_quicktest, qwen14b_bce30_s42_v2, bce_framework_lr*, jsd_50pct_s42, kl_lagrangian_quicktest, kl_mag_reg_*, kl_norm_v3_quicktest, mvp_kl_s42, reverse_kl_50pct_s42, kl_sparsity30_s42, kl_sparsity40_s42, tau_ablation_dryrun, spon_* 等 20 个目录 |
| db_sweep 已完成扫描目录 | ~939M | db_sweep_64, db_sweep_256, db_sweep_512 |
| 14B dryrun 输出 | ~896M | outputs/qwen14b_dryrun{,2,3,4} |
| pip cache | 705M | /root/.cache/pip |
| HF datasets cache | 783M | /root/.cache/huggingface/datasets |
| lm_eval 大结果文件 | ~380M | 5 个 lm_eval 结果目录（每个 76M） |
| miniconda3 __pycache__ | ~486M | 所有编译缓存 |
| /tmp 测试/dryrun 产物 | ~1.1G | test_wikitext, ste_test, ste_dryrun, gumbel_test, dryrun_*, comp_dryrun, vip.tar.gz |
| tests/mini_llama 测试模型 | 272M | 可再下载的测试 fixture |
| bitsandbytes 未使用包 | 177M | 项目代码未引用，无反向依赖 |
| torch cache + wandb + misc | ~130M | 缓存和离线日志 |

**保留未动：** 所有 conclusion=success 的 checkpoint（4.7G）、模型权重、HF 模型缓存、项目数据文件、其他项目文件。

---
