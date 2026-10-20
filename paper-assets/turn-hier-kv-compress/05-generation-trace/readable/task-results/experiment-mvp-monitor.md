# experiment mvp monitor

**turn hier kv compress** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_mvp_monitor_20260513T104850_result.json`
- **Structured JSON:** [`110eea580fea13d5e659.json`](../../sessions/11/110eea580fea13d5e659.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇报

### GPU 状态
| GPU | 型号 | 显存占用 | 利用率 | 进程 |
|-----|------|---------|--------|------|
| 0 | RTX PRO 6000 Blackwell (98GB) | 17.3GB | 90% | evaluate.py (CR70) |
| 1 | RTX PRO 6000 Blackwell (98GB) | 16.9GB | 80% | evaluate.py (CR85) |

### 实验进度
- **两个 tmux session 均在运行**：`mvp_eval_01_cr70`、`mvp_eval_01_cr85`
- **CR70**: 进度 **90% (9/10 traces)**，~14.71s/trace，即将完成
- **CR85**: 日志大小 55KB（CR70 为 59KB），进度接近，但日志尾部未显示进度条
- **结果文件**：目录下只有 `log_cr70.txt` 和 `log_cr85.txt`，**尚无 summary JSON 或 CSV** → 两个实验均未完成

### Traces 数据
- 总计 **10 条** trace（6 standard + 4 adversarial）
- 共 **80 个** planted info

### evaluate.py 检查
- 模型加载用 **bfloat16** ✓
- 使用 **TurnKVPress** from `turnkv.press` ✓
- `make_press` / `apply_press` 上下文管理器模式 ✓
- 支持 `--max_traces` 参数 ✓
- 代码结构正确

### 预估
CR70 还剩 1 条 trace（~15s），预计 **1 分钟内完成**。CR85 进度相近，两个实验应在几分钟内全部结束。

---
