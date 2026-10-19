# code eval ablation modes

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval_ablation_modes_20260516T204513_result.json`
- **Structured JSON:** [`a7b737e04e311b8aae3a.json`](../../sessions/a7/a7b737e04e311b8aae3a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。修改了 3 个文件：

**`meta_brain_assembly.py`**:
- `random` 模式：Dirichlet 软采样 → 基于 `_random_expert_idx` 的 one-hot（每 episode 固定一个 expert）
- `oracle` 模式：nominal 时从 uniform 1/3 → 全零（等效无 LoRA）
- 新增 `set_random_expert(idx)` 方法

**`evaluate_libero_plus.py`**:
- 在 evaluate 循环中，routing=="random" 时每个 episode 用 `np.random.default_rng(ep_seed)` 确定性选一个 expert，保证可复现

**`openpi_metabrain_policy.py`**:
- 添加 `set_random_expert` no-op 方法（API 兼容）

`--help` 确认 `--routing {par,oracle,random,none,universal}` 正常显示。par/universal/none 代码路径未改动。

---
