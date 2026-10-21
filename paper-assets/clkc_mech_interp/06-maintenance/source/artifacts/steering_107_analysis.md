## steering_107 分析结果

### Conclusion: failed

实验在第一个 steering 条件（alpha=-20.0）的第一个样本生成时崩溃，未产生任何 steering 结果。

### 核心指标
- steering_flip_rate_positive: N/A（脚本崩溃，未执行）
- steering_flip_rate_negative: N/A
- random_flip_rate: N/A
- best_layer: 28（探针峰值层，实验配置）
- best_alpha: N/A
- probe_accuracy_layer28: 77.57%
- baseline_distribution: {'both': 35, 'neither': 28, 'parametric': 32, 'contextual': 41}（136 conflict samples）
- orthogonality_check: dot=0.000000（探针方向与随机对照方向正交性验证通过）

### 详细分析

**崩溃原因**: `SteeringHook.__call__`（steering_experiment.py:119）假设 decoder layer 输出的 hidden states 为 3D tensor `(batch, seq, hidden_dim)`，使用 `h[:, -1, :] += self.alpha * d` 索引最后一个 token 位置。但 `model.generate()` 使用 KV cache 时，后续生成步骤中 hidden states 可能降为 2D tensor，导致 `IndexError: too many indices for tensor of dimension 2`。

**Baseline 阶段为何未崩溃**: Baseline 运行时 hook 未注册或 alpha=0（steering 未激活），因此未触发该代码路径。

**修复方向**: hook 需处理 2D/3D 两种情况：
```python
if h.dim() == 2:
    h += self.alpha * d
elif self.position == "last":
    h[:, -1, :] += self.alpha * d
```

**与 hypothesis 对比**: 无法评估。实验未完成任何 steering 条件，无 flip rate 数据，无法验证探针权重是否定义了知识冲突信号的因果方向。

**Baseline 观察**: 136 个冲突样本中，contextual=41（30.1%）、parametric=32（23.5%）、both=35（25.7%）、neither=28（20.6%）。模型在无干预时略倾向 contextual answer，但分布相对均匀，说明冲突数据集确实引发了模型的 parametric/contextual 竞争。

### Checkpoint/Log 路径
- log_path: /root/runs/clkc_mech_interp/steering_107.log
- log_path_alt: /root/clkc_mech_interp/logs/steering_llama.log
- results_path: N/A（未生成结果文件）
- source: /root/clkc_mech_interp/src/steering_experiment.py
- model: /root/models/Llama-3.1-8B-Instruct/
- activation_data: layer 28, dim 4096
