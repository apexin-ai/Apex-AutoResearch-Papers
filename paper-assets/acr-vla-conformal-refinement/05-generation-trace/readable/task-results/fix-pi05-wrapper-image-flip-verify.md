# fix pi05 wrapper image flip verify

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_pi05-wrapper-image-flip-verify_20260521T073006_result.json`
- **Structured JSON:** [`8cd538cd9a47cbbfa730.json`](../../sessions/8c/8cd538cd9a47cbbfa730.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**100% SR (3/3)！** 修复验证成功！

结果：
- Task: `pick_up_the_alphabet_soup_and_place_it_in_the_basket`
- Success rate: **100.0% (3/3)**
- Overall: **100.0% (3/3)**

## 总结

**修复状态 — 全部到位：**
1. **Image 180° flip** (`pi05_wrapper.py:154`): `torch.flip(img, dims=[2, 3])` 在 `_preprocess_image` 中，resize 之前执行，与官方 `LiberoProcessorStep` 一致
2. **Vision tower key remap** (`pi05_wrapper.py:102-123`): `vision_tower.vision_model.` → `vision_tower.` 重映射，修复了 437 个 keys
3. **诊断日志** — 我补充了 missing_keys/unexpected_keys 的打印

**改动：**
- 仅在 `_fix_vision_tower_keys` 中追加了 4 行诊断日志打印

**Quick verify 结果：**
- 1 task × 3 episodes = **3/3 成功 (100% SR)**
- 之前 5 轮修复前全是 0% SR
- 与官方 lerobot-eval 的 100% SR 一致

**修复成功，准备全量 baseline eval。** 注意启动 eval 时必须：
- 设 `HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1`（否则 tokenizer 加载会卡住）
- 确保无其他大内存进程（cgroup 限制 60GB，PI05 加载峰值 ~30GB）

---
