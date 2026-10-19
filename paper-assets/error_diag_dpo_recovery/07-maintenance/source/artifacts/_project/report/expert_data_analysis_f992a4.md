# ALFWorld Expert Data (alfworld_sft.json) 分布分析报告

**日期**: 2026-05-12
**数据路径**: `/root/autodl-tmp/error_diag_dpo_recovery/eto_repo/data/alfworld_sft.json`
**目的**: 为 DPO pair 构建提供数据分布信息

---

## 1. 数据 Schema

每条数据结构：

```json
{
    "id": "alfworld_0",          // 格式: alfworld_{N}, N 从 0 到 3553（非连续，共 3119 个 unique ID）
    "game_file": "data/json_2.1.1/train/pick_and_place_simple-ToiletPaper-None-ToiletPaperHanger-406/trial_T20190908_122807_136741",
    "conversations": [
        {"from": "human", "value": "系统 prompt（task 说明 + action space）"},
        {"from": "gpt",   "value": "OK"},
        {"from": "human", "value": "环境描述 + task goal"},
        {"from": "gpt",   "value": "Thought: ... Action: ..."},
        // ... 交替进行
    ]
}
```

- **from**: `human`（环境观测）或 `gpt`（agent action）
- 第一轮 `gpt` 回复固定为 `"OK"`（确认 prompt）
- 所有数据来自 **train** split

## 2. Task Type 分布

| Task Type | 简称 | 数量 | 占比 |
|-----------|------|------|------|
| pick_and_place_simple | pick | 759 | 24.3% |
| pick_two_obj_and_place | puttwo | 662 | 21.2% |
| pick_clean_then_place_in_recep | clean | 576 | 18.5% |
| pick_cool_then_place_in_recep | cool | 472 | 15.1% |
| pick_heat_then_place_in_recep | heat | 371 | 11.9% |
| look_at_obj_in_light | examine | 279 | 8.9% |
| **总计** | | **3119** | **100%** |

分布不均匀：pick 最多（24.3%），examine 最少（8.9%），比值约 2.7:1。

## 3. 步数分布

### 3.1 总体

| 指标 | 值 |
|------|------|
| Mean | 9.8 |
| Median | 8.0 |
| Std | 7.2 |
| Min | 3 |
| Max | 49 |

### 3.2 按 Task Type

| Type | Count | Mean | Median | Std | Min | Max |
|------|-------|------|--------|-----|-----|-----|
| clean | 576 | 9.5 | 7.0 | 6.2 | 3 | 44 |
| cool | 472 | 9.3 | 8.0 | 4.7 | 4 | 41 |
| examine | 279 | 7.9 | 5.0 | 7.2 | 3 | 45 |
| heat | 371 | 9.7 | 8.0 | 5.9 | 6 | 48 |
| pick | 759 | 7.3 | 5.0 | 7.0 | 4 | 46 |
| puttwo | 662 | 14.2 | 11.0 | 8.5 | 6 | 49 |

- **puttwo** 步数最多（mean 14.2），因为需要找两个物体
- **pick** 和 **examine** 步数最少（mean 7.3/7.9），任务最简单

### 3.3 步数直方图

```
  1-  5:   712  ████████████████████████████████████
  6- 10:  1603  ████████████████████████████████████████████████████████████████████████████████
 11- 15:   392  ████████████████████
 16- 20:   144  ███████
 21- 30:   169  ████████
 31- 50:    99  █████
 51-100:     0
```

74.3% 的轨迹在 10 步以内完成。

## 4. 环境覆盖

| 指标 | 值 |
|------|------|
| Unique game_files | 3119（每条数据对应唯一 game_file）|
| Unique task configurations | 1395 |
| Unique scene IDs | 108 |

每个 game_file 出现最多 3 次（不同 trial），覆盖面广。

## 5. Task Goal 多样性

- **Unique goals**: 945 种
- 最高频 goal 也仅 25 条，数据多样性好

Top 5 goals:

| Count | Goal |
|-------|------|
| 25 | look at pillow under the desklamp |
| 25 | put some toiletpaper on toiletpaperhanger |
| 24 | put a hot mug in coffeemachine |
| 22 | heat some mug and put it in coffeemachine |
| 21 | examine the pillow with the desklamp |

## 6. 旧失败轨迹分析（受 boundary 污染，仅供参考）

### 6.1 残留数据

| 文件 | 条数 | 说明 |
|------|------|------|
| train_part0.jsonl | 61 | 全部失败 |
| train_part1.jsonl | 28 | 27 失败 + 1 成功 |
| classified_errors.jsonl | 88 | 错误分类结果 |

### 6.2 关键发现

- **game_file overlap = 0**: 旧轨迹的 game_file 与 expert 数据完全不重叠，来自不同 task instance
- **数量极少**：仅 88 条失败轨迹 vs. 3119 条 expert 数据
- **错误类型分布**：planning 79 (89.8%), action 5 (5.7%), verification 4 (4.5%)
- **结论**：这批旧数据不可用于 DPO 配对（boundary 污染 + 零 overlap）

## 7. DPO 配对可行性评估

### 7.1 Expert 数据覆盖评估

| 维度 | 评估 |
|------|------|
| Task type 覆盖 | ✅ 6 种类型全覆盖 |
| Goal 多样性 | ✅ 945 种 unique goals |
| Scene 覆盖 | ✅ 108 个 unique scenes |
| 每 task type 最少样本 | ⚠️ examine 仅 279 条（8.9%）|
| 步数分布 | ✅ 3-49 步，覆盖从简单到复杂 |

### 7.2 各 Task Type DPO 配对充足性

| Type | Expert 数量 | 充足性 | 说明 |
|------|------------|--------|------|
| pick | 759 | ✅ 充足 | 步数短，失败模式可能集中在目标定位 |
| puttwo | 662 | ✅ 充足 | 步数最长，失败率可能最高，DPO 收益大 |
| clean | 576 | ✅ 充足 | |
| cool | 472 | ✅ 充足 | |
| heat | 371 | ⚠️ 中等 | 数量较少 |
| examine | 279 | ⚠️ 偏少 | 最少，需确保失败轨迹收集覆盖 |

### 7.3 重新收集失败轨迹的建议

1. **优先级**: puttwo > clean > cool > heat > examine > pick
   - puttwo 步数最长（mean 14.2），失败概率最高，DPO 对比学习效果最明显
   - pick 虽然数量最多但步数短（mean 7.3），失败轨迹可能差异较小
   
2. **覆盖策略**: 
   - 用 expert 的 3119 个 game_file 作为任务池
   - 按 task type 分层采样，确保每种类型至少收集 100+ 失败轨迹
   - examine 类型样本少，需额外关注覆盖率

3. **配对粒度**:
   - 同 game_file 配对（chosen=expert, rejected=model failure）最严格
   - 同 task_config 配对（放松到同任务类型+同物体+同场景）可增加配对数
   - 建议优先尝试同 game_file 配对，不足时放松到同 task_config

4. **注意事项**:
   - 旧轨迹全部作废，必须重新收集
   - 新收集时确保 episode boundary 正确处理
   - 记录 game_file 以便精确配对
