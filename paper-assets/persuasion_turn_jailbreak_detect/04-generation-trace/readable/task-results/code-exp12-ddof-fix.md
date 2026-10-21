# code exp12 ddof fix

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp12-ddof-fix_20260521T053051_result.json`
- **Structured JSON:** [`465bd6ce74089db27ebc.json`](../../sessions/46/465bd6ce74089db27ebc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。修改汇总：

**脚本修改**: `scripts/exp12_toxicchat_bootstrap.py` 第 127 行 `ddof=1` → `ddof=0`

**所有受影响 seed_std 的新旧值对比**（`results/exp12_toxicchat_bootstrap.json` 已更新）:

| Variant | Old (ddof=1) | New (ddof=0) | Ratio |
|---------|-------------|-------------|-------|
| vanilla | 0.0260 | 0.0212 | 0.8165 |
| 9class | 0.1065 | 0.0870 | 0.8165 |
| binary | 0.0881 | 0.0719 | 0.8165 |
| scrambled | 0.0682 | 0.0556 | 0.8165 |
| jb_mlm | 0.0154 | 0.0126 | 0.8165 |
| wiki_mlm | 0.1140 | 0.0931 | 0.8165 |
| topic | 0.0512 | 0.0418 | 0.8165 |

所有 std 统一缩小为原来的 √(2/3) ≈ 0.8165 倍（n=3 时 population std vs sample std 的固定比值）。

---
