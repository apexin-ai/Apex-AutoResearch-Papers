# Label Statistics Report

## 1. 窗口总数

| 指标 | 值 |
|------|-----|
| 总窗口数 | 59,496 |
| 总轨迹数 | 5,000 |
| 短轨迹数 (<12 steps) | 228 |
| Resolved 轨迹窗口 | 5,248 |
| Unresolved 轨迹窗口 | 54,248 |

## 2. 每个 LF 的覆盖率

| LF | 非 Abstain 数 | 覆盖率 |
|-----|--------------|--------|
| file_diff_delta | 33,977 | 57.1% |
| command_repetition | 39,024 | 65.6% |
| outcome_backpropagation | 14,370 | 24.2% |

## 3. 每个 LF 的标签分布

### file_diff_delta

| 标签 | 数量 | 占比 |
|------|------|------|
| progress | 25,286 | 42.5% |
| stagnation | 8,691 | 14.6% |
| abstain | 25,519 | 42.9% |

### command_repetition

| 标签 | 数量 | 占比 |
|------|------|------|
| progress | 28,695 | 48.2% |
| stagnation | 10,329 | 17.4% |
| abstain | 20,472 | 34.4% |

### outcome_backpropagation

| 标签 | 数量 | 占比 |
|------|------|------|
| progress | 1,590 | 2.7% |
| stagnation | 12,780 | 21.5% |
| abstain | 45,126 | 75.8% |

## 4. LF 一致性

- ≥2 个 LF 都非 abstain 的窗口数：27,398
- 其中标签一致的窗口数：11,029
- **一致率：40.3%**

## 5. 多数投票标签分布（高置信度，confidence ≥ 2）

高置信度窗口总数：15,401

| 标签 | 数量 | 占比 |
|------|------|------|
| progress | 9,555 | 62.0% |
| stagnation | 5,846 | 38.0% |

## 6. 按 Resolved/Unresolved 分组的标签分布

### Resolved 轨迹

| Majority Label | 数量 | 占比 |
|----------------|------|------|
| progress | 4,456 | 84.9% |
| stagnation | 499 | 9.5% |
| abstain | 293 | 5.6% |

### Unresolved 轨迹

| Majority Label | 数量 | 占比 |
|----------------|------|------|
| progress | 34,753 | 64.1% |
| stagnation | 15,101 | 27.8% |
| abstain | 4,394 | 8.1% |

## 7. 类别平衡评估

- Progress (高置信): 9,555
- Stagnation (高置信): 5,846
- 比例 (多/少): 1.6:1

**中度不平衡。** 建议使用 class weights 或在评估时关注 F1 而非 accuracy。
