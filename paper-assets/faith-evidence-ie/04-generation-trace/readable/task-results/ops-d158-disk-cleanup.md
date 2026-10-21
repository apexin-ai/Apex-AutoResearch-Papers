# ops d158 disk cleanup

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d158_disk_cleanup_20260524T091538_result.json`
- **Structured JSON:** [`8395f9e29bd4da661ea0.json`](../../sessions/83/8395f9e29bd4da661ea0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕，汇总如下。

---

## 1. 磁盘空间总览

| 项目 | 值 |
|------|-----|
| 总容量 | 350G |
| 已用 | 286G (82%) |
| 可用 | 65G |
| 目标 | ≥100G free（需腾出 ≥35G） |

## 2. 可清理项列表

### Tier 1: Safe 删除（无争议，共 ~43.5G）

| # | 路径 | 大小 | 理由 | 风险 |
|---|------|------|------|------|
| 1 | `/root/autodl-tmp/models/Qwen/Qwen3-14B/Qwen3-14B/` | **28G** | 嵌套重复下载，父目录已有完整模型文件 | safe |
| 2 | `/root/autodl-tmp/dpo_output_rebuilt_3ep/` | **7.0G** | DPO 实验已弃用（conclusion=negative），被 RSFT 方法替代 | safe |
| 3 | `/root/autodl-tmp/dpo_output_rebuilt_1ep/` | **5.0G** | 同上（DPO 1ep，conclusion=negative） | safe |
| 4 | `/root/autodl-tmp/grpo_bf16_g4/` | **3.5G** | GRPO 实验已弃用，被 RSFT 方法替代 | safe |
| 5 | `/root/autodl-tmp/dpo_data_rebuilt/` | **15M** | DPO 训练数据，对应实验已弃用 | safe |
| 6 | `/root/autodl-tmp/rsft_filtered_topk3/` | 93M | k=3 旧数据，已被 k=1 替代 | safe |
| 7 | `/root/autodl-tmp/rsft_filtered_topk3_ced_filtered/` | 25M | 同上 | safe |
| 8 | `/root/autodl-tmp/rsft_filtered_topk3_random/` | 26M | 同上 | safe |
| 9 | `/root/autodl-tmp/eval_results/rsft_topk3*` (3 dirs) | ~30M | k=3 旧 eval 结果 | safe |
| 10 | `/root/autodl-tmp/analysis/error_analysis_plan006_k3/` | <1M | k=3 旧分析 | safe |
| 11 | 所有 `__pycache__` 目录 (12个) | ~10M | 编译缓存，自动重建 | safe |

### Tier 2: needs_confirmation（共 ~36G，如需要可进一步清理）

| # | 路径 | 大小 | 理由 | 风险 |
|---|------|------|------|------|
| 12 | `/root/autodl-tmp/rsft_output_nli_large/` | **8.0G** | NLI-large RSFT ablation 实验输出。如果论文不再需要 NLI-large ablation 可删 | needs_confirmation |
| 13 | `/root/autodl-tmp/sft_output_14b/` | **7.3G** | 原始 14B SFT (seed42, DeepSpeed 格式)。`sft_output_14b_s43` 已有替代 | needs_confirmation |
| 14 | `/root/autodl-tmp/rsft_output_4b_sft_s44_bf16/` | **7.5G** | 4B RSFT bf16 版本，与 rsft_output_4b_sft_s44 (4.1G) 可能重复 | needs_confirmation |
| 15 | `/root/autodl-tmp/sft_output/` (原始 4B) | **5.8G** | 原始 d076 4B SFT baseline (DeepSpeed 格式) | needs_confirmation |
| 16 | `/root/autodl-tmp/rsft_output_4b_sft_s44/` | **4.1G** | 4B RSFT 输出，如果已不再使用 4B 模型 | needs_confirmation |
| 17 | `/root/autodl-tmp/rsft_output_random_k1/` | **3.5G** | Random baseline，论文是否还需要此 ablation | needs_confirmation |

### Tier 3: 中间 checkpoint 清理（保留 final adapter，删除 optimizer.pt + 非最终 checkpoint）

每个 SFT/RSFT 目录中，final adapter 在根级别，中间 checkpoint 含 1-3GB 的 optimizer.pt。可逐目录清理，保守估计可回收 **~30-40G**。最大的几个：

| 目录 | 中间 ckpt 数 | 预估可回收 |
|------|------------|-----------|
| sft_output_14b (如保留) | 2 × 3.4G | 6.8G |
| sft_output (如保留) | 2 × 2.8G | 5.6G |
| rsft_output_nli_large (如保留) | 4 × 1.5G | 6.0G |
| rsft_output_ced_s42_v2 | 4 × ~1.5G | ~6G |
| rsft_output_ced_s43 | 同上 | ~6G |
| rsft_output_ced_s44 | 同上 | ~6G |
| rsft_output_4b_sft_s44 | 4 × 772M | 3.1G |
| 各 LLaMA/Qwen SFT/RSFT dirs | 2 ckpts each | 各 1-2G |

## 3. 预计可腾出空间

| 方案 | 腾出 | 达到 free |
|------|------|----------|
| 仅 Tier 1 | **~43.5G** | **~108.5G** ✅ 超过 100G 目标 |
| Tier 1 + Tier 2 | ~79.5G | ~144.5G |
| Tier 1 + Tier 2 + Tier 3 | ~110-120G | ~175-185G |

**仅执行 Tier 1 即可满足 100G 目标。** 其中 28G 来自重复的 Qwen3-14B 目录。

## 4. D158 进度

| 实验 | 进度 | ETA | 状态 |
|------|------|-----|------|
| **d158_14b_sft_s44** (PID 302391) | 48/144 steps (33%), epoch 1/3 | ~35 min | 运行中 ✅ |
| **d158_1_7b_rsft_s44_generate** (PID 302254) | 138/3027 docs (4.6%) | ~6.5 hours | 运行中 ✅ |

两个进程均存活（uptime ~24 min）。

1.7B generate 的 monitor 报告：format_ok_rate=100%, truncation_rate=19.2%（WARNING: >10%），mean_diversity=7.5/8。truncation 较高但 max_new_tokens 已设为 1024，这是 1.7B 模型的固有限制。

---
