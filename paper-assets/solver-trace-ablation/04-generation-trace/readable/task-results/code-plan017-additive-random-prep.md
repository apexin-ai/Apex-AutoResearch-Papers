# code plan017 additive random prep

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan017-additive-random-prep_20260514T030008_result.json`
- **Structured JSON:** [`651915580029b6078427.json`](../../sessions/65/651915580029b6078427.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

不是 git 仓库，无法 diff。改动很小——只在 `additive_random` 分支前添加了一行注释。

总结一下已完成的工作：

**现状**：`additive_random` reward mode 和配置文件都已存在。

**本次唯一改动**：在 `scripts/train_grpo.py` 第 197 行插入注释：
```python
# plan017: matched control for additive_bonus — random replaces ISR to isolate structural signal
```

**代码验证通过**：
- proved sample → `reward=1.0403` = `1.0 * (1 + 0.3 * 0.134)` ✓ 
- unproved/garbage sample → `reward=0.0` ✓

**配置文件** `configs/grpo_additive_random.yaml` 已就绪：
- `reward_mode: additive_random`, `beta: 0.3`, `seed: 42`
- `output_dir: /root/autodl-tmp/outputs/plan017_additive_random_s42`
- `data_path: data/train_500_seed42.jsonl`（符合 C001）

**未运行完整 GPU dry-run**：两张 GPU 各占 80GB VRAM，无空间加载第三个模型实例。reward 函数逻辑已通过 CPU 端单元测试验证。正式训练时分配空闲 GPU 即可。

---
