# exp021 SFT Checkpoint - RAGEN val_before_train Report

## VERDICT: FAIL

## Method
- Script: `train.py --config-name _alfworld_exp022_grpo_from_sft_v4 trainer.val_only=True`
- Model: `/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4` (Qwen3 1.72B)
- Val: 16 ALFWorld episodes (env_groups=16, group_size=1)
- gpu_memory_utilization: 0.2 (to fit alongside FSDP actor+ref)
- Generation time: 92.68 seconds

## Key Metrics

| Metric | Value | Threshold | Status |
|--------|-------|-----------|--------|
| success | 6.25% (1/16) | >= 10% | FAIL |
| action_is_valid | 68.75% | >= 85% | FAIL |
| action_is_effective | 100% | - | OK |
| num_actions | 28.69 | - | - |
| pass@1 | 6.25% | - | - |
| response_length | 2818.25 | - | - |
| episodic_return | 0.0 | - | - |
| reward/mean@16 | 0.625 | - | - |
| reward/best@16/mean | 6.28 | - | - |

## Full Metrics Dump
- val-env/AlfworldSG/success: 0.0625
- val-env/AlfworldSG/num_actions: 28.6875
- val-env/AlfworldSG/episodic_return: 0.0
- val-env/AlfworldSG/action_is_effective: 1.0
- val-env/AlfworldSG/action_is_valid: 0.6875
- val-env/AlfworldSG/raw_reward: 0.0
- val-env/AlfworldSG/pass@1: 0.0625
- val-env/charts/avg_episode_return: 0.0
- val-env/AlfworldSG/non-zero/success: 1.0
- val-env/AlfworldSG/non-zero/num_actions: 28.6875
- val-env/AlfworldSG/non-zero/action_is_effective: 1.0
- val-env/AlfworldSG/non-zero/action_is_valid: 0.6875
- val-env/AlfworldSG/non-zero/pass@1: 1.0
- val-env/response_length: 2818.25
- val-core/unknown/reward/mean@16: 0.625
- val-aux/unknown/reward/std@16: 2.4206
- val-aux/unknown/reward/best@2/mean: 1.24
- val-aux/unknown/reward/best@4/mean: 2.27
- val-aux/unknown/reward/best@8/mean: 4.05
- val-core/unknown/reward/best@16/mean: 6.28

## Diagnosis
1. action_is_valid=68.75%: ~31% of actions don't conform to ALFWorld format
2. success=6.25%: Only 1/16 episodes succeeded
3. action_is_effective=100%: Valid actions are all meaningful
4. response_length=2818: Potentially verbose outputs

## Date
2026-05-15
