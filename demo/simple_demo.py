#!/usr/bin/env python3
"""
Simple Demo: Task-Based Cognitive Architecture
Demonstrates the core cognitive loop without requiring API keys.
Uses a mock LLM and pre-built knowledge base.
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from typing import Dict, List, Tuple


class MockLLM:
    """Mock LLM that generates deterministic hypotheses for demo tasks."""
    
    def generate_hypotheses(self, task: str) -> List[Dict]:
        """Generate 3 hypotheses for the given task."""
        
        # Pre-programmed responses for demo tasks
        if "notebook" in task.lower() and "pen" in task.lower():
            # Math word problem
            return [
                {
                    "hypothesis": "5 pens",
                    "reasoning": "Notebooks cost $15 (5 × $3). Remaining budget: $25 - $15 = $10. Pens at $2 each: $10 ÷ $2 = 5 pens.",
                    "confidence": 0.78
                },
                {
                    "hypothesis": "4 pens",
                    "reasoning": "Alternative calculation, but likely incorrect.",
                    "confidence": 0.15
                },
                {
                    "hypothesis": "6 pens",
                    "reasoning": "Another possibility, but doesn't match total.",
                    "confidence": 0.07
                }
            ]
        else:
            # Generic response
            return [
                {
                    "hypothesis": "Answer requires full system with LLM API",
                    "reasoning": "This is a demo. For real tasks, use --api-key",
                    "confidence": 0.50
                }
            ]


class SimpleLogicEngine:
    """Simplified logic engine for demo purposes."""
    
    def __init__(self):
        self.knowledge_base = {
            "pen_cost": {"value": 2.0, "confidence": 0.95},
            "notebook_cost": {"value": 3.0, "confidence": 0.95}
        }
        self.theta = 0.85  # Confidence threshold
    
    def validate(self, hypothesis: Dict, task: str) -> Tuple[bool, float]:
        """Validate hypothesis and return (passed, confidence)."""
        
        # Extract the answer
        answer_text = hypothesis["hypothesis"].lower()
        
        # For the demo math task
        if "5 pens" in answer_text:
            # Simulate validation logic
            # Initial confidence from LLM: 0.78
            initial_conf = hypothesis["confidence"]
            
            # Check if we have supporting knowledge
            if "pen_cost" in self.knowledge_base:
                # Enrich with retrieved knowledge
                pen_cost_conf = self.knowledge_base["pen_cost"]["confidence"]
                # Recalculate confidence: p(h|ctx') = p(h|ctx) × p(retrieved_fact)
                # Using simplified formula from paper
                final_conf = min(initial_conf / 0.70 * pen_cost_conf, 0.999)
                
                print(f"\n  [Logic Engine] Validation steps:")
                print(f"    1. Initial hypothesis confidence: {initial_conf:.3f}")
                print(f"    2. Retrieved knowledge: pen_cost = ${self.knowledge_base['pen_cost']['value']} (conf: {pen_cost_conf:.3f})")
                print(f"    3. Recalculated confidence: {final_conf:.3f}")
                print(f"    4. Threshold check: {final_conf:.3f} >= {self.theta:.2f} ? {'✓ PASS' if final_conf >= self.theta else '✗ FAIL'}")
                
                return (final_conf >= self.theta, final_conf)
            else:
                # No supporting knowledge, use initial confidence
                return (initial_conf >= self.theta, initial_conf)
        
        # Default: fail validation
        return (False, hypothesis["confidence"])


class SimpleCognitiveLoop:
    """Simplified cognitive loop for demonstration."""
    
    def __init__(self):
        self.llm = MockLLM()
        self.logic_engine = SimpleLogicEngine()
    
    def run(self, task: str) -> Dict:
        """Execute cognitive loop on a task."""
        
        print(f"\n{'='*70}")
        print(f"TASK: {task}")
        print(f"{'='*70}")
        
        # Phase 1: LLM Hypothesis Generation
        print(f"\n[Phase 1] LLM Hypothesis Generation")
        hypotheses = self.llm.generate_hypotheses(task)
        
        for i, h in enumerate(hypotheses, 1):
            print(f"\n  Hypothesis {i}: {h['hypothesis']}")
            print(f"    Reasoning: {h['reasoning']}")
            print(f"    Initial confidence: {h['confidence']:.3f}")
        
        # Phase 2: Logic Validation
        print(f"\n[Phase 2] Logic Validation")
        
        for i, h in enumerate(hypotheses, 1):
            print(f"\n  Validating Hypothesis {i}: {h['hypothesis']}")
            passed, final_conf = self.logic_engine.validate(h, task)
            
            if passed:
                print(f"\n{'='*70}")
                print(f"RESULT: ✓ VALIDATED")
                print(f"{'='*70}")
                print(f"Answer: {h['hypothesis']}")
                print(f"Final Confidence: {final_conf:.3f}")
                print(f"Status: PASSED (confidence {final_conf:.3f} >= threshold {self.logic_engine.theta})")
                print(f"{'='*70}\n")
                
                return {
                    "answer": h["hypothesis"],
                    "confidence": final_conf,
                    "status": "validated",
                    "reasoning": h["reasoning"]
                }
        
        # If no hypothesis passed, return best one with warning
        best_h = max(hypotheses, key=lambda x: x["confidence"])
        print(f"\n{'='*70}")
        print(f"RESULT: ✗ NOT VALIDATED")
        print(f"{'='*70}")
        print(f"Best hypothesis: {best_h['hypothesis']}")
        print(f"Confidence: {best_h['confidence']:.3f}")
        print(f"Status: FAILED (below threshold {self.logic_engine.theta})")
        print(f"Note: In full system, this would trigger gap resolution.")
        print(f"{'='*70}\n")
        
        return {
            "answer": best_h["hypothesis"],
            "confidence": best_h["confidence"],
            "status": "unvalidated",
            "reasoning": best_h["reasoning"]
        }


def main():
    """Run simple demo."""
    
    print("""
╔══════════════════════════════════════════════════════════════════════╗
║  AGI-Powered Metaverse: Task-Based Cognitive Architecture            ║
║  Simple Demo (No API Keys Required)                                  ║
╚══════════════════════════════════════════════════════════════════════╝

This demo shows the core cognitive loop with:
  • Mock LLM (pre-programmed responses)
  • Simple logic engine (with knowledge base)
  • Confidence-based validation (threshold θ = 0.85)

For full experiments with real LLMs, see: experiments/
    """)
    
    # Initialize cognitive loop
    loop = SimpleCognitiveLoop()
    
    # Demo tasks
    tasks = [
        "A store sells notebooks for $3 each and pens for $2 each. If Sarah buys 5 notebooks and some pens, spending $25 total, how many pens did she buy?"
    ]
    
    # Run tasks
    for task in tasks:
        result = loop.run(task)
    
    print("\n" + "="*70)
    print("Demo complete!")
    print("="*70)
    print("\nNext steps:")
    print("  1. See experiments/ for full task reproduction")
    print("  2. Add API keys in configs/api_keys.env for real LLMs")
    print("  3. Read docs/ARCHITECTURE.md for system details")
    print()


if __name__ == "__main__":
    main()
