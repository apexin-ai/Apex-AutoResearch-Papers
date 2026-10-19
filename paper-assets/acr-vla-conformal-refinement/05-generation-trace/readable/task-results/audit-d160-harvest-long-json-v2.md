# audit d160 harvest long json v2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_d160-harvest-long-json-v2_20260526T073000_result.json`
- **Structured JSON:** [`f55052887a8f2da74636.json`](../../sessions/f5/f55052887a8f2da74636.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Long VLA-only JSON Harvest

| seed | JSON file | SR | server | registry exp_id | 已更新 |
|------|-----------|-----|--------|------------------|--------|
| 42 | logs/eval_long_vla_only_seed42.json (2026-05-23 22:10) | **0.58** | bjb1-32546 | eval-supp-long-vla-only-s42 | ✅ |
| 44 | logs/eval_long_vla_only_seed44.json (2026-05-24 03:20) | **0.565** | bjb1-32546 | eval-supp-long-vla-only-s44 | ✅ |
| 43 | logs/eval_long_vla_only_seed43.json | 0.57 | bjb1-32546 | (已有 s43=0.595, 不同run, 未覆盖) | — |
| 44 (mean) | logs/eval_long_vla_only_seed44.json | 0.545 | bjb2-28827 | baseline_mode=**mean** 不匹配, 忽略 | — |

注：registry 中原本不存在 s42/s44 条目，update_registry 已新建（status=PREPARING）。两条新建条目均为 baseline_mode=single, n_rollouts=20, benchmark=long。

## evaluate.py Diff

文件 mtime: 2026-05-26 08:27:38，最后 commit a594db5 之后**有大量未提交修改**（约 30+ 处）。

### 关键影响 evaluation 逻辑的改动

| 改动 | 影响 |
|------|------|
| `SUITE_MAX_STEPS["long"] = 520`，当 `args.max_steps==300` 时自动覆盖 | **重大**：long suite 默认 max_steps 由 300 → 520，rollout 时长大幅增加，会显著提高 long SR |
| `rollout_single` 初始 reset: `range(5)` zeros → `range(10)` `[0,0,0,0,0,0,-1]` | **影响**：初始状态由 5 步零动作改为 10 步带 gripper=-1（张开），改变 episode 起始 |
| 新增 OOM try/except：rollout 抛 OOM → success=False, steps=-1 | **轻微**：仅在 OOM 时生效，正常运行不影响 |
| 默认 CRM checkpoint: `crm_v3_norm/obs_only/crm_best.pt` → `crm_smolvla_3suite_v1/crm_best.pt` | **重大**：adaptive_k/adaptive_unc_head/adaptive_conformal_crm 模式默认 checkpoint 换了 |
| 删除 `baseline_mode=="mean"` 时 `args.K=10` 自动设置 | **影响**：k2mean 现在使用用户传入的 K（如 --K 2），不再强制 K=10 |
| 新增 `_pad_obs` 函数和 `unified_obs_dim` 参数 | **新功能**：仅当 `--unified_obs_dim` 显式设置时生效 |
| 新增 openvla_oft 模型支持 | 新增 model 选项，不影响已有 smolvla/pi05 |
| Output filename: 新增 `k_tag` 和 `k2mean` 模式标签 | **影响**：vla_only mean 模式 JSON 文件名由 `eval_&lt;bench>_vla_only_*` 改为 `eval_&lt;bench>_k{K}mean_*`，新旧 JSON 可能不会互相覆盖 |
| `select_action_conformal_crm` 新增 `correction_norm` 到 step_metadata, summary 增加 `detailed_steps` | adaptive_conformal_crm 模式输出新增字段，不影响 SR |

**结论**：05-26 修改**不是注释/格式变更**，对 evaluation 逻辑有实质影响。Long suite 后续 eval 默认 max_steps 从 300 翻到 520，会让 long SR 数据**不再可与历史 long 实验直接对比**；adaptive 系列默认 checkpoint 也换了。已有的 s42/s44/s43 JSON (5-23/24 生成) 是在旧代码下产出，与新代码运行结果不可直接比较。

---
