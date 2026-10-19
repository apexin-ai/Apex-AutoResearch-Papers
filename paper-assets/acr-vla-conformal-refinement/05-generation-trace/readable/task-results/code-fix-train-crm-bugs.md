# code fix train crm bugs

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-train-crm-bugs_20260513T041426_result.json`
- **Structured JSON:** [`5533941531597dd27364.json`](../../sessions/55/5533941531597dd27364.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 修复报告

### Bug 1: `--horizon` 参数
**状态**: 无需修复。确认 `src/utils.py` 中 `H_EFF=5` 存在，`train_crm.py` argparse 无 `--horizon` 参数。

### Bug 2: `--benchmark` 多值支持
**改动**:
- argparse: `nargs='+'`, `default=["spatial"]`，choices 保留（对列表中每个值校验）
- `precompute_features()`: 重构为先检查哪些 benchmark 需要 precompute，加载 SmolVLA 一次，然后循环处理每个 benchmark
- `train()`: 循环加载所有 benchmark 的 cache 并 `torch.cat` 合并
- `main()` auto 模式: `any()` 检查所有 benchmark 是否有 cache

### Bug 3: augmentation loss target
**改动**: 原来对 expert target 加噪声、用 clean input 给 CRM——方向反了。修复为：
```python
ma_noise = noise_scale.repeat(H_EFF)           # (30,) 匹配 mean_action 维度
aug_ma = ma[:n_aug] + randn_like * ma_noise     # 扰动 mean action 输入
aug_uf = uf[:n_aug] + randn_like * noise_scale.mean() * 0.1  # 扰动 uncertainty features
aug_refined = crm(aug_ma, aug_uf, obs_feat[:n_aug])  # noisy input
aug_loss = loss_fn(aug_refined, expert_flat[:n_aug])  # clean target
```

### verify_pipeline.py 输出
**ALL CHECKS PASSED** — 12/12 维度检查通过（action_dim=6, CGS=40D, CRM input=1030D, output=30D）

### train_crm.py --help
`--benchmark` 正确显示为 `{object,spatial,goal,long,90} [{...} ...]`，无 `--horizon`

### dry-run 结果
- 参数解析正确: `'benchmark': ['spatial']`
- SmolVLA 加载成功: `VLM hidden_size = 960`
- LIBERO 数据加载成功: `1231 training samples from 10 trajectories`
- 无 crash/报错，被 120s timeout 正常终止

### 推荐完整训练命令

```bash
# Phase 1: Precompute (spatial + object)
python src/train_crm.py --precompute --benchmark spatial object --K 10

# Phase 2: Train
python src/train_crm.py --benchmark spatial object --epochs 50 --batch_size 32 --lr 1e-3 --seed 42
```

---
