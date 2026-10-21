# code extra seeds prep

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_extra-seeds-prep_20260516T021842_result.json`
- **Structured JSON:** [`d00296b339ef5949d792.json`](../../sessions/d0/d00296b339ef5949d792.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 产出汇总

### Config 文件内容

| Config | reward_mode | beta (默认) | 其他关键参数 |
|--------|-------------|-------------|-------------|
| `grpo_exec_only.yaml` | execution_only | — | exec_weight=1.0, sta_weight=0.0 |
| `grpo_additive_bonus.yaml` | additive_bonus | 0.3 | CLI `--beta 0.1` 覆盖 |
| `grpo_additive_random_b01.yaml` | additive_random | 0.1 | 已是 0.1 |

三个 config 共享：model=Qwen3-4B, batch=4, grad_accum=2, num_gen=8, max_len=512, lr=1e-6, solver=prover9。

### Launch 脚本

已创建：`/root/solver-trace-ablation/scripts/launch_extra_seeds.sh`

6 个命令全部注释状态，启动时取消对应注释并填入 GPU 编号。

### Seed 兼容性

- `--seed` 是纯 argparse int（train_grpo.py:376），直接传入 `TrainingArguments(seed=...)`（:467），无任何范围限制
- 数据文件路径由 `--data_path` 显式指定，不从 seed 派生 → seed=45/46 无需额外数据文件
- `save_total_limit=1` 已硬编码（:463），满足 C003

### 注意事项

1. **`grpo_additive_bonus.yaml` 中 beta 默认 0.3**，CLI `--beta 0.1` 会覆盖，已在脚本中显式指定
2. Random 条件使用 `grpo_additive_random_b01.yaml`（不是 `grpo_additive_random.yaml`，后者不存在）
3. 每次最多并行 2 个实验（2 GPU），6 个实验需分 3 批跑

---
