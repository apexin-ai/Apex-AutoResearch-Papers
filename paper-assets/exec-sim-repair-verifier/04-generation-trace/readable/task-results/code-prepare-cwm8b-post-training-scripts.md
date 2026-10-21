# code prepare cwm8b post training scripts

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare-cwm8b-post-training-scripts_20260515T194627_result.json`
- **Structured JSON:** [`253c08f35c24ad389afe.json`](../../sessions/25/253c08f35c24ad389afe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本已部署，语法验证通过。

## 产出摘要

| 脚本 | 路径 | 功能 |
|------|------|------|
| `cwm8b_val_sweep.sh` | `/root/autodl-tmp/scripts/cwm8b_val_sweep.sh` | 自动检测所有 checkpoint，3 GPU 并行跑 val eval (bs=8) |
| `cwm8b_final_test_eval.sh` | `/root/autodl-tmp/scripts/cwm8b_final_test_eval.sh` | 自动找最高 step checkpoint，跑 test eval (bs=8) |

**脚本特性**:
- 自动检测 checkpoint（无需硬编码 step 列表）
- val sweep 用 cuda:0,1,2 并行，GPU 3 留给正在跑的 ckpt-400 test eval
- final test eval 默认 cuda:0，可传参覆盖：`bash cwm8b_final_test_eval.sh cuda:1`
- 错误处理：checkpoint 不存在跳过，单个失败不阻塞其他
- 进度日志：每个 checkpoint 有独立 log 文件

**预计运行时间**（假设 bs=8 提速 ~4-6x）:
- Val sweep: 5 checkpoints × ~6h/ckpt ÷ 3 GPU 并行 ≈ **10-12h**
- Final test eval: 9784 samples × ~3s/sample ≈ **8h**

**启动方式**（训练完成后）:
```bash
# 先启 val sweep（后台）
nohup bash /root/autodl-tmp/scripts/cwm8b_val_sweep.sh > /root/autodl-tmp/eval_results/cwm8b_val_sweep.log 2>&1 &

# 同时启 final test eval on GPU 3（如果 ckpt-400 test 已完成）
nohup bash /root/autodl-tmp/scripts/cwm8b_final_test_eval.sh cuda:3 > /root/autodl-tmp/eval_results/cwm8b_final_test.log 2>&1 &
```

---
