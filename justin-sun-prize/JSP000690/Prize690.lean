set_option maxRecDepth 100000
set_option maxHeartbeats 4000000
namespace Prize690
abbrev V := Fin 9
abbrev Edge := V × V × V
abbrev HGraph := List Edge

def edges : HGraph := [
  (0,1,2),(0,1,8),(0,2,7),(0,3,5),(0,3,7),(0,3,8),
  (0,4,6),(0,4,7),(0,4,8),(0,5,6),(1,2,5),(1,2,6),
  (1,3,8),(1,4,8),(1,5,6),(2,3,7),(2,4,7),(2,5,6),
  (3,5,7),(3,5,8),(4,6,7),(4,6,8)]

def edgeProperB {k : Nat} (c : V → Fin k) (e : Edge) : Bool :=
  decide (c e.1 ≠ c e.2.1 ∨ c e.1 ≠ c e.2.2 ∨ c e.2.1 ≠ c e.2.2)

def properB {k : Nat} (G : HGraph) (c : V → Fin k) : Bool :=
  G.all (edgeProperB c)

def Proper {k : Nat} (G : HGraph) (c : V → Fin k) : Prop := properB G c = true

instance {k : Nat} (G : HGraph) (c : V → Fin k) : Decidable (Proper G c) := by
  unfold Proper
  infer_instance

def bitColour (m : Nat) (v : V) : Fin 2 :=
  ⟨m / (2 ^ v.val) % 2, Nat.mod_lt _ (by decide)⟩

/-- Exact exhaustive encoding of all 2^9 binary colourings. -/
def TwoColourable (G : HGraph) : Prop :=
  (List.range 512).any (fun m => properB G (bitColour m)) = true

instance (G : HGraph) : Decidable (TwoColourable G) := by
  unfold TwoColourable
  infer_instance

def triColour (v : V) : Fin 3 :=
  if v = 0 then 0 else if v = 1 then 1 else if v = 2 then 2 else
  if v = 3 then 0 else if v = 4 then 0 else if v = 5 then 1 else
  if v = 6 then 2 else if v = 7 then 1 else 2

def Degree (G : HGraph) (v : V) : Nat :=
  (G.filter (fun e => decide (e.1 = v ∨ e.2.1 = v ∨ e.2.2 = v))).length

theorem edge_count : edges.length = 22 := by decide
theorem min_degree : ∀ v : V, 7 ≤ Degree edges v := by decide
theorem no_isolated : ∀ v : V, 0 < Degree edges v := by decide
theorem three_colourable : Proper edges triColour := by decide
theorem not_two_colourable : ¬ TwoColourable edges := by decide

theorem every_edge_deletion : ∀ e ∈ edges, TwoColourable (edges.erase e) := by
  intro e he
  simp [edges] at he
  rcases he with rfl|rfl|rfl|rfl|rfl|rfl|rfl|rfl|rfl|rfl|rfl|rfl|rfl|rfl|rfl|rfl|rfl|rfl|rfl|rfl|rfl|rfl
  all_goals decide

/-- Finite certificate for the published critical 3-chromatic witness.
    Edge-deletion criticality plus no isolated vertices implies the usual
    proper edge/vertex-subhypergraph criticality by colouring restriction. -/
theorem finite_witness :
    edges.length = 22 ∧
    (∀ v : V, 7 ≤ Degree edges v) ∧
    Proper edges triColour ∧
    ¬ TwoColourable edges ∧
    (∀ e ∈ edges, TwoColourable (edges.erase e)) ∧
    (∀ v : V, 0 < Degree edges v) := by
  exact ⟨edge_count, min_degree, three_colourable, not_two_colourable,
    every_edge_deletion, no_isolated⟩

#print axioms finite_witness
#print axioms not_two_colourable
end Prize690
