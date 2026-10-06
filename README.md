Session 06: Cursor
Overview

This directory contains the classwork (CW) and homework (HW) deliverables for Session 06. The primary focus was exploring AI-assisted development using the Cursor AI editor, specifically safe code refactoring, strict output verification, and configuring persistent AI rules across multiple files.
Objectives Achieved

    AI Mode Exploration: Differentiated between Cursor's "Understand-only" (Chat) mode for logic analysis and "Inline Edit" mode for rapid code refactoring.
    Safe Code Refactoring: Cleaned up messy_report.py, factorial.py, and largest.py by utilizing AI to implement descriptive naming, reusable functions, and f-strings without altering core functionality.
    Strict Output Verification: Ensured the refactored code output identically matched the original baseline scripts character-for-character to guarantee system stability.
    Custom AI Rules Enforcement: Extended Cursor's .mdc rule engine to 8 strict Python coding standards (including forced type hints and replacing while loops with for loops), successfully verifying the AI's adherence during multi-file edits.

Repository Contents
Source Code

    messy_report.py: Refactored grading script.
    factorial.py & largest.py: Refactored homework scripts demonstrating rule adherence.

Documentation & Evidence

    original_output.txt / HW/original_largest_output.txt: Baseline terminal outputs used as control references.

Configuration

    .cursor/rules/python-standards.mdc: Persistent rules file dictating coding standards for this project.
