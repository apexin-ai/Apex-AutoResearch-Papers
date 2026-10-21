# code dual server gpu audit

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_dual-server-gpu-audit_20260521T105712_result.json`
- **Structured JSON:** [`13834ead42a68829a2f1.json`](../../sessions/13/13834ead42a68829a2f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有已定义任务均已完成。以下是完整报告：

---

## GPU 状态报告

### westd-35694 (4 GPU)

| GPU | 任务 | PID | 进度 | 预计完成 |
|-----|------|-----|------|---------|
| 0 | **空闲** | - | contam_50 train+eval 已完成 | - |
| 1 | **空闲** | - | clean_s2 train+eval 已完成 | - |
| 2 | GRPO run2 | 97791 | 2529/14042 (18%) | ~17h (~明天 12:00) |
| 3 | **空闲** | - | contam_15 train+eval 已完成 | - |

### westd-19912 (4 GPU)

| GPU | 任务 | PID | 进度 | 预计完成 |
|-----|------|-----|------|---------|
| 0-3 | **全部空闲** | - | ARC-C 4 条件 train+eval 全部完成 | - |

---

## 关键结果

### GRPO (step 2529/14042, 18%)
- reward: 0.85, entropy: 0.859, lr: 4.14e-06
- ~5.3s/step，预计还需 ~17h

### s10 eval (已完成)
- accuracy: **0.676**, lz*: **8.149**, theta: -0.116
- 全部 14042 items 均为 unseen

### MIA SFT AUC
- **best: 0.611** (min_k_10)
- loss AUC: 0.592, min_k_pp_10: 0.569

### ARC-C 各条件结果（19912 训练）

| Condition | Acc Overall | Acc Seen | Acc Unseen | lz* | lz* Seen | lz* Unseen |
|-----------|------------|----------|------------|-----|----------|------------|
| clean_s1 | 0.902 | - | 0.902 | -5.448 | - | -5.448 |
| clean_s2 | 0.895 | - | 0.895 | -5.433 | - | -5.433 |
| contam_15 | 0.909 | 0.909 | 0.908 | -4.917 | **+0.568** | -5.414 |
| contam_50 | **0.942** | **0.966** | 0.919 | -4.573 | **-0.331** | -3.902 |

### ARC-C 各条件结果（35694 训练，独立 seed）

| Condition | Acc Overall | Acc Seen | Acc Unseen | lz* | lz* Seen | lz* Unseen |
|-----------|------------|----------|------------|-----|----------|------------|
| clean_s1 | 0.895 | - | 0.895 | -5.511 | - | -5.511 |
| clean_s2 | 0.898 | - | 0.898 | -5.493 | - | -5.493 |
| contam_15 | 0.909 | 0.886 | 0.912 | -5.032 | **+0.186** | -5.464 |
| contam_50 | **0.946** | **0.966** | 0.926 | -4.185 | **-0.475** | -4.316 |

---

## 已启动新任务

1. **35694 GPU 0**: ARC-C contam_50 训练 → eval（已完成）
2. **35694 GPU 1**: ARC-C clean_s2 eval（已完成）
3. **35694 GPU 3**: ARC-C contam_15 eval（已完成）
4. **19912 GPU 0-3**: ARC-C 4 条件 eval 全部（已完成）
5. 修复了 19912 缺失的 IRT params 文件和过期的 eval_lz.py

---

## 当前瓶颈

**7/8 GPU 空闲** — 所有已定义任务（ARC-C 4 条件 x2 服务器、Llama 5 条件、Mistral 3 条件）均已完成训练和 eval。仅 GRPO 在跑。如需填满 GPU，需要：
- 扩展 ARC-C seed 数 (clean_s3-s10，data 需先用 prepare_arcc_data.py 生成)
- 或部署新的实验方向

---
