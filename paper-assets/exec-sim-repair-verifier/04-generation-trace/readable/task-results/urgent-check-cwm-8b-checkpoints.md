# urgent check cwm 8b checkpoints

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_check-cwm-8b-checkpoints_20260514T140908_result.json`
- **Structured JSON:** [`2b07e2051dfdb2cda1ca.json`](../../sessions/2b/2b07e2051dfdb2cda1ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## CWM 8B Checkpoint 状况汇报

### Checkpoint 保留

| 位置 | 内容 |
|------|------|
| **主目录** (`checkpoints_repo_cwm_8b_conda`) | checkpoint-400, 900, 1000, 1100, 1200 （共 5 个，满 save_total_limit） |
| **备份目录** (`checkpoints_backup_cwm_8b`) | checkpoint-300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200 （共 10 个） |

### 配置

- `save_steps=100`（默认值），`save_total_limit=5`

### 关键结论

1. **备份脚本运行正常** — 300~1200 的 checkpoint 全部备份，不存在 CLS 8B s123 那样的丢失问题
2. **checkpoint-100、200 两处都没有** — 可能在备份脚本启动前就已被淘汰，或训练从其他 step 开始
3. **checkpoint-400 安全** — 主目录和备份目录都有
4. **无需紧急备份操作**

### ⚠️ 新问题：训练已崩溃

日志显示训练进程报 `ValueError` 退出：

```
ValueError: type of {'input_ids': [...]} unknown: &lt;class 'dict'>. 
Should be one of a python, numpy, or pytorch object.
```

进度条显示 `0%| | 0/6633`，说明在尝试恢复训练时 DataLoader 崩溃。训练当前**没有在运行**，停在 step 1200。这是 data collator 处理样本时的类型错误，可能是某条数据格式异常。

### 需要决策

- 训练崩溃需要排查修复后重启（从 checkpoint-1200 resume）
- checkpoint 备份情况良好，不需要类似 CLS 8B s123 的恢复训练

---
