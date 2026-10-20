# code probe 35694 collect

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_probe-35694-collect_20260521T143809_result.json`
- **Structured JSON:** [`c6719dafb5aba4f16acc.json`](../../sessions/c6/c6719dafb5aba4f16acc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 服务器状态报告 (westd-35694, 22:38 UTC)

### 1. GPU 利用率

| GPU | 型号 | VRAM | 利用率 | 任务 |
|-----|------|------|--------|------|
| 0 | RTX PRO 6000 Blackwell | 0 / 98 GB | **0%** | 空闲 |
| 1 | RTX PRO 6000 Blackwell | 10 / 98 GB | **89%** | Mistral clean_s8 训练 |
| 2 | RTX PRO 6000 Blackwell | 18 / 98 GB | **96%** | Mistral clean_s9 训练 + GRPO eval |
| 3 | RTX PRO 6000 Blackwell | 10 / 98 GB | **93%** | Mistral clean_s10 训练 |

### 2. Llama clean s8/s9/s10 eval 结果 (已全部完成)

| Seed | accuracy | lz_star | theta_mle | n_items |
|------|----------|---------|-----------|---------|
| **s8** | 0.5860 | **1.166** | -0.698 | 14042 |
| **s9** | 0.5922 | **0.190** | -0.659 | 14042 |
| **s10** | 0.5951 | **-2.250** | -0.621 | 14042 |

全部为 clean 条件 (n_seen=0)。lz_star 跨 seed 变异较大（-2.25 ~ 1.17）。

### 3. Mistral 训练状态

| Seed | GPU | 进度 | 速度 | ETA |
|------|-----|------|------|-----|
| clean_s8 | cuda:1 | **35%** (331/939) | ~1.1s/it | ~11 min |
| clean_s9 | cuda:2 | **21%** (199/939) | ~2.3s/it | ~28 min (与 GRPO eval 抢 GPU) |
| clean_s10 | cuda:3 | **41%** (385/939) | ~1.1s/it | ~10 min |

Loss 在 ~1.3 附近，epoch ~0.99（s8/s10）/ ~0.4（s9）。Checkpoint 目录已有 clean_s8/s9/s10 文件夹。Results 目录尚无 s8/s9/s10 结果（需训练完成后 eval）。

### 4. GRPO checkpoint-1000 eval

- **PID 153583 仍在运行**，刚完成模型加载 + LoRA merge，推理尚未开始
- 现有 `grpo_results.json` 和 `grpo_results_step500.json` **内容完全相同**（242301 bytes），疑似 bug：
  - accuracy_overall: 0.7144, lz_star: 7.770, theta_mle: 0.157
  - accuracy_seen: 0.730 (n=2106), accuracy_unseen: 0.712 (n=11936)
- 当前运行的 eval 应该会产出真正的 ckpt-1000 结果

### 5. 其他发现

- **GPU 0 完全空闲**，可立即分配新任务
- Mistral s9 因与 GRPO eval 共享 GPU 2，速度慢约 2 倍
- Mistral **s4-s7 未见训练任务或结果**（results 目录只有 clean/s2/s3/contam_15/contam_50）
- 有 monitor 进程（PID 156133）在等待 GRPO eval 完成后自动输出结果

---
