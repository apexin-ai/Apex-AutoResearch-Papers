# analysis exp 059 walker trained s5

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_059_walker_trained_s5_20260524T062221_result.json`
- **Structured JSON:** [`00877fb029a6c59ba14d.json`](../../sessions/00/00877fb029a6c59ba14d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新 (DONE/negative)。以下是完整分析：

## exp_059_walker_trained_s5 分析结果

### CIVO 判断
- **是否触发 CIVO：是**（ve_ratio 峰值 3.3 > 2.0 阈值 @ step 85K）
- **是否 sustained CIVO：否**（85K→95K 从 3.3 骤降至 0.6，105K 仅 0.8）
- 最终 ve_ratio：**0.8** @ step 105K
- Peak ve_ratio：**3.3** @ step 85K
- eval_return_final：**95.8**
- eval_return_peak：**188.3** @ step 55K
- 分类：**transient CIVO with self-correction**（~10K steps 内自修复）

### ve_ratio 演变轨迹
```
15K→25K→35K→45K→55K→65K→75K→85K→95K→105K
0.0→0.2→0.4→0.8→0.6→1.2→1.5→3.3→0.6→0.8
                                 ↑ spike   ↑ collapse back
```

### 与前 5 seeds 对比（Walker trained dt_emb + subsample ON + H=8）

| Seed | Exp ID | ve_ratio_peak | ve_ratio_final | NVE_peak | Classification | Conclusion |
|------|--------|---------------|----------------|----------|----------------|------------|
| s0 | exp_008d_subsample_on_h8 | high* | high* | high* | CIVO | success |
| s1 | exp_009e_008d_walker_s1 | 1.67 | 1.03 | 2.44 | transient | negative |
| s2 | exp_009b_008d_walker_s2 | 0.57 | 0.25 | 0.83 | no_civo | negative |
| s3 | exp_008d_civo_trigger_s3 | ~1.53 | ~1.53 | 1.53 | late-onset | success |
| s4 | exp_008d_civo_trigger_s4 | 3.03 | 3.03 | 4.44 | transient | success |
| **s5** | **exp_059_walker_trained_s5** | **3.3** | **0.8** | **—** | **transient** | **negative** |

*s0 (exp_008d) registry 中无 ve_ratio 明确数值，仅记录了 value/eval ratio 加速上升。

### 统计检验

**注意：hypothesis 中 "4/4 seeds triggered sustained CIVO" 与 registry 数据不一致。** 实际 registry 记录：
- s0: success (CIVO confirmed)
- s1: **negative** (transient, ve_ratio_peak=1.67)
- s2: **negative** (no_civo, ve_ratio_peak=0.57)
- s3: success (nve=1.53, late-onset)
- s4: success (ve_ratio_peak=3.03)
- s5: **negative** (transient, self-corrected)

按 "CIVO ever triggered"（ve_ratio > 2.0 at any point）统计：
- Triggered: s0, s4, s5 = 3/6 seeds (s3 的 ve_ratio 不明确，NVE=1.53 接近阈值)
- Binomial test (3/6 vs null p=0.5): p = 0.656, **不显著**

按 "sustained CIVO"（ve_ratio 在最后 25% 维持 > 2.0）统计：
- Sustained: s0 可能, s3 可能, s4 是（3.03@105K = final step）
- 最多 2-3/6 seeds，**不显著**

### W&B run ID
- 未使用 W&B（日志中无 wandb 相关输出）

### 关键观察
1. **s5 展现典型 transient CIVO pattern**：ve_ratio 在 65K-85K 攀升（1.2→1.5→3.3），伴随 eval 崩塌（97→77→29），但 95K 即自修复（ve_ratio→0.6, eval→133）。与 exp_045 的 s3 extended run 自修复 pattern 一致。
2. **Gate 完全锁死在 dt=2**（gate_dt_2_frac=1.0, entropy=0），整个训练过程 gate 未学习。
3. **hypothesis 中 "4/4 sustained CIVO" 的前提有误**：registry 显示 s1、s2 均为 negative，实际仅 3/6 seeds（含 s5）出现过 CIVO 触发，且多数为 transient。
4. **s5 的 CIVO 自修复速度极快**（仅 ~10K steps），暗示 105K 训练长度不足以区分 transient vs sustained — exp_045 显示延长到 300K 后 s3 也完全自修复（nve 4.91→0.052）。

---
