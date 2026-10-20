# paper figure d123 fetch

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_d123_fetch_20260520T184347_result.json`
- **Structured JSON:** [`64e221853299055e3f50.json`](../../sessions/64/64e221853299055e3f50.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

SSH 密钥认证被拒绝。这是 AutoDL 实例，可能端口已变（实例重启后端口会变）。

根据 AutoDL 专项注意事项：**实例重启后 SSH 端口会变**。当前配置的端口 25068 可能已过期。

请去 AutoDL 控制台确认 `westd-25068` 实例的当前 SSH 端口，并检查公钥是否已添加到实例。如果端口变了，需要更新 `~/.ssh/config` 中的端口号。

另外也可能是实例上的 authorized_keys 没有配置当前的公钥 (`SHA256:79L8occ2olkZ3yPraqZvQLiXu3ov/I2w43oddjKzRw8`)。

---
