# code fig2 regenerate

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fig2-regenerate_20260519T130008_result.json`
- **Structured JSON:** [`7fc34b88c3c6475fe09c.json`](../../sessions/7f/7fc34b88c3c6475fe09c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

PDF 已重新生成。

**修改内容**：
- `scripts/plot_fig2_cross_attack_bar.py` 中 9-class stds 最后一个值：`0.005` → `0.006`（对齐 Table 1 的 0.997±0.006）

**确认**：脚本中所有 Full 列数值现在与 Table 1 一致：
| Variant | Mean | Std |
|---------|------|-----|
| Vanilla | 0.312 | 0.026 |
| MLM-only | 0.914 | 0.115 |
| 9-class | 0.997 | 0.006 |

**输出路径**：
- `/root/persuasion_turn_jailbreak_detect/figures/paper/fig2_cross_attack_bar.pdf`
- `/root/persuasion_turn_jailbreak_detect/docs/paper/figures/paper/fig2_cross_attack_bar.pdf`（已同步）

**关于 "0.28 / +72pp" 标注**：脚本中不包含任何文字标注代码，Vanilla Full 的 bar 高度一直是 0.312。如果 Figure 2 中有 "0.28 / +72pp" 的文字标注，这些可能在 LaTeX 源文件中（如 `\includegraphics` 旁的 overlay 或 caption 中）。需要我查找 LaTeX 中的标注吗？

---
