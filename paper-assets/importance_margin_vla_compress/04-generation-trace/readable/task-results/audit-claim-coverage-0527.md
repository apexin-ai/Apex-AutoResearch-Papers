# audit claim coverage 0527

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_claim_coverage_0527_20260527T010732_result.json`
- **Structured JSON:** [`63e6b060c73a2764b742.json`](../../sessions/63/63e6b060c73a2764b742.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Claim 覆盖度审计 Checklist

### Core Claims — 全部 ✅ 有数据支撑
| Claim | 状态 | 说明 |
|-------|------|------|
| C1: 2-Axis Framework (connector × task) | ✅ | 5 models, CV spectrum, X-VLA cross-suite 全齐 |
| C2: Pixel Shuffle Irreversible | ✅ | dual-seed + official checkpoint + 4 suites |
| C3a: Linear Pipeline Dependency | ✅ | π0 immune + X-VLA 8-point + random reversal |
| C3b: MLP Graded Degradation | ✅ | OpenVLA 6-point + OFT entropy + method independence |
| C4: VTR Learned Re-Encoding | ✅ | M-sweep + flat curve + arch independence + cross-suite |
| C5: CV Predicts Strategy | ✅ | k=0.5 & k=0.7 monotonic trend + multi-seed |

### Cliff Curves — 54/72 (75%) 完成
| Curve | 完成 | 在跑 | 缺失 |
|-------|------|------|------|
| OpenVLA Object | 15/18 | 3 | 0 |
| OpenVLA Goal | 13/18 | 2 | 3 |
| OpenVLA Long | 10/18 | 6 | 2 |
| π0.5 Long | 16/18 | 2 | 0 |

### 关键缺口（4 个未部署 k=0.95 实验）
1. ❌ Goal k=0.95 Attn — 需 Blackwell GPU
2. ❌ Goal k=0.95 Random — 需 Blackwell GPU
3. ❌ Long k=0.95 L2norm — 需 Blackwell GPU
4. ❌ Long k=0.95 Attn — 需 Blackwell GPU

**当前 0 张 Blackwell GPU 空闲**，需等 running 实验完成后立即部署（每个约 4h，deadline 还有 ~28h，可以赶上）。

### 结论
**所有 5 条 core claims 的核心证据已完备，论文写作不受阻。** 唯一风险是 4 个 k=0.95 cliff curve 顶端数据点未部署，需在 GPU 释放后立即行动。即使这些实验未完成，cliff curve 可从 k=0.9 起画，不影响 claim 成立。

---
