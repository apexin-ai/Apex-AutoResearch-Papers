# code d097 config fix

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d097-config-fix_20260516T031042_result.json`
- **Structured JSON:** [`783572eac28a7c0b6921.json`](../../sessions/78/783572eac28a7c0b6921.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Config merge 正常工作：`num_steps=500`（来自 config），`num_generations=8`（来自 config，fallback 是 4）。

## 结论

**代码已经修复了。** 当前 `parse_args()` 的状态：

1. **所有 `add_argument` 的 default 已经是 `None`**（除 `--no_wandb` 的 `store_true` 和 `--config`）
2. **Config merge 逻辑正确**：先加载 YAML，对每个 key，仅当 `current is None` 时才从 config 覆盖
3. **Fallback 字典位置正确**：在 config merge 之后，仅填充仍为 None 的参数
4. **`reward_mode` choices 已包含所有 6 种模式**：`execution_only`, `execution_sta`, `random_reward`, `additive_bonus`, `additive_random`, `execution_fast_sta`

验证结果：用 `grpo_additive_bonus.yaml`（`num_steps: 500`）测试，`parse_args()` 返回 `num_steps=500`，而非 fallback 的 100。config 中的 `num_generations: 8` 也正确覆盖了 fallback 的 4。

**不需要做任何修改。**

### 附：完整 parse_args() 代码（当前版本，line 354+）

```python
def parse_args():
    parser = argparse.ArgumentParser(description="Phase 1 GRPO Training")
    parser.add_argument("--model_path", type=str, default=None)
    parser.add_argument("--data_path", type=str, default=None)
    parser.add_argument("--reward_mode", type=str, default=None,
                        choices=["execution_only", "execution_sta", "random_reward", "additive_bonus", "additive_random", "execution_fast_sta"])
    parser.add_argument("--output_dir", type=str, default=None)
    parser.add_argument("--num_steps", type=int, default=None)
    parser.add_argument("--per_device_batch_size", type=int, default=None)
    parser.add_argument("--gradient_accumulation_steps", type=int, default=None)
    parser.add_argument("--num_generations", type=int, default=None)
    parser.add_argument("--max_completion_length", type=int, default=None)
    parser.add_argument("--learning_rate", type=float, default=None)
    parser.add_argument("--exec_weight", type=float, default=None)
    parser.add_argument("--sta_weight", type=float, default=None)
    parser.add_argument("--beta", type=float, default=None, ...)
    parser.add_argument("--beta_schedule", type=str, default=None, choices=["fixed", "linear", "sigmoid"], ...)
    parser.add_argument("--beta_schedule_midpoint", type=int, default=None, ...)
    parser.add_argument("--seed", type=int, default=None)
    parser.add_argument("--solver", type=str, default=None)
    parser.add_argument("--logic_type", type=str, default=None, choices=["fol", "prolog"])
    parser.add_argument("--wandb_project", type=str, default=None)
    parser.add_argument("--wandb_run", type=str, default=None)
    parser.add_argument("--no_wandb", action="store_true")
    parser.add_argument("--warmup_ratio", type=float, default=None)
    parser.add_argument("--config", type=str, default=None, ...)
    args = parser.parse_args()

    # Config merge: YAML values fill in None args
    if args.config:
        cfg = load_yaml_config(args.config)
        for k, v in cfg.items():
            if hasattr(args, k):
                current = getattr(args, k)
                if current is None or (isinstance(v, bool) and v and not current):
                    setattr(args, k, v)
            else:
                setattr(args, k, v)

    # Fallbacks: only apply when still None after config merge
    if args.num_steps is None:          args.num_steps = 100
    if args.per_device_batch_size is None: args.per_device_batch_size = 4
    if args.gradient_accumulation_steps is None: args.gradient_accumulation_steps = 2
    if args.num_generations is None:    args.num_generations = 4
    if args.max_completion_length is None: args.max_completion_length = 512
    if args.learning_rate is None:      args.learning_rate = 1e-6
    if args.exec_weight is None:        args.exec_weight = 0.5
    if args.sta_weight is None:         args.sta_weight = 0.5
    if args.beta is None:               args.beta = 0.3
    if args.beta_schedule is None:      args.beta_schedule = "fixed"
    if args.beta_schedule_midpoint is None: args.beta_schedule_midpoint = 250
    if args.seed is None:               args.seed = 42
    if args.warmup_ratio is None:       args.warmup_ratio = 0.0
    if args.solver is None:             args.solver = "prover9"
    if args.logic_type is None:         args.logic_type = "fol"

    missing = [f for f in ("model_path", "data_path", "reward_mode", "output_dir")
               if getattr(args, f, None) is None]
    if missing:
        parser.error(f"the following arguments are required: {', '.join('--' + f for f in missing)}")

    return args
```

### 附：所有 config 文件内容

| Config | num_steps | beta | reward_mode |
|--------|-----------|------|-------------|
| grpo_additive_bonus.yaml | 500 | 0.3 | additive_bonus |
| grpo_additive_bonus_b01.yaml | 500 | 0.1 | additive_bonus |
| grpo_additive_random.yaml | 500 | 0.3 | additive_random |
| grpo_additive_random_b01.yaml | 500 | 0.1 | additive_random |
| grpo_exec_only.yaml | 100 | - | execution_only |
| grpo_exec_only_8b.yaml | 50 | - | execution_only |
| grpo_exec_sta.yaml | 100 | - | execution_sta |
| grpo_fast_isr_ablation.yaml | 500 | - | execution_fast_sta |
| grpo_prolog_exec_only.yaml | 500 | - | execution_only |
| grpo_prolog_exec_only_k16_warmup.yaml | 500 | - | execution_only |
| grpo_prolog_exec_sta.yaml | 500 | - | execution_sta |
| grpo_random_reward.yaml | 500 | - | random_reward |
| plan018_random_b01_s43.yaml | 500 | 0.1 | additive_random |
| plan018_random_b01_s44.yaml | 500 | 0.1 | additive_random |

sweep-isr-b005-s42 和 sweep-isr-b01-s45 对应的 config 不在 configs/ 目录中。如果这两个实验没有用 `--config` 启动（或用的 config 里没有 `num_steps`），就会 fallback 到 100 步——这是行为正确但调用方的问题，不是 parse_args 的 bug。

---
