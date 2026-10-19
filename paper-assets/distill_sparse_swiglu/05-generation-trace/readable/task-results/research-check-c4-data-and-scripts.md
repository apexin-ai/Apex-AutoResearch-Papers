# research check c4 data and scripts

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_check_c4_data_and_scripts_20260523T005500_result.json`
- **Structured JSON:** [`7c1e69f43ff7c4049ab7.json`](../../sessions/7c/7c1e69f43ff7c4049ab7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
== 1. 数据集可用性 ==
C4:        有
  - /root/autodl-tmp/data/c4_val/    785MB, 364,608 条 (C4 validation split, load_from_disk 格式)
  - /root/autodl-tmp/.hf_cache/hub/datasets--allenai--c4/  419MB (HF cache)
  - ⚠️ 只有 validation split，没有 train split 本地缓存
RedPajama: 没有
Pile:      没有
SlimPajama:没有
其他:      wikitext103 (564MB), wikitext2 (test split)
磁盘剩余:  181GB (250G 数据盘用了 28%)

== 2. 脚本数据集支持 ==
--dataset 参数: choices=["wikitext-103", "c4"]，默认 "wikitext-103"
支持的脚本: train.py (E2E KL), train_perlayer_kl.py (per-layer KL) 均支持
数据加载逻辑 (data_utils.py):
  - get_calibration_loader(dataset_name="c4") 先查本地 /root/autodl-tmp/data/c4_val，
    有则 load_from_disk + shuffle；无则 streaming 从 HF 拉
  - 不需要修改任何代码，直接加 --dataset c4 即可

== 3. C4 训练准备工作 ==
无需准备，开箱即用：
  1. 代码已支持 --dataset c4
  2. 本地已有 c4_val 数据 (364K 条)
  3. 1000 steps × bs=4 × seq_len=2048 ≈ 需 ~8M tokens，364K 条绰绰有余

唯一注意点：
  - 本地缓存的是 C4 validation split (非 train split)
  - 对 1000 步 predictor 校准来说数据量足够，但如果严格要求用 train split，
    需下载 C4-en train（全量 ~305GB，或用 streaming 模式，代码已支持 fallback）

启动命令示例：
  python train_perlayer_kl.py --dataset c4 --num_steps 1000 --gpu 0
预估额外时间：0（无需下载/预处理）
```

---
