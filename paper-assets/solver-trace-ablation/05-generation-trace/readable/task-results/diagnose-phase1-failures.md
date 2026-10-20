# diagnose phase1 failures

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_phase1-failures_20260513T193357_result.json`
- **Structured JSON:** [`4c10f4dc780d49ed42f5.json`](../../sessions/4c/4c10f4dc780d49ed42f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 根因

**argparse 的 `required=True` 在 YAML config 加载之前就触发了校验失败。**

脚本逻辑是先 `parse_args()`（第 178 行），再在 `main()` 里读 YAML config 覆盖参数（第 185-188 行）：

```python
args = parse_args()          # ← argparse 在这里就报错退出了
if args.config:              # ← 永远执行不到
    cfg = load_yaml_config(args.config)
```

`--model_path`、`--data_path`、`--reward_mode`、`--output_dir` 四个参数都设了 `required=True`，但命令行只传了 `--config`，所以 argparse 直接退出，EXIT_CODE=2。

此外 YAML 配置文件也缺少 `model_path` 和 `data_path` 两个字段。

### 完整错误信息

```
train_grpo.py: error: the following arguments are required: --model_path, --data_path, --reward_mode, --output_dir
EXIT_CODE=2
```

### 修复建议

需要改两处：

**1. 修改 `scripts/train_grpo.py` 的参数解析逻辑**——两阶段解析，先解析 `--config`，再用 YAML 值填充 defaults：

```python
def parse_args():
    parser = argparse.ArgumentParser(description="Phase 1 GRPO Training")
    parser.add_argument("--config", type=str, default=None,
                        help="YAML config file (overrides defaults)")
    # 先解析 config
    pre_args, _ = parser.parse_known_args()
    if pre_args.config:
        cfg = load_yaml_config(pre_args.config)
        parser.set_defaults(**cfg)

    # 其余参数改为非 required，由 config 或 CLI 提供
    parser.add_argument("--model_path", type=str, required=pre_args.config is None)
    parser.add_argument("--data_path", type=str, required=pre_args.config is None)
    parser.add_argument("--reward_mode", type=str, required=pre_args.config is None,
                        choices=["execution_only", "execution_sta"])
    parser.add_argument("--output_dir", type=str, required=pre_args.config is None)
    # ... 其余可选参数不变 ...
    return parser.parse_args()
```

**2. 在两个 YAML 配置中补上缺失字段：**

```yaml
# grpo_exec_only.yaml / grpo_exec_sta.yaml 各自加上：
model_path: /root/autodl-tmp/models/Qwen3-4B
data_path: data/proofwriter_fol_500.jsonl
```

需要我直接修复这两处吗？

---
