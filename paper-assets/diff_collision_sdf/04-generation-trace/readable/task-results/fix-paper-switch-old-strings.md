# fix paper switch old strings

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_paper_switch_old_strings_20260527T212108_result.json`
- **Structured JSON:** [`76ed71f5efb3927c9d9a.json`](../../sessions/76/76ed71f5efb3927c9d9a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All fixes verified. Summary:

### 修改内容

**7 处 old_string 修复：**

| # | 位置 | 修改 |
|---|------|------|
| 1 | abstract L7 | `$p{\approx}0.039$)` → `$p{\approx}0.071$, two-tailed permutation test)`, 删尾部 `requiring further investigation` |
| 2 | abstract L9 | `can be neither credited with nor expected to deliver` → `cannot be credited with delivering collision avoidance, nor expected to do so` |
| 3 | claim3 L7 caption | `($z = 1.76$, $p \approx 0.039$, ` → `($p \approx 0.071$, two-tailed permutation test, ` |
| 4 | claim3 L27 body | `confirming`→`which confirms`, `0.25`→`0.33`, `;`替换`,`, 加 `Figure~\ref{fig:pertask_fingerprint}` |
| 5 | claim3 L32-33 dose-response | z-test 统计→permutation test + footnote, `identical`→`preserved` |
| 6 | claim3 L38 fig caption | `($p \approx 0.039$)` → `($p \approx 0.071$, two-tailed permutation test)` |
| 7 | discussion L12 | `($p \approx 0.039$)` → `($p \approx 0.071$, two-tailed permutation test)` |

**1 处 new_string 修复：** claim3 L27 Scenario C 的 `0.25\,pp` → `0.33\,pp`

### Dry-run 结果
- **Scenario C** (`--s2-car 58 --s2-tsr 48`): **12/12** matched
- **Scenario B** (`--s2-car 55 --s2-tsr 45`): **11/11** matched（discussion L3 scope 为 C-only，正确排除）

### p 值逻辑确认
- 正文位置全部使用 `{p_value}`（双尾 permutation）✓
- 脚注位置全部使用 `{p_one_value}`（单尾 permutation）✓

脚本仅在本地修改。服务器上无 `docs/paper/` 目录和 `paper_switch.py`，需要 sync 后才能在服务器上运行。

---
