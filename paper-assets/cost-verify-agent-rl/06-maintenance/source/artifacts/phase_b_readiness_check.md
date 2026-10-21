# Phase B (B-IAVR) Code Readiness Check

**Date**: 2026-05-14  
**Reviewer**: Code Review Worker  
**Status**: Code ready, pending checkpoint + config fixups

---

## 1. B-IAVR Code Structure

### Core Modules (`RAGEN/ragen/biavr/`)

| File | Key APIs | Function |
|------|----------|----------|
| `reward.py` | `biavr_reward()`, `lagrangian_update()`, `BIAVRTracker` | Per-step reward: `r = -λ·1[verify] + α·1[verify ∧ action_changed]`; Lagrangian dual update: `λ ← max(0, λ + η·(v̄ − β))` |
| `verify_mechanism.py` | `parse_verify_token()`, `build_biavr_system_prompt()`, `build_no_guidance_prompt()` | `<VERIFY>` token parsing; system prompts for B-IAVR and counterfactual (no-guidance) modes |
| `action_canonicalize.py` | `canonicalize_action()`, `actions_equivalent()` | ALFWorld action parsing into `(verb, object, receptacle)` tuples for a_pre vs a_post comparison |
| `pre_action.py` | `compute_pre_action_prompt()`, `compare_actions()` | Builds counterfactual prompt (no self-guidance) for greedy a_pre decoding |

### Integration Points

- **`agent_proxy.py`** (lines 204–378): Initializes `BIAVRTracker` from config, parses `<VERIFY>` during rollout, injects B-IAVR rewards into trajectory history, computes a_pre when `enable_a_pre=true`
- **`ctx_manager.py`** (lines 113, 563, 645, 1300, 1449–1456): `biavr_enabled` property, switches system prompt to B-IAVR format, handles verify token in response parsing
- **`agent_trainer.py`** (lines 1068–1073): Logs B-IAVR metrics (`biavr/lambda`, `biavr/verify_rate`, `biavr/informativeness_rate`) and calls `update_lambda()` at end of each training step

### Config (`RAGEN/config/_alfworld_phase_b.yaml`)

```yaml
biavr:
  beta: 0.3           # target verification rate
  alpha: 1.0           # action_changed reward weight
  lambda_init: 0.0     # initial Lagrangian multiplier
  eta: 0.01            # dual variable learning rate
  enable_a_pre: true   # compute pre-guidance action for informativeness
```

Environment tag `AlfworldBIAVR` is registered in `config/envs.yaml` with B-IAVR-specific instruction prompt.

---

## 2. Checkpoint Compatibility

### Current State
- **exp008_grpo** checkpoint exists at `/root/autodl-tmp/checkpoints/exp008_grpo/global_step_5/actor/`
- Format: **FSDP-sharded** (`model_world_size_2_rank_0.pt`, `model_world_size_2_rank_1.pt`) + HuggingFace tokenizer files only
- **exp010 checkpoint does not exist yet** (no `exp010*` directory under `/root/autodl-tmp/checkpoints/`)

### Compatibility Issue
- Phase B config `model_path: TO_BE_SET` feeds into `actor_rollout_ref.model.path`, which is used by `AutoTokenizer.from_pretrained()` and `vLLM(model_name)` — both expect **HuggingFace format**
- FSDP sharded checkpoints are NOT directly loadable as `model_path`
- **Conversion required**: Use `verl/verl/model_merger/fsdp_model_merger.py` (`FSDPModelMerger`) to merge FSDP shards into HuggingFace format before Phase B

---

## 3. Test Status

**61/61 tests passed** (3.46s, CPU-only, no GPU required)

```
ragen/biavr/tests/test_biavr.py — 61 passed
```

Coverage across all modules:
- `TestCanonicalizeAction` (16 tests): all ALFWorld action formats
- `TestActionsEquivalent` (4 tests): semantic comparison
- `TestBIAVRReward` (5 tests): reward computation edge cases
- `TestLagrangianUpdate` (5 tests): dual variable dynamics
- `TestBIAVRTracker` (4 tests): tracker state management
- `TestParseVerifyToken` (5 tests): `<VERIFY>` parsing
- `TestExtractAction` (4 tests): `<answer>` extraction
- `TestBuildPreActionMessages` (3 tests): counterfactual prompt construction
- `TestCompareActions` (6 tests): a_pre vs a_post comparison
- `TestCtxManagerBIAVRParsing` (3 tests): end-to-end parsing
- `TestBIAVRRewardInjection` (3 tests): reward injection into history
- `TestBIAVRFormatPrompt` (2 tests): prompt format validation
- `TestPreActionMessages` (1 test): pipeline integration

---

## 4. Phase B Launch Preparation Checklist

| # | Task | Status | Notes |
|---|------|--------|-------|
| 1 | Wait for exp010 to complete | ⏳ Blocked | No checkpoint directory exists yet |
| 2 | Convert exp010 FSDP checkpoint to HuggingFace format | ⬜ TODO | Use `FSDPModelMerger` |
| 3 | Update `model_path` in `_alfworld_phase_b.yaml` | ⬜ TODO | Currently `TO_BE_SET` |
| 4 | Update `experiment_name` | ⬜ TODO | Currently `exp003-alfworld-biavr-selective-verify` — should be `exp011` or similar |
| 5 | Update `local_log_dir` | ⬜ TODO | Currently `/root/autodl-tmp/checkpoints/exp_003/` — stale path |
| 6 | Verify GPU availability on cuda:0,1 | ⬜ TODO | After exp010 finishes |
| 7 | Dry-run Phase B training (1-2 steps) | ⬜ TODO | Validate end-to-end pipeline |

---

## 5. Potential Risks

### High
- **FSDP→HF conversion**: Must be done correctly. The merger needs the original model config (available in `huggingface/` subdir) and both rank files. If exp010 uses different world_size than 2, the merger command must match.

### Medium  
- **Stale config paths**: `experiment_name` and `local_log_dir` reference exp003, not the actual Phase B experiment. If not updated, checkpoints will overwrite or be saved to wrong location.
- **a_pre computation overhead**: With `enable_a_pre: true`, each VERIFY step triggers an additional forward pass (greedy decode). This roughly doubles inference cost for verified steps. Monitor wall-clock time.

### Low
- **No integration test with real model**: The 61 unit tests cover logic correctness but do not test actual model loading + rollout + B-IAVR reward injection end-to-end. A 1-2 step dry run is essential before full training.
- **`max_model_len: 32768`** in Phase B config is much larger than exp008's `8192`. Verify vLLM memory fits within 2× RTX PRO 6000 at `gpu_memory_utilization: 0.4`.
