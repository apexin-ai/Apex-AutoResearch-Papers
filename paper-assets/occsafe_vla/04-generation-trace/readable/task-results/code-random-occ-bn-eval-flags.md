# code random occ bn eval flags

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_random-occ-bn-eval-flags_20260528T180753_result.json`
- **Structured JSON:** [`7c440675a052a8b3ebc1.json`](../../sessions/7c/7c440675a052a8b3ebc1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

draccus API 可能不同，但 syntax + config instantiation 已通过。两个 flag 是标准 dataclass bool 字段，draccus 会自动解析。

## 修改汇总

| # | 位置 | 行号 | 修改内容 |
|---|------|------|----------|
| 1 | `FinetuneConfig` | 100 | 添加 `random_occ: bool = False` |
| 2 | `FinetuneConfig` | 101 | 添加 `occ_bn_eval: bool = False` |
| 3 | `run_forward_pass` 签名 | 326 | 添加参数 `random_occ=False` |
| 4 | OCC loss 计算 | 491-493 | `if random_occ: perm = torch.randperm(...); occ_targets = occ_targets[perm]` |
| 5 | 训练循环 | 1197-1200 | `if cfg.occ_bn_eval: ... m.eval()` (在 `run_forward_pass` 调用前) |
| 6 | 训练循环调用 | 1221 | 传入 `random_occ=cfg.random_occ` |

**验证结果**：
- `py_compile`: Syntax OK
- Config 实例化：`random_occ=False, occ_bn_eval=False` 正确

**是否需要同步到 westd-10894**：代码在 westd-34685 上修改完成。如果 westd-10894 也需要运行这些实验，需要通过 git push/pull 同步。

---
