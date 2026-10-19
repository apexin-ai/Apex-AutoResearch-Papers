# Server Status Check — 2026-05-16

## PID 状态

| PID | 任务 | GPU | 状态 | 备注 |
|-----|------|-----|------|------|
| 195242 | lm_eval_mistral_kl_50pct | cuda:1 | **RUNNING** (53min) | GSM8K generate_until 941/1319 (71%), 预计约17min完成 |
| 194814 | lm_eval_teal_30pct | cuda:0 | **DEAD** (已完成) | 结果已在 results/lm_eval_teal_30pct/ |

## GPU 使用情况

| GPU | VRAM 使用 | 利用率 | 状态 |
|-----|-----------|--------|------|
| cuda:0 | 18,327 / 97,887 MiB | 0% | **空闲可用** |
| cuda:1 | 62,082 / 97,887 MiB | 95% | 忙 (Mistral eval) |

## 已完成的 Eval 结果汇总

### 关键 Benchmark 对比表

| 方法 | Sparsity | ARC-c | WinoGrande | MMLU | GSM8K (flex) |
|------|----------|-------|------------|------|--------------|
| **Llama dense** | 0% | 0.5819 | 0.7814 | 0.6532 | 0.5004 |
| **Mistral dense** | 0% | 0.6024 | 0.7869 | 0.6244 | 0.3654 |
| KL distill (kl_30pct) | 30% | 0.3575 | 0.6756 | 0.2874 | 0.0781 |
| KL distill (kl_s42) | 30% | 0.3063 | 0.6212 | 0.2359 | 0.0197 |
| Vanilla TEAL 30% | 30% | 0.3933 | 0.6559 | 0.3598 | 0.0925 |
| Vanilla TEAL 50% | 50% | 0.2491 | 0.5556 | 0.2856 | 0.0190 |
| **Mistral KL 50%** | 50% | — | — | — | — |

### 分析

- **Mistral KL 50% eval 尚未完成**，预计 ~17min 后出结果
- Vanilla TEAL 30% 是目前 30% sparsity 下表现最好的方法（ARC 0.3933, MMLU 0.3598）
- 所有 sparse 方法相比 dense baseline 仍有较大差距：ARC 最好 0.3933 vs dense 0.6024，MMLU 最好 0.3598 vs 0.6244
- GSM8K 在所有 sparse 模型上几乎崩溃（<10% vs dense 36.5%+）

## 结论

- **cuda:0 立即可用**，无活跃进程
- **cuda:1 预计 ~17min 后释放**（Mistral KL 50% eval 接近完成）
- Mistral eval 完成后需及时收取结果并与 dense baseline 对比
