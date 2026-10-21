# ops server backup cqa1

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_server-backup-cqa1_20260523T194920_result.json`
- **Structured JSON:** [`1eddce6fc67656c26a73.json`](../../sessions/1e/1eddce6fc67656c26a73.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

备份完成。汇总如下：

## 备份结果

### 已备份（3 个包，总计 7.8G）

| 包 | 大小 | 内容 |
|---|---|---|
| `backup_p1_code_and_results.tar.gz` | 23M | 项目代码仓库（84M 未压缩，含 exp001-exp008、analysis、figures、stan_models、scripts、results、results_mmlu_s42、logs）+ wandb runs (58M) |
| `backup_p2_experiment_data.tar.gz` | 1.9G | SFT 训练数据 (572M)、QC 过滤数据 (360M)、eval 结果 (361M)、detection signals exp002 (755M)、RRF 分析 exp003 (250M)、IRT MCMC traces exp006 (3.3G)、exp009 signals+eval (107M)、exp015 SFT data (92M) |
| `backup_p3_lora_adapters.tar.gz` | 5.9G | 52 个 LoRA adapter 权重（仅 final，排除 checkpoint-* 中间检查点）覆盖：Qwen2.5-0.5B/1.5B/3B/7B/14B、Llama-3.2-3B、gemma-2-9b、Falcon3-7B-Base，多 dosage (d000-d100)、多 seed (s0/s42/s123) |

**本地路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/server_backup_cqa1/`

### 跳过的内容

| 内容 | 大小 | 原因 |
|---|---|---|
| Base models (Qwen2.5-7B, gemma-2-9b 等) | 78G | 可从 HuggingFace/ModelScope 重新下载 |
| HF cache (.hf_cache, .hf_cache_system) | 38G | 缓存，可重建 |
| miniconda3 | 14G | 环境，可重装 |
| cmdstan / tmp_cmdstan | 2.7G | 可重装 |
| nltk_data | 64M | 可重新下载 |
| LoRA 中间 checkpoint | ~10G | 仅保留 final adapter |

### 服务器上其他独占数据（需关注）

| 目录 | 大小 | 说明 |
|---|---|---|
| **`/root/democalib/`** | **3.1G** | **非 git 仓库**，含 DPO 实验代码和输出（dpo_dryrun_output 2.5G、3 个 dpo_output 各 173M、results 97M）。如果是活跃项目需要单独备份 |
| `/root/structfuse-context/` | 35M | 非 git 仓库，另一个项目 |
| `/root/structfuse-mvp/` | 60K | 非 git 仓库，另一个项目 |
| `/root/tau-bench/` | 131M | 有 git remote (github sierra-research/tau-bench)，本地修改可能丢失 |
| `/root/runs/` (非 contamcal) | 8M | 其他项目的 wandb runs |

**democalib 是最大风险** — 3.1G 数据，无版本控制，释放后不可恢复。建议确认是否需要备份。

---
