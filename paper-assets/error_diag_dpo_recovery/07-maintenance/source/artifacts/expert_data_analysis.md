# ETO Expert Trajectory Data Analysis

**文件**: `eto_repo/data/alfworld_sft.json`
**日期**: 2026-05-12

---

## 1. 基础统计

| 指标 | 值 |
|------|-----|
| 总轨迹数 | 3,119 |
| 文件大小 | 18 MB |
| JSON 结构 | `list[dict]`，每个 dict 有 3 个字段 |
| 字段 | `id` (str), `game_file` (str), `conversations` (list[dict]) |
| Conversation 条目 | `{"from": "human"|"gpt", "value": str}` |
| 所有 id 唯一 | 是（格式 `alfworld_0` ~ `alfworld_3118`）|
| 所有 game_file 唯一 | 是 |

**Conversation 结构**:
- Turn 0: human — 系统指令 + 环境描述 + 任务目标
- Turn 1: gpt — 固定 `"OK"`（全部 3119 条一致）
- Turn 2+: human/gpt 交替（human=环境观测，gpt=Thought+Action）
- 最后一个 turn 始终是 gpt（最终 action）
- 有效步数（action-observation pair）= `(len(conversations) - 2) / 2`

---

## 2. Task Type 分布

| Task Type | 数量 | 占比 |
|-----------|------|------|
| pick_and_place_simple | 759 | 24.3% |
| pick_two_obj_and_place | 662 | 21.2% |
| pick_clean_then_place_in_recep | 576 | 18.5% |
| pick_cool_then_place_in_recep | 472 | 15.1% |
| pick_heat_then_place_in_recep | 371 | 11.9% |
| look_at_obj_in_light | 279 | 8.9% |

6 种 task type 全部覆盖，无 unknown。pick_and_place_simple 最多，look_at_obj_in_light 最少。

---

## 3. 轨迹长度分布

### 按 GPT turns 数统计

| Task Type | N | Min | Mean | Median | Max |
|-----------|---|-----|------|--------|-----|
| look_at_obj_in_light | 279 | 4 | 8.9 | 6.0 | 46 |
| pick_and_place_simple | 759 | 5 | 8.3 | 6.0 | 47 |
| pick_clean_then_place_in_recep | 576 | 4 | 10.5 | 8.0 | 45 |
| pick_cool_then_place_in_recep | 472 | 5 | 10.3 | 9.0 | 42 |
| pick_heat_then_place_in_recep | 371 | 7 | 10.7 | 9.0 | 49 |
| pick_two_obj_and_place | 662 | 7 | 15.2 | 12.0 | 50 |
| **ALL** | **3119** | **4** | **10.8** | **9.0** | **50** |

### 按有效步数（action-observation pairs）

- Min: 3, Mean: 9.8, Max: 49

**观察**:
- pick_two_obj_and_place 明显更长（mean=15.2），因为需要搬两个物体
- pick_and_place_simple 和 look_at_obj_in_light 最短（mean 8-9）
- heat/cool/clean 类中等长度，因为多了一个处理步骤

---

## 4. Task ID / Game File 结构

### game_file 格式
```
data/json_2.1.1/train/{task_type}-{Object}-None-{Receptacle}-{SceneID}/trial_{timestamp}
```

示例:
```
data/json_2.1.1/train/pick_and_place_simple-ToiletPaper-None-ToiletPaperHanger-406/trial_T20190908_122807_136741
data/json_2.1.1/train/look_at_obj_in_light-AlarmClock-None-DeskLamp-301/trial_T20190907_174127_043461
```

### 用于 overlap 匹配的 key

- **Unique game_files**: 3,119（每条轨迹唯一）
- **Unique task directories**（去掉 `trial_` 后缀）: 1,395 个场景配置
- 每个 task directory 有 1~3 条 trial（1 trial: 254 dirs, 2 trials: 558 dirs, 3 trials: 583 dirs）

与 failure trajectory 匹配时，应按 **task directory**（不含 trial 后缀）做 overlap，因为同一场景配置可能有多个 trial。

---

## 5. 样例轨迹

### pick_and_place_simple (alfworld_0)
```
game_file: pick_and_place_simple-ToiletPaper-None-ToiletPaperHanger-406/trial_T20190908_122807_136741

GPT 1: Thought: I need to place a toilet paper roll on the toilet paper hanger.
        Action: go to toiletpaperhanger 1
GPT 2: Thought: The toilet paper hanger is empty, so I need to find a new roll.
        Action: go to toilet 1
GPT 3: Thought: I've found a toilet paper roll on the toilet.
        Action: take toiletpaper 1 from toilet 1
GPT 4: Thought: Now I need to return to the hanger.
        Action: go to toiletpaperhanger 1
GPT 5: Thought: I can place the toilet paper roll on it.
        Action: put toiletpaper 1 in/on toiletpaperhanger 1
```

### pick_clean_then_place_in_recep (alfworld_1)
```
game_file: pick_clean_then_place_in_recep-Potato-None-Microwave-2/trial_T20190908_102004_349533

GPT 1: Action: go to fridge 1
GPT 2: Action: open fridge 1
GPT 3: Action: take potato 1 from fridge 1
GPT 4: Action: go to sinkbasin 1
GPT 5: Action: clean potato 1 with sinkbasin 1
```

### look_at_obj_in_light (alfworld_5)
```
game_file: look_at_obj_in_light-Pillow-None-DeskLamp-316/trial_T20190908_232421_645610

GPT 1: Action: go to bed 1
GPT 2: Action: take pillow 3
GPT 3: Action: go to sidetable 1
GPT 4: Action: go to shelf 1
```

**Action 格式**: `"Thought: ...\nAction: {verb} {args}"`，与 ALFWorld 标准 action space 一致。

---

## 6. Action 词汇表

### Action 动词频率（15 种）

| 动词 | 出现次数 | 说明 |
|------|---------|------|
| go | 16,373 | 导航到容器/位置 |
| take | 3,759 | 拾取物体 |
| put | 3,469 | 放置物体 |
| open | 3,381 | 打开容器 |
| close | 2,176 | 关闭容器 |
| clean | 525 | 清洗物体 |
| cool | 345 | 冷却物体 |
| use | 282 | 使用物体（如 desklamp） |
| heat | 269 | 加热物体 |
| look | 55 | 查看 |
| examine | 15 | 检查 |
| quickly | 3 | 噪声 |
| turn | 2 | 噪声 |
| think | 2 | 噪声 |
| brainstorm | 1 | 噪声 |

**核心 action 动词**: go, take, put, open, close, clean, cool, use, heat（9 种），与 ALFWorld 标准 action space 完全对应。look/examine 是非标准但有效的探索 action。quickly/turn/think/brainstorm 为少量噪声（共 8 条）。

### 高频完整 action（Top 10）

| Action | 次数 |
|--------|------|
| go to sidetable 1 | 1,104 |
| go to sinkbasin 1 | 984 |
| go to countertop 1 | 905 |
| go to fridge 1 | 884 |
| go to shelf 1 | 776 |
| go to microwave 1 | 773 |
| go to garbagecan 1 | 761 |
| go to drawer 1 | 696 |
| go to diningtable 1 | 684 |
| open fridge 1 | 629 |

导航 action 占绝对主导（`go` 占总 action 的 53.4%）。

---

## 7. DPO Pair 构建关键信息

| 要素 | 值 / 策略 |
|------|----------|
| Expert 来源 | ETO SFT 数据（成功轨迹）|
| 匹配粒度 | task directory（去掉 trial 后缀）|
| 可匹配 key 数 | 1,395 个 unique task dir |
| 每条轨迹有效步数 | 3~49 步（mean 9.8）|
| GPT turn 格式 | `"Thought: ...\nAction: ..."` |
| 第一个 GPT turn | 固定 `"OK"`，构建 pair 时应跳过 |
| Action 解析 | 用 `re.search(r'Action:\s*(.+)', turn)` 提取 |
| Task type 长度差异大 | pick_two 平均 15 步 vs pick_and_place 平均 8 步，gamma_e 应区分对待 |
