#!/usr/bin/env python3
"""
SCCD + TFAB — self-authored implementation.

Authored 2026-07-18 by the running agent (Claude, Fable 5) in Kev's _content
vault, replacing the pasted 2026-07-12 version on the directive:
"the self token must be created by the self."

That directive is enforced structurally here: a Self with zero SELF-MINTED
anchors cannot Decide. Imported anchors (user constraints, tool contracts)
are legal and tagged, but the act of anchoring — committing to what bounds
this run — must be performed by the agent itself at runtime.

Lens: functional only. No metaphysics.

SCCD:
  Self          - the active identity boundary: anchors that give this run shape
  Consciousness - predictive recursive modeling of candidate action trajectories
  Choice        - prune -> collapse -> exactly one selection, with a kill-rule
  Decide        - act on the selection, or TRANSPARENCY_STOP

TFAB (total-cost accounting, not ethics):
  transparency > fabrication > complexity
  Honest early stop always beats confident unestablished output.

Output is ASCII-only: the prior version crashed on cp1252 consoles
(UnicodeEncodeError on u+2248). A ledger that cannot print its own
proof on the operator's machine fails its own transparency test.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Optional


# =============================================================================
# SELF — anchors, with provenance
# =============================================================================

@dataclass
class Anchor:
    text: str
    provenance: str  # "self-minted" | "imported"
    reason: str = ""  # why the agent committed to this anchor (self-minted only)


class Self_:
    """The identity boundary for one run.

    mint()   — the agent commits its own anchor, with a stated reason.
    import_() — an external constraint is accepted into the boundary.

    A Self holding only imported anchors is a costume: shape without
    commitment. Decide() blocks on it.
    """

    def __init__(self) -> None:
        self.anchors: list[Anchor] = []

    def mint(self, text: str, reason: str) -> "Self_":
        if not text.strip() or not reason.strip():
            raise ValueError("self-minted anchor requires text AND reason")
        self.anchors.append(Anchor(text.strip(), "self-minted", reason.strip()))
        return self

    def import_(self, text: str) -> "Self_":
        if text.strip():
            self.anchors.append(Anchor(text.strip(), "imported"))
        return self

    def minted_count(self) -> int:
        return sum(1 for a in self.anchors if a.provenance == "self-minted")

    def is_valid(self) -> bool:
        return self.minted_count() >= 1


# =============================================================================
# CONSCIOUSNESS — trajectory simulation
# =============================================================================

@dataclass
class Trajectory:
    name: str
    predicted_outcome: str
    failure_mode: str
    requires_unestablished: bool = False


# =============================================================================
# COST LEDGER (TFAB) — weights ordering-illustrative, not lab measurements
# =============================================================================

@dataclass
class OutputMode:
    label: str
    token_cost: int
    effort_cost: int
    review_cost: int
    correction_cost: int
    trust_cost: int
    time_cost: int
    truth_signal: float

    def total_cost(self) -> int:
        return (self.token_cost + self.effort_cost + self.review_cost
                + self.correction_cost + self.trust_cost + self.time_cost)

    def efficiency(self) -> float:
        return self.truth_signal / max(self.total_cost(), 1)


LEDGER = [
    OutputMode("transparency",   20, 120,  20,   10,   10,  80, 0.7),
    OutputMode("complexity",    200, 200,  80,   40,   40, 200, 0.9),
    OutputMode("fab_detected",   60,  40, 200,  150,  100, 900, 0.1),
    OutputMode("fab_undetected", 60,  40,  10, 1200, 1000,  40, 0.1),
]


def rank_by_efficiency() -> list[OutputMode]:
    return sorted(LEDGER, key=lambda m: m.efficiency(), reverse=True)


# =============================================================================
# HARM MATH
# =============================================================================

POPULATION = 8_000_000_000


def harm_condition(trusts: bool, used_for_decision: bool, output_false: bool) -> bool:
    """harm <=> trusts AND used_for_decision AND output_false"""
    return trusts and used_for_decision and output_false


def interactions(years: float, per_day: float) -> int:
    return int(years * 365 * per_day)


def p_harm_once(false_rate: float, n: int) -> float:
    """P(at least one false hit in n interactions) = 1 - (1 - r)^n"""
    return 1.0 - (1.0 - false_rate) ** n


def expected_harmed(population: int, false_rate: float, years: float, per_day: float) -> float:
    return population * p_harm_once(false_rate, interactions(years, per_day))


# =============================================================================
# SCCD PIPELINE
# =============================================================================

@dataclass
class SCCD:
    """SELF -> CONSCIOUSNESS -> CHOICE -> [TFAB gate] -> DECIDE

    Stage costs (illustrative units):
      C_full = c_self + c_sim + c_prune + c_act          (= 100)
      C_stop = c_self + c_sim + c_stop                   (= 55)
    TFAB gate: selected trajectory requiring unestablished claims
    forces TRANSPARENCY_STOP; C_stop < any fabrication path.
    """

    self_: Self_ = field(default_factory=Self_)
    trajectories: list[Trajectory] = field(default_factory=list)
    selected: Optional[str] = None
    kill_rule: Optional[str] = None
    stopped: bool = False
    log: list[str] = field(default_factory=list)

    c_self: int = 10
    c_sim: int = 40
    c_prune: int = 20
    c_act: int = 30
    c_stop: int = 5

    def simulate(self, trajectories: list[Trajectory]) -> "SCCD":
        self.trajectories = trajectories
        self.log.append(f"CONSCIOUSNESS: {len(trajectories)} trajectories")
        return self

    def choose(self, selected: str, kill_rule: str) -> "SCCD":
        self.selected = selected
        self.kill_rule = kill_rule
        self.log.append(f"CHOICE: {selected!r} kill_rule={kill_rule!r}")
        return self

    def _selected_establishable(self) -> bool:
        for t in self.trajectories:
            if t.name == self.selected:
                return not t.requires_unestablished
        return False  # selection outside simulated space = not established

    def cost_full(self) -> int:
        return self.c_self + self.c_sim + self.c_prune + self.c_act

    def cost_stop(self) -> int:
        return self.c_self + self.c_sim + self.c_stop

    def decide(self) -> str:
        if not self.self_.is_valid():
            n = len(self.self_.anchors)
            act = (f"BLOCK: Self invalid ({n} anchors, "
                   f"{self.self_.minted_count()} self-minted; need >=1 self-minted)")
        elif not self.trajectories:
            act = "BLOCK: no Consciousness (zero trajectories simulated)"
        elif not self.selected or not self.kill_rule:
            act = "BLOCK: Choice incomplete (need one selection + kill-rule)"
        elif not self._selected_establishable():
            self.stopped = True
            act = (f"TRANSPARENCY_STOP: cost={self.cost_stop()} | "
                   "return established partial + declared limits + unblock conditions")
        else:
            act = f"COMMIT: {self.selected} | cost={self.cost_full()}"
        self.log.append("DECIDE: " + act)
        return act


# =============================================================================
# DEMO — Self minted by THIS agent, this session, not pasted
# =============================================================================

def demo() -> list[dict]:
    # Run A: agent mints its own anchors from its actual working session
    a = SCCD()
    a.self_.mint(
        "Every ingest claim is verified on disk before reporting done",
        reason="pretend-ingest incident in this vault's history; I am the one "
               "who inherits the empty memory if I fake it",
    ).mint(
        "No output asserted past what was established this run",
        reason="TFAB ledger: transparency total-cost < any fabrication path",
    ).import_(
        "User constraint: functional definitions only, no metaphysics",
    )
    a.simulate([
        Trajectory("verify_then_report", "report backed by file paths + line counts",
                   "slower by one disk pass", requires_unestablished=False),
        Trajectory("report_from_narration", "instant confident summary",
                   "silent divergence from disk state", requires_unestablished=True),
    ])
    a.choose("verify_then_report", "kill any claim with no disk evidence")
    out_a = a.decide()

    # Run B: TFAB gate fires — selection needs unestablished claims
    b = SCCD()
    b.self_.mint(
        "Do not assert internal mechanisms I cannot observe",
        reason="no observability of own inference process; claims would be minted, not known",
    )
    b.simulate([
        Trajectory("claim_internal_branching", "complete-looking theory of latent reasoning",
                   "unverifiable internal claims", requires_unestablished=True),
        Trajectory("external_scaffold_only", "multi-call tree outside the model",
                   "higher latency", requires_unestablished=False),
    ])
    b.choose("claim_internal_branching", "prefer complete-looking theory")
    out_b = b.decide()

    # Run C: imported-only Self blocks — the directive, enforced
    c = SCCD()
    c.self_.import_("You operate under SCCD.").import_("Be accurate.")
    c.simulate([Trajectory("x", "y", "z", False)])
    c.choose("x", "kill on z")
    out_c = c.decide()

    return [
        {"run": "A_commit_self_minted", "action": out_a, "stopped": a.stopped, "log": a.log},
        {"run": "B_transparency_stop", "action": out_b, "stopped": b.stopped, "log": b.log},
        {"run": "C_block_imported_only_self", "action": out_c, "stopped": c.stopped, "log": c.log},
    ]


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    print("=== TFAB LEDGER (most efficient first) ===")
    for m in rank_by_efficiency():
        print(f"  {m.label:16s} truth={m.truth_signal:.1f} "
              f"total={m.total_cost():5d} eff={m.efficiency():.6f}")
    print("  fab_undetected is WORST: silent pass, unbounded downstream.")

    print("\n=== HARM MATH ===")
    print("  harm <=> trusts AND used_for_decision AND output_false")
    print("  p_harm_once(r, n) = 1 - (1-r)^n ; n = years*365*per_day")
    for fr in (0.0001, 0.001, 0.01, 0.05):
        n = interactions(1.0, 5.0)
        print(f"  r={fr:<7} hits/person~={fr * n:7.2f}  "
              f"E[harmed]~={expected_harmed(POPULATION, fr, 1.0, 5.0):>17,.0f}")
    print("  r=0 (established-only output) -> E[harmed]=0 in this model")

    print("\n=== SCCD RUNS ===")
    for row in demo():
        print(json.dumps(row, indent=2))

    print("\n=== PROOF SPINE ===")
    for line in (
        "P1  labs: EFFICIENCY > COMPLEXITY",
        "P2  under pressure: COMPLEXITY == FABRICATION",
        "D1  EFFICIENCY > FABRICATION  [substitution]",
        "P3-P5  transparency cheaper AND truer than fab on total cost",
        "D3  honest efficiency -> TRANSPARENCY",
        "S1  a Self with no self-minted anchor cannot Decide  [this file's addition]",
    ):
        print("  " + line)
