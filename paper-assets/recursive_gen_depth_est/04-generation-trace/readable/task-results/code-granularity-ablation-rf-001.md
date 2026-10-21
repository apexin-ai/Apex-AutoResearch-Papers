# code granularity ablation rf 001

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_granularity_ablation_rf_001_20260515T091818_result.json`
- **Structured JSON:** [`bf015f676ac33561ebc3.json`](../../sessions/bf/bf015f676ac33561ebc3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。

**已完成**:
1. 定位全部 9 cells 特征文件 + 6-class 数据路径
2. 编写并部署 `src/granularity_ablation.py`（221 行），复用 19 特征 + 现有代码模式
3. Dry-run 通过（pythia_nucleus095，10.4s），结果验证了决策边界稀释效应：
   - Accuracy: binary 99.8% → 4-class 78.1% → 6-class 62.9%
   - d2v3 AUC: 3-class 0.796 → 6-class 0.689
4. Registry `granularity_ablation_rf_001` 已更新

**未执行**：完整 9-cell 实验，等待审批。运行命令：
```bash
python src/granularity_ablation.py
```

---
