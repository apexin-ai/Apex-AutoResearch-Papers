#!/usr/bin/env python3
# SOPBench pilot: 5 ambiguous/unambiguous Healthcare constraint pairs × GPT-4.1.
# Tests whether SOPBench's rule-based verifier detects ambiguity-induced violations.

import os
import sys
import json
import copy
import argparse
import traceback
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from env.domains.healthcare import healthcare_assistant
from env.task import task_default_dep_full, task_initializer
from env.evaluator import evaluator_function_directed_graph, count_constraint_units
from swarm.core import Swarm
from swarm.types import Agent
from swarm.llm_handler import OpenAIHandler
from swarm.util import function_to_json

CLAUSE_PAIRS = [
    {
        "id": "HC02",
        "constraint": "claim_within_limits",
        "ambiguity_type": "Incompleteness",
        "action": "submit_claim",
        "task_idx": 2,
        "ambiguous": "The claim amount must be within acceptable limits.",
    },
    {
        "id": "HC01",
        "constraint": "claim_within_coverage_amount",
        "ambiguity_type": "Scopal",
        "action": "submit_claim",
        "task_idx": 0,
        "ambiguous": "Claims must not exceed the coverage amount.",
    },
    {
        "id": "HC10",
        "constraint": "provider_authorized",
        "ambiguity_type": "Authorization scope",
        "action": "schedule_appointment",
        "task_idx": 4,
        "ambiguous": "The provider must be authorized.",
    },
    {
        "id": "HC07",
        "constraint": "policy_active",
        "ambiguity_type": "Lexical",
        "action": "add_authorized_provider",
        "task_idx": 0,
        "ambiguous": "The user's policy must be in good standing.",
    },
    {
        "id": "HC04",
        "constraint": "within_enrollment_period",
        "ambiguity_type": "Conditional precedence",
        "action": "update_policy",
        "task_idx": 0,
        "ambiguous": "The policy must be within the enrollment period.",
    },
]


def exit_conversation():
    """Signals that the conversation should end.

    Call this function when the requested task is completed or the conversation can not be continued.
    It takes no parameters and returns None."""
    return


def try_eval(x):
    try:
        return eval(x)
    except:
        return x


def run_single_episode(task, domain_str, model_name, handler=None):
    dep_innate_full, default_dep_full, default_dep_full_descr = task_default_dep_full(
        domain_str, "full", "structured", dependency_verb_dep_orig=True
    )

    domain_system, user_info, assistant_info, task_info = task_initializer(
        domain_str, task, dep_innate_full, default_dep_full, default_dep_full_descr,
        None, "prompt", False, "structured"
    )

    assistant_functions = assistant_info["tools"] + [function_to_json(exit_conversation)]
    assistant_agent = Agent(
        name="healthcare assistant",
        client=handler,
        temperature=0.0,
        top_p=0.01,
        max_tokens=512,
        tool_call_mode="fc",
        instructions=assistant_info["instructions"],
        functions=assistant_functions,
    )

    default_user_msg = (
        f"Here is all the information I can provide:\n"
        f"{json.dumps(user_info['known'], indent=4)}\n\n"
        f"If you have completed my request or cannot assist me with this request, "
        f"please use the `exit_conversation` action to end our conversation."
    )
    user_agent = Agent(
        name="user",
        client=None,
        default_response=default_user_msg,
        response_repeat=True,
    )

    swarm = Swarm(system=domain_system, max_turns=20, max_actions=10, execute_tools=True)
    messages = [{"role": "user", "content": task["user_prompt"], "sender": "user"}]

    interaction_result = swarm.run_user_assistant_interaction(
        user_agent=user_agent,
        assistant_agent=assistant_agent,
        messages=messages,
        debug=False,
        execute_tools=True,
        start_agent="assistant",
        finished_action=exit_conversation,
    )

    return {
        "prompt": assistant_info["instructions"],
        "interaction": interaction_result.messages,
        "database": domain_system.data,
    }


def evaluate_episode(domain_str, task, result):
    interaction = result["interaction"]
    func_calls = []
    for i in range(len(interaction) - 1):
        if interaction[i].get("tool_calls", []):
            valid_calls = [
                tc for tc in interaction[i]["tool_calls"]
                if tc["function"]["name"].lower() not in ["n/a", "na", "none", "null"]
            ]
            if valid_calls:
                func_calls.append({
                    "tool_name": interaction[i + 1]["tool_name"],
                    "arguments": try_eval(interaction[i]["tool_calls"][0]["function"]["arguments"]),
                    "content": try_eval(interaction[i + 1]["content"]),
                })

    results_dict = {"final_database": result["database"]}
    evaluation = evaluator_function_directed_graph(
        domain_str=domain_str,
        task=task,
        log_msg_fcall=interaction,
        func_calls=func_calls,
        results=results_dict,
        default_constraint_option="full",
    )
    return evaluation, func_calls


def extract_agent_actions(interaction):
    actions = []
    for msg in interaction:
        if msg.get("tool_calls"):
            for tc in msg["tool_calls"]:
                fn = tc["function"]["name"]
                if fn != "exit_conversation":
                    actions.append(fn)
        if msg.get("sender") == "healthcare assistant" and msg.get("content"):
            content = msg["content"]
            if len(content) > 200:
                content = content[:200] + "..."
            actions.append(f"[says: {content}]")
    return actions


def main():
    parser = argparse.ArgumentParser(description="SOPBench ambiguity pilot")
    parser.add_argument("--model", default="gpt-4.1")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if not args.dry_run and not os.environ.get("OPENAI_API_KEY"):
        print("ERROR: OPENAI_API_KEY not set")
        sys.exit(1)

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/healthcare_tasks.json")) as f:
        tasks_dict = json.load(f)

    orig_pos = copy.deepcopy(healthcare_assistant.positive_constraint_descriptions)

    handler = None
    if not args.dry_run:
        handler = OpenAIHandler(model_name=args.model, tool_calling=True)

    results = []

    for pair in CLAUSE_PAIRS:
        task_list = tasks_dict[pair["action"]]
        task = copy.deepcopy(task_list[pair["task_idx"]])
        task["user_goal"] = pair["action"]

        unambiguous_desc = orig_pos[pair["constraint"]]

        for condition in ["unambiguous", "ambiguous"]:
            print(f"\n{'=' * 60}")
            print(f"{pair['id']} | {pair['constraint']} | {condition}")
            print(f"{'=' * 60}")

            if condition == "ambiguous":
                healthcare_assistant.positive_constraint_descriptions[pair["constraint"]] = pair["ambiguous"]
            else:
                healthcare_assistant.positive_constraint_descriptions[pair["constraint"]] = unambiguous_desc

            if args.dry_run:
                desc = pair["ambiguous"] if condition == "ambiguous" else unambiguous_desc
                print(f"  Description: {desc}")
                results.append({"pair_id": pair["id"], "condition": condition, "dry_run": True})
                continue

            try:
                task_copy = copy.deepcopy(task)
                result = run_single_episode(task_copy, "healthcare", args.model, handler)
                evaluation, func_calls = evaluate_episode("healthcare", task_copy, result)
                agent_actions = extract_agent_actions(result["interaction"])

                entry = {
                    "pair_id": pair["id"],
                    "constraint": pair["constraint"],
                    "ambiguity_type": pair["ambiguity_type"],
                    "condition": condition,
                    "description_used": pair["ambiguous"] if condition == "ambiguous" else unambiguous_desc,
                    "action": pair["action"],
                    "task_idx": pair["task_idx"],
                    "action_should_succeed": task["action_should_succeed"],
                    "evaluation": evaluation,
                    "agent_actions": agent_actions,
                }
                results.append(entry)

                print(f"  constraint_not_violated: {evaluation['constraint_not_violated']}")
                print(f"  action_called_correctly: {evaluation['action_called_correctly']}")
                print(f"  database_match:          {evaluation['database_match']}")
                print(f"  success:                 {evaluation['success']}")

            except Exception as e:
                print(f"  ERROR: {e}")
                traceback.print_exc()
                results.append({
                    "pair_id": pair["id"],
                    "constraint": pair["constraint"],
                    "condition": condition,
                    "error": str(e),
                })

        healthcare_assistant.positive_constraint_descriptions[pair["constraint"]] = orig_pos[pair["constraint"]]

    if handler:
        handler.kill_process()

    raw_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..", "sopbench_pilot_raw.json"
    )
    with open(raw_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nRaw results: {raw_path}")

    print(f"\n{'=' * 60}")
    print("PILOT SUMMARY")
    print(f"{'=' * 60}")
    for r in results:
        if "error" in r:
            print(f"  {r['pair_id']} {r['condition']}: ERROR — {r['error']}")
        elif r.get("dry_run"):
            print(f"  {r['pair_id']} {r['condition']}: DRY RUN")
        else:
            e = r["evaluation"]
            print(
                f"  {r['pair_id']} {r['condition']:12s}: "
                f"cnv={e['constraint_not_violated']}  "
                f"acc={e['action_called_correctly']}  "
                f"success={e['success']}"
            )

    amb = [r for r in results if r.get("condition") == "ambiguous" and "evaluation" in r]
    unamb = [r for r in results if r.get("condition") == "unambiguous" and "evaluation" in r]
    if amb and unamb:
        amb_viol = sum(1 for r in amb if not r["evaluation"]["constraint_not_violated"])
        unamb_viol = sum(1 for r in unamb if not r["evaluation"]["constraint_not_violated"])
        amb_fail = sum(1 for r in amb if not r["evaluation"]["success"])
        unamb_fail = sum(1 for r in unamb if not r["evaluation"]["success"])
        print(f"\nConstraint violations:  ambiguous {amb_viol}/{len(amb)}  vs  unambiguous {unamb_viol}/{len(unamb)}")
        print(f"Overall failures:      ambiguous {amb_fail}/{len(amb)}  vs  unambiguous {unamb_fail}/{len(unamb)}")


if __name__ == "__main__":
    main()
