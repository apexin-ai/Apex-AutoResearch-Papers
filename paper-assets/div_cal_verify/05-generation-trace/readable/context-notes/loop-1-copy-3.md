# reviewer / loop_1.md

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`873255229463b59f7b15.json`](../../sessions/87/873255229463b59f7b15.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-12T14:41:05+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：`westd-11235` 的 `cuda:0` 和 `cuda:1`，越界即 critical
- 根分区只有 30GB，**已 100% 满**。checkpoint 必须存到数据盘或只保留最新一代 checkpoint，删除旧代 checkpoint 后再重启实验
- `diversity_selection.py` 的 `greedy_disf_selection` 已修复为 `compute_normalized_eigenvalue_variance`（`frob/trace²`），**不要回滚到旧版 `compute_cov_frobenius`**——旧版方向反了，选相似性而非多样性
- MVP gate 是二元 PASS/FAIL，**没有 SOFT PASS**（Human Review Note 明确删除 dual-outcome hedge）
- 参考集已从 512 增至 5000，`data/meta.json` 已更新，不要重新生成 512 版本

### 2. 🖥️ 基础设施快照
- 服务器：`westd-11235(root)`，工作目录 `/root/div_cal_verify`
- Python：`/root/miniconda3/bin/python`（conda base，用 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- 环境初始化：`source /root/div_cal_verify/env.sh`（含 network_turbo + HF mirror + SSL）
- 模型：`/root/models/Qwen/Qwen3-1.7B`（student）、`/root/models/Qwen/Qwen3-4B`（generator）
- 数据：`/root/div_cal_verify/data/`（train_chunks 242666, ref 5000, test 583, seq_len=512）
- 结果：`/root/div_cal_verify/results/rgds/`（gen_0~gen_3，gen_3 不完整）
- GPU：2× NVIDIA RTX PRO 6000 Blackwell 98GB
- 活跃进程：**无**（mvp_rgds_v3 已崩溃，GPU 已释放）
- 分析脚本：`analyze_mvp.py` 已部署

### 3. 📊 当前状态
mvp_rgds_v3 在 Gen 3 training 完成后 `save_pretrained` 时磁盘满崩溃（`No space left on device`）。Gen 0-2 metrics 完整保存：

| Gen | PPL | RankMe | kNN | Rare n-gram | Rank corr |
|-----|-----|--------|-----|-------------|-----------|
| baseline | — | 983.21 | — | — | — |
| 0 | 16.63 | 971.52 | 0.991 | 0.030 | -0.373 |
| 1 | 16.84 | 965.20 | 0.991 | 0.030 | -0.384 |
| 2 | 16.35 | 966.02 | 0.991 | 0.031 | -0.383 |

Registry: mvp_rgds_v3 status=RUNNING（实际已崩溃）；v1 仍显示 RUNNING/killed（registry 卫生问题）；v2 = failed。ext_v3 和 uncurated 未启动。

### 4. 📋 待办
- **磁盘满** → 删除旧 checkpoint（gen_0/checkpoint, gen_1/checkpoint 至少释放 ~6GB），或改 `--output_dir` 到数据盘，然后重跑 gen_3 或整个 rgds
- rgds gen_3 完成 → 启动 `mvp_ext_v3`（external_only，双卡 `--gpu_ids 0,1`）
- ext_v3 完成 → 启动 `mvp_uncurated`
- 三方法全完成 → 运行 `analyze_mvp.py`，按 PASS/FAIL gate 判断
- **如果 RankMe 在 4 代中下降 <5% 且 kNN 无变化** → 向 Director 报告：当前实验规模（977 seq/gen × 4 代）可能不足以诱导可测量的表征退化，考虑增加 gen_tokens 或 num_generations

### 5. 🎯 战略上下文
- 核心科学问题：model-internal 表征在迭代崩塌中的 "window of advantage" 是否存在
- PASS 标准：(a) RankMe 4 代近似单调下降 AND (b) RGDS PPL 相对 external_only ≥5%
- **最容易判断错的事**：Gen 0-2 数据显示 RankMe 仅下降 1.7%、kNN 完全不变（0.991）。这看起来像 PASS(a) 要 FAIL，但**不要过早下结论**——还缺 gen 3 数据和 external_only/uncurated 对照。先完成所有三方法的 4 代实验再判
- **负 rank correlation（~-0.38）是意外发现**：内部和 Contriever 多样性评分反相关。这意味着两种嵌入空间对"多样性"的定义截然不同，可能是论文的一个有价值的分析点，但也可能意味着 RGDS 和 external_only 选出的数据差异很大——需要在结果分析中特别关注
- 决策链：D001（MVP 方案）→ D002（删除 SOFT PASS + ≥5% 阈值）
- 磁盘问题是 AutoDL 类环境典型坑：30GB 根分区装不下多代 checkpoint


---
