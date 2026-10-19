# code fix eval obs only mode

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-eval-obs-only-mode_20260514T124101_result.json`
- **Structured JSON:** [`0db21908f458a3bbea8d.json`](../../sessions/0d/0db21908f458a3bbea8d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇报：

**修改内容（evaluate.py，4 处）：**
1. `--mode` choices 新增 `crm_obs_only`
2. CRM 初始化：`crm_obs_only` 模式 `uncertainty_dim=0`（input_dim=990=30+960，无 40D conformal features）
3. `select_action_crm`：`crm_obs_only` 时传 `None` 给 uncertainty_features，跳过 conformal 特征拼接
4. `main()` 末尾加 `sys.exit(0)` 防止 Python 3.12 SWIG cleanup 导致假 exit code 1

**验证结果：**
- import OK
- `--help` 显示 `crm_obs_only` 在 choices 里
- obs_only checkpoint `crm_best.pt` 加载成功：首层 weight shape `[256, 990]`，与 `uncertainty_dim=0` 的 CRM 完全匹配

**实验 `eval-obs-only-spatial-v2` 已提交 RUNNING**，bjb1-18228 cuda:2，LIBERO spatial 10 tasks x 10 rollouts。

---
