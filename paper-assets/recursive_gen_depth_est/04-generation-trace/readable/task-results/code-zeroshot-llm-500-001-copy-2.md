# code zeroshot llm 500 001

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_zeroshot_llm_500_001_20260515T161117_result.json`
- **Structured JSON:** [`84034538fd4220d35304.json`](../../sessions/84/84034538fd4220d35304.json)

## Before a recorded user message

1 recorded events

### Log line

_source line 1_

{
  "raw": "脚本验证通过：500 条平衡样本（每类 125），数据加载正常。\n\n**状态报告：**\n\n- 脚本已就绪：`scripts/run_zeroshot_500.py` + `scripts/run_zeroshot_500.sh`\n- 与 200-sample 实验完全一致：模型 `deepseek/deepseek-v3.2`，同一 prompt，同一 API proxy (`http://47.94.22.126/v1`)\n- 500 条类别平衡样本（seed=42），带 checkpoint 断点续传\n- 输出包含 accuracy + 95% bootstrap CI + per-class recall + 与 RF 78.2% 对比 + 与 200-sample 对比\n\n**阻塞问题：`OPENAI_API_KEY` 未设置。**\n\nshell 脚本注释 `# OPENAI_API_KEY 由外部注入`，服务器 `.bashrc` 和环境变量中均不存在该 key。proxy `http://47.94.22.126/v1` 已验证需要有效 key（dummy key 返回 401）。\n\n运行方式（拿到 key 后）：\n```bash\nexport OPENAI_API_KEY=[REDACTED]"your_key_here\"\nbash scripts/run_zeroshot_500.sh\n```\n\n预计运行时间：500 samples × 0.5s delay ≈ 4-5 分钟。请提供 `OPENAI_API_KEY`。"
}

---
