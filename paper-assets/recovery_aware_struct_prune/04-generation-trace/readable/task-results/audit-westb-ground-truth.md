# audit westb ground truth

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_westb-ground-truth_20260517T104022_result.json`
- **Structured JSON:** [`03111feb45aa42d1c32d.json`](../../sessions/03/03111feb45aa42d1c32d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westb-23072 状态审计报告

---

### 1. 磁盘清理

| 项目 | 状态 |
|------|------|
| checkpoint-935 | **DELETED** |
| checkpoint-1870 | **DELETED** |
| model.safetensors | 存在，12G |
| /root/autodl-tmp | **162G/250G (65%)，89G 可用** |

---

### 2. Random eval (PID 696141)

**状态: ALIVE，运行 1h45m，约 85% 完成 (171/200)**

- 命令: `eval_gsm8k.py --model_path pruned_random_20 --max_samples 200`
- GPU 1，占用 12880MiB，76% 利用率
- 最近进度点 (150/200): **acc=0.3400, eos_rate=45.33%, avg_len=2636**
- 速度极慢（~35-50s/it），因为 eos_rate 低、生成长度大（平均 2636 tokens，频繁 truncate 到 max_length）
- 结果 JSON **尚未生成**，预计 ~15-20 分钟完成
- `random_cka_ablation_log.txt` 存在于 autodl-tmp/results/，记录了 random pruning 过程（20.04% sparsity, 210 MLP groups pruned, 0 attn groups）

---

### 3. Gradient post-SFT eval

**状态: 已完成**

| 项目 | 值 |
|------|-----|
| tmux sessions | V1 GONE, V2 GONE |
| V1 结果 | **GSM8K acc = 0.6150 ± 0.0344 (123/200)** |
| eos_rate | 99.50% |
| avg_len | 167 |
| 结果文件 | `eval_gradient_postsft.json` (May 17 18:23, 153KB) |
| 退出码 | 129 (SIGHUP, session 关闭导致) |
| V2 session | 失败，`python: command not found` |

---

### 4. GPU + 进程状态

**GPU:**
| GPU | 状态 | 显存 | 利用率 |
|-----|------|------|--------|
| 0 | **空闲** | 0MiB / 97887MiB | 0% |
| 1 | random eval | 12889MiB / 97887MiB | 76% |

**tmux sessions:**
- `scoring_ablation_random` (created 16:54) — 正在运行 random eval
- `scoring_ablation_v2` (created 15:37) — 可能已完成

**Python 进程:**
- PID 696141 — random eval (活跃，110% CPU)
- PID 680597 — eval_unstructured_20 tmux (0% CPU，已完成)
- jupyter-lab, tensorboard, http.server (常驻)

---

### 5. 最新结果文件 (autodl-tmp/results/, top 10)

| 文件 | 时间 | 说明 |
|------|------|------|
| random_cka_ablation_log.txt | 18:40 | random pruning 日志 |
| eval_gradient_postsft.json | 18:23 | **gradient SFT 后 eval, acc=0.615** |
| eval_gradient_sft.log | 18:14 | python not found 错误 |
| ablation_log.txt | 17:07 | ablation 日志 |
| eval_unstructured_20_n1319.json | 16:48 | unstructured eval 完成 |
| eval_postprune_gradient_20.json | 16:48 | gradient 剪枝后 eval |
| eval_sft_standard_20_seed456.json | 15:47 | |
| eval_sft_rasp_20_seed456.json | 15:28 | |
| eval_sft_standard_20_seed123.json | 14:40 | |
| eval_sft_rasp_20_seed123.json | 14:02 | |

---

### 关键要点

1. **GPU 0 空闲**，可立即调度新任务
2. **Random eval 即将完成**（~85%），但中间指标很差：acc=34%, eos_rate=45%（对比 gradient postsft acc=61.5%, eos_rate=99.5%）
3. **Gradient postsft eval 已落盘**，acc=0.615，可直接使用
4. V2 eval session 因 `python: command not found` 失败（可能缺少 conda activate）

---
