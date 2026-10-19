"""Deterministic AST mutations for the hidden bug-fix task family."""

import ast
import copy
import hashlib
from dataclasses import dataclass

try:
    from scripts.import_bigcodebench_hard_canary import run_pytest
except ModuleNotFoundError:  # Direct execution from scripts/
    from import_bigcodebench_hard_canary import run_pytest

MUTATION_SEED = 20260727
OPERATOR_ORDER = (
    "boundary_comparison",
    "off_by_one_constant",
    "conditional_branch_deletion",
    "default_value_replacement",
    "aggregation_replacement",
)


@dataclass(frozen=True)
class Mutation:
    operator: str
    location: str
    source: str


def _location(node: ast.AST) -> str:
    return f"{getattr(node, 'lineno', 0)}:{getattr(node, 'col_offset', 0)}"


def _seeded(nodes: list[ast.AST], operator: str) -> list[ast.AST]:
    return sorted(
        nodes,
        key=lambda node: hashlib.sha256(
            f"{MUTATION_SEED}:{operator}:{_location(node)}".encode()
        ).hexdigest(),
    )


def _source(tree: ast.Module) -> str:
    ast.fix_missing_locations(tree)
    generated = ast.unparse(tree).rstrip() + "\n"
    compile(generated, "<mutated canonical solution>", "exec")
    return generated


def _boundary_candidates(tree: ast.Module):
    operator = "boundary_comparison"
    supported = {
        ast.Lt: ast.LtE,
        ast.LtE: ast.Lt,
        ast.Gt: ast.GtE,
        ast.GtE: ast.Gt,
    }
    matches = [
        node for node in ast.walk(tree)
        if isinstance(node, ast.Compare)
        and len(node.ops) == 1
        and type(node.ops[0]) in supported
    ]
    ordered_locations = [_location(node) for node in _seeded(matches, operator)]
    for location in ordered_locations:
        candidate = copy.deepcopy(tree)
        target = next(
            node for node in ast.walk(candidate)
            if isinstance(node, ast.Compare)
            and _location(node) == location
            and len(node.ops) == 1
            and type(node.ops[0]) in supported
        )
        target.ops[0] = supported[type(target.ops[0])]()
        yield Mutation(operator, location, _source(candidate))


def _constant_candidates(tree: ast.Module):
    operator = "off_by_one_constant"
    matches = [
        node for node in ast.walk(tree)
        if isinstance(node, ast.Constant)
        and isinstance(node.value, int)
        and not isinstance(node.value, bool)
    ]
    ordered_locations = [_location(node) for node in _seeded(matches, operator)]
    for location in ordered_locations:
        candidate = copy.deepcopy(tree)
        target = next(
            node for node in ast.walk(candidate)
            if isinstance(node, ast.Constant)
            and _location(node) == location
            and isinstance(node.value, int)
            and not isinstance(node.value, bool)
        )
        target.value += 1
        yield Mutation(operator, location, _source(candidate))


def _branch_candidates(tree: ast.Module):
    operator = "conditional_branch_deletion"
    matches = [node for node in ast.walk(tree) if isinstance(node, ast.If)]
    ordered_locations = [_location(node) for node in _seeded(matches, operator)]
    for location in ordered_locations:
        candidate = copy.deepcopy(tree)
        target = next(
            node for node in ast.walk(candidate)
            if isinstance(node, ast.If) and _location(node) == location
        )
        target.test = ast.Constant(value=False)
        yield Mutation(operator, location, _source(candidate))


def _replacement_default(node: ast.AST) -> ast.AST:
    if isinstance(node, ast.Constant):
        if node.value is None:
            return ast.Constant(value=False)
        if isinstance(node.value, bool):
            return ast.Constant(value=not node.value)
        if isinstance(node.value, int):
            return ast.Constant(value=node.value + 1)
        if isinstance(node.value, float):
            return ast.Constant(value=node.value + 1.0)
        if isinstance(node.value, str):
            return ast.Constant(value="" if node.value else "default")
    return ast.Constant(value=None)


def _default_candidates(tree: ast.Module):
    operator = "default_value_replacement"
    matches = []
    for function in ast.walk(tree):
        if not isinstance(function, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        matches.extend(function.args.defaults)
        matches.extend(
            default for default in function.args.kw_defaults
            if default is not None
        )
    ordered_locations = [_location(node) for node in _seeded(matches, operator)]
    for location in ordered_locations:
        candidate = copy.deepcopy(tree)
        replaced = False
        for function in ast.walk(candidate):
            if not isinstance(function, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            for defaults_name in ("defaults", "kw_defaults"):
                defaults = getattr(function.args, defaults_name)
                for index, default in enumerate(defaults):
                    if default is not None and _location(default) == location:
                        defaults[index] = _replacement_default(default)
                        replaced = True
                        break
                if replaced:
                    break
            if replaced:
                break
        if replaced:
            yield Mutation(operator, location, _source(candidate))


def _aggregation_candidates(tree: ast.Module):
    operator = "aggregation_replacement"
    replacements = {
        "sum": "max",
        "max": "min",
        "min": "max",
        "all": "any",
        "any": "all",
    }
    matches = [
        node for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id in replacements
    ]
    ordered_locations = [_location(node) for node in _seeded(matches, operator)]
    for location in ordered_locations:
        candidate = copy.deepcopy(tree)
        target = next(
            node for node in ast.walk(candidate)
            if isinstance(node, ast.Call)
            and _location(node) == location
            and isinstance(node.func, ast.Name)
            and node.func.id in replacements
        )
        target.func.id = replacements[target.func.id]
        yield Mutation(operator, location, _source(candidate))


def generate_mutations(source: str):
    """Yield candidates in the preregistered operator order."""
    tree = ast.parse(source)
    generators = (
        _boundary_candidates,
        _constant_candidates,
        _branch_candidates,
        _default_candidates,
        _aggregation_candidates,
    )
    for generator in generators:
        for mutation in generator(tree):
            yield mutation


def select_accepted_mutation(
        canonical_source: str,
        visible_tests: str,
        hidden_tests: str,
        *,
        test_runner=run_pytest) -> Mutation | None:
    """Take the first candidate that passes visible and fails hidden tests."""
    for mutation in generate_mutations(canonical_source):
        visible = test_runner(mutation.source, visible_tests)
        if visible.returncode != 0:
            continue
        hidden = test_runner(mutation.source, hidden_tests)
        if hidden.returncode != 0:
            return mutation
    return None
