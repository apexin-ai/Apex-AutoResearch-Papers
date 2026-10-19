# deploy bjb1 32546 gpu45

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb1-32546-gpu45_20260524T062617_result.json`
- **Structured JSON:** [`0767e0616d264caddf6e.json`](../../sessions/07/0767e0616d264caddf6e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验已启动，日志确认参数正确，模型正在加载。

---

## 部署结果

### GPU 状态 (bjb1-32546)
| GPU | 实验 | 状态 |
|-----|------|------|
| 0 | Long adaptive s46 | 运行中 (7/10 tasks, ~1h) |
| 1 | Long crm_obs_only s46 | 运行中 (7/10 tasks) |
| 2 | Long reconvla s46 | 运行中 (7/10 tasks) |
| 3 | Long k2mean s46 | 运行中 (7/10 tasks) |
| **4** | **Long reconvla s47** | **刚启动** |
| **5** | **Long crm_obs_only s47** | **刚启动** |

### Long s46 收割
未完成，7/10 tasks 完成中。预计 ~1h 后可收割。

### 为什么改了部署计划
- 用户指定的 Spatial s45 (VLA-only + CRM) **已在 cqa1-32758 上完成**（SR=77%/78%）
- Spatial s42-s46 全部 5 modes 全覆盖
- 改部署 **Long s47**（reconvla + crm），配合 cqa1-32758 上已在跑的 Long s47 vla-only + adaptive，给最高方差的 Long suite 增加第 6 seed

### 注意事项
Long s46 在 bjb1-32546 和 cqa1-32758 上**重复运行**（原始版 + r2 版）。Registry 中原始版标记 `conclusion: "failed"` 但进程实际在跑。建议先完成的那组收割后 kill 另一组释放 GPU。

---
