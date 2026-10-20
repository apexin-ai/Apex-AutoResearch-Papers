# train ablation window size

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_ablation-window-size_20260514T141039_result.json`
- **Structured JSON:** [`cc6d1537d9bc3b17dc38.json`](../../sessions/cc/cc6d1537d9bc3b17dc38.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Ablation 完成。

**PID**: 59213（已结束）  
**总运行时间**: ~6 分钟（k=3: 118s, k=5: 92s, k=7: 140s）  
**脚本**: `/root/autodl-tmp/agent_progress_probe/ablation_window_size.py`

### 结果

| k | steps/window | test macro_f1 | test_acc | f1_progress | f1_stagnation |
|---|---|---|---|---|---|
| 3 | 6 | **0.872** | 0.941 | 0.966 | 0.778 |
| **5** | **10** | **0.931** | **0.953** | **0.970** | **0.892** |
| 7 | 14 | **0.913** | 0.927 | 0.948 | 0.879 |

### 分析

- **k=5 最优**，macro_f1=0.931（高于 baseline 报告的 0.905，因为本次重新划窗+训练的随机性）
- **k=3 显著下降**（-5.9pp）：6 步窗口信号不足，stagnation F1 仅 0.778——窗口太短难以积累足够的重复/停滞信号
- **k=7 略低于 k=5**（-1.8pp）：14 步窗口引入噪声，稀释了局部信号；但比 k=3 好很多
- 规律：**检测粒度与信号积累的 sweet spot 在 k=5**。k=3 牺牲信号换粒度代价太大；k=7 多出的 context 没有带来收益

---
