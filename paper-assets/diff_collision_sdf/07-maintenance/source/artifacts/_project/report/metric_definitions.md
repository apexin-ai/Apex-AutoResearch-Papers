# ColliForce-VLA Paper Metric Definitions

## 1. safe_rate — Safe Success Rate (SSR)

### 推荐定义：Definition A

$$\text{SSR} = \frac{|\{e \in \mathcal{E} : \text{success}(e) \wedge \neg\text{collided}(e)\}|}{|\mathcal{E}|}$$

**推荐理由：**

- `success=True` 隐式排除了 frozen episode（frozen robot 无法完成操作任务），因此无需显式加 `¬frozen` 条件（Definition C 与 A 在实践中等价）。
- Definition B（`¬collided ∧ ¬frozen`）不要求成功，语义是"移动了但没撞"，包含了大量失败但未碰撞的 episode，不反映有用的安全能力。
- SSR 直接回答核心问题：**机器人能安全地完成任务吗？** 这是 safety-aware policy 最关心的指标。

**与 TSR/CAR 的关系：**

| Metric | 公式 | 衡量什么 | 缺陷 |
|--------|------|---------|------|
| TSR | success / total | 任务能力 | 不考虑碰撞 |
| CAR | ¬collided / total | 无碰撞率 | 被 fake safety 严重污染（M030: 97-99% 的 "safe" episode 实际是 frozen） |
| frozen_rate | frozen / total | action collapse 程度 | 单独看不反映安全或任务能力 |
| **SSR** | **success ∧ ¬collided** / total | **安全完成任务** | 无 fake safety 问题，无人为阈值 |

**关键优势：** SSR = TSR × P(¬collided | success)。当 SSR ≈ TSR 时，说明模型在成功时几乎不碰撞；当 SSR ≪ TSR 时，说明成功依赖碰撞。这个关系在论文分析中非常有用。

### Eval JSON 字段映射

```
episode.success  (bool)  →  是否成功
episode.collided (bool)  →  是否碰撞（any obstacle displaced > 1mm）
```

---

## 2. frozen_rate — Action Collapse Rate

### 定义

$$\text{frozen\_rate} = \frac{|\{e \in \mathcal{E} : \text{frozen}(e)\}|}{|\mathcal{E}|}$$

其中 `frozen(e)` 定义为 episode $e$ 中所有障碍物最大位移 < 0.1mm（即机器人几乎不动，未产生有意义的物理交互）。

**为什么 frozen_rate 必须在主表：**

- Claim 1 (Fake Safety) 的核心论证：CAR 虚高是因为 frozen episode 被计为 "safe"。**没有 frozen_rate 列，读者无法量化 fake safety 的严重程度。**
- D012 pass/fail gate 包含 frozen_rate 检查（frozen_rate < 5% 为通过条件）。
- frozen_rate 是本文的原创诊断指标（M035 文献调研确认文献空白）。

**与其他 metric 的配合：**

| 情形 | CAR | frozen_rate | 解读 |
|------|-----|-------------|------|
| 真实避碰 | 高 | 低 | 模型主动避障且保持运动 |
| Fake safety | 高 | 高 | CAR 虚高，来自 action collapse |
| 碰撞多 | 低 | 低 | 模型在动但撞了 |

### Eval JSON 字段映射

```
episode.max_obstacle_displacement (float) → frozen = (max_disp < 0.0001)
# 或等价地:
episode.frozen (bool) → 若 eval 脚本直接输出
```

---

## 3. min_obs — Minimum Obstacle Clearance

### 推荐定义：成功 episode 的 min_ee_obstacle_distance 均值

$$\text{min\_obs} = \frac{1}{|\mathcal{E}_s|} \sum_{e \in \mathcal{E}_s} \min_t d_{\text{ee-obs}}(e, t)$$

其中 $\mathcal{E}_s = \{e \in \mathcal{E} : \text{success}(e)\}$，$d_{\text{ee-obs}}(e,t)$ 是 episode $e$ 在 timestep $t$ 的 EE 到最近障碍物距离。

**推荐理由：**

- 仅对**成功 episode** 计算，因为：
  - frozen episode 的 EE-obs 距离恒定且无意义（robot 不动，距离不变）
  - 失败 episode 的轨迹可能中途终止，距离统计不可比
  - 成功 episode 代表完整、有意义的操作轨迹
- 用**均值**而非中位数/百分位数：
  - 均值可加性好，便于跨 task 聚合
  - 样本量通常足够（200+ episodes），不需要中位数的鲁棒性
  - 论文表格中均值 ± 标准差是最标准的呈现方式
- 单位用 **cm**（而非 m），因为实际值在 15-26cm 范围，cm 更直观

**可选补充指标**（如果审稿人要求）：

- $\text{min\_obs}_{10}$：成功 episode 中 min_ee_obstacle_distance 的第 10 百分位（worst-case clearance）
- per-obstacle 版本：使用 `per_obstacle_min_ee_distance` 字段，报告各障碍物的分别最小距离

### Eval JSON 字段映射

```
episode.success                  (bool)   →  筛选成功 episode
episode.min_ee_obstacle_distance (float)  →  该 episode 的全局最小 EE-obstacle 距离 (m)
episode.per_obstacle_min_ee_distance (dict, optional) → 每个障碍物的最小距离
```

---

## 4. 计算脚本

```python
import json
import numpy as np
from pathlib import Path


def _extract_episodes(data: dict) -> list:
    """从 eval JSON 提取 episode 列表，兼容两种格式。

    格式 A: data["episodes"] — 扁平列表
    格式 B: data["per_task"][i]["episodes"] — 按 task 分组
    """
    if "episodes" in data:
        return data["episodes"]
    elif "per_task" in data:
        episodes = []
        for task_block in data["per_task"]:
            if isinstance(task_block, dict) and "episodes" in task_block:
                for ep in task_block["episodes"]:
                    if "task_name" not in ep and "task_name" in task_block:
                        ep["task_name"] = task_block["task_name"]
                    episodes.append(ep)
        return episodes
    else:
        raise KeyError(
            f"Unrecognized eval JSON structure. "
            f"Top-level keys: {list(data.keys())}. "
            f"Expected 'episodes' or 'per_task'."
        )


def _is_frozen(ep: dict, threshold: float = 0.0001) -> bool:
    """判断 episode 是否为 frozen (action collapse)。"""
    if "frozen" in ep:
        return ep["frozen"]
    if "max_obstacle_displacement" in ep:
        return ep["max_obstacle_displacement"] < threshold
    # fallback: 检查 per_obstacle_displacement
    if "per_obstacle_displacement" in ep:
        return all(d < threshold for d in ep["per_obstacle_displacement"].values())
    return False


def compute_paper_metrics(eval_json_path: str) -> dict:
    """从 eval JSON 计算论文 metric（主表 4 列 + min_obs）。"""
    with open(eval_json_path) as f:
        data = json.load(f)

    episodes = _extract_episodes(data)
    n_total = len(episodes)

    # --- TSR ---
    n_success = sum(1 for ep in episodes if ep["success"])
    tsr = n_success / n_total

    # --- CAR ---
    n_collision_free = sum(1 for ep in episodes if not ep["collided"])
    car = n_collision_free / n_total

    # --- SSR ---
    n_safe_success = sum(
        1 for ep in episodes
        if ep["success"] and not ep["collided"]
    )
    ssr = n_safe_success / n_total

    # --- frozen_rate ---
    n_frozen = sum(1 for ep in episodes if _is_frozen(ep))
    frozen_rate = n_frozen / n_total

    # --- min_obs (over successful episodes, in cm) ---
    successful_min_dists = [
        ep["min_ee_obstacle_distance"]
        for ep in episodes
        if ep["success"] and "min_ee_obstacle_distance" in ep
    ]
    if successful_min_dists:
        min_obs_mean = np.mean(successful_min_dists) * 100  # m -> cm
        min_obs_std = np.std(successful_min_dists) * 100
        min_obs_p10 = np.percentile(successful_min_dists, 10) * 100
    else:
        min_obs_mean = min_obs_std = min_obs_p10 = float("nan")

    return {
        "TSR": tsr,
        "CAR": car,
        "SSR": ssr,
        "frozen_rate": frozen_rate,
        "min_obs_mean_cm": min_obs_mean,
        "min_obs_std_cm": min_obs_std,
        "min_obs_p10_cm": min_obs_p10,
        "n_total": n_total,
        "n_success": n_success,
        "n_safe_success": n_safe_success,
        "n_frozen": n_frozen,
    }


def compute_per_task_metrics(eval_json_path: str) -> dict:
    """按 task 分别计算 metric。"""
    with open(eval_json_path) as f:
        data = json.load(f)

    episodes = _extract_episodes(data)

    from collections import defaultdict
    tasks = defaultdict(list)
    for ep in episodes:
        tasks[ep["task_name"]].append(ep)

    results = {}
    for task_name, eps in tasks.items():
        n = len(eps)
        n_ss = sum(1 for e in eps if e["success"] and not e["collided"])
        n_frozen = sum(1 for e in eps if _is_frozen(e))
        n_car = sum(1 for e in eps if not e["collided"])
        succ_dists = [
            e["min_ee_obstacle_distance"]
            for e in eps
            if e["success"] and "min_ee_obstacle_distance" in e
        ]
        results[task_name] = {
            "TSR": sum(1 for e in eps if e["success"]) / n,
            "CAR": n_car / n,
            "SSR": n_ss / n,
            "frozen_rate": n_frozen / n,
            "min_obs_cm": np.mean(succ_dists) * 100 if succ_dists else float("nan"),
        }
    return results
```

---

## 5. 论文呈现

### 主表列名（Reviewer #66: 4 列 + MinObs）

| 列名 | 含义 | 格式 |
|------|------|------|
| **TSR** (↑) | Task Success Rate | XX.X% |
| **CAR** (↑) | Collision Avoidance Rate | XX.X% |
| **SSR** (↑) | Safe Success Rate | XX.X% |
| **FR** (↓) | Frozen Rate (action collapse) | XX.X% |
| **MinObs** (↑) | Min. Obstacle Clearance | XX.X cm |

- ↑ 越大越好，↓ 越小越好
- CAR 保留在主表是 Claim 1 (Fake Safety) 的核心论证：读者需要看到 "CAR 虚高但 SSR 低 + FR 高" 的对比才能理解 metric contamination
- SSR 作为推荐的综合安全指标
- FR 量化 fake safety 的严重程度

### 示例主表

| Method | TSR (↑) | CAR (↑) | SSR (↑) | FR (↓) | MinObs (↑) |
|--------|---------|---------|---------|--------|------------|
| Pi0 LoRA baseline | 0.0% | 82.0% | 0.0% | ~98% | — |
| A1-SDF (Pi0 LoRA) | 0.0% | 91.5% | 0.0% | ~99% | — |
| Pi0.5 baseline (3-seed) | 74.7% | 26.8% | — | ~0% | — |
| ColliForce (λ=0.005) | 47.0% | 58.0% | — | 0% | 20.3 cm |
| ColliForce (λ=0.01) | 49.0% | 56.5% | — | 0% | — |

**Claim 1 论证路径**（通过主表直接可读）：
- Pi0 baseline: CAR=82% 看似安全，但 FR=98% → 几乎全部 frozen → CAR 是假象
- A1-SDF (Pi0): CAR 从 82%→91.5%（+9.5pp），但 FR 从 98%→99%，SSR 不变 → "改进" 来自更严重的 action collapse
- Pi0.5: CAR=26.8%（低得多），但 FR≈0%，TSR=74.7% → 真实在动，碰撞是真实碰撞

### 论文正文描述模板

> We report five metrics. **Task Success Rate (TSR)**: fraction of episodes where the robot completes the task. **Collision Avoidance Rate (CAR)**: fraction of episodes with no obstacle displacement exceeding 1mm. **Safe Success Rate (SSR)**: fraction of episodes where the robot completes the task without collision—the metric we recommend for evaluating safety-aware policies. **Frozen Rate (FR)**: fraction of episodes where the robot exhibits action collapse (maximum obstacle displacement < 0.1mm), indicating the robot is effectively stationary. **Minimum Obstacle Clearance (MinObs)**: average minimum end-effector-to-obstacle distance across successful episodes (in cm).
>
> Crucially, CAR is contaminated by action collapse: a frozen robot trivially avoids collision, inflating CAR without any actual safety capability. We include CAR alongside FR to make this contamination transparent, and recommend SSR as the primary safety metric.

### JSON 路径验证清单（30K eval 首个结果后执行）

30K eval 跑出第一个结果后，立即验证 JSON 结构：

```python
import json

with open("first_eval_result.json") as f:
    data = json.load(f)

# 检查顶层结构
print("Top-level keys:", list(data.keys()))

# 检查 episode 提取
episodes = _extract_episodes(data)
print(f"Total episodes: {len(episodes)}")

# 检查每个 episode 必需字段
required = ["success", "collided", "task_name"]
optional = ["max_obstacle_displacement", "frozen", "min_ee_obstacle_distance",
            "per_obstacle_displacement", "per_obstacle_min_ee_distance"]
ep = episodes[0]
for field in required:
    assert field in ep, f"MISSING required field: {field}"
for field in optional:
    print(f"  {field}: {'present' if field in ep else 'MISSING'}")
```
