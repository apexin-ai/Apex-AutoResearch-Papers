# ssh d046 home cls v5 prep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d046-home-cls-v5-prep_20260513T072211_result.json`
- **Structured JSON:** [`692a107f619a156982ae.json`](../../sessions/69/692a107f619a156982ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## Step 4: 汇报

### 1. seed123 进程
全部已 kill（PID 2940520/2940525 及所有子进程），无残留。

### 2. GPU 状态
RTX 5090 完全空闲：**0% util, 0 MiB / 32607 MiB**

### 3. 超参修改对比

| 参数 | 修改前 | 修改后 |
|------|--------|--------|
| `learning_rate` (--lr default) | 2e-4 | **5e-5** |
| `weight_decay` | 不存在 | **0.01**（新增） |
| `warmup_ratio` | 0.1 | **0.05** |
| `save_total_limit` | 3 | **5** |

其余参数不变：`num_train_epochs=3, save_steps=200, eval_steps=200, batch_size=2, grad_accumulation=16, lora_rank=16, lora_alpha=32`

### 4. Dry-run 结果
通过，无报错。5 steps 训练日志：

| Step | Loss | LR | Grad Norm |
|------|------|----|-----------|
| 1 | 100.5 | 0.0 | 658.3 |
| 2 | 129.1 | 5e-05 | 775.4 |
| 3 | 64.9 | 3.75e-05 | 467.9 |
| 4 | 122.1 | 2.5e-05 | 916.8 |
| 5 | 88.2 | 1.25e-05 | 631.1 |

- learning_rate 确认为 **5e-05**（step 2 达到峰值后 cosine decay）
- train_loss 平均 101.0，train_runtime 32.6s（~6.5s/step）
- `warmup_ratio` 已生效（注意 transformers 提示 warmup_ratio deprecated，建议改用 warmup_steps，但不影响功能）

### 5. 推荐 CLS v5 启动命令

```bash
cd /home/sonny/exec-sim-repair-verifier && source /home/sonny/miniconda3/etc/profile.d/conda.sh && conda activate base && nohup python3 train_repo_verifier.py \
  --output_dir /home/sonny/exec-sim-repair-verifier/checkpoints_repo_cls_v5/ \
  --seed 42 \
  --run_name repo-cls-qwen3-4b-lora-v5 \
  > /tmp/cls_v5_stdout.log 2>&1 & echo "CLS_V5_PID=$!"
```

（默认开启 wandb，3 epochs，其余超参使用脚本中已修改的新默认值）

---
