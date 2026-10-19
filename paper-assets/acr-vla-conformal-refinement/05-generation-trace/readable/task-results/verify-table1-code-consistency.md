# verify table1 code consistency

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_table1-code-consistency_20260526T014141_result.json`
- **Structured JSON:** [`3b3182a420a7a41c2054.json`](../../sessions/3b/3b3182a420a7a41c2054.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

# 验证报告：Table 1 Goal Suite 代码版本一致性

## 1. evaluate.py 现状（三台服务器）

| 服务器 | 文件大小 | 当前 mtime | .git 状态 |
|---|---|---|---|
| bjb1-32546 | **36365 B** | **2026-05-26 08:27:36** | **无 .git** |
| bjb2-28827 | **36365 B** | 2026-05-26 08:27:34 | 有 git log |
| cqa1-32758 | **36365 B** | 2026-05-26 08:32:39 | 有 git log（与 bjb2 完全相同） |

`md5sum` 被 sandbox 屏蔽，但三台 size 一致 + 几乎同时（今天 08:27）被覆盖 → **当前 evaluate.py 是事后同步的，跟生成 Table 1 结果时的版本不是同一份**。

## 2. Git log（仅 bjb2/cqa1 可见，bjb1 无 git）

| epoch | 本地时间 (+0800) | commit msg |
|---|---|---|
| 1778822260 | 2026-05-14 23:57 | initial: init from existing code on bjb2-40593 |
| 1779231935 | 2026-05-19 17:25 | feat: add --mode adaptive_k with K2 L2 threshold-based adaptive inference |
| 1779629989 | **2026-05-23 21:39** | **fix: disambiguate output filename for vla_only baseline_mode=mean** |

5/23 的 disambiguation commit 把 `vla_only baseline_mode=mean` 的输出从 `eval_goal_vla_only_seed{N}.json` 改为 `eval_goal_k10mean_seed{N}.json`。fix 之前，K=10 mean 和 K=1 single 会写到同一文件名。

## 3. Goal Suite 文件清单与 SR（直接读 JSON 验证）

### bjb1-32546（**Table 1 实际来源**）

| 文件 | mtime | mode (JSON) | n_rollouts | SR |
|---|---|---|---|---|
| `eval_goal_vla_only_seed42.json` | **05-25 06:09** | vla_only / single | 20 | **0.835** |
| `eval_goal_vla_only_seed43.json` | **05-23 21:34** | vla_only / single | 20 | **0.825** |
| `eval_goal_vla_only_seed44.json` | **05-24 00:34** | vla_only / single | 20 | **0.850** |
| `eval_goal_vla_only_seed43_r4.json` | 05-23 00:15 | vla_only / single | 20 | **0.980** ← 异常高 |
| `eval_goal_vla_only_seed44_r4.json` | 05-23 00:16 | vla_only / single | 20 | **0.975** ← 异常高 |
| `eval_goal_crm_seed43.json` | 05-25 20:20 | crm_obs_only | 20 | 0.820 |
| `eval_goal_crm_seed44.json` | 05-25 20:16 | crm_obs_only | 20 | 0.820 |
| `eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json` | 05-23 18:38 | adaptive_conformal_crm (tau=0.25) | 20 | 0.845 |
| `eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json` | 05-23 19:00 | adaptive_conformal_crm | 20 | 0.865 |
| `eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json` | 05-24 06:06 | adaptive_conformal_crm | 20 | 0.810 |

VLA-only 均值 (0.835+0.825+0.850)/3 = **0.837 ↔ Table 1 报告的 83.7% 精确匹配**。

### bjb2-28827

| 文件 | mtime | mode | n_rollouts | SR |
|---|---|---|---|---|
| `eval_goal_vla_only_seed42.json` | 05-23 17:31 | vla_only / single | 20 | 0.835 |
| `eval_goal_vla_only_seed44_r2.json` | 05-20 02:20 | vla_only / single | **10** | 0.730 |
| `eval_crm_goal_seed44_r2.json` | 05-20 07:10 | crm_obs_only | **10** | 0.640 |
| `eval_crm_goal_seed45_r2.json` | 05-20 07:13 | crm_obs_only | **10** | 0.825 |
| `eval_goal_adaptive_conformal_crm_norm0.2_tau0.25_seed42.json` | 05-23 16:52 | adaptive_conformal_crm | 20 | 0.835 |
| `eval_goal_adaptive_seed42.json` | 05-25 20:43 | adaptive_conformal_crm | 20 | 0.840 |

### cqa1-32758

| 文件 | mtime | mode | n_rollouts | SR |
|---|---|---|---|---|
| `eval_goal_vla_only_seed42.json` | 05-25 06:31 | vla_only / single | 20 | **0.820** (≠ bjb1 的 0.835) |
| `eval_goal_vla_only_seed43.json` | 05-25 06:21 | vla_only / single | 20 | 0.835 |
| `eval_goal_vla_only_seed44.json` | 05-25 06:32 | vla_only / single | 20 | 0.850 |
| `eval_goal_vla_only_seed48/49` | 05-25 02:34 | vla_only / single | 20 | 0.85/0.82 |

## 4. r4/r2/无后缀差异解释

evaluate.py 第 861 行：
```python
mode_str = f"k{args.K}mean" if args.mode == "vla_only" and args.baseline_mode == "mean" else args.mode
```

- **r4 文件**（05-23 00:15，SR≈98%）：mtime 比 disambiguation commit（05-23 21:39）早 21 小时。当时 K=10 mean 和 K=1 single 共用同一文件名，**r4 几乎肯定是 K=10 mean 基线（pre-fix）被手动改名保留**。98% 的 SR 完全符合 K=10 mean 的水平。
- **r2 文件**（05-20，**n_rollouts=10**）：是更早的 10-rollout 实验，与 Table 1 的 20-rollout 不可比。
- **无后缀文件**（05-23 21:34 起，SR≈83%）：mode=vla_only + baseline_mode=single + n_rollouts=20，是 Table 1 实际使用的版本。

## 5. 每列代码一致性逐项判断

| Table 1 列 | 使用文件（bjb1） | 时间窗口 | 受 disambiguation commit 影响？ | 内部一致 |
|---|---|---|---|---|
| **VLA-only** | seed42/43/44 无后缀 | 05-23 21:34 → 05-25 06:09（**33 小时跨度**） | **No** — disambiguation 只改 `baseline_mode=mean` 的命名，single 模式不受影响 | ✓ 三者均为 mode=vla_only, baseline_mode=single, n_rollouts=20 |
| **CRM** | crm_seed43/44 | 05-25 20:16 → 20:20（4 分钟内） | No — 该 commit 不涉及 crm_obs_only | ✓ 完全一致 |
| **Adaptive** | adaptive_conformal_crm_norm0.2_tau0.25 seed43/44/45 | 05-23 18:38 → 05-24 06:06（**12 小时跨度**） | No — 该 commit 不涉及 adaptive_conformal_crm | ✓ 配置参数完全相同 |

## 6. 结论

**A）三列大概率使用同一代码逻辑**，但存在不可消除的残余风险：

**支持论据**
1. 三列结果均来自 **同一台服务器 bjb1-32546**，时间窗口集中在 5/23-5/25（48 小时）
2. JSON 字段 schema（mode / baseline_mode / n_rollouts / adaptive_stats.tau / total_steps / crm_applied_steps）与当前 evaluate.py 输出格式完全吻合
3. 期间唯一已知代码变更（5/23 21:39 的 disambiguation commit）**仅影响 vla_only baseline_mode=mean 的命名**，对 single / CRM / Adaptive 三种模式 **逻辑上零影响**

**残余风险**
1. **bjb1-32546 无 .git** → 无法直接证明 evaluate.py 在每次实验时点是同一版本
2. 当前 evaluate.py 在三台服务器都被 **今天 05-26 08:27 重新覆盖**（极可能是事后 sync）→ 现存代码 ≠ 实验时代码，本地 hash 无法回溯
3. **跨服务器复现存在系统性差异**：bjb1 vla_only seed42 = 0.835 vs cqa1 vla_only seed42 = 0.820（同 seed、同 mode 但不同机器 SR 差 1.5pp），暗示评测有非确定性来源
4. r4 文件（97.5-98%）虽未进 Table 1，但其存在说明同名文件历史上确实出现过严重歧义

**给 reviewer 的建议**：在响应函中明确标注 Table 1 Goal VLA-only 使用 `mode=vla_only, baseline_mode=single, K=1, n_rollouts=20`，并在附录列出每个 JSON 文件路径 + mtime + per-task counts；同时声明 r4/r2 文件不参与 Table 1（r4 = K=10 mean 基线，r2 = 早期 10-rollout 实验）。

---
