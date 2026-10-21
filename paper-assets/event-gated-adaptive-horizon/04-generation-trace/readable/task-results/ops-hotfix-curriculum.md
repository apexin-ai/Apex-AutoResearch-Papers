# ops hotfix curriculum

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_hotfix-curriculum_20260513T063626_result.json`
- **Structured JSON:** [`4729016407bd1ba534b7.json`](../../sessions/47/4729016407bd1ba534b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

热修复完成。汇总：

## 修改报告

### models.py（6 处修改）

| 行号 | 原代码 | 新代码 |
|------|--------|--------|
| 171 | `step = self.gate_step.item() if hasattr(...)` | `step = self._step` |
| 172,174-177 | `self._config.gate_curriculum_phase1/phase2` | 硬编码 `50000` / `150000` |
| 236 | `step = self.gate_step.item()` | `step = self._step` |
| 256,258-261 | `self._config.gate_curriculum_phase1/phase2` | 硬编码 `50000` / `150000` |
| 527 | `self._world_model.gate_step.item() if hasattr(...)` | `self._world_model._step` |
| 531 | `config.gate_curriculum_phase1` | `50000` |

保留不动：line 170 `self.gate_step += 1`（自增逻辑不变）

### configs.yaml（供未来 run 使用）
- `gate_curriculum_phase1`: 25000 → 50000
- `gate_curriculum_phase2`: 75000 → 150000

### 验证
- 语法检查：通过
- PID 18110：仍在运行
- 备份：`models.py.bak.hotfix`

### 当前状态
- **当前 env step**: ~48000
- **Phase 1 → Phase 2 过渡**：step 50000 时开始（约差 2000 步）
- **Phase 2 完成**：step 150000

由于 `self._step` 是 agent 传入的 env step counter，下次 `_train` 调用时即刻生效，无需重启。

---
