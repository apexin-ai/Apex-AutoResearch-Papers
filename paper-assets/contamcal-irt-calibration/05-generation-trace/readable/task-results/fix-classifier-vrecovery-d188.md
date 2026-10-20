# fix classifier vrecovery d188

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_classifier-vrecovery-d188_20260520T162445_result.json`
- **Structured JSON:** [`862940e0013a9dc172a8.json`](../../sessions/86/862940e0013a9dc172a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有修改完成。总结：

**#1 V-recovery 分类修复**：
- `classify_pattern()` 的 dip-detection 块增加 `delta_100 < 1.0` 门控
- dip ≥2pp + recovery ≥50% 但 d100 > +1pp → 返回 `Benefit` 而非 `V-recovery`
- Gemma-2-9B s123 验证：从 `V-recovery` 改为 `Benefit` ✓

**#2 Direction + Dir-Con 列**：
- 文本表和 LaTeX 表均已新增
- Direction: mean Δ(d100) 符号（±1pp 阈值）
- Dir-Con: 所有种子方向一致 → ✓，否则 ✗

**Bootstrap 结果**：

| Family | Pattern | Dir. | Dir-C |
|--------|---------|------|-------|
| Phi-4 | Immune† | 0 | ✗ |
| Qwen2.5-14B | Collapse | − | ✓ |
| Qwen2.5-7B | V-recovery | 0 | ✗ |
| Gemma-2-9B | Benefit-sat† | + | ✓ |
| OLMo-2-7B | Benefit-sat† | + | ✗ |

服务器和本地副本均已同步修改。

---
