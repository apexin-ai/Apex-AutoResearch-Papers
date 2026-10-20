# Memory

## GPT2-Medium 355M Scaling 关键发现 (2026-05-14)

355M 上 RGDS vs Uncurated 排序与 125M **相反**：
- 125M: RGDS (74.29) >> Uncurated (47.04) — RGDS 最差
- 355M: RGDS (82.84) < Uncurated (91.66) — RGDS 反而优于 Uncurated

**原因**：355M 的 baseline collapse 极度严重（Uncurated +245%），50% 数据裁剪的正则化效应足以抵消 alignment gap 损害。

**但 C3 仍成立**：RGDS (82.84) > Random 50% (70.25)，alignment gap 相对于同 budget random 仍有害（+18%）。

**355M 四方法完整排序 (seed=42)**：Random (70.25) < External (77.74) < RGDS (82.84) < Uncurated (91.66)

**论文叙事影响**：不能简单说"RGDS 是最差的"——需要按 scale 区分。核心 claim 应锚定在"同 budget 内 RGDS 劣于 Random"（C3），而非 RGDS vs Uncurated 的绝对排序。

## 355M 统计检验方法论 (2026-05-14)

Bootstrap CI (10000 resamples) 是 2-seed 阶段的主要统计工具（配对 t-test 需 ≥3 seed）。关键发现：
- RGDS vs Random-50 (+15.15, CI 排除零) 和 RGDS vs External (+7.90, CI 排除零) 在 2-seed 下已显著
- RGDS vs Uncurated (-2.81, CI 含零) 在 355M 不显著——这是 scaling narrative 的统计基础
- **不对称 gap 收窄**量化：125M→355M 收窄 57-109%，所有 CI 排除零，是论文 scaling 论证的核心证据

## 355M 3-seed 全量 t-test 关键结果 (2026-05-14)

- **C3 强显著**: RGDS vs Random50 PPL p=0.0100, d=5.73, diff=+15.74
- **RGDS vs Uncurated 完全不显著**: p=0.8868 — 355M 下两者 PPL 无差距
- **边界 case**: ext vs random50 PPL p=0.0507 — 未达显著，论文报告为 marginal
- **Uncurated 方差问题**: SD=6.95, CV=8.1%, seed=456(78.00) 是 outlier，导致所有涉及 Uncurated 的 PPL t-test 偏保守

## Alignment Gap 机制的 Scale 依赖性 (2026-05-14)

**关键跨 scale 发现**：RGDS 选择偏差在 355M 消失。
- 125M: RGDS 强烈选择低 PPL 样本（Cohen's d=-1.11, Gen 4）→ 加速 collapse
- 355M: 无系统性差异（Cohen's d=0.09, Gen 4; d=0.01, Gen 7）

解释：gpt2-medium 生成的样本 PPL 分布更窄（mean≈1.8），diversity score 不再与 PPL 高度相关。这直接支持"表征冗余缓冲"假说——更大模型的表征空间足够丰富，内部嵌入 diversity 不再与语义模板化强耦合。

**论文叙事价值**：这是 alignment gap scale-dependent 的直接证据，可以作为 Discussion 中 scaling narrative 的机制解释。

## 缓解方法诊断（已验证）(2026-05-14)

- **ADR/SemDeDup**: 近重复率 <9%（ε=0.70），去重空间不足 ❌
- **RPF (PPL Filter)**: Gen-0 PPL 分布 P99=2.1，信号太弱 ❌
- **External embedding**: 已验证有效（C2）✅

## tmux chain 最佳实践 (2026-05-14)

**教训**：tmux send-keys 方式不可靠。chain_cuda1 session 退出后 send-keys 无目标，导致 cuda:1 空闲 ~1h。

**正确做法**：所有 chain 用单个 bash 脚本串行执行（`script1.sh && script2.sh`），不用 send-keys 追加命令。跨 GPU 调度用 flag 文件 + while loop 等待机制。

## 训练超参一致性 (2026-05-13)

所有实验（125M 和 355M）使用完全相同的训练超参：lr=5e-5, AdamW, batch=4, grad_accum=8 (effective 32), max_len=512, 3 epochs/gen, 500K tokens/gen。不同方法之间唯一变量是 selection_method。
