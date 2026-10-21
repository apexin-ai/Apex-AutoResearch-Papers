# ssh crafter text wrapper

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_crafter-text-wrapper_20260518T040932_result.json`
- **Structured JSON:** [`d41ae279b752ffba853e.json`](../../sessions/d4/d41ae279b752ffba853e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

---

**已部署到** `/root/autodl-tmp/simgate-modular-routing/crafter_pilot/`（westb-14838）

**文件结构：**
```
crafter_pilot/
├── config.py           # semantic map encoding, actions, API config
├── text_wrapper.py     # CrafterTextWrapper: semantic map → text obs
├── llm_agent.py        # CrafterLLMAgent (vLLM API) + RandomAgent
├── episode_runner.py   # 主 runner，支持 --agent random/llm
└── results/            # JSON 输出
```

**Text Observation 格式：**
- Status: health/food/drink/energy + step count
- Nearby Objects: 8方向扫描，每方向最近3个 interesting object + 距离
- Inventory: resources + tools
- Achievements: unlocked count + list
- Available Actions: 17个 action 的 index:name 映射

**Action Mapping：** LLM 输出任意文本 → regex 匹配 action name → fallback 到 noop

**验证结果：**
- Text wrapper: 正常生成 text obs，directional scan 正确识别 objects
- Action parsing: "move_up", "do", "SLEEP", 带上下文的句子均正确解析
- Random agent 3 episodes: 全部完成（179/169/182 steps），3-5 achievements，均以 death 结束，JSON 输出格式正确

**使用 LLM agent：**
```bash
cd /root/autodl-tmp/simgate-modular-routing/crafter_pilot
/root/miniconda3/bin/python episode_runner.py --agent llm --episodes 5
```
需要先在另一个 GPU 上启动 vLLM server 到 localhost:8000。

---
