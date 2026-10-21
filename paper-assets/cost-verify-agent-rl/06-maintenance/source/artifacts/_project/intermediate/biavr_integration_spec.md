# B-IAVR Integration Spec for Phase B

## 1. Module Overview

B-IAVR code lives in `RAGEN/ragen/biavr/` with four modules:

| Module | Purpose |
|--------|---------|
| `verify_mechanism.py` | `<VERIFY>` token parsing, system prompts (with/without self-guidance) |
| `pre_action.py` | `a_pre` counterfactual prompt construction, action comparison |
| `action_canonicalize.py` | ALFWorld action normalization for semantic equivalence |
| `reward.py` | `biavr_reward()`, `lagrangian_update()`, `BIAVRTracker` class |

## 2. Function Signatures and Data Flow

### 2.1 Verify Token Detection

```python
# verify_mechanism.py
def parse_verify_token(llm_response: str) -> Tuple[bool, str]
    # Returns (should_verify, cleaned_response)
```

Called in `ctx_manager.py:get_env_inputs()` (line ~1620) to determine if agent chose `<VERIFY>`.

### 2.2 a_pre Prompt Construction

```python
# pre_action.py
def build_pre_action_messages(
    conversation_history: List[Dict[str, str]],  # previous user/assistant turns
    current_observation: str,                      # latest env observation
) -> List[Dict[str, str]]
    # Returns OpenAI-format messages with NO self-guidance system prompt

def compute_pre_action_prompt(
    conversation_history: List[Dict[str, str]],
    current_observation: str,
) -> Dict  # {"messages": [...], "sampling_params": {"temperature": 0.0, "top_k": 1, "max_tokens": 256}}

def compare_actions(a_pre: Optional[str], a_post: Optional[str]) -> bool
    # Returns True if actions DIFFER (verification was informative)
```

### 2.3 Action Canonicalization

```python
# action_canonicalize.py
def canonicalize_action(action_str: str) -> Tuple[str, Optional[str], Optional[str]]
    # Returns (verb, object, receptacle) — handles all ALFWorld action formats

def actions_equivalent(action_a: str, action_b: str) -> bool
```

### 2.4 Reward Computation

```python
# reward.py
def biavr_reward(
    verify_t: bool,            # did agent choose <VERIFY>?
    action_changed_t: bool,    # did a_pre != a_post?
    lambda_cost: float,        # Lagrangian multiplier (verification cost)
    alpha: float = 1.0,        # action_changed reward weight
) -> float
    # r = 0 if not verify; -lambda if verify & no change; -lambda + alpha if verify & change

def lagrangian_update(
    lambda_t: float,
    mean_verify_rate: float,
    beta: float = 0.3,        # target verification rate
    eta: float = 0.01,         # dual LR
) -> float
    # lambda_{t+1} = max(0, lambda_t + eta * (verify_rate - beta))
```

**BIAVRTracker** (dataclass):
- `record_step(verify, action_changed) -> float` — returns per-step reward
- `update_lambda() -> float` — updates lambda and resets counters
- `get_metrics() -> dict` — returns biavr/lambda, verify_rate, informativeness_rate, etc.

## 3. Data Flow Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│  LLMAgentProxy.rollout()  (agent_proxy.py:238)                      │
│                                                                     │
│  for each turn:                                                     │
│    1. ctx_manager.get_lm_inputs(env_outputs)                        │
│    2. generate_sequences(lm_inputs)         → a_post (sampled)      │
│    3. ctx_manager.get_env_inputs(lm_outputs)                        │
│       └─ parse_verify_token(response) → verify_t, cleaned_response  │
│       └─ extract_action_from_response(cleaned) → a_post_action      │
│                                                                     │
│    4. IF biavr_enabled:                                             │
│       ├─ biavr_verify[eid].append(verify_t)                        │
│       ├─ biavr_changed[eid].append(False)  # default               │
│       │                                                             │
│       └─ IF enable_a_pre AND any verify_t==True:                    │
│          ├─ _build_a_pre_inputs()                                   │
│          │   └─ build_pre_action_messages(history, obs)             │
│          ├─ _generate_a_pre_greedy(prompts, dataproto)              │
│          │   └─ vLLM greedy decode (temp=0, top_k=1, max_tokens=256)│
│          └─ compare_actions(a_pre, a_post) → update biavr_changed   │
│                                                                     │
│    5. es_manager.step(env_inputs) → next env_outputs                │
│                                                                     │
│  After loop:                                                        │
│    6. _inject_biavr_rewards(rollout_states, biavr_verify, changed)  │
│       └─ biavr_tracker.record_step(vt, ac) → per-turn reward       │
│       └─ turn['biavr_reward'] = r                                   │
│       └─ turn['action_changed'] = ac                                │
│                                                                     │
│    7. ctx_manager.formulate_rollouts(rollout_states)                │
│       └─ biavr_reward folded into turn_scores if use_turn_scores    │
└─────────────────────────────────────────────────────────────────────┘
```

## 4. Integration Points (RAGEN Code)

### 4.1 Primary Integration: `agent_proxy.py`

| Line | What | Integration |
|------|------|-------------|
| 192-214 | `LLMAgentProxy.__init__()` | Reads `config.biavr`, creates `BIAVRTracker` |
| 238-345 | `rollout()` main loop | Tracks `biavr_verify`, `biavr_changed` per turn |
| 296-308 | Inside turn loop | After `get_env_inputs()`, records verify decisions, triggers a_pre if enabled |
| 327-328 | After turn loop | Calls `_inject_biavr_rewards()` for training rollouts only |
| 347-377 | `_inject_biavr_rewards()` | Iterates rollout states, computes per-step B-IAVR reward via tracker |
| 380-409 | `_build_a_pre_inputs()` | Builds no-guidance prompt from conversation history |
| 411-435 | `_compute_and_update_a_pre()` | Orchestrates a_pre generation + action comparison |
| 437-503 | `_generate_a_pre_greedy()` | vLLM/RayWorkerGroup greedy decode for counterfactual a_pre |

### 4.2 Secondary Integration: `ctx_manager.py`

| Line | What |
|------|------|
| 113-114 | `biavr_enabled` property (reads config.biavr) |
| 563 | System prompt: uses `build_biavr_system_prompt()` if biavr enabled |
| 645 | User prompt suffix: appends `build_biavr_user_prompt_suffix()` |
| 1419 | Sample building: handles biavr-specific scoring |
| 1613-1620 | `get_env_inputs()`: calls `parse_verify_token()` on LLM response |

### 4.3 Config Integration: `_alfworld_phase_b.yaml`

```yaml
biavr:
  beta: 0.3           # target verification rate
  alpha: 1.0           # action_changed reward weight
  lambda_init: 0.0     # initial Lagrangian multiplier
  eta: 0.01            # dual variable learning rate
  enable_a_pre: true   # compute a_pre for informativeness
```

## 5. Files Requiring Modification for Phase B

| File | Change |
|------|--------|
| `config/_alfworld_phase_b.yaml` | Update `model_path` to exp026 best checkpoint, add `agent_proxy.context_window_mode: step_independent`, add `wandb` to logger |
| `ragen/llm_agent/agent_proxy.py` | **No changes needed** — B-IAVR hooks already wired in |
| `ragen/llm_agent/ctx_manager.py` | Verify `biavr_reward` is correctly aggregated into `turn_scores` for step-independent mode (line ~1040) |
| `ragen/biavr/reward.py` | Potentially tune `BIAVRTracker` defaults or add W&B metric logging |
| Training entry point | Ensure `biavr_tracker.update_lambda()` is called at end of each training step for Lagrangian update |

## 6. Risk Analysis

### 6.1 Compute Overhead of a_pre Rollout
- **Per-turn cost**: One extra greedy decode (max 256 tokens) per verifying environment
- **Worst case**: If verify_rate ~ 30% (target beta), ~30% of environments need a_pre each turn
- **Estimate**: With 4 env_groups x 16 group_size = 64 envs, ~19 extra greedy decodes per turn
- **Latency**: vLLM batched greedy decode of 19 x 256 tokens ~ 1-2 seconds on RTX PRO 6000
- **Mitigation**: `enable_a_pre: false` disables entirely; can also set `max_tokens: 128` for shorter decodes

### 6.2 Memory Requirements
- a_pre greedy decode reuses the same vLLM instance (no additional model copy)
- For RayWorkerGroup path: creates temporary DataProto with new input_ids (batch size = # verifying envs)
- **Peak additional memory**: ~200MB for tokenized inputs + KV cache of 19 sequences x 256 tokens
- GPU memory utilization set at 0.4 in exp026 — sufficient headroom on 98GB RTX PRO 6000

### 6.3 Correctness Risks
- **Action parsing failure**: If `extract_action_from_response()` returns None (no `<answer>` tag), `compare_actions()` returns False (conservative: not informative). Safe but may undercount informativeness.
- **Lagrangian instability**: `eta=0.01` is conservative. If verify_rate oscillates, lambda may grow unbounded. Monitor `biavr/lambda` in W&B; consider clamping `lambda_cost <= 2.0`.
- **step_independent mode interaction**: exp026 uses `context_window_mode: step_independent`. The `_build_a_pre_inputs()` method extracts history from env_outputs, which should be compatible. Verify that `step_independent_history_length` truncation is applied consistently to both a_post and a_pre prompts.

### 6.4 Integration Gaps
- `_alfworld_phase_b.yaml` is outdated (references `exp_003`, missing `step_independent` config, wandb disabled)
- Lambda update (`biavr_tracker.update_lambda()`) call site unclear — not found in current training loop. Must be added to the GRPO training step callback.
- `env_configs.tags` uses `AlfworldBIAVR` in phase_b config but exp026 uses `AlfworldSG` — need to verify if B-IAVR requires a different env tag or if the same tag works.
