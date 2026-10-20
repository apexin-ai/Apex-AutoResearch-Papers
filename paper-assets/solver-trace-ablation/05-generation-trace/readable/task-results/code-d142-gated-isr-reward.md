# code d142 gated isr reward

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d142-gated-isr-reward_20260519T030919_result.json`
- **Structured JSON:** [`9efabfaa3cfb232b2404.json`](../../sessions/9e/9efabfaa3cfb232b2404.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 已清空。所有验证完成。

---

## D142 产出汇报

### 1. 修改的文件

**`/root/solver-trace-ablation/scripts/train_grpo.py`** — 两处修改：

- **Line 277-295**: 新增 `additive_bonus_gated` reward mode 分支
  ```python
  elif reward_mode == "additive_bonus_gated":
      result = _full_fn({}, cleaned, solver, execution_weight=1.0, sta_weight=1.0, timeout=5)
      execution_reward = result["execution_reward"]
      isr_val = result.get("sta_reward", 0.0)
      details = result.get("details", {})
      n_premises = len(details.get("premises", []))
      beta_t = compute_beta_t()
      gate = 1 if n_premises >= 2 else 0
      reward_val = execution_reward + beta_t * isr_val * gate
      # ... gated_total/h7_blocked/gated_passed tracking
  ```

- **Line 437**: argparse choices 添加 `"additive_bonus_gated"`

### 2. n_components 计算逻辑

`n_premises = len(details.get("premises", []))` — 使用 `_parse_formalization()` 解析后的 premise 列表长度，与 STA evaluate 的 premise 提取逻辑一致。

- H7 tautology（单前提=结论）: `n_premises=1` → gate=0 → ISR bonus 归零
- Genuine proof（多 premise 推导）: `n_premises≥2` → gate=1 → ISR bonus 正常

### 3. Dry-run 结果

**Gate 逻辑验证（静态测试）：**

| 样本 | n_premises | exec | ISR | gate | reward |
|------|-----------|------|-----|------|--------|
| H7: Cat(tom) |- Cat(tom) | 1 | 1.0 | 0.500 | 0 | 1.000 |
| Genuine-2prem | 2 | 1.0 | 0.667 | 1 | 1.067 |
| Genuine-3prem | 3 | 1.0 | 0.750 | 1 | 1.075 |
| Zero-prem | 0 | 0.0 | 0.000 | 0 | 0.000 |

**训练 dry-run（3 steps, seed=52）：**

| Step | reward | prove_rate | ISR | gate_pass | loss | grad_norm |
|------|--------|-----------|-----|-----------|------|-----------|
| 1 | 0.135 | 0.125 | 0.097 | 1.000 | - | - |
| 2 | 0.272 | 0.250 | 0.222 | 1.000 | 0.097 | 10.38 |
| 3 | 0.127 | 0.125 | 0.018 | 1.000 | 0.214 | 3.42 |

- 无 OOM，~10-15s/step（与 D134 一致）
- gate_pass=1.000 符合预期（base model 初期不产 H7）
- Loss 和 grad_norm 正常

### 4. 新增文件

- **Config**: `/root/solver-trace-ablation/configs/d142_gated_isr.yaml`
- **Pipeline**: `/root/autodl-tmp/d142_gated_isr_pipeline.sh`

### 5. 启动命令

```bash
# 在 tmux 中运行（串行跑 s52/s53/s54，每轮训练+eval+classify+cleanup）
tmux new-session -d -s d142 'bash /root/autodl-tmp/d142_gated_isr_pipeline.sh 2>&1 | tee /root/autodl-tmp/d142_pipeline.log'
```

---
