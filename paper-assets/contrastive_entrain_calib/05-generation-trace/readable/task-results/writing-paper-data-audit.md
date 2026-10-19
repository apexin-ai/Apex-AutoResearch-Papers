# writing paper data audit

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_paper-data-audit_20260525T083134_result.json`
- **Structured JSON:** [`88e9c1ddda9b7a17ea0d.json`](../../sessions/88/88e9c1ddda9b7a17ea0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。以下是完整审计报告。

---

## 数据一致性审计报告

### (a) 修改记录

| 文件 | 行号 | 旧值 | 新值 | 原因 |
|------|------|------|------|------|
| `appendix.tex` | L56 | "three consecutive declining checkpoints" | "three consecutive checkpoints showed no sustained improvement (..., all well below vanilla)" | Registry: gs=8 轨迹为 0.0844→0.0845→0.0538，第一步是微增(+0.0001)不是下降 |

### (b) 一致性核对结果：全部通过

6 处交叉核对均一致：

**AUROC 值**：
- Intro 用近似值 0.83/0.78，Framework/Direction Quality 用精确值 0.827±0.028 / 0.779±0.019 — 一致 ✓
- Registry truth: 0.8269±0.0278 (Qwen), 0.7793±0.0189 (Llama) — 四舍五入正确 ✓

**4/28 GRPO > vanilla**：Abstract、Intro(×2)、Discussion(×2)、Conclusion、Fig caption — 全部一致 ✓。14.3% = 4/28 ✓

**31/31 ACT > vanilla**：Abstract、Intro(×2)、Discussion、Conclusion、Fig caption — 全部一致 ✓。Registry 确认 16/16 (s1) + 15/15 (s2) = 31/31 ✓

**1,300-step lag**：Abstract、Intro(×2)、Probe Trap(×2)、Conclusion、Related Work、Limitations — 全部一致 ✓ (1840-500=1340≈1300)

**Entropy 0.70**：Abstract、Intro、Probe Trap table (0.702→0.70) — 一致 ✓

**Vanilla 0.134**：Main table、Ablation table footnote — 一致 ✓。Registry: 0.1335→0.134 ✓

### 主结果表 vs Registry 逐行核对

| 方法 | 论文 SYCONScore | Registry 值 | 匹配 |
|------|----------------|-------------|------|
| Vanilla | 0.134 | 0.1335 | ✓ |
| Cosine R1 (F1a-d) | 0.000 | collapse confirmed | ✓ |
| Binary Probe (F2) | 0.000 | exp-008v3: 0.000 | ✓ |
| Continuous Probe (F3) | 0.124 | exp-009: 0.1238 | ✓ |
| R3-only GRPO | 0.153 | exp-003 ckpt-6500: 0.1529 | ✓ |
| SFT probe (s2) | 0.393 | exp-008-seed2: 0.3928 | ✓ |
| SFT probe (s3) | 0.407 | exp-008-seed3: 0.4067 | ✓ |
| ActAdd α=5 | 0.054 | exp-016: 0.0537 | ✓ |
| ACT s1 | 0.301 | exp-004 ckpt-8000: 0.3013 | ✓ |
| ACT s2 | 0.286 | exp-004-s2 ckpt-7000: 0.2858 | ✓ |

### Ablation 表 vs Registry

| 方法 | 论文 Best | Registry | 匹配 |
|------|----------|----------|------|
| GRPO gs=2 | 0.153, 4/28 | 0.1529, 4/28 | ✓ |
| GRPO gs=8 | 0.085, 0/3 | 0.0845, 0/3 | ✓ |
| ACT reduced | 0.326, 16/16 | 0.3257, 16/16 | ✓ |
| ACT full s1 | 0.301, 16/16 | 0.3013, 16/16 | ✓ |
| ACT full s2 | 0.286, 15/15 | 0.2858, 15/15 | ✓ |

### Direction Quality 表 vs Registry

| 指标 | 论文 | Registry | 匹配 |
|------|------|----------|------|
| Qwen L19 AUROC | 0.827±0.028 | 0.8269±0.0278 | ✓ |
| Qwen weak/med/strong | 0.675/0.883/0.929 | 0.675/0.883/0.929 | ✓ |
| Llama L16 AUROC | 0.779±0.019 | 0.7793±0.0189 | ✓ |
| Llama weak/med/strong | 0.711/0.864/0.911 | 0.7106/0.8635/0.9109 | ✓ |
| Probe vs random | 0.835 vs 0.727 (Δ+0.108) | 0.835/0.727/0.108 | ✓ |

### (c) 占位符检查

搜索 `XX.X`, `TBD`, `TODO`, `FIXME`, `??`, `PLACEHOLDER`, `\cite{?}`, `\ref{?}` — **无占位符**。

### (d) 需要 Director 确认的问题

1. **Discussion held-out 0.205 的来源**：`discussion.tex` L87 写 "held-out $0.205$, $3.7{\times}$ vanilla"。Registry 中 ACT s1 ckpt-500 held-out = 0.2045→0.205，ckpt-8000 held-out = 0.2841。用 ckpt-500 的 held-out 值而非最佳 checkpoint 的，是否有意为之？如果是报告最佳 checkpoint 的 held-out，应改为 0.284。

2. **Cosine failure 两处 AUROC 基线差异**：`cosine_failure.tex` L4 写 "from 0.827 to approximately 0.60"，L30 写 "from 0.76 (full response) to 0.60"。前者是离线 CV AUROC→截断后 AUROC，后者是训练时全长→截断 AUROC。两处描述不同测量语境，可能让读者误以为矛盾。建议确认是否需要加一句澄清。

3. **Probe gaming onset 的 "~30 steps"**：`probe_trap.tex` L10 写 "within ~30 steps"，L11 写 "both collapse within ~50 steps"。Registry 显示两个 seed 分别在 ~50 和 ~60 步 onset。~30 偏低，但因为是近似值（~），不一定需要修改。

---
