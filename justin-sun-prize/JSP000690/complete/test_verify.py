import unittest
from verify import audit, NAMES

class AxiomAuditTests(unittest.TestCase):
    def valid(self):
        return '\n'.join(f"'{n}' depends on axioms: [propext, Classical.choice, Quot.sound]" for n in NAMES)
    def test_all_expected_targets(self):
        self.assertEqual(set(audit(self.valid())), set(NAMES))
    def test_missing_target(self):
        with self.assertRaises(ValueError): audit('\n'.join(self.valid().splitlines()[:-1]))
    def test_sorry_axiom(self):
        with self.assertRaises(ValueError): audit(self.valid().replace('Quot.sound', 'sorryAx', 1))
    def test_native_axiom(self):
        with self.assertRaises(ValueError): audit(self.valid().replace('Quot.sound', 'Lean.ofReduceBool', 1))
    def test_custom_axiom(self):
        with self.assertRaises(ValueError): audit(self.valid().replace('Quot.sound', 'AssumeEverything', 1))
    def test_duplicate_report(self):
        with self.assertRaises(ValueError): audit(self.valid() + '\n' + self.valid().splitlines()[0])
    def test_empty(self):
        with self.assertRaises(ValueError): audit('')

if __name__ == '__main__': unittest.main()
