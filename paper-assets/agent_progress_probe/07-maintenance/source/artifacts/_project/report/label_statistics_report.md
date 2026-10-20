# Label Statistics Report

## 1. 窗口总数

| 指标 | 值 |
|------|-----|
| 总窗口数 | 12,331 |
| 总轨迹数 | 1,000 |
| 短轨迹数 (<12 steps) | 43 |
| Resolved 轨迹窗口 | 1,085 |
| Unresolved 轨迹窗口 | 11,246 |

## 2. 每个 LF 的覆盖率

| LF | 非 Abstain 数 | 覆盖率 |
|-----|--------------|--------|
| file_diff_delta | 10,193 | 82.7% |
| test_pass_rate_transition | 40 | 0.3% |
| outcome_backpropagation | 2,687 | 21.8% |

## 3. 每个 LF 的标签分布

### file_diff_delta

| 标签 | 数量 | 占比 |
|------|------|------|
| progress | 4,598 | 37.3% |
| stagnation | 5,595 | 45.4% |
| abstain | 2,138 | 17.3% |

### test_pass_rate_transition

| 标签 | 数量 | 占比 |
|------|------|------|
| progress | 4 | 0.0% |
| stagnation | 36 | 0.3% |
| abstain | 12,291 | 99.7% |

### outcome_backpropagation

| 标签 | 数量 | 占比 |
|------|------|------|
| progress | 333 | 2.7% |
| stagnation | 2,354 | 19.1% |
| abstain | 9,644 | 78.2% |

## 4. LF 一致性

- ≥2 个 LF 都非 abstain 的窗口数：1,864
- 其中标签一致的窗口数：1,094
- **一致率：58.7%**

## 5. 多数投票标签分布（高置信度，confidence ≥ 2）

高置信度窗口总数：1,102

| 标签 | 数量 | 占比 |
|------|------|------|
| progress | 98 | 8.9% |
| stagnation | 1,004 | 91.1% |

## 6. 按 Resolved/Unresolved 分组的标签分布

### Resolved 轨迹

| Majority Label | 数量 | 占比 |
|----------------|------|------|
| progress | 698 | 64.3% |
| stagnation | 192 | 17.7% |
| abstain | 195 | 18.0% |

### Unresolved 轨迹

| Majority Label | 数量 | 占比 |
|----------------|------|------|
| progress | 4,125 | 36.7% |
| stagnation | 6,031 | 53.6% |
| abstain | 1,090 | 9.7% |

## 7. 类别平衡评估

- Progress (高置信): 98
- Stagnation (高置信): 1,004
- 比例 (多/少): 10.2:1

**严重不平衡。** 建议：
1. 对少数类进行过采样 (SMOTE 或重复采样)
2. 使用 class weights 在训练时补偿
3. 考虑调整 LF 阈值以增加少数类覆盖
4. 使用 focal loss 代替 cross-entropy
