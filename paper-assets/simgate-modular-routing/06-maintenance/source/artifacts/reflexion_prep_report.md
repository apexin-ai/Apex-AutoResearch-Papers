# Reflexion Baseline 实验代码准备报告

## 1. 现有代码架构（与 Reflexion 相关部分）

### 1.1 Episode 执行流程

```
episode_level_collection.py / collect_trajectories.py
  → LLMAgent (llm_agent.py)
    → select_action_react()      # internal modality: LLM ReAct 选 action
    → generate_candidate_actions() # deterministic modality: LLM 生成 candidates
  → scienceworld_utils.py
    → create_env() → reset_env() → step_env() → close_env()
    → fork_and_lookahead()       # deterministic: 创建 JVM fork 评估 candidate
```

### 1.2 核心函数

| 函数 | 文件 | 用途 |
|------|------|------|
| `run_episode_internal()` | `episode_level_collection.py` | 跑一个 always-internal episode，LLM ReAct 每步选 action |
| `run_episode_deterministic()` | `episode_level_collection.py` | 跑一个 always-deterministic episode，fork+lookahead 选最优 |
| `select_action_react()` | `llm_agent.py` | 标准 ReAct：observation+history → action |
| `select_action_deep_react()` | `llm_agent.py` | Deep internal：更长 CoT reasoning |
| `is_lethal()` / `is_dead()` | 多个文件 | death 判定：`score <= -100` |

### 1.3 当前 Death Rate 数据（Aggregate, 30 tasks, 249 episodes）

| 指标 | Internal | Deterministic |
|------|----------|---------------|
| Death rate | **49.0%** | 11.65% |
| Mean score | -47.49 | -9.16 |
| Mean score (no-death only) | 2.95 | 3.43 |
| DAF (death avoidance fraction) | — | **98.75%** |

核心发现：det-preferred 信号的 98.75% 来自 death asymmetry，排除 death 后 delta 仅 0.48。

### 1.4 Reflexion 相关代码现状

**不存在任何 Reflexion 相关代码。** 没有 `*reflex*`、`*retry*`、`*self_reflect*` 文件或配置。需要从零实现。

---

## 2. Reflexion 实现方案

### 2.1 核心机制（来自 Shinn et al., NeurIPS 2023）

Reflexion 的 loop：
1. **Trial 1**: 正常跑 episode → 得到 trajectory + outcome
2. **Self-Reflection**: LLM 看 trajectory 和 outcome，生成文本反思（"what went wrong, what to do differently"）
3. **Trial 2**: 把 reflection 注入 agent prompt，重跑**同一 task+variation** → 新 trajectory + outcome
4. **重复**: 最多 K 次（通常 K=3）

### 2.2 新增文件

#### (1) `src/reflexion_baseline.py` — 主实验脚本（~200 行）

```python
"""Reflexion baseline: self-reflection + retry for internal modality death rate reduction.

Hypothesis: If Reflexion reduces internal death rate to <20%, 
death dominance is no longer the primary routing signal.

For each task/variation:
  1. Run episode (internal mode)
  2. If failed (death or score <= 0), generate self-reflection
  3. Retry same task/variation with reflection in context
  4. Repeat up to max_trials times

Output:
  {output_dir}/{task}/reflexion_episodes.jsonl  — all trials per variation
  {output_dir}/{task}/reflexion_summary.jsonl   — per-variation summary
  {output_dir}/aggregate_report.json            — death rate per trial

Usage:
  python src/reflexion_baseline.py \
    --task_types "boil,melt,change-the-state-of-matter-of" \
    --episodes 20 --max_trials 3 --gpu_id 0
"""
```

**关键函数设计：**

```python
def run_reflexion_episode(
    agent: LLMAgent,
    task_name: str,
    variation_idx: int,
    max_steps: int,
    max_trials: int = 3,
) -> Dict[str, Any]:
    """Run up to max_trials of the same task/variation with self-reflection."""
    
    reflections = []  # accumulated reflection texts
    all_trials = []
    
    for trial_idx in range(max_trials):
        # Run episode with reflections in context
        result = run_episode_with_reflections(
            agent, task_name, variation_idx, max_steps, reflections
        )
        all_trials.append({
            "trial_idx": trial_idx,
            "final_score": result["final_score"],
            "is_death": result["final_score"] <= DEATH_THRESHOLD,
            "num_steps": result["num_steps"],
            "trajectory_summary": summarize_trajectory(result),
            **result,
        })
        
        # Success: stop retrying
        if result["final_score"] > 0:
            break
        
        # Generate self-reflection for next trial
        if trial_idx < max_trials - 1:
            reflection = generate_self_reflection(
                agent, task_name, result, reflections
            )
            reflections.append(reflection)
    
    return {
        "task_name": task_name,
        "variation_idx": variation_idx,
        "n_trials": len(all_trials),
        "trials": all_trials,
        "final_trial_score": all_trials[-1]["final_score"],
        "final_trial_death": all_trials[-1]["is_death"],
        "death_trajectory": [t["is_death"] for t in all_trials],
        "reflections": reflections,
    }


def run_episode_with_reflections(
    agent: LLMAgent,
    task_name: str,
    variation_idx: int,
    max_steps: int,
    reflections: List[str],
) -> Dict[str, Any]:
    """Same as run_episode_internal but injects reflections into agent prompt."""
    
    env = create_env(task_name, variation_idx)
    obs, _ = reset_env(env)
    steps, history_dicts = [], []
    
    for step_idx in range(max_steps):
        valid_actions = get_valid_actions(env)
        if not valid_actions:
            break
        
        # Key difference: pass reflections to agent
        action, raw = agent.select_action_react_with_reflections(
            obs, valid_actions, history_dicts, reflections
        )
        
        obs_new, reward, done, info = step_env(env, action)
        score_after = get_score(env)
        
        steps.append({
            "step_idx": step_idx,
            "observation_text": obs[:500],
            "action_text": action,
            "score_before": get_score(env),  # before step
            "score_after": score_after,
            "score_delta": score_after - get_score(env),
            "is_death": score_after <= DEATH_THRESHOLD,
            "done": done,
        })
        history_dicts.append({
            "action": action,
            "observation": obs_new[:200],
            "score": score_after,
        })
        obs = obs_new
        if done:
            break
    
    final_score = get_score(env)
    close_env(env)
    return {
        "final_score": final_score,
        "steps": steps,
        "num_steps": len(steps),
        "total_time_s": ...,
    }


def generate_self_reflection(
    agent: LLMAgent,
    task_name: str,
    episode_result: Dict,
    previous_reflections: List[str],
) -> str:
    """Generate verbal self-reflection on a failed episode."""
    
    trajectory_summary = summarize_trajectory(episode_result)
    
    prompt = REFLECTION_PROMPT_TEMPLATE.format(
        task_name=task_name,
        final_score=episode_result["final_score"],
        is_death="YES - the agent died" if episode_result["final_score"] <= -100 else "No",
        trajectory_summary=trajectory_summary,
        previous_reflections=format_previous_reflections(previous_reflections),
    )
    
    messages = [
        {"role": "system", "content": REFLECTION_SYSTEM_PROMPT},
        {"role": "user", "content": prompt},
    ]
    return agent._generate(messages, temperature=0.3)


def summarize_trajectory(result: Dict) -> str:
    """Compact trajectory summary: last 5 steps before death + death step."""
    steps = result["steps"]
    if not steps:
        return "No steps taken."
    
    death_idx = None
    for i, s in enumerate(steps):
        if s.get("is_death"):
            death_idx = i
            break
    
    if death_idx is not None:
        start = max(0, death_idx - 4)
        relevant = steps[start:death_idx + 1]
    else:
        relevant = steps[-5:]
    
    lines = []
    for s in relevant:
        lines.append(
            f"Step {s['step_idx']}: action='{s['action_text']}' "
            f"score_delta={s['score_delta']:+.0f} obs='{s['observation_text'][:100]}'"
        )
    return "\n".join(lines)
```

#### (2) `src/llm_agent.py` 修改 — 新增 ~50 行

```python
# === 新增 prompt templates ===

REFLEXION_SYSTEM_PROMPT = """You are an agent interacting with a ScienceWorld text environment. 
Your goal is to complete the given task by choosing actions from the available action list.

You have attempted this task before and reflected on your mistakes. 
Use your reflections to avoid repeating past errors.

Use the following format for each step:
Thought: <your reasoning, considering past reflections>
Action: <exact action string from the valid actions list>

Rules:
- You MUST choose an action from the valid actions list. Do not invent actions.
- Actively use your reflections to guide decision-making.
- Avoid actions that led to failure in previous attempts."""

REFLEXION_USER_TEMPLATE = """Current observation:
{observation}

Valid actions:
{valid_actions_str}

Previous actions taken: {history_str}

{reflections_block}

Choose your next action, keeping your reflections in mind."""

REFLECTION_SYSTEM_PROMPT = """You are an expert at analyzing failed episodes in a ScienceWorld text game. 
Reflect on what went wrong and provide actionable advice for the next attempt."""

REFLECTION_USER_TEMPLATE = """Task: {task_name}
Final score: {final_score}
Death occurred: {is_death}

Trajectory summary:
{trajectory_summary}

{previous_reflections}

Analyze what went wrong. Focus on:
1. What specific actions led to failure or death?
2. What should the agent have done instead?
3. What general strategy should be followed next?

Provide a concise reflection (3-5 sentences) with concrete, actionable advice."""


# === 新增 LLMAgent 方法 ===

def select_action_react_with_reflections(
    self,
    observation: str,
    valid_actions: List[str],
    history: List[dict],
    reflections: List[str],
) -> Tuple[str, str]:
    """ReAct with accumulated self-reflections from previous trials."""
    
    if not reflections:
        return self.select_action_react(observation, valid_actions, history)
    
    reflections_block = "Your reflections from previous attempts:\n"
    for i, r in enumerate(reflections, 1):
        reflections_block += f"Attempt {i} reflection: {r}\n"
    
    messages = [
        {"role": "system", "content": REFLEXION_SYSTEM_PROMPT},
        {"role": "user", "content": REFLEXION_USER_TEMPLATE.format(
            observation=observation,
            valid_actions_str=_format_valid_actions(valid_actions),
            history_str=_format_history(history),
            reflections_block=reflections_block,
        )},
    ]
    raw = self._generate(messages)
    action = parse_action(raw, valid_actions)
    if action is None:
        action = valid_actions[0]
    return action, raw
```

#### (3) `scripts/run_reflexion_baseline.sh` — 启动脚本

```bash
#!/bin/bash
# Reflexion baseline experiment
# Hypothesis: self-reflection + retry reduces internal death rate to <20%

GPU_ID=${1:-0}
MAX_TRIALS=3
EPISODES=20
OUTPUT_DIR="results/reflexion_baseline"
SEED=42

# High death rate tasks (from death_decomposition_report.json)
HIGH_DEATH_TASKS="boil,melt,change-the-state-of-matter-of,chemistry-mix-paint-secondary-color,chemistry-mix"
MEDIUM_DEATH_TASKS="freeze,grow-plant,find-animal,find-non-living-thing"

echo "=== Reflexion Baseline ==="
echo "GPU: $GPU_ID | Trials: $MAX_TRIALS | Episodes: $EPISODES"

python src/reflexion_baseline.py \
    --task_types "$HIGH_DEATH_TASKS,$MEDIUM_DEATH_TASKS" \
    --episodes $EPISODES \
    --max_trials $MAX_TRIALS \
    --gpu_id $GPU_ID \
    --output_dir $OUTPUT_DIR \
    --seed $SEED \
    --use_vllm
```

### 2.3 对照组设计

| 条件 | 描述 | 目的 |
|------|------|------|
| **reflexion** | 带 self-reflection 的重试 | 测试 Reflexion 机制 |
| **retry-only** | 不带 reflection 的纯重试（`--no_reflection`） | 控制组：隔离 stochastic retry 效果 |
| **baseline (trial-1)** | 每个条件的 trial-1 结果 | 等同于现有 always-internal |

### 2.4 输出格式

```jsonl
// reflexion_episodes.jsonl
{
  "task_name": "boil",
  "variation_idx": 3,
  "n_trials": 3,
  "trials": [
    {"trial_idx": 0, "final_score": -100.0, "is_death": true, "num_steps": 16},
    {"trial_idx": 1, "final_score": -100.0, "is_death": true, "num_steps": 22},
    {"trial_idx": 2, "final_score": 10.0, "is_death": false, "num_steps": 28}
  ],
  "reflections": ["...", "..."],
  "death_trajectory": [true, true, false],
  "final_trial_score": 10.0,
  "final_trial_death": false
}
```

```json
// aggregate_report.json
{
  "per_trial_death_rate": {"trial_1": 0.49, "trial_2": 0.35, "trial_3": 0.25},
  "per_trial_mean_score": {"trial_1": -47.5, "trial_2": -30.0, "trial_3": -15.0},
  "reflexion_vs_retry_only": {
    "reflexion_trial3_death": 0.25,
    "retry_only_trial3_death": 0.40
  }
}
```

---

## 3. 启动命令草案

### 3.1 Dry Run（GPU 空闲后第一步）

```bash
python src/reflexion_baseline.py \
    --task_types "boil" \
    --episodes 2 \
    --max_trials 3 \
    --gpu_id 0 \
    --output_dir results/reflexion_dryrun \
    --seed 42 \
    --use_vllm
```

### 3.2 正式实验

```bash
# Reflexion 条件
python src/reflexion_baseline.py \
    --task_types "boil,melt,change-the-state-of-matter-of,chemistry-mix-paint-secondary-color,chemistry-mix,freeze,grow-plant,find-animal,find-non-living-thing,find-plant,find-living-thing" \
    --episodes 20 \
    --max_trials 3 \
    --gpu_id 0 \
    --output_dir results/reflexion_baseline \
    --seed 42 \
    --use_vllm 2>&1 | tee logs/reflexion_baseline.log

# Retry-only 对照组
python src/reflexion_baseline.py \
    --task_types "boil,melt,change-the-state-of-matter-of,chemistry-mix-paint-secondary-color,chemistry-mix,freeze,grow-plant,find-animal,find-non-living-thing,find-plant,find-living-thing" \
    --episodes 20 \
    --max_trials 3 \
    --no_reflection \
    --gpu_id 0 \
    --output_dir results/retry_only_baseline \
    --seed 42 \
    --use_vllm 2>&1 | tee logs/retry_only_baseline.log
```

### 3.3 时间估算

- 单 episode trial: ~30s (boil task baseline)
- 每 variation: ~30s x 3 trials + ~10s reflection = ~100s
- 20 episodes x 11 tasks x 100s = **~6.1 hours** (Reflexion)
- 加 retry-only 对照: **~12 hours total**
- 可用 2 GPU 并行: ~6 hours

---

## 4. 预计额外准备工作

### 4.1 必须做

1. **编写 `src/reflexion_baseline.py`** (~200 行) — 基于 `run_episode_internal()` 改造
2. **修改 `src/llm_agent.py`** (~50 行新增) — 添加 `select_action_react_with_reflections()` 和 prompt templates
3. **编写 `scripts/run_reflexion_baseline.sh`** (~20 行)

### 4.2 可选优化

4. **Trajectory summarization**: trajectory 太长放不进 context，采用方案 A（death step 前 5 步 + death step）
5. **分析脚本**: `scripts/analyze_reflexion_results.py`，生成 death rate 趋势图

### 4.3 无需做

- 不需要修改 `scienceworld_utils.py`（env 接口不变）
- 不需要新模型/新依赖（复用 Qwen2.5-7B-Instruct + vLLM）

---

## 5. 风险与注意事项

1. **Context length**: 3 trials reflections + step history 可能较长，但 Qwen2.5-7B-Instruct 支持 32K tokens，足够。需控制 trajectory summary 长度。

2. **Reflection 质量**: 7B 模型的 self-reflection 可能不够深刻。如果效果不佳，本身也是有价值的 negative result（说明 Reflexion 需要更强 backbone，routing 是更 cost-effective 的替代方案）。

3. **公平对比**: Reflexion 每个 variation 用 3x 计算量。论文中需明确讨论 compute overhead。

4. **环境确定性**: 同一 task+variation 的 `create_env` + `reset_env` 产生相同初始状态。LLM 的 stochasticity (temperature>0) 导致不同 trajectory，这是预期行为。
