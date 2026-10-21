# code post grpo pipeline verify

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_post-grpo-pipeline-verify_20260515T050733_result.json`
- **Structured JSON:** [`fc395e311e4b6ca534b4.json`](../../sessions/fc/fc395e311e4b6ca534b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 管线就绪验证报告

### 1. Full GSM8K eval (`scripts/run_full_eval.sh`)

**覆盖 7 个 checkpoint** ✓ — baseline, pruned_rasp_20, pruned_standard_20, sft_rasp_20, sft_standard_20, grpo_rasp_20, grpo_standard_20

**🔴 GRPO 路径错误** — 脚本指向旧路径（无 v2 后缀），而实际训练输出目录是 v2：

| 脚本中的路径 | 应改为 |
|---|---|
| `grpo_stage2_rasp_20` | `grpo_stage2_rasp_20_v2` |
| `grpo_stage2_standard_20` | `grpo_stage2_standard_20_v2` |

旧目录（无 v2）存在但大小为 0，v2 目录才有实际内容。

---

### 2. α ablation (`scripts/run_alpha_ablation_v3.sh`)

- α 值 {0.0, 0.25, 0.5, 1.0, 2.0} ✓
- α=1.0 复用 `/root/autodl-tmp/pruned_rasp_20` ✓
- 磁盘清理逻辑：每个 α 值 prune → eval → `rm -rf` ✓
- 有 `--dry-run` 预检模式 ✓
- **就绪** ✓

---

### 3. GRASPrune (`scripts/run_graspune.sh`)

- 脚本存在 ✓
- `/root/GRASPrune/` 目录存在 ✓
- 配置正确：keep_ratio=0.80（即 20% sparsity），device=cuda:0，model=DeepSeek-R1-Distill-Qwen-7B ✓
- **就绪** ✓

---

### 4. 磁盘空间

```
/root/autodl-tmp/  250GB total, 222GB used, 29GB free (89%)
```

各目录占用：
| 目录 | 大小 |
|---|---|
| sft_rasp_20 | **81GB** |
| sft_standard_20 | **81GB** |
| grpo_stage2_rasp_20_v2 | ~20K（训练中，未保存 checkpoint） |
| grpo_stage2_standard_20_v2 | ~16K（训练中，未保存 checkpoint） |
| logs | 17MB |
| 旧 grpo 目录（无 v2）×2 | 0 |

**🟡 空间风险**：GRPO 完成后会写入 2 个模型 checkpoint（估计各 ~12GB），剩余空间降至 ~5GB。α ablation 每轮需要 ~12GB 临时空间（虽然有 prune→eval→delete 循环），**不够**。

**建议**：GRPO 完成 + Full eval 跑完后，清理 SFT checkpoint（162GB）释放空间。或者先跑 α ablation 再跑 GRPO full eval。

---

### 5. GRPO 训练进度

- **rasp_20_v2**：5% (12/250 steps)，已跑 ~1h27m，每步 ~7.3min，**预计还需 ~29h**
- **standard_20_v2**：日志 1389 行，进度类似（晚启动 ~12min），输出目录时间戳接近

---

### 需修复问题清单

| # | 严重度 | 问题 | 修复 |
|---|---|---|---|
| 1 | 🔴 必须修 | `run_full_eval.sh` GRPO 路径缺少 `_v2` 后缀 | 将 `grpo_stage2_rasp_20` → `grpo_stage2_rasp_20_v2`，`grpo_stage2_standard_20` → `grpo_stage2_standard_20_v2` |
| 2 | 🟡 需规划 | GRPO 完成后仅剩 ~5GB，不够跑 α ablation | GRPO eval 后清理 SFT 或旧 checkpoint |
| 3 | 🟢 可清理 | 旧 GRPO 目录（无 v2）占位但为空 | 可删除 `grpo_stage2_rasp_20/` 和 `grpo_stage2_standard_20/` |

---
