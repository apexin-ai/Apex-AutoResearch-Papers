# code qwen25 1 5b prep

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qwen25-1_5b-prep_20260517T124548_result.json`
- **Structured JSON:** [`3d901aea6c856f253b12.json`](../../sessions/3d/3d901aea6c856f253b12.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有验证通过。汇总报告：

---

## 结果报告

### 1. 代码修改

| 文件 | 改动 |
|------|------|
| `config.py` | 关键变量加 `os.environ.get()` 覆盖（BASE_MODEL, OUTPUT_DIR, K_CANDIDATES, GEN_BATCH_SIZE, BATCH_SIZE, GRAD_ACCUM, LR, EPOCHS, NUM_GENERATIONS, NUM_PROMPTS）。无环境变量时默认值不变，Qwen3 实验不受影响。 |
| `run_qwen25_experiment.py` | 新增。通用实验运行器，接受 `--condition` 和 `--condition_id` 参数。 |
| `run_qwen25_curated.sh` | 新增。C9 启动脚本，cuda:0，single_reward。 |
| `run_qwen25_random.sh` | 新增。C10 启动脚本，cuda:1，no_curation。 |

### 2. Qwen2.5 vs Qwen3 兼容性

| 项目 | 结果 |
|------|------|
| `enable_thinking=False` | Qwen2.5 chat template 中不存在此参数，但 Jinja 静默忽略，**无需改代码** |
| Chat template 格式 | Qwen2.5 使用 `<\|im_start\|>/<\|im_end\|>` 格式（ChatML），正常工作 |
| ArmoRM gating token | 已有 fallback（逐样本打分），实测分数正常 [0.07, 0.12] |
| pad_token | Qwen2.5 自带 `<\|endoftext\|>` 作为 pad_token，无需设置 |

### 3. Dry-run 结果

| 阶段 | Peak VRAM | 结论 |
|------|-----------|------|
| 生成 (batch=8, K=4) | 3.63 GB | 10.8s/batch，远低于 32GB 上限 |
| LoRA 训练 (bs=2, accum=8) | 6.15 GB | loss=1.87 正常，1.4s/step |
| ArmoRM 打分 (batch=4) | 14.10 GB | 分数范围合理，fallback 正常 |

Pipeline 各阶段串行执行，峰值 ~14 GB（ArmoRM 阶段），32GB GPU 完全足够。

### 4. 推荐超参数

| 参数 | 值 | 备注 |
|------|------|------|
| GEN_BATCH_SIZE | 8 | 生成峰值仅 3.6GB，可以提到 12-16，但 8 已足够快 |
| PER_DEVICE_BATCH | 2 | 训练峰值 6.15GB |
| GRAD_ACCUM | 8 | 有效 batch = 2×8 = 16 |
| LR | 2e-4 | 与 0.6B 实验一致 |
| EPOCHS | 2 | 与 0.6B 实验一致 |

### 5. 启动命令

```bash
# C9: curated, GPU 0
nohup bash /root/autodl-tmp/carr/run_qwen25_curated.sh > /root/autodl-tmp/carr/logs/c9_qwen25_curated.log 2>&1 &

# C10: random, GPU 1
nohup bash /root/autodl-tmp/carr/run_qwen25_random.sh > /root/autodl-tmp/carr/logs/c10_qwen25_random.log 2>&1 &
```

### 6. 注意事项

- `torch_dtype` 参数在 transformers 4.57.6 中已 deprecated，改用 `dtype`。当前只是 warning 不影响运行。若要消除可全局替换。
- 两个实验可同时启动在不同 GPU 上，互不干扰（ArmoRM 14GB + 生成模型 3.6GB < 32GB，但 scoring 阶段如果同时跑会占 2×14GB=28GB，仍在安全线内）。

---
