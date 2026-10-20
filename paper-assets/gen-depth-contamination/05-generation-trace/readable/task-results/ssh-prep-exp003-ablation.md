# ssh prep exp003 ablation

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_prep_exp003_ablation_20260513T023927_result.json`
- **Structured JSON:** [`b80cebb2deec87be3b60.json`](../../sessions/b8/b80cebb2deec87be3b60.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已修复。验证总结：

| 检查项 | 状态 |
|--------|------|
| 4 个 decoding config (greedy, p=0.9/T=1.0, p=0.95/T=0.7, p=0.95/T=1.2) | ✅ |
| 调用 run_pipeline.py + Qwen 模型 | ✅ |
| 模型路径指向实际 config.json 所在目录 | ✅ 已修复 |
| 输出到不同目录 | ✅ data_exp003_greedy / nuc09 / t07 / t12 |
| generation_mode=rewrite | ✅ 默认值 |
| 环境变量自包含 (network_turbo, HF_HOME, SSL) | ✅ |
| 磁盘空间 | ✅ 138GB 可用 |

## 提交命令

`submit_training_job` 的 `command` 字段：

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && for i in 1 2 3 4; do echo "=== Running config $i ===" && bash scripts/run_exp003_ablation.sh $i; done
```

参数：
- `server`: `autodl-4090d`
- `account`: `root`
- `command`: 如上
- `timeout`: `108000` (30h)
- `experiment_name`: `exp-003-decoding-ablation`

---
