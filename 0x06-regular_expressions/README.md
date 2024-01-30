# Regular Expressions Project

This project involves creating Ruby scripts that use regular expressions with the Oniguruma library. Each script performs a specific regex matching task.

## Table of Contents

1. [Simply Matching School](#1-simply-matching-school)
2. [Repetition Token #0](#2-repetition-token-0)
3. [Repetition Token #1](#3-repetition-token-1)
4. [Repetition Token #2](#4-repetition-token-2)
5. [Repetition Token #3](#5-repetition-token-3)
6. [Not Quite HBTN Yet](#6-not-quite-hbtn-yet)
7. [Call Me Maybe](#7-call-me-maybe)
8. [OMG WHY ARE YOU SHOUTING?](#8-omg-why-are-you-shouting)

## 1. Simply Matching School

The regular expression must match "School." The Ruby script accepts one argument and passes it to the regular expression matching method.

Example:

```bash
./0-simply_match_school.rb School | cat -e
School$
./0-simply_match_school.rb "Best School" | cat -e
School$
./0-simply_match_school.rb "School Best School" | cat -e
SchoolSchool$
./0-simply_match_school.rb "Grace Hopper" | cat -e
$
Link to scrip
2. Repetition Token #0
Find the regular expression that matches specific cases. The Ruby script accepts one argument and passes it to the regular expression matching method.

Link to script

(Repeat the pattern for other tasks)

8. OMG WHY ARE YOU SHOUTING?
The regular expression must match only capital letters. The Ruby script accepts one argument and passes it to the regular expression matching method.

Example:
./7-OMG_WHY_ARE_YOU_SHOUTING.rb "I realLy hOpe VancouvEr posseSs Yummy Soft vAnilla Dupper Mint Ice Nutella cream" | cat -e
ILOVESYSADMIN$
./7-OMG_WHY_ARE_YOU_SHOUTING.rb "WHAT do you SAY?" | cat -e
WHATSAY$
./7-OMG_WHY_ARE_YOU_SHOUTING.rb "cannot read you" | cat -e
$
Link to script

Author
Abayo24
