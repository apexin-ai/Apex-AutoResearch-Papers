# code random s42 retrain script

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_random_s42_retrain_script_20260516T074833_result.json`
- **Structured JSON:** [`3a139c480bdfa01d0b9e.json`](../../sessions/3a/3a139c480bdfa01d0b9e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

**总结**：

| 项目 | 状态 |
|------|------|
| 脚本路径 | `/root/structfuse/scripts/run_random_s42_retrain.sh` |
| 语法检查 | PASS |
| 训练数据 | train: 11308 行 (1.1GB), val: 2980 行 (361MB) |
| 模型文件 | `/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B/config.json` 存在 |
| 输出目录 | `/root/autodl-tmp/structfuse/full_m2_qwen_outputs/random_s42_retrain/` 不存在（安全） |
| GPU | 2× RTX PRO 6000 Blackwell (96GB) |
| 预估时间 | ~45-90 分钟 (11308 样本 × 2 epochs ÷ batch 8 ≈ 2828 步, 单 Blackwell GPU) |

**提交命令**（训练时使用 GPU 0）：

```bash
nohup bash /root/structfuse/scripts/run_random_s42_retrain.sh 0 > /root/autodl-tmp/structfuse/full_m2_qwen_outputs/random_s42_retrain.log 2>&1 &
```

**关键配置对比**：

| 参数 | 原 s42 (错误) | 本次 retrain | s43/s44 (正确) |
|------|--------------|-------------|---------------|
| epochs | 3 | 2 | 2 |
| patience | 0 (无ES) | 2 | 2 |
| 其余参数 | batch=8, lr=2e-5, neg=7 | 相同 | 相同 |

训练代码自动保存 `best_by_val_loss` 和 `best_by_recall_at_1` 两个 checkpoint。无 `--dry-run` 或 `--max-steps` 参数可用于单步验证。

---
