"""Patch run_debate.py to support LogiQA (multichoice) in addition to FOLIO."""
import re

filepath = '/root/symb_invariant_consensus/run_debate.py'
with open(filepath) as f:
    content = f.read()

original = content

# --- Patch 1: Add _CHOICE_ANSWER_PATTERNS after _ANSWER_PATTERNS block ---
marker1 = "    re.compile(r'(?:conclusion|therefore|thus|hence)[:\\\\s]*.*?\\\\b(true|false|unknown|uncertain)\\\\b', re.I),\n]"
insert1 = """\n
_CHOICE_ANSWER_PATTERNS = [
    re.compile(r'(?:the\\s+)?(?:final\\s+)?answer\\s+is[:\\s]*\\(?([A-D])\\)?', re.I),
    re.compile(r'(?:conclusion|therefore|thus|hence)[:\\s]*.*?\\(?([A-D])\\)?', re.I),
]"""
assert marker1 in content, "Patch 1 FAILED: marker not found"
content = content.replace(marker1, marker1 + insert1, 1)
print("Patch 1 OK: added _CHOICE_ANSWER_PATTERNS")

# --- Patch 2: extract_debate_answer — add dataset param + multichoice ---
old2 = 'def extract_debate_answer(text: str) -> str:\n    """Extract True/False/Unknown from free-form debate response text."""'
new2 = 'def extract_debate_answer(text: str, dataset: str = "folio") -> str:\n    """Extract answer from free-form debate response text (FOLIO or LogiQA)."""'
assert old2 in content, "Patch 2a FAILED"
content = content.replace(old2, new2, 1)

# After boxed extraction, add multichoice branch
old2b = """    if boxed:
        return normalize_logic_answer(boxed[-1])

    # Try structured patterns (last match wins"""
new2b = """    if boxed:
        ans = boxed[-1].strip()
        if dataset == "logiqa" and ans.upper() in ("A", "B", "C", "D"):
            return ans.upper()
        return normalize_logic_answer(ans)

    if dataset == "logiqa":
        for pattern in _CHOICE_ANSWER_PATTERNS:
            matches = pattern.findall(clean)
            if matches:
                return matches[-1].upper()
        tail = clean[-300:]
        m = re.search(r'\\b([A-D])\\b', tail)
        if m:
            return m.group(1).upper()
        return ""

    # Try structured patterns (last match wins"""
assert old2b in content, "Patch 2b FAILED"
content = content.replace(old2b, new2b, 1)
print("Patch 2 OK: extract_debate_answer supports multichoice")

# --- Patch 3: critic_disagrees — add dataset param ---
old3 = 'def critic_disagrees(proposer_answer: str, critic_text: str) -> bool:\n    """Check if critic produced a different answer than proposer."""\n    critic_answer = extract_debate_answer(critic_text)'
new3 = 'def critic_disagrees(proposer_answer: str, critic_text: str, dataset: str = "folio") -> bool:\n    """Check if critic produced a different answer than proposer."""\n    critic_answer = extract_debate_answer(critic_text, dataset=dataset)'
assert old3 in content, "Patch 3 FAILED"
content = content.replace(old3, new3, 1)
print("Patch 3 OK: critic_disagrees")

# --- Patch 4: run_single_debate — add dataset param ---
old4 = 'def run_single_debate(llm, problem_text: str, debate_idx: int) -> dict:'
new4 = 'def run_single_debate(llm, problem_text: str, debate_idx: int, dataset: str = "folio") -> dict:'
assert old4 in content, "Patch 4 FAILED"
content = content.replace(old4, new4, 1)

content = content.replace(
    '    proposer_answer = extract_debate_answer(proposer_response)',
    '    proposer_answer = extract_debate_answer(proposer_response, dataset=dataset)', 1)
content = content.replace(
    '    critic_answer = extract_debate_answer(critic_response)',
    '    critic_answer = extract_debate_answer(critic_response, dataset=dataset)', 1)
content = content.replace(
    '    valid = critic_disagrees(proposer_answer, critic_response)',
    '    valid = critic_disagrees(proposer_answer, critic_response, dataset=dataset)', 1)
content = content.replace(
    '    defense_answer = extract_debate_answer(defense_response)',
    '    defense_answer = extract_debate_answer(defense_response, dataset=dataset)', 1)
print("Patch 4 OK: run_single_debate threaded dataset")

# --- Patch 5: Add --dataset arg ---
old5 = '    parser.add_argument("--data", required=True,'
new5 = '    parser.add_argument("--dataset", choices=["folio", "logiqa"], default="folio",\n                        help="Dataset type: folio (3-class) or logiqa (4-choice)")\n    parser.add_argument("--data", required=True,'
assert old5 in content, "Patch 5 FAILED"
content = content.replace(old5, new5, 1)
print("Patch 5 OK: --dataset arg")

# --- Patch 6: Remove hardcoded gen.domain = "math" ---
content = content.replace(
    '        gen.domain = "math"\n        return gen\n    elif args.mode == "vllm":',
    '        return gen\n    elif args.mode == "vllm":', 1)
content = content.replace(
    '        gen.domain = "math"\n        return gen\n    raise ValueError',
    '        return gen\n    raise ValueError', 1)
print("Patch 6 OK: removed hardcoded domain")

# --- Patch 7: Set domain in main() ---
old7 = '    generator = build_generator(args)\n    debate_llm = build_debate_llm(args)'
new7 = '    generator = build_generator(args)\n    generator.domain = "multichoice" if args.dataset == "logiqa" else "math"\n    debate_llm = build_debate_llm(args)'
assert old7 in content, "Patch 7 FAILED"
content = content.replace(old7, new7, 1)
print("Patch 7 OK: domain set in main()")

# --- Patch 8: Thread dataset through run_single_debate call in process_single ---
old8 = '        debate = run_single_debate(debate_llm, problem_text, d_idx)'
new8 = '        debate = run_single_debate(debate_llm, problem_text, d_idx, dataset=getattr(args, "dataset", "folio"))'
assert old8 in content, "Patch 8 FAILED"
content = content.replace(old8, new8, 1)
print("Patch 8 OK: dataset threaded in process_single")

# --- Patch 9: Fix hardcoded dataset label ---
old9 = '            "dataset": "folio",'
new9 = '            "dataset": args.dataset,'
assert old9 in content, "Patch 9 FAILED"
content = content.replace(old9, new9, 1)
print("Patch 9 OK: dynamic dataset label")

# Write
with open(filepath, 'w') as f:
    f.write(content)
with open(filepath + '.bak_pre_logiqa', 'w') as f:
    f.write(original)

print(f"\nALL PATCHES APPLIED. Delta: {len(content) - len(original):+d} chars")
