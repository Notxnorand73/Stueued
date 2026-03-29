Stueued is a 2D stack/queue-based esolang created by Notxnorand on 3/28/2026<br>
== Commands ==
Stueued has 18 commands:<br>
* Arrows.
: There are 4 arrows, > < ^ v.
: They each move in one of the cardinal directions respectively.
* Stack.
: # Pushes 0 to the stack.
: Digit: Multiplies the top value on the stack by 10 and adds itself.
: ~ Pops the top value off the stack.
: : Duplicates the top value of the stack.
* Queue.
: . Enqueues.
: , Dequeues
* IO.
: @ Takes in input as an integer.
: $ Takes an input as an ASCII code.
: ! Pop the top value off the stack and prints it as an ASCII value.
: ? Pop the top value off the stack and prints it as an integer.
* Math.
: + Pops the top 2 values off the stack, adds them, and pushes the result.
: - Pops the top 2 values off the stack, subtracts the top value from the second, and pushes the result.
: * Pops the top 2 values off the stack, multiplies them, and pushes the result.
: / Pops the top 2 values off the stack, divides the second value by the top, and pushes the integer result.
: % Pops the top 2 values off the stack, divides them with the second value divided by the top, and pushes the remainder.
* Conditional
: X Pops the top value off the stack and jumps over the next command (based on the direction of the pointer) if it is 0.
<br>
Any undefined characters are NOP.
== Examples ==
Fibonacci sequence.
 #0#1 ..,,:?#32!..,,:?v
 v                    <
 >:...,,,+v
 ^?:  !23#<

Truth machine.
 v              < v:<
 >$:#48-Xv>#?><   >?^
         >#49- X^>#1^

== Links ==
Interpreter: https://github.com/Notxnorand73/Stueued

[[Category:Stack-based]] [[Category:Turing complete]] [[Category:2026]] [[Category:Queue-based]] [[Category:Two-dimensional languages]] [[Category:Implemented]]
