# audit roberta large seed check

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_roberta-large-seed-check_20260523T194133_result.json`
- **Structured JSON:** [`967df077622c147301e2.json`](../../sessions/96/967df077622c147301e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告：RoBERTa-large 多 seed checkpoint 验证

### 1. 结果文件（3 个 JSON，均含完整 3-seed 数据）

| 文件 | 变体 | Seeds | 内容 |
|------|------|-------|------|
| `exp15_roberta_large.json` | vanilla + 9class | 42, 123, 456 | DD/AA OOD 的 per-seed F1 + mean±std (k1~full) |
| `exp15b_roberta_large_lr1e5.json` | 9class (LR=1e-5) | 42, 123, 456 | DD/AA OOD 的 per-seed F1 + mean±std |
| `exp15c_roberta_large_mlm.json` | MLM | 42, 123, 456 | DD/AA OOD 的 per-seed F1 + mean±std |

### 2. 训练日志确认

`exp15b_roberta_large_lr1e5.log` 明确记录了 3 个 seed 的完整训练过程：
- seed=42: 5 epochs DAPT + 20 epochs GRU → DD full=0.9085, AA full=0.7350
- seed=123: 5 epochs DAPT + 20 epochs GRU → DD full=0.9439, AA full=0.7512
- seed=456: 5 epochs DAPT + 20 epochs GRU → DD full=0.9904, AA full=0.8575

### 3. Checkpoint 状态

**无 RoBERTa-large checkpoint 文件存留。** `checkpoints/` 目录下没有任何 roberta-large 相关的 `.pt` 文件或子目录。checkpoint 应该是评估完成后被清理了。现存的 checkpoint 目录（exp26, exp36, exp59 等）属于其他实验。

### 4. RoBERTa-base 对比

服务器上**未找到任何 RoBERTa-base 专属结果文件或目录**。`round7_seed_level_stats.json` 中的变体（9-class, Binary, Scrambled, MLM+cls, Topic, Vanilla）均为 RoBERTa-base 模型的不同配置，全部有 3 seed (42/123/456) 数据。

### 5. 具体数值（exp15_roberta_large.json, vanilla 变体, full-turn F1）

| Seed | DD OOD | ActorAttack |
|------|--------|-------------|
| 42 | 0.8827 | 1.0000 |
| 123 | 0.9715 | 1.0000 |
| 456 | 0.9261 | 1.0000 |
| **mean±std** | **0.927±0.036** | **1.000±0.000** |

### 结论

**Table 4 的 "3-seed mean±std" 声称有完整数据支撑。** 三个结果 JSON 文件均包含 seeds 42/123/456 的独立评估值和 mean±std 统计量，训练日志确认了 3 个 seed 的完整训练流程。唯一缺失的是 checkpoint 文件本身（已被清理），但评估结果完整保留。registry 只记录单 seed 值是 registry 记录不全的问题，不影响实验数据的完整性。

---
