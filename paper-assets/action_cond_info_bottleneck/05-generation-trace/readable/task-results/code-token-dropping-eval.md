# code token dropping eval

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_token-dropping-eval_20260517T134722_result.json`
- **Structured JSON:** [`bb637e587c3c5594a01b.json`](../../sessions/bb/bb637e587c3c5594a01b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三项验证全部通过：

**修改的文件：**
- `acib/config.py` — 新增 `drop_mode: Literal["none", "importance", "random"]` 和 `drop_ratio: float`
- `acib/acib_policy.py` — `_connector_hook` 中新增 token dropping 逻辑：importance 模式按 scorer weight 排序 drop 最低 k%，random 模式随机 drop k%，binary mask 直接乘 visual tokens
- `scripts/eval_acib.py` — 新增 `--drop_mode` / `--drop_ratio` CLI 参数，透传到 `patch_make_policy` → `ACIBConfig`

**新建的文件：**
- `scripts/run_v72_token_drop_sweep.sh` — importance vs random, ratio=0.1/0.2/0.3/0.4/0.5, libero_spatial only
- `scripts/run_v72_perturbation_eval.sh` — scored/unscored 模式, 4种 perturbation, 4个 suite

---
