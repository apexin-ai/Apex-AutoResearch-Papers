# code c5b retry prep

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_c5b_retry_prep_20260514T185112_result.json`
- **Structured JSON:** [`03e259d94bd70c389987.json`](../../sessions/03/03e259d94bd70c389987.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

## 验证结果

| 项目 | 状态 |
|------|------|
| CVD 修复 `run_c5b_pilot.py:580-581` | `if "CUDA_VISIBLE_DEVICES" not in os.environ` 保护已生效 |
| CVD 修复 `run_mitigation_pilot.py:572-573` | 同上，已生效 |
| s025 数据 | 已有完整结果（30 problems, strategy=all），无需重跑 |
| 模型路径 `/root/autodl-tmp/pacs/checkpoints/DeepSeek-R1-Distill-Qwen-7B` | 存在 |
| 数据路径 `/root/autodl-tmp/pacs/data/math500.json` | 存在 (458KB) |

## 重试脚本 `/root/autodl-tmp/pacs/run_c5b_retry.sh`

相对原始方案的改进：
- **不指定 `--output_dir`**，让脚本自动生成 `profiling_output_c5b_all_s030`，避免路径冲突和结果覆盖
- **自动跳过已有结果的 sparsity**（s025 会被 skip）
- **默认只跑 s030**（s025 已完成）
- screen 启动防 SIGHUP、sentinel 文件、完整日志

## 启动命令

```bash
# 只跑 s030（推荐，s025 已完成）
screen -dmS c5b bash /root/autodl-tmp/pacs/run_c5b_retry.sh 0

# 强制跑两个（s025 会被自动 skip 因为结果已存在）
screen -dmS c5b bash /root/autodl-tmp/pacs/run_c5b_retry.sh 0 "0.25 0.30"
```

**预估**：单个 sparsity (s030) 30 problems × ~2048 tokens，7B 模型单 GPU，约 30-60 分钟。需要 1 张 GPU。

---
