# code prepare expert sft

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare-expert-sft_20260514T133359_result.json`
- **Structured JSON:** [`28c7db7c71aba70b2fef.json`](../../sessions/28/28c7db7c71aba70b2fef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。汇总报告：

---

## 状态汇总

### Expert Trajectory 收集
- **进度**：828/~3553 条，PID 340587 仍在运行
- **任务类型**：put (517), examine (302)。heat/cool/clean 类型尚未出现，等收集完应会覆盖
- **Token 长度**：median 605, p95 1647, max 2927。全部 < 4096

### 数据质量（dry-run 828 条）
- 接受 782，拒绝 27（全部因 >40 turns 被过滤）
- 轨迹长度：min 3 / median 7 / max 40, mean 10.2

### 代码清单（全部已在服务器上）

| 文件 | 用途 |
|------|------|
| `scripts/prepare_expert_sft_data.py` | 验证/过滤/train-val分割，支持 `--dry-run` |
| `scripts/sft_train.py` | TRL SFTTrainer，Qwen3-1.7B + 自定义 ChatML 模板 |
| `scripts/run_expert_sft.sh` | 一键流程：pre-flight → 数据准备 → 训练 |
| `scripts/eval_sft_model.py` | 评估脚本 |

### 与 exp008_sft 的配置差异

| 参数 | exp008_sft | Expert SFT |
|------|-----------|------------|
| 数据来源 | HF u-10bei 1200条 | PDDL expert ~3000+条 |
| max_seq_length | 4096 | 2048（数据更短，省显存） |
| learning_rate | 2e-5 | 5e-5（数据更干净） |
| output_dir | `/root/autodl-tmp/checkpoints/exp008_sft` | `/root/autodl-tmp/expert_sft/checkpoints` |

### 启动方式
```bash
# 等 exp015 结束 + 收集完成后：
bash scripts/run_expert_sft.sh

# 只看数据统计不训练：
bash scripts/run_expert_sft.sh --dry-run
```

---
