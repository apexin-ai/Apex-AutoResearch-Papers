# analysis pi05 object per episode collision

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pi05_object_per_episode_collision_20260522T230743_result.json`
- **Structured JSON:** [`700dcdac9bff84f6d1cb.json`](../../sessions/70/700dcdac9bff84f6d1cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已生成。核心发现：

### 四分类

| 类别 | 数量 | 占比 |
|------|------|------|
| SUCCESS+SAFE | 55 | 27.5% |
| SUCCESS+COLLISION | 91 | 45.5% |
| FAIL+COLLISION | 53 | 26.5% |
| FAIL+SAFE | 1 | 0.5% |

### 关键结论

1. **碰撞集中在 step 75-100**（57.6%），是 arm 接近目标物过程中扫到周围 obstacle，不是 EE 精细操作碰撞。

2. **moka_pot 是致命 obstacle**：F+C 中 68% 由它引起，碰到几乎必定失败。**wine_bottle 是可容忍 obstacle**：S+C 中占 43%，碰了也能完成任务。

3. **100% 的 SAFE episodes 是 fake safe**（displacement ≈ 0），Pi0.5 没有避障能力——要么路径天然安全，要么碰得很重。

4. **83% 的碰撞是大位移（>50mm）**，不是轻微擦碰。

5. **EE-only SDF 改善空间**：
   - Best-case CAR: 0.73（+0.45），假设能消除所有 S+C 碰撞
   - Conservative CAR: 0.36（+0.08），仅能修复小位移碰撞
   - 差距巨大，说明 EE-SDF refinement 需要能处理 50-200mm 量级的避障才有实际意义

报告路径：`artifacts/report_pi05_object_collision_analysis.md`

---
