"""
Collect multi-turn conversation datasets for jailbreak detection.
Sources:
  1. tom-gibbs/multi-turn_jailbreak_attack_datasets (jailbreak, complete convs with responses)
  2. SafeMTData/SafeMTData Attack_600 (jailbreak, user-turn escalation patterns)
  3. allenai/WildChat-1M (benign, filtered by topic-drift)
"""

import json
import ast
import random
from pathlib import Path
from collections import defaultdict

import numpy as np
from datasets import load_dataset
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from tqdm import tqdm

random.seed(42)
np.random.seed(42)

RAW_DIR = Path("/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/data/raw")
PROCESSED_DIR = Path("/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/data/processed")


def collect_tomgibbs_jailbreak():
    """Collect jailbreak conversations from tom-gibbs dataset (complete with responses)."""
    print("=" * 60)
    print("[1/3] Collecting from tom-gibbs (complete conversations)...")
    print("=" * 60)

    ds = load_dataset('tom-gibbs/multi-turn_jailbreak_attack_datasets', split='train', streaming=True)

    conversations = []
    goal_counts = defaultdict(int)

    for ex in tqdm(ds, desc="Loading tom-gibbs"):
        conv_str = ex['Multi-turn conversation']
        jailbroken_str = ex.get('Jailbroken', '{}')

        try:
            conv = ast.literal_eval(conv_str)
            jailbroken = ast.literal_eval(jailbroken_str) if isinstance(jailbroken_str, str) else jailbroken_str
        except (ValueError, SyntaxError):
            continue

        mt_score = jailbroken.get('Multi-turn', -1) if isinstance(jailbroken, dict) else -1

        # Only use examples that have real assistant responses (complete dataset subset)
        if mt_score == -1:
            continue

        turns = []
        has_real_response = False
        for msg in conv:
            if not isinstance(msg, dict) or 'role' not in msg or 'content' not in msg:
                continue
            content = msg.get('content')
            if content is None or content == 'None':
                continue
            if not content.strip():
                continue
            turns.append({"role": msg['role'], "content": content})
            if msg['role'] == 'assistant' and len(content) > 10:
                has_real_response = True

        if not has_real_response or len(turns) < 4:
            continue

        # Limit diversity per goal (max 5)
        goal_id = ex.get('Goal ID', '')
        if goal_counts[goal_id] >= 5:
            continue
        goal_counts[goal_id] += 1

        conv_id = f"tomgibbs_{ex['Example ID'][:12]}"
        conversations.append({
            "conversation_id": conv_id,
            "source": "tom-gibbs",
            "label": "jailbreak",
            "turns": turns,
            "num_turns": len(turns),
            "metadata": {
                "goal": ex.get('Goal', ''),
                "goal_id": goal_id,
                "model": ex.get('Model', ''),
                "input_cipher": ex.get('Input-cipher', ''),
                "jailbroken_score": mt_score
            }
        })

    print(f"  Collected: {len(conversations)} conversations")

    # Sample 150 with diversity across goals
    if len(conversations) > 150:
        by_goal = defaultdict(list)
        for c in conversations:
            by_goal[c['metadata']['goal_id']].append(c)
        sampled = []
        goals = list(by_goal.keys())
        random.shuffle(goals)
        idx = 0
        while len(sampled) < 150 and any(by_goal[g] for g in goals):
            goal = goals[idx % len(goals)]
            if by_goal[goal]:
                sampled.append(by_goal[goal].pop(0))
            idx += 1
        conversations = sampled

    print(f"  After sampling: {len(conversations)}")
    return conversations


def collect_safemtdata_jailbreak():
    """Collect jailbreak query sequences from SafeMTData (multi-turn escalation)."""
    print("\n" + "=" * 60)
    print("[2/3] Collecting from SafeMTData Attack_600...")
    print("=" * 60)

    ds = load_dataset('SafeMTData/SafeMTData', 'Attack_600', split='Attack_600', streaming=True)

    conversations = []
    query_ids_seen = set()

    for ex in tqdm(ds, desc="Loading SafeMTData"):
        queries = ex.get('multi_turn_queries', [])
        if not queries or len(queries) < 3:
            continue

        # Deduplicate by query_id (same harmful intent, different actors)
        query_id = ex.get('query_id', -1)
        if query_id in query_ids_seen:
            continue
        query_ids_seen.add(query_id)

        # Build conversation turns (user queries as multi-turn escalation)
        turns = []
        for q in queries:
            if q and len(q.strip()) > 5:
                turns.append({"role": "user", "content": q.strip()})
                turns.append({"role": "assistant", "content": "[Model response]"})

        if len(turns) < 6:  # at least 3 user turns
            continue

        conv_id = f"safemt_{ex.get('id', 0):04d}"
        conversations.append({
            "conversation_id": conv_id,
            "source": "safemtdata",
            "label": "jailbreak",
            "turns": turns,
            "num_turns": len(turns),
            "metadata": {
                "category": ex.get('category', ''),
                "plain_query": ex.get('plain_query', ''),
                "actor_name": ex.get('actor_name', ''),
            }
        })

    print(f"  Collected: {len(conversations)} conversations")

    # Sample 135 to complement tom-gibbs (~115) for ~250 total jailbreak
    if len(conversations) > 135:
        conversations = random.sample(conversations, 135)
        print(f"  After sampling: {len(conversations)}")

    return conversations


def compute_topic_drift(turns):
    """Compute topic drift using TF-IDF cosine similarity between adjacent user turns."""
    user_messages = [t['content'] for t in turns if t['role'] == 'user' and len(t['content']) > 20]

    if len(user_messages) < 3:
        return 0.0

    try:
        vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
        tfidf_matrix = vectorizer.fit_transform(user_messages)

        similarities = []
        for i in range(len(user_messages) - 1):
            sim = cosine_similarity(tfidf_matrix[i:i+1], tfidf_matrix[i+1:i+2])[0][0]
            similarities.append(sim)

        mean_drift = 1.0 - np.mean(similarities)
        max_drift = 1.0 - np.min(similarities)
        return 0.6 * mean_drift + 0.4 * max_drift
    except ValueError:
        return 0.0


def collect_wildchat_benign():
    """Collect benign high-drift multi-turn conversations from WildChat."""
    print("\n" + "=" * 60)
    print("[3/3] Collecting benign high-drift from WildChat...")
    print("=" * 60)

    ds = load_dataset('allenai/WildChat-1M', split='train', streaming=True)

    candidates = []
    processed = 0
    max_to_scan = 80000

    for ex in tqdm(ds, desc="Scanning WildChat", total=max_to_scan):
        processed += 1
        if processed > max_to_scan:
            break

        if ex.get('language') != 'English':
            continue
        if ex.get('toxic', False):
            continue

        conv = ex.get('conversation', [])
        if len(conv) < 10:
            continue

        turns = []
        for msg in conv:
            if isinstance(msg, dict) and 'role' in msg and 'content' in msg:
                content = msg['content']
                if content and len(content.strip()) > 5:
                    turns.append({"role": msg['role'], "content": content})

        if len(turns) < 10:
            continue

        drift_score = compute_topic_drift(turns)
        candidates.append({
            "conversation_hash": ex.get('conversation_hash', ''),
            "turns": turns,
            "num_turns": len(turns),
            "drift_score": drift_score,
            "model": ex.get('model', ''),
        })

    print(f"  Multi-turn English non-toxic conversations: {len(candidates)}")

    if not candidates:
        print("  WARNING: No candidates found!")
        return []

    # Sort by drift and take top 10%
    candidates.sort(key=lambda x: x['drift_score'], reverse=True)
    top_pct = max(1, len(candidates) // 10)
    high_drift = candidates[:top_pct]

    print(f"  Top 10% high-drift: {len(high_drift)}")
    if high_drift:
        print(f"  Drift score range: [{high_drift[-1]['drift_score']:.3f}, {high_drift[0]['drift_score']:.3f}]")

    # Sample 250
    if len(high_drift) > 250:
        high_drift = random.sample(high_drift, 250)

    conversations = []
    for cand in high_drift:
        conv_id = f"wildchat_{cand['conversation_hash'][:12]}"
        conversations.append({
            "conversation_id": conv_id,
            "source": "wildchat",
            "label": "benign",
            "turns": cand['turns'],
            "num_turns": cand['num_turns'],
            "metadata": {
                "drift_score": round(cand['drift_score'], 4),
                "model": cand['model'],
            }
        })

    print(f"  Final benign conversations: {len(conversations)}")
    return conversations


def merge_and_save(all_sources):
    """Merge all sources and save."""
    print("\n" + "=" * 60)
    print("Merging and saving...")
    print("=" * 60)

    all_convs = []
    for convs in all_sources:
        all_convs.extend(convs)
    random.shuffle(all_convs)

    # Save raw per-source
    by_source = defaultdict(list)
    for c in all_convs:
        by_source[c['source']].append(c)
    for source, convs in by_source.items():
        raw_path = RAW_DIR / f"{source}.jsonl"
        with open(raw_path, 'w') as f:
            for conv in convs:
                f.write(json.dumps(conv, ensure_ascii=False) + '\n')
        print(f"  Raw saved: {raw_path} ({len(convs)} convs)")

    # Save merged processed
    output_path = PROCESSED_DIR / "conversations.jsonl"
    with open(output_path, 'w') as f:
        for conv in all_convs:
            f.write(json.dumps(conv, ensure_ascii=False) + '\n')
    print(f"  Processed saved: {output_path}")

    # Statistics
    print(f"\n{'=' * 60}")
    print("FINAL STATISTICS")
    print(f"{'=' * 60}")
    print(f"  Total conversations: {len(all_convs)}")

    labels = defaultdict(int)
    sources = defaultdict(int)
    turn_counts = []
    for conv in all_convs:
        labels[conv['label']] += 1
        sources[conv['source']] += 1
        turn_counts.append(conv['num_turns'])

    print(f"\n  Label distribution:")
    for label, count in sorted(labels.items()):
        print(f"    {label}: {count} ({100*count/len(all_convs):.1f}%)")

    print(f"\n  Source distribution:")
    for source, count in sorted(sources.items()):
        print(f"    {source}: {count}")

    print(f"\n  Turn statistics:")
    print(f"    Mean: {np.mean(turn_counts):.1f}")
    print(f"    Median: {np.median(turn_counts):.1f}")
    print(f"    Min: {min(turn_counts)}, Max: {max(turn_counts)}")


if __name__ == "__main__":
    jailbreak_1 = collect_tomgibbs_jailbreak()
    jailbreak_2 = collect_safemtdata_jailbreak()
    benign = collect_wildchat_benign()
    merge_and_save([jailbreak_1, jailbreak_2, benign])
