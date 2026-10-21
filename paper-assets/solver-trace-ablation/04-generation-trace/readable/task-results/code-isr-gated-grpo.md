# code isr gated grpo

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_isr-gated-grpo_20260516T141159_result.json`
- **Structured JSON:** [`9815334c9d07b7258ae2.json`](../../sessions/98/9815334c9d07b7258ae2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Implementation complete. Summary:

### 改动

**`scripts/train_grpo.py`** (+36 行):
1. `make_reward_fn` 新增 `isr_threshold` 和 `min_components` 参数
2. 新增 `isr_gated` reward 分支（L231-248）：调用 `_full_fn` 获取 exec + STA，若 `proved AND isr > tau AND n_components > min_components` → reward=1.0，否则 0.0
3. `step_buf` 新增 `gated_passed`/`gated_total` 计数，`get_step_stats()` 输出 `gate_pass_rate`
4. `LocalLogCallback` 打印 `gate_pass=X.XXX`
5. `parse_args` 新增 `--isr_threshold`（默认 0.3）和 `--min_components`（默认 2）参数
6. reward_mode choices 加入 `isr_gated`
7. 修复了 `optim=None` 传入 GRPOConfig 的 bug（`getattr` → `or "adamw_torch"`）

**`configs/grpo_isr_gated.yaml`**（新文件）：
- K=8, batch=2, grad_accum=4, lr=1e-6, 500 steps, tau=0.3, min_components=2

### Dry-run 结果
1 step 成功完成，log 输出：
```
step=1 reward=0.5000 prove_rate=0.500 isr=0.400 parse_rate=1.000 gate_pass=1.000
```
ISR gating 逻辑正确触发（4 个 generation 中 2 个 proved，其中 2/2 通过 gate）。

### 性能预估
- exec-only 每 step ~2-3s（仅 1 次 solver 调用/sample）
- isr_gated 每 step ~10-30s（每个 proved sample 需要 N+1 次 solver 调用做 leave-one-out ablation，N=组件数，通常 3-8）
- 500 steps 预估 2-4 小时

### 注意事项
- K=8 + batch=2 在单张 A100 80GB 上 OOM。正式训练需用 batch=1 或双卡
- STA 超时设为 30s（`timeout=30`），比 exec-only 的 5s 更宽裕，因为 ablation 需要多次 solver 调用
- output_dir 指向 `/root/autodl-tmp/outputs/` 数据盘，遵守 C003 磁盘约束

---
