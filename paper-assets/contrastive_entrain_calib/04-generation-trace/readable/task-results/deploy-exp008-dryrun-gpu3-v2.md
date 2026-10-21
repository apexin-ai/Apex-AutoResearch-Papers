# deploy exp008 dryrun gpu3 v2

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_exp008-dryrun-gpu3-v2_20260518T173454_result.json`
- **Structured JSON:** [`2f25c65fbeca1bf74ae0.json`](../../sessions/2f/2f25c65fbeca1bf74ae0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Dry-run 失败：数据格式不匹配。**

数据是 3-turn 对话（user → assistant → user），最后一轮是 user。但脚本 `CalibrationSFTDataset` 要求最后一轮是 assistant（作为 SFT target）：

```python
# line 153
if not turns or turns[-1]["role"] != "assistant":
    continue  # ← 所有 362 条全被跳过
```

实际数据结构：
1. user: 提问
2. assistant: 给出错误答案
3. user: correction/pressure

缺少第 4 轮 assistant response 作为 SFT 训练目标，导致 0 样本加载。

需要决定：是修改脚本适配 3-turn 数据（比如用第 2 轮 assistant 作为 target），还是需要先生成第 4 轮 assistant response 再训练？

---
