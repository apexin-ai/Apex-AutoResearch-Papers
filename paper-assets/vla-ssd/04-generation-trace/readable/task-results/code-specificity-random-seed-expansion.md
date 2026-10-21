# code specificity random seed expansion

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_specificity_random_seed_expansion_20260519T202943_result.json`
- **Structured JSON:** [`7f5990f768db203c6330.json`](../../sessions/7f/7f5990f768db203c6330.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**汇报：需要 GPU 做一次性缓存生成**

分析结论：
- **Method A 不可行**：服务器上没有 per-head 独立 ablation 数据。已有数据都是 group ablation（24头/8头/32头同时 ablate），不是单个 head 独立 ablate 后的 R² drop。
- **必须走 Method B**：`random_subset_ablation.py` 的工作方式是先做一次 model forward pass 缓存 Layer 1 的 per-head attention intermediates（full_context, non_inst_sum, non_inst_weight, residual），再用这些缓存做不同 head 组合的 feature 重建 + probe 训练。
- **缓存未持久化**：parent 实验运行时缓存在 RAM 中，进程挂起后丢失，磁盘上没有 `.pt` / `.npz` 缓存文件。

**已完成：**
- 脚本已写好：`/root/vla-ssd/scripts/specificity_bootstrap_30seeds.py`
- 两阶段设计：
  - `--generate-cache`：GPU 阶段，加载模型做 forward pass，保存 cache 到 `/root/autodl-tmp/vla-ssd/results/l1_head_ablation/l1_attention_cache.pt`（约 ~2GB）
  - 默认模式：CPU-only，加载 cache，跑 30 seeds bootstrap + 统计（约 1-2 小时）
- 实验已注册为 QUEUED

**GPU 状态：**
- GPU 0：空闲（3 MiB / 97887 MiB，0% 利用率）
- GPU 1：少量负载（1739 MiB，45%）

**请决定：**
1. 是否允许我用 GPU 0 跑 `--generate-cache`（约 20 分钟，完成后立即释放 GPU）？
2. 或者分配其他资源？

缓存生成完成后，bootstrap 阶段完全不碰 GPU（`CUDA_VISIBLE_DEVICES=""`）。

---
