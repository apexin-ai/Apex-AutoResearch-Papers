# audit d160 code version check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_d160-code-version-check_20260526T072201_result.json`
- **Structured JSON:** [`67883ba9445211b919ed.json`](../../sessions/67/67883ba9445211b919ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 代码版本检查结果

**1. evaluate.py 变更历史 (05-23 ~ 05-25)**
- 该期间无 git commit；最新 commit 为 `a594db5 (2026-05-22 13:02:00 +0800) Add 3 CRM loss variants: perdof_weighted, conformal_guided, combined`
- 但 evaluate.py 文件在 **2026-05-26 08:27** 被本地修改（两台服务器同步），未 commit
- evaluate.py md5 两台服务器一致：`c15065ec7deee1f059f24879ecd6d7e6`
- 文件 Birth time：bjb1-18228 = 2026-05-22 18:30；bjb1-32546 = 2026-05-23 14:51

**2. CRM checkpoint**

| 用途 | 路径 | bjb1-32546 md5 | bjb1-18228 md5 | 一致 |
|---|---|---|---|---|
| smolvla (Table 1) | `crm_smolvla_3suite_v1/crm_best.pt` (1320219B) | `4161c6403b8eb268864b99dd986be784` | `4161c6403b8eb268864b99dd986be784` | ✅ |
| pi05 (Table 1) | `crm_pi05_unified_3suite/crm_best.pt` | `25093621fd5158951b2297ca406472f4` | `25093621fd5158951b2297ca406472f4` | ✅ |
| unified 4suite | `crm_unified_4suite/crm_best.pt` | `d47f7f2dfe29782ef22eef5033239678` | `fb2e02055d67a76a5f9e9cc028bc9375` | ❌ |
| r4 变体 | `crm_unified_4suite_r4/crm_best.pt` | `e9a4bfce8d86ac079e71d0a5a346ccbf` | (不存在) | — |

- 注：smolvla checkpoint mtime 不同（32546=05-23 07:23 / 18228=05-25 04:27），但 md5 与大小完全相同，说明是同一权重的拷贝。

**3. 代码 HEAD commit**
- bjb1-32546: **不是 git 仓库**（`/root/acr-vla-conformal-refinement` 下无 .git 目录，仅是源码拷贝，无法比较 HEAD）
- bjb1-18228: `a594db578deeeeddc0ab068549e315c5a3bb4d6a`
- 由于 evaluate.py md5 一致，可推断 src/ 实际运行代码同步

**4. evaluate.py 关键默认值**
- `K=10`, `mode=crm_perdof`, `baseline_mode=single`
- `n_rollouts=20`, `max_steps=300`, `seed=42`, `n_action_steps=10`
- `max_correction_norm=None`, `adaptive_threshold=0.1`
- `k_init=2`, `k_full=5`
- `unc_threshold=0.5`, `conformal_threshold=0.074855`
- `obs_dim=OBS_DIM` (常量), `unified_obs_dim=None`, `hidden_dim=256`

**结论**
- Table 1 涉及的 smolvla / pi05 CRM checkpoint **一致**，可放心合并。
- evaluate.py 当前版本两台服务器 md5 一致，运行代码本身没有版本漂移。
- 但需要注意：当前文件被 05-26 修改但未 commit，**与 05-23/05-25 实际跑实验时的代码可能不同**。若需严格还原 batch 当时的代码，需查 `logs/` 中保留的脚本或对应日期的源码备份。
- `crm_unified_4suite` 在两台机器 md5 不一致，但该 checkpoint 与 Table 1 无关（Table 1 用的是 _smolvla_3suite_v1 / _pi05_unified_3suite）。

---
