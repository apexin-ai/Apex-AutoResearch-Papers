# exp009 分析报告

## 配置摘要

| 项目 | 值 |
|------|-----|
| 模型 | Qwen3-1.7B (SFT warmup checkpoint) |
| 模型路径 | `/root/autodl-tmp/checkpoints/exp008_sft/final` |
| 算法 | GRPO |
| 总步数 | 30 |
| 轨迹数/步 | 64 (8 env_groups × 8 group_size) |
| max_turn | 30 |
| collapse_detection | off |
| KL coef | 0.01 |
| lr | 1e-6 |
| response_length | 1024 |
| GPU | 2× GPU (CUDA 0,1) |
| 配置文件 | `_alfworld_exp008_sft_grpo.yaml` |

## 训练进度

**完成步数: 0 / 30 — 训练从未启动**

日志仅 18 行，全部为启动错误信息。无 W&B run 产生，无 checkpoint 保存。

## 失败原因

**AssertionError** in `RAGEN/train.py:137`:

```
assert ("qwen" in config.model_path.lower() or "llama-3" in config.model_path.lower()) or (not config.enable_response_mask)
```

- `model_path` = `/root/autodl-tmp/checkpoints/exp008_sft/final` — 不包含 "qwen" 或 "llama-3"
- `enable_response_mask` = `True` (base.yaml 默认值，GRPO 配置未覆盖)
- 模型实际上 **是** Qwen3ForCausalLM (`config.json` 中 `model_type: "qwen3"`)，但路径检查基于字符串匹配而非模型架构，导致误报

## 关键指标

无数据。训练未启动，无指标产生。

## vs 前序实验对比

| 指标 | exp007 (无 SFT) | exp008_sft | exp009 (SFT→GRPO) |
|------|-----------------|------------|-------------------|
| success_rate | 0.0625 | N/A (SFT) | N/A (未启动) |
| action_is_valid | 0.0835 | 0.9 | N/A |
| 状态 | DONE | DONE | FAILED |

## 结论判定

- **status**: FAILED (技术故障，训练未启动)
- **conclusion**: 无法判定。假设未经测试。
- success_rate >= 76%? → **无法评估**
- 学习信号是否有效? → **无法评估**

## 修复方案

在 `_alfworld_exp008_sft_grpo.yaml` 中添加一行即可修复：

```yaml
enable_response_mask: False
```

或将 checkpoint 路径改为包含 "qwen" 的路径（如软链接）：

```bash
ln -s /root/autodl-tmp/checkpoints/exp008_sft/final /root/autodl-tmp/checkpoints/exp008_sft_qwen3/final
```

然后更新配置中的 `model_path`。

**推荐方案**: 添加 `enable_response_mask: False`，因为 response mask 对 GRPO 训练稳定性有帮助但不是必须的，且该断言检查逻辑有 bug（应检查 model_type 而非路径字符串）。如果需要保留 response mask，则改用路径方案。

## 建议下一步

1. **立即修复配置**：在 GRPO yaml 中显式设置 `enable_response_mask`
2. **重跑 exp009**：配置修复后重新启动训练
3. **考虑修复断言逻辑**：`train.py:137` 的检查应基于 `config.json` 的 `model_type` 而非路径字符串匹配
