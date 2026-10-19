# research position ids v2 consistency

**tbab multi turn** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_position-ids-v2-consistency_20260518T053058_result.json`
- **Structured JSON:** [`b9ff6cafb0ad8db558ad.json`](../../sessions/b9/b9ff6cafb0ad8db558ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/position_ids_v2_report.md` 并注册。核心结论：

**选定方案 B（bridge 归属后 turn）**，理由：

1. **信息传递瓶颈在功能 2**（新 turn 读取 bridge）。方案 A 中新 turn 到 bridge 的 RoPE 距离 >= n（前 turn 长度），高频通道退化为噪声。方案 B 中距离仅为 1 到 K+m，所有频率通道充分贡献。
2. 功能 1（bridge 读取前 turn）在方案 B 中距离较大，但可通过 content-based attention + 大 rope_theta 的慢衰减补偿。
3. 与 Prefix Tuning、RMT、Register Tokens 等所有主流工作一致：需要被当前 segment 使用的 special tokens 作为该 segment 的前缀。
4. 实现更简洁（固定偏移 K，无需跟踪前 turn 长度）。

**模型泛化**：position_ids 接口、4D mask bypass、渐进式 tokenization turn 检测均为 HuggingFace 通用机制，代码不依赖任何模型特定常量。

---
