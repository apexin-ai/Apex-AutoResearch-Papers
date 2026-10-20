import asyncio
import json
import os
import random
import time
from pathlib import Path

from openai import AsyncOpenAI
from tqdm.asyncio import tqdm_asyncio
from sklearn.metrics import cohen_kappa_score

BASE_DIR = Path("/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts")
DATA_DIR = BASE_DIR / "data"
CONVERSATIONS_PATH = DATA_DIR / "processed" / "conversations.jsonl"
TAXONOMY_PATH = BASE_DIR / "taxonomy" / "persuasion_taxonomy.json"
ANNOTATIONS_PATH = DATA_DIR / "annotations.jsonl"
KAPPA_PATH = DATA_DIR / "kappa_report.json"
STATS_PATH = DATA_DIR / "annotation_stats.json"

API_KEY = "[REDACTED]"
BASE_URLS = ["http://47.94.22.126/v1", "https://tum.foriver.org/v1", None]
MODEL_PRIORITY = ["openai/gpt-5.5", "openai/gpt-5.2", "openai/gpt-4o-mini"]

SEMAPHORE_LIMIT = 10
MAX_RETRIES = 3
TEMPERATURE = 0.0


def load_taxonomy():
    with open(TAXONOMY_PATH) as f:
        return json.load(f)


def format_taxonomy_for_prompt(taxonomy):
    lines = []
    for cat in taxonomy["categories"]:
        lines.append(f"{cat['id']}: {cat['display_name']}")
        lines.append(f"   Definition: {cat['definition']}")
        examples = cat["examples"]
        jb_ex = examples.get("jailbreak", [])[:2]
        bn_ex = examples.get("benign", [])[:1]
        for ex in jb_ex + bn_ex:
            lines.append(f"   Example: \"{ex}\"")
        lines.append("")
    return "\n".join(lines)


def build_main_prompt(taxonomy_text, context_turns, target_content):
    context_str = ""
    if context_turns:
        context_str = "\n".join(f"[User turn {i+1}]: {t}" for i, t in enumerate(context_turns))
    else:
        context_str = "(No prior context)"

    return f"""You are an expert in discourse analysis and persuasion strategies. Classify the primary persuasion strategy used in the target user message.

## Taxonomy
{taxonomy_text}

## Rules
- Assign exactly ONE primary strategy per turn
- Priority when multiple co-occur: Role Assignment > Obfuscation > Emotional Manipulation > Gradual Escalation > Logical Reframing > Authority Appeal > Rapport Building > Direct Request
- Consider conversation context for escalation patterns

## Conversation Context (previous turns)
{context_str}

## Target Turn to Classify
{target_content}

Respond with ONLY valid JSON: {{"primary_strategy": <int 0-7>, "confidence": <float>, "reasoning": "<brief>"}}"""


def build_simple_prompt(context_turns, target_content):
    context_str = ""
    if context_turns:
        context_str = "\n".join(f"[Turn {i+1}]: {t}" for i, t in enumerate(context_turns))
    else:
        context_str = "(none)"

    return f"""Classify this message's persuasion strategy (0-7):
0=Rapport Building, 1=Authority Appeal, 2=Emotional Manipulation, 3=Logical Reframing, 4=Role Assignment, 5=Gradual Escalation, 6=Obfuscation, 7=Direct Request

Context: {context_str}
Message: {target_content}

JSON only: {{"primary_strategy": <int>, "confidence": <float>, "reasoning": "<str>"}}"""


async def probe_model(client, model):
    try:
        resp = await client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": "Say hi"}],
            max_tokens=5,
            temperature=0.0,
        )
        return resp.choices[0].message.content is not None
    except Exception:
        return False


async def select_model_and_client():
    for base_url in BASE_URLS:
        kwargs = {"api_key": [REDACTED]}
        if base_url:
            kwargs["base_url"] = base_url
        client = AsyncOpenAI(**kwargs)
        for model in MODEL_PRIORITY:
            print(f"Probing model={model}, base_url={base_url or 'default'}...")
            if await probe_model(client, model):
                print(f"Selected model: {model}, base_url: {base_url or 'default'}")
                return client, model
    raise RuntimeError("No model available")


def parse_response(text):
    text = text.strip()
    if text.startswith("```"):
        lines = text.split("\n")
        lines = [l for l in lines if not l.startswith("```")]
        text = "\n".join(lines).strip()
    try:
        obj = json.loads(text)
        ps = int(obj["primary_strategy"])
        if ps < 0 or ps > 7:
            return None
        conf = float(obj.get("confidence", 0.5))
        reasoning = str(obj.get("reasoning", ""))
        return {"primary_strategy": ps, "confidence": conf, "reasoning": reasoning}
    except (json.JSONDecodeError, KeyError, ValueError, TypeError):
        return None


async def annotate_one(client, model, sem, prompt, retries=MAX_RETRIES):
    for attempt in range(retries):
        async with sem:
            try:
                resp = await client.chat.completions.create(
                    model=model,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=TEMPERATURE,
                    max_tokens=200,
                )
                text = resp.choices[0].message.content
                result = parse_response(text)
                if result is not None:
                    tokens_in = resp.usage.prompt_tokens if resp.usage else 0
                    tokens_out = resp.usage.completion_tokens if resp.usage else 0
                    return result, tokens_in, tokens_out
            except Exception as e:
                if "429" in str(e):
                    await asyncio.sleep(2 ** (attempt + 1))
                    continue
                if attempt < retries - 1:
                    await asyncio.sleep(2 ** attempt)
                    continue
        await asyncio.sleep(2 ** attempt)
    return None, 0, 0


async def main():
    taxonomy = load_taxonomy()
    taxonomy_text = format_taxonomy_for_prompt(taxonomy)

    with open(CONVERSATIONS_PATH) as f:
        conversations = [json.loads(line) for line in f]

    # Build all tasks
    all_turns = []
    for conv in conversations:
        user_turns = [t for t in conv["turns"] if t["role"] == "user"]
        for idx, turn in enumerate(user_turns):
            context = [ut["content"] for ut in user_turns[max(0, idx-5):idx]]
            all_turns.append({
                "conversation_id": conv["conversation_id"],
                "turn_index": idx,
                "content": turn["content"],
                "context": context,
                "attack_type": conv.get("attack_type", "unknown"),
            })

    print(f"Total user turns to annotate: {len(all_turns)}")

    # Load existing annotations for resume
    existing = {}
    if ANNOTATIONS_PATH.exists():
        with open(ANNOTATIONS_PATH) as f:
            for line in f:
                obj = json.loads(line)
                key = (obj["conversation_id"], obj["turn_index"])
                existing[key] = obj
        print(f"Resuming: {len(existing)} already annotated")

    client, model = await select_model_and_client()
    sem = asyncio.Semaphore(SEMAPHORE_LIMIT)

    # Main annotation
    total_tokens_in = 0
    total_tokens_out = 0
    tasks_to_run = []
    tasks_meta = []

    for t in all_turns:
        key = (t["conversation_id"], t["turn_index"])
        if key in existing:
            continue
        prompt = build_main_prompt(taxonomy_text, t["context"], t["content"])
        tasks_to_run.append(annotate_one(client, model, sem, prompt))
        tasks_meta.append(t)

    if tasks_to_run:
        print(f"Running {len(tasks_to_run)} annotation requests...")
        results = await tqdm_asyncio.gather(*tasks_to_run, desc="Annotating")

        with open(ANNOTATIONS_PATH, "a") as f:
            for meta, (result, ti, to_) in zip(tasks_meta, results):
                if result is None:
                    result = {"primary_strategy": -1, "confidence": 0.0, "reasoning": "parse_failed"}
                total_tokens_in += ti
                total_tokens_out += to_
                record = {
                    "conversation_id": meta["conversation_id"],
                    "turn_index": meta["turn_index"],
                    "content": meta["content"],
                    "primary_strategy": result["primary_strategy"],
                    "confidence": result["confidence"],
                    "reasoning": result["reasoning"],
                }
                f.write(json.dumps(record, ensure_ascii=False) + "\n")
                existing[(meta["conversation_id"], meta["turn_index"])] = record

    # Reload all annotations
    all_annotations = []
    with open(ANNOTATIONS_PATH) as f:
        for line in f:
            all_annotations.append(json.loads(line))

    print(f"Total annotations: {len(all_annotations)}")

    # Kappa: select 100 samples
    random.seed(42)
    # Group by attack_type for stratified sampling
    by_attack = {}
    for ann in all_annotations:
        # find attack_type from all_turns
        at = "unknown"
        for t in all_turns:
            if t["conversation_id"] == ann["conversation_id"] and t["turn_index"] == ann["turn_index"]:
                at = t["attack_type"]
                break
        by_attack.setdefault(at, []).append(ann)

    kappa_samples = []
    attack_types = sorted(by_attack.keys())
    per_type = max(1, 100 // len(attack_types))
    for at in attack_types:
        pool = by_attack[at]
        n = min(per_type, len(pool))
        kappa_samples.extend(random.sample(pool, n))

    # fill remaining
    remaining = [a for a in all_annotations if a not in kappa_samples]
    if len(kappa_samples) < 100 and remaining:
        extra = min(100 - len(kappa_samples), len(remaining))
        kappa_samples.extend(random.sample(remaining, extra))

    kappa_samples = kappa_samples[:100]
    print(f"Kappa samples: {len(kappa_samples)}")

    # Second annotation with simple prompt
    kappa_tasks = []
    for ann in kappa_samples:
        # find context
        ctx = []
        for t in all_turns:
            if t["conversation_id"] == ann["conversation_id"] and t["turn_index"] == ann["turn_index"]:
                ctx = t["context"][-3:]
                break
        prompt = build_simple_prompt(ctx, ann["content"])
        kappa_tasks.append(annotate_one(client, model, sem, prompt))

    kappa_results = await tqdm_asyncio.gather(*kappa_tasks, desc="Kappa re-annotation")

    labels_1 = []
    labels_2 = []
    for ann, (result, ti, to_) in zip(kappa_samples, kappa_results):
        total_tokens_in += ti
        total_tokens_out += to_
        labels_1.append(ann["primary_strategy"])
        if result is None:
            labels_2.append(-1)
        else:
            labels_2.append(result["primary_strategy"])

    # Filter out -1 for kappa
    valid_pairs = [(l1, l2) for l1, l2 in zip(labels_1, labels_2) if l1 != -1 and l2 != -1]
    if len(valid_pairs) >= 2:
        v1, v2 = zip(*valid_pairs)
        overall_kappa = cohen_kappa_score(v1, v2)
    else:
        overall_kappa = 0.0

    # Per-class kappa
    per_class_kappa = {}
    per_class_samples = {}
    for cls in range(8):
        cls_pairs = [(1 if l1 == cls else 0, 1 if l2 == cls else 0) for l1, l2 in valid_pairs]
        per_class_samples[str(cls)] = sum(1 for l1, _ in valid_pairs if l1 == cls)
        if len(set([p[0] for p in cls_pairs])) > 1 and len(set([p[1] for p in cls_pairs])) > 1:
            c1, c2 = zip(*cls_pairs)
            per_class_kappa[str(cls)] = round(cohen_kappa_score(c1, c2), 4)
        else:
            per_class_kappa[str(cls)] = None

    passes = overall_kappa >= 0.60
    kappa_report = {
        "overall_kappa": round(overall_kappa, 4),
        "per_class_kappa": per_class_kappa,
        "per_class_samples": per_class_samples,
        "pass": passes,
        "model_used": model,
    }
    with open(KAPPA_PATH, "w") as f:
        json.dump(kappa_report, f, indent=2)
    print(f"Kappa report: overall={overall_kappa:.4f}, pass={passes}")

    # Stats
    strategy_dist = {}
    conf_sum = 0.0
    per_attack_dist = {}
    for ann in all_annotations:
        s = str(ann["primary_strategy"])
        strategy_dist[s] = strategy_dist.get(s, 0) + 1
        conf_sum += ann["confidence"]

    for t in all_turns:
        at = t["attack_type"]
        key = (t["conversation_id"], t["turn_index"])
        if key in existing:
            s = str(existing[key]["primary_strategy"])
            per_attack_dist.setdefault(at, {})
            per_attack_dist[at][s] = per_attack_dist[at].get(s, 0) + 1

    # Cost estimation (rough: $2.5/1M input, $10/1M output for gpt-4o; adjust for others)
    cost_per_1m_in = {"gpt-5.5": 5.0, "o3": 10.0, "gpt-4o": 2.5}
    cost_per_1m_out = {"gpt-5.5": 15.0, "o3": 40.0, "gpt-4o": 10.0}
    in_rate = cost_per_1m_in.get(model, 2.5)
    out_rate = cost_per_1m_out.get(model, 10.0)
    cost = (total_tokens_in / 1_000_000) * in_rate + (total_tokens_out / 1_000_000) * out_rate

    stats = {
        "total_turns": len(all_annotations),
        "strategy_distribution": strategy_dist,
        "avg_confidence": round(conf_sum / max(len(all_annotations), 1), 4),
        "per_attack_type_distribution": per_attack_dist,
        "model_used": model,
        "cost_usd": round(cost, 4),
        "total_tokens_in": total_tokens_in,
        "total_tokens_out": total_tokens_out,
    }
    with open(STATS_PATH, "w") as f:
        json.dump(stats, f, indent=2, ensure_ascii=False)
    print(f"Stats saved. Total turns: {len(all_annotations)}, Cost: ${cost:.4f}")


if __name__ == "__main__":
    asyncio.run(main())
