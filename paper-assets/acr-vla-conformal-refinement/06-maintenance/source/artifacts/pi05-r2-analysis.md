# π0.5 Baseline Object seed42 r2 Analysis

## 结果

- **SR: 0.0%** (全线零)
- **Episodes: 200** (10 tasks × 20 rollouts)
- **完成时间**: 2026-05-21T03:40:07Z, exit code 0 (正常退出)
- **当前 quicktest** (PID 831620, 5 rollouts): task 0 也是 0% (0/5), 仍在运行

### Per-task breakdown (全部 0%)

| Task | SR | Successes/Total |
|------|----|-----------------|
| pick_up_the_alphabet_soup_and_place_it_in_the_basket | 0.0% | 0/20 |
| pick_up_the_cream_cheese_and_place_it_in_the_basket | 0.0% | 0/20 |
| pick_up_the_salad_dressing_and_place_it_in_the_basket | 0.0% | 0/20 |
| pick_up_the_bbq_sauce_and_place_it_in_the_basket | 0.0% | 0/20 |
| pick_up_the_ketchup_and_place_it_in_the_basket | 0.0% | 0/20 |
| pick_up_the_tomato_sauce_and_place_it_in_the_basket | 0.0% | 0/20 |
| pick_up_the_butter_and_place_it_in_the_basket | 0.0% | 0/20 |
| pick_up_the_milk_and_place_it_in_the_basket | 0.0% | 0/20 |
| pick_up_the_chocolate_pudding_and_place_it_in_the_basket | 0.0% | 0/20 |
| pick_up_the_orange_juice_and_place_it_in_the_basket | 0.0% | 0/20 |

## 环境验证

| Fix | Status | 验证方式 |
|-----|--------|---------|
| MEAN_STD normalization | ✅ OK | 代码 + stats 文件验证: state mean [8], action mean [7], 数值合理 |
| Image [-1,1] for SigLIP | ✅ OK | 代码确认: `img * 2.0 - 1.0` (pi05_wrapper.py:150) |
| Vision tower key remapping | ✅ OK | 日志确认: `[pi05] Fixed 437 vision tower keys` |
| Tokenizer padding_side right | ✅ OK | 代码确认: `self.tokenizer.padding_side = "right"` (pi05_wrapper.py:86) |
| TORCH_COMPILE_DISABLE=1 | ❌ 未设置 | /proc/831620/environ 中未发现该变量 |

### Normalizer Stats 验证
```
State mean:  [-0.0465,  0.0344,  0.7646,  2.9722, -0.2205, -0.1256,  0.0269, -0.0272]
State std:   [ 0.1049,  0.1518,  0.3785,  0.3443,  0.9069,  0.3254,  0.0142,  0.0141]
Action mean: [ 0.0628,  0.0868, -0.0904,  0.0005,  0.0056, -0.0052, -0.0496]
Action std:  [ 0.3355,  0.3784,  0.4447,  0.0392,  0.0634,  0.0780,  0.9988]
```
文件: `policy_preprocessor_step_2_normalizer_processor.safetensors` (7668 bytes)

### Tokenizer 验证
- 独立测试确认: `padding_side="right"` 时 tokenizer 正确编码 prompt (BOS + content + padding)
- diag_pi05.log 中出现 all-pad tokens → 可能来自旧版代码(padding_side 修复前)

## 诊断日志摘要 (diag_pi05.log)

```
Model dtype: torch.bfloat16
Obs features shape: [1, 2048], range: [-12.82, 19.99]
Samples shape: [1, 2, 50, 7]  (K=2, horizon=50, action_dim=7)

Sample 0 first step: [-0.331, 0.253, -0.300, 0.013, -0.020, 0.184, 0.981]
Sample 1 first step: [-0.305, 0.118, -0.361, 0.028, -0.064, 0.249, 0.968]

Gripper values (所有 sample): 全部 ~0.97-0.98 (始终 open)
```

**异常**: 
- 所有 sample 的 gripper 值恒定 ~0.98 (open), 机器人永远无法抓取
- lerobot native API 崩溃: `AssertionError: both a fallback and a decomp for same op: aten.addmm.default` (torch.compile 兼容性问题)

## 失败根因分析

尽管 5 个已知 fix 均已在代码中实现，SR 仍为 0%。可能的深层原因：

1. **Action space mismatch**: 模型输出的 gripper 恒定 ~0.98, 无法完成 pick-and-place 任务。可能 training 时的 action 编码/解码与 inference 不一致
2. **Flow-matching 推理实现问题**: 自定义的 denoising loop 可能与 lerobot 原生实现不一致
3. **模型权重问题**: fine-tuned 权重可能未正确训练或转换
4. **TORCH_COMPILE_DISABLE 缺失**: 虽然不直接影响自定义 wrapper 路径，但可能有间接影响

## 结论

**NO-GO for π0.5 pipeline.**

0% SR (200 episodes) 表明问题不是随机波动，而是系统性故障。所有表面 fix (normalization, image range, vision tower, padding, torch.compile) 都已应用，但未解决根本问题。

### Plan B 评估
lerobot native API 也因 `torch.compile` / `aten.addmm.default` 错误而崩溃。需要：
- 设置 `TORCH_COMPILE_DISABLE=1` 后重试 native API
- 或降级 PyTorch / lerobot 版本解决兼容性问题
- 或使用 OpenPI 原始代码而非 lerobot 封装

### 建议下一步
1. 用 `TORCH_COMPILE_DISABLE=1` 重试 lerobot native API (`policy.predict_action_chunk`)
2. 对比 native API vs custom wrapper 的 action 输出
3. 如果 native API 也 0%, 需要验证 fine-tuned 模型本身是否有效 (在 OpenPI 原始 repo 中测试)
