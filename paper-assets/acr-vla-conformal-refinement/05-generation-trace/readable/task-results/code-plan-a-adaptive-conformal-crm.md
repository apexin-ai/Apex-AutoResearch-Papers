# code plan a adaptive conformal crm

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan-a-adaptive-conformal-crm_20260520T185941_result.json`
- **Structured JSON:** [`149a614d36ca01941a5e.json`](../../sessions/14/149a614d36ca01941a5e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

初始化完全成功，但 dry-run 被 180s timeout 终止——GPU 被正在运行的 `random_selection` 评估（PID 759093，seed48，10 rollouts × K=10）占满，无法在超时内完成任何 rollout。

代码实现已验证：
- `adaptive_conformal_crm` mode 正确注册
- `conformal_threshold=0.074855` 参数正确解析
- SmolVLA 加载成功
- CRM obs_only 加载成功（327,198 params）
- `max_correction_norm=0.2` 覆盖生效
- 10 个 LIBERO object tasks 加载成功

**实现摘要（11 处修改全部成功应用到 evaluate.py）：**

| # | 修改 | 状态 |
|---|------|------|
| 1 | mode choices 添加 `adaptive_conformal_crm` | ✓ |
| 2 | 新增 `--conformal_threshold` 参数 (default=0.074855) | ✓ |
| 3 | 新增 `select_action_conformal_crm()` 函数 | ✓ |
| 4 | 默认 checkpoint 路径支持 | ✓ |
| 5 | CRM 加载模式列表 | ✓ |
| 6 | unc_dim=0 模式列表 | ✓ |
| 7 | 默认 max_correction_norm=0.2 | ✓ |
| 8 | rollout 循环 mode dispatch | ✓ |
| 9 | metadata 路由到 all_unc_head_meta | ✓ |
| 10 | conformal CRM stats 报告块 | ✓ |
| 11 | 输出文件命名 `_tau{threshold}` | ✓ |

**Dry-run 结果：** 初始化成功，但因 GPU 被 random_selection 评估占用，180s 内未完成 rollout，未生成 JSON 输出。等 random_selection 跑完后可重跑 dry-run 或直接启动正式评估。

---
