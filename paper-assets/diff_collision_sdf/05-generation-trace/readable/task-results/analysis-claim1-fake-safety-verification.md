# analysis claim1 fake safety verification

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_claim1_fake_safety_verification_20260525T221006_result.json`
- **Structured JSON:** [`24c5f4bbfc9c1579b524.json`](../../sessions/24/24c5f4bbfc9c1579b524.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 验证结论

### 1. JSON 文件
- **路径**: `/root/autodl-tmp/eval_results/a1_rerun_v11_eval_safelibero_object_all_levelII_best_lora_baseline_seed0.json`
- **800 episodes** (4 tasks × 200), CAR=91.5%, TSR=0%

### 2. Displacement 字段
Episode 字段：`['collided', 'collision_obstacle', 'collision_step', 'episode', 'max_displacement', 'smoothness', 'success', 'total_steps']`

**没有 `max_ee_displacement` 字段**（该 eval 用的是旧版脚本）。

### 3. "99.6% fake safety" 计算方法

通过 `analyze_displacement.py` 的 **fallback 路径**计算：
- 脚本检测到无 `max_ee_displacement` → 回退到 `max_displacement`（障碍物位移）
- 阈值 = 0.0001m (0.1mm)（项目定义 M037）
- 结果：729/732 safe episodes 的障碍物位移 < 0.1mm → **99.6%**
- 3 个例外 episode 的 `max_displacement` 分别为 0.18mm、0.46mm、0.65mm（未达碰撞阈值 1mm，但超过 frozen 阈值 0.1mm）

### 4. 结论：**不受 EE displacement bug 影响**

| 项 | 说明 |
|---|---|
| 使用的字段 | `max_displacement`（障碍物位移），不是 `max_ee_displacement` |
| 该字段是否有 bug | 无。障碍物位移 tracking 一直正确 |
| 99.6% 是否可信 | 数值正确，但语义上是间接证据 |

**"障碍物没动 < 0.1mm" ≠ "机器人没动"**，但结合以下辅助证据，action collapse 判定成立：
- TSR = 0%（无一成功）
- 所有 episode 跑满 300 步（无提前终止）
- 障碍物中位位移 ~5nm（几乎恒零）

### 5. 是否需要重跑？

**无需重跑来 defend Claim 1 的 99.6%** — 它不依赖 buggy 字段。

但如果 reviewer 质疑 "obstacle displacement ≠ EE displacement"，可用已有的 Pi0.5 fixed eval 数据作为补充证据：修复后的脚本在 Pi0.5+A1 30K safe episodes 上显示 `max_ee_displacement` 范围 0.27-1.2m（非零，说明 Pi0.5 不完全 collapse），而 Pi0 模型仍需一次 fixed-script rerun 来获得直接 EE 证据。

**资源估算**（如需）：Pi0+A1 object 4tasks × 200eps，~2.5h on 1 GPU。

---
