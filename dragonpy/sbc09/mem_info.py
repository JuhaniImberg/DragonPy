#!/usr/bin/env python

"""
    DragonPy - sbc09 memory info
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :created: 2013 by Jens Diemer - www.jensdiemer.de
    :copyleft: 2013 by the DragonPy team, see AUTHORS for more details.
    :license: GNU GPL v3 or above, see LICENSE for more details.
"""


import logging
from dragonpy.core.memory_info import BaseMemoryInfo


log = logging.getLogger("DragonPy.sbc09.mem_info")


class SBC09MemInfo(BaseMemoryInfo):
    MEM_INFO = (
        # generated from "monitor.lst":
        (0xe400, 0xe400, "Disable interrupts."),
        (0xe403, 0xe403, "Set direct page register to 0."),
        (0xe411, 0xe411, "Initialize interrupt vectors from ROM."),
        (0xe41b, 0xe41b, "Initialize I/O vectors from ROM."),
        (0xe41d, 0xe41d, "Initialize serial port."),
        (0xe41f, 0xe41f, "Enable interrupts"),
        (0xe421, 0xe421, "Put the 'saved' registers of the program being monitored on top of the stack. There are 12 bytes on the stack for cc,b,a,dp,x,y,u and pc pc is initialized to 0x400, the rest to zero."),
        (0xe437, 0xe437, "Clear the variable area."),
        (0xe43c, 0xe43c, "Set XMODEM filler and end-of-line."),
        (0xe445, 0xe445, "Print a welcome message."),
        (0xe44a, 0xe44a, "Block move routine, from X to U length B. Modifies them all and A."),
        (0xe452, 0xe452, "Initialize serial communications port, buffers, interrupts."),
        (0xe45a, 0xe45a, "O.S. routine to read a character into B register."),
        (0xe465, 0xe465, "O.S. rotuine to check if there is a character ready to be read."),
        (0xe471, 0xe471, "O.S. routine to write the character in the B register."),
        (0xe480, 0xe480, "O.S. routine to read a line into memory at address X, at most B chars long, return actual length in B. Permit backspace editing."),
        (0xe491, 0xe491, "Recognize BS and DEL as backspace key."),
        (0xe492, 0xe492, "ignore if line already zero length."),
        (0xe49c, 0xe49c, "Send BS,space,BS. This erases last"),
        (0xe49e, 0xe49e, "character on most terminals."),
        (0xe4a0, 0xe4a0, "Decrement address."),
        (0xe4ab, 0xe4ab, "CR or LF character ends line."),
        (0xe4af, 0xe4af, "Move length to B"),
        (0xe4b1, 0xe4b1, "restore registers."),
        (0xe4b3, 0xe4b3, "<--- Here is the exit point."),
        (0xe4b6, 0xe4b6, "Ignore control characters."),
        (0xe4ba, 0xe4ba, "Ignore char if line full."),
        (0xe4bc, 0xe4bc, "Echo the character."),
        (0xe4be, 0xe4be, "Store it in memory."),
        (0xe4c3, 0xe4c3, "O.S. routine to write a line starting at address X, B chars long."),
        (0xe4d4, 0xe4d4, "O.S. routine to terminate a line."),
        (0xe4dc, 0xe4dc, "Send the CR and LF characters."),
        (0xe4e1, 0xe4e1, "Output a counted string at addr X"),
        (0xe4f7, 0xe4f7, "Wait D times 20ms."),
        (0xe4ff, 0xe4ff, "This table will be copied to the interrupt vector area in RAM."),
        (0xe51a, 0xe51a, "And this one to the I/O vector table."),
        (0xe53e, 0xe53e, "Stack something where the pc comes"),
        (0xe53e, 0xe53e, "The J command returns here."),
        (0xe540, 0xe540, "Stack the normal registers."),
        (0xe545, 0xe545, "Stack the old pc value."),
        (0xe549, 0xe549, "The G and P commands return here through a breakpoint. Registers are already stacked."),
        (0xe54e, 0xe54e, "Decrement pc before breakpoint"),
        (0xe550, 0xe550, "reenable the interrupts."),
        (0xe552, 0xe552, "Disarm the breakpoints."),
        (0xe566, 0xe566, "Ignore line if it is empty"),
        (0xe569, 0xe569, "Make location after line zero."),
        (0xe570, 0xe570, "Make 1st char uppercase."),
        (0xe578, 0xe578, "Unknown cmd if it is not a letter."),
        (0xe57d, 0xe57d, "Index into command table."),
        (0xe5b4, 0xe5b4, "Unknown command handling routine."),
        (0xe5c1, 0xe5c1, "Here are some useful messages."),
        (0xe6c5, 0xe6c5, "Output hex digit contained in A"),
        (0xe6ca, 0xe6ca, "It's the standard conversion trick ascii"),
        (0xe6cb, 0xe6cb, "to hex without branching."),
        (0xe6d0, 0xe6d0, "Output contents of A as two hex digits"),
        (0xe6de, 0xe6de, "Output contents of d as four hex digits"),
        (0xe6e7, 0xe6e7, "Skip X past spaces, B is first non-space character."),
        (0xe6ee, 0xe6ee, "Convert ascii hex digit in B register to binary Z flag set if no hex digit."),
        (0xe6f6, 0xe6f6, "Make uppercase."),
        (0xe6f8, 0xe6f8, "If higher than digit 9 it must be a letter."),
        (0xe702, 0xe702, "clear zero"),
        (0xe70f, 0xe70f, "Scan for hexadecimal number at address X return in D, Z flag is set it no number found."),
        (0xe74a, 0xe74a, "Scan two hexdigits at in and convert to byte into A, Z flag if error."),
        (0xe760, 0xe760, "Clear zero flag"),
        (0xe763, 0xe763, "This is the code for the D command, hex/ascii dump of memory Syntax: D or D<addr> or D<addr>,<length>"),
        (0xe769, 0xe769, "Scan address and length, default length=64"),
        (0xe77d, 0xe77d, "display row of 16 mem locations as hex"),
        (0xe78a, 0xe78a, "Do a - after the eighth byte."),
        (0xe792, 0xe792, "And now for the ascii dump."),
        (0xe7a2, 0xe7a2, "Convert all nonprintables to ."),
        (0xe7bd, 0xe7bd, 'This is the code for the E command, enter hex bytes or ascii string. Syntax E or E<addr> or E<addr> <bytes> or E<addr>"string"'),
        (0xe7ca, 0xe7ca, "No bytes, then enter interactively."),
        (0xe7da, 0xe7da, "Display Eaddr + space"),
        (0xe7e1, 0xe7e1, "Get the line."),
        (0xe7f0, 0xe7f0, "Enter a line of hex bytes or ascci string at address X, Z if empty."),
        (0xe800, 0xe800, "Enter hex digits."),
        (0xe824, 0xe824, "This is the code for the I command, display the contents of an address Syntax: Iaddr"),
        (0xe82c, 0xe82c, "Read the byte from memory."),
        (0xe82e, 0xe82e, "Display itin hex."),
        (0xe836, 0xe836, "This is the code for the H command, display result of simple hex expressionSyntax Hhexnum{+|-hexnum}"),
        (0xe86a, 0xe86a, "This is the code for the G command, jump to the program Syntax G or G<addr>"),
        (0xe872, 0xe872, "Store parameter in pc location."),
        (0xe874, 0xe874, "Arm the breakpoints."),
        (0xe879, 0xe879, "This is the code for the J command, run a subroutine. Syntax J<addr>"),
        (0xe87e, 0xe87e, "Save old pc"),
        (0xe884, 0xe884, "Store parameter in PC location"),
        (0xe88c, 0xe88c, "Move the saved register set 2 addresses"),
        (0xe88e, 0xe88e, "down on the stack."),
        (0xe894, 0xe894, "Prepare subroutine return address."),
        (0xe896, 0xe896, "Jump to the routine."),
        (0xe898, 0xe898, "Get program counter value."),
        (0xe898, 0xe898, "This is the code for the P command, run instruction followed by breakpoint Syntax P"),
        (0xe89b, 0xe89b, "Find out location past current insn."),
        (0xe8a4, 0xe8a4, "This is the code for the T command, single step trace an instruction. Syntax T"),
        (0xe8a7, 0xe8a7, "Display the contents of 8 bit register, name in B, contents in A"),
        (0xe8b5, 0xe8b5, "Display the contents of 16 bit register, name in B, contents in Y"),
        (0xe8c5, 0xe8c5, "Display the contents of the registers and disassemble instruction at PC location."),
        (0xe8c7, 0xe8c7, "Note that there's one return address on"),
        (0xe8ca, 0xe8ca, "stack so saved register offsets are"),
        (0xe8cc, 0xe8cc, "inremented by 2."),
        (0xe8de, 0xe8de, "S of the running program is 12 higher,"),
        (0xe8e0, 0xe8e0, "because regs are not stacked when running."),
        (0xe906, 0xe906, "Disassemble instruction at PC"),
        (0xe90c, 0xe90c, "This is the code for the R command, display or alter the registers. Syntax R or R<letter><hex>"),
        (0xe915, 0xe915, "Display regs ifnothing follows."),
        (0xe91f, 0xe91f, "Make letter uppercase."),
        (0xe923, 0xe923, "At end of register tab, unknown reg"),
        (0xe929, 0xe929, "Found the register?"),
        (0xe930, 0xe930, "Convert the hex argument."),
        (0xe935, 0xe935, "Get register number."),
        (0xe93b, 0xe93b, "It's 8 bit."),
        (0xe93d, 0xe93d, "Remove temp stuff from stack."),
        (0xe93f, 0xe93f, "Store it in the reg on stack."),
        (0xe948, 0xe948, "It's 16 bit."),
        (0xe94d, 0xe94d, "Convert reg no to stack offset."),
        (0xe954, 0xe954, "It's the stack pointer."),
        (0xe95c, 0xe95c, "Set new stack pointer."),
        (0xe960, 0xe960, "Move register set to new stack location."),
        (0xe970, 0xe970, "Disarm the breakpoints, this is replace the SWI instructions with the original byte."),
        (0xe977, 0xe977, "Get address in u, byte in b"),
        (0xe987, 0xe987, "Clear the step breakpoint."),
        (0xe98a, 0xe98a, "3"),
        (0xe98a, 0xe98a, "Arm the breakponts, this is replace the byte at the breakpoint address with an SWI instruction."),
        (0xe98d, 0xe98d, "Arm them in reverse order of disarming."),
        (0xe98f, 0xe98f, "Get address in u."),
        (0xe997, 0xe997, "Compare to program counter location"),
        (0xe99e, 0xe99e, "Store SWI instruction if not equal."),
        (0xe9a6, 0xe9a6, "This is the code for the break command, set, clear display breakpoints. Syntax B or B<addr>. B displays, B<addr> sets or clears breakpoint."),
        (0xe9a8, 0xe9a8, "Store number of breakpoints to visit."),
        (0xe9b0, 0xe9b0, "No number then display breakpoints"),
        (0xe9bd, 0xe9bd, "Found the breakpoint, so clear it,"),
        (0xe9bf, 0xe9bf, "Is location zero"),
        (0xe9c4, 0xe9c4, "Set free address to y"),
        (0xe9cc, 0xe9cc, "Address not found in list of breakpoints"),
        (0xe9d0, 0xe9d0, "Was free address found."),
        (0xe9d2, 0xe9d2, "If so, store breakpoint there."),
        (0xea06, 0xea06, "Scan hex byte into a and add it to check sum in temp2+1"),
        (0xea14, 0xea14, "This tis the code for the S command, the Motorola S records entry. Syntax SO<addr> or SS<addr>,<len> or S1<bytes> or S9<bytes>"),
        (0xea31, 0xea31, "clear checksum."),
        (0xea35, 0xea35, "discount the address bytes from the count."),
        (0xea37, 0xea37, "Read length byte."),
        (0xea41, 0xea41, "Read address into d."),
        (0xea4d, 0xea4d, "Sorg is nonzero and soffs is zero, now"),
        (0xea4f, 0xea4f, "set soffs"),
        (0xea57, 0xea57, "Subtract the address offset."),
        (0xea66, 0xea66, "Check checksum."),
        (0xea6c, 0xea6c, "Was it no S9 record?"),
        (0xea76, 0xea76, "Store address into program counter."),
        (0xea7b, 0xea7b, "Reset sorg, next S loads will be normal."),
        (0xea86, 0xea86, "Error in srecord, display message."),
        (0xea91, 0xea91, "Set S record origin."),
        (0xea9f, 0xea9f, "Scan address and length parameter."),
        (0xea9f, 0xea9f, "Send a memory region as S-records."),
        (0xeab0, 0xeab0, "Compute offset for origin."),
        (0xeab6, 0xeab6, "All bytes sent?"),
        (0xeabe, 0xeabe, "If more than 16 left, then send 16."),
        (0xeac8, 0xeac8, "Discount line length from length."),
        (0xead3, 0xead3, "Clear check sum"),
        (0xead9, 0xead9, "Output byte b as hex and add to check sum."),
        (0xeae9, 0xeae9, "Output address (add into check sum)"),
        (0xeafa, 0xeafa, "Output checksum byte."),
        (0xeb0b, 0xeb0b, "Output byte in register B and add it into check sum at temp+1"),
        (0xeb19, 0xeb19, "This is the code for the M command, move memory region. Syntax: Maddr1,addr2,length"),
        (0xeb47, 0xeb47, "Read the argument separated by commas"),
        (0xeb49, 0xeb49, "src addr to x, dest addr to u, length to y"),
        (0xeb4b, 0xeb4b, "Don't tolerate syntax deviations."),
        (0xeb51, 0xeb51, "Perform the block move."),
        (0xeb56, 0xeb56, 'This is the code for the F command, find byte/ascii string in memory. Syntax: Faddr bytes or Faddr "ascii"'),
        (0xeb5c, 0xeb5c, "Scan the start address."),
        (0xeb65, 0xeb65, "Quote found, so scan for quoted string."),
        (0xeb6b, 0xeb6b, "End of line without final quote."),
        (0xeb6f, 0xeb6f, "End quote found"),
        (0xeb76, 0xeb76, "Convert string of hex bytes."),
        (0xeb79, 0xeb79, "String will be stored at start of line"),
        (0xeb7b, 0xeb7b, "buffer and may overwrite part of the"),
        (0xeb7c, 0xeb7c, "already converted string."),
        (0xeb8c, 0xeb8c, "Start searching, start addr in Y,"),
        (0xeb8d, 0xeb8d, "Quit with zero length string."),
        (0xeb8d, 0xeb8d, "string starts at linebuf, length A"),
        (0xeba0, 0xeba0, "Stop at I/O addresses."),
        (0xebb0, 0xebb0, "Not equal, try next address."),
        (0xebb7, 0xebb7, "String found"),
        (0xebc2, 0xebc2, "If 10 matches found, just stop."),
        (0xebca, 0xebca, "Send the contents of the xmodem buffer and get it acknowledged, zero flag is set if transfer aborted."),
        (0xebcc, 0xebcc, "Send SOH"),
        (0xebd1, 0xebd1, "Send block number."),
        (0xebd5, 0xebd5, "and its complement."),
        (0xebeb, 0xebeb, "Send the buffer contents."),
        (0xebef, 0xebef, "Send the check sum"),
        (0xebf7, 0xebf7, "^X for abort."),
        (0xebfb, 0xebfb, "Send again if NAK"),
        (0xec03, 0xec03, "Clear zero flag after ACK"),
        (0xec06, 0xec06, "Start an XMODEM send session."),
        (0xec08, 0xec08, "Initialize block number."),
        (0xec0f, 0xec0f, "If ^X exit with zero flag."),
        (0xec15, 0xec15, "Wait until NAK received."),
        (0xec17, 0xec17, "Send ETX and wait for ack."),
        (0xec2d, 0xec2d, "Read character into B with a timeout of A seconds,  Carry set if timeout."),
        (0xec41, 0xec41, "Wait until line becomes quiet."),
        (0xec49, 0xec49, "Receive an XMODEM block and wait till it is OK, Z set if etx."),
        (0xec51, 0xec51, "Send an ack."),
        (0xec5a, 0xec5a, "Send a NAK"),
        (0xec63, 0xec63, "Keep sending NAKs when timed out."),
        (0xec67, 0xec67, "End of file reached, acknowledge EOT."),
        (0xec6b, 0xec6b, "Not, SOH, bad block."),
        (0xec73, 0xec73, "Is it the right block?"),
        (0xec78, 0xec78, "Was it the previous block."),
        (0xec87, 0xec87, "Is the complement of the block number OK"),
        (0xec9f, 0xec9f, "Get the data bytes."),
        (0xeca9, 0xeca9, "Check the check sum."),
        (0xecad, 0xecad, "Block was the previous block, get next one"),
        (0xecbb, 0xecbb, "EOT was received."),
        (0xecc3, 0xecc3, "Send 3 acks in a row."),
        (0xece6, 0xece6, "O.S. routine to open input through XMODEM transfer."),
        (0xecee, 0xecee, "Display message to start XMODEM send."),
        (0xecf5, 0xecf5, "Disable character output."),
        (0xecfa, 0xecfa, ""),
        (0xed05, 0xed05, "set xmode to 2."),
        (0xed09, 0xed09, "O.S. routine to open output through XMODEM transfer."),
        (0xed10, 0xed10, "Display message to start XMODEM receive"),
        (0xed2e, 0xed2e, "O.S. routine to abort input through XMODEM transfer."),
        (0xed3f, 0xed3f, "Send 8 CAN characters to kill transfer."),
        (0xed4b, 0xed4b, "Send diagnostic message."),
        (0xed4e, 0xed4e, "O.S. routine to close output through XMODEM transfer."),
        (0xed62, 0xed62, "Transfer filler chars to force block out."),
        (0xed64, 0xed64, "Send EOT"),
        (0xed71, 0xed71, "O.S. routine to close input through XMODEM, by gobbling up the remaining bytes."),
        (0xed7b, 0xed7b, "putchar routine for XMODEM"),
        (0xed84, 0xed84, "Store character in XMODEM buffer."),
        (0xed88, 0xed88, "is buffer full?"),
        (0xed99, 0xed99, "putcr routine for XMODEM"),
        (0xedb4, 0xedb4, "getchar routine for XMODEM"),
        (0xedb6, 0xedb6, "No characters left?"),
        (0xedbc, 0xedbc, "Receive new block."),
        (0xedc1, 0xedc1, "End of input?"),
        (0xedcd, 0xedcd, "Get character from buffer"),
        (0xeddd, 0xeddd, "Restore I/O vectors"),
        (0xedf4, 0xedf4, "This is the code for the X command, various XMODEM related commands. Syntax: XSaddr,len XLaddr,len XX XOcrlf,filler, XSSaddr,len"),
        (0xedf9, 0xedf9, "Convert to uppercase."),
        (0xee15, 0xee15, "XSaddr,len command."),
        (0xee18, 0xee18, "Send binary through XMODEM"),
        (0xee2a, 0xee2a, "Send all the bytes through XMODEM."),
        (0xee2f, 0xee2f, "XSSaddr,len command."),
        (0xee31, 0xee31, "Send Srecords through XMODEM"),
        (0xee36, 0xee36, "XLaddr command"),
        (0xee39, 0xee39, "Load binary through XMODEM"),
        (0xee3f, 0xee3f, "File ended? then done"),
        (0xee49, 0xee49, "XX command"),
        (0xee4b, 0xee4b, "Execute commands received from XMODEM"),
        (0xee63, 0xee63, "mnemonics table, ordered alphabetically. 5 bytes name, 1 byte category, 2 bytes opcode, 8 bytes total."),
        (0xf2fb, 0xf2fb, "-mnemtab)/8"),
        (0xf2fb, 0xf2fb, "Register table for PUSH/PULL and TFR/EXG instructions. 3 bytes for name, 1 for tfr/exg, 1 for push/pull, 5 total"),
        (0xf33e, 0xf33e, "opcode offsets to basic opcode, depends on first nibble."),
        (0xf34e, 0xf34e, "mode depending on first nibble of opcode."),
        (0xf35e, 0xf35e, "mode depending on category code stored in mnemtab"),
        (0xf36b, 0xf36b, "Decode instruction pointed to by Y for disassembly (and to find out how long it is). On return, U points to appropriate mnemonic table entry, Y points past instruction. It's rather clumsy code, but we do want to reuse the same table as used with assembling."),
        (0xf36b, 0xf36b, "modes in this context: 0 no operands, 1 8-bit immediate, 2 16 bit imm, 3, 8-bit address, 4 16 bit address, 5 indexed with postbyte, 6 short relative, 7 long relative, 8 pushpul, 9 tftetx"),
        (0xf37b, 0xf37b, "Store 0x10 or 0x11 prebyte."),
        (0xf37e, 0xf37e, "Get new opcode."),
        (0xf386, 0xf386, "Get high nibble."),
        (0xf394, 0xf394, "Add opcode offset to opcode."),
        (0xf397, 0xf397, "Store the 'basis' opcode."),
        (0xf3a2, 0xf3a2, "Compare category code with 13"),
        (0xf3a4, 0xf3a4, "13=pseudo op, no valid opcode"),
        (0xf3ac, 0xf3ac, "Opcode&prebyte agree, operation found."),
        (0xf3ae, 0xf3ae, "point to next mnemonic"),
        (0xf3b4, 0xf3b4, "mnemonic not found, use FCB byte."),
        (0xf3b9, 0xf3b9, "Store mode 3, 8 bit address."),
        (0xf3c4, 0xf3c4, "if it was the combination prebyte"),
        (0xf3c7, 0xf3c7, "and opcode that was not found,"),
        (0xf3ca, 0xf3ca, "FCB just the prebyte"),
        (0xf3cc, 0xf3cc, "The byte must be stored as operand."),
        (0xf3d6, 0xf3d6, "Is it really the BSR opcode?"),
        (0xf3dd, 0xf3dd, "We mistakenly found BSR instead of JSR"),
        (0xf3e7, 0xf3e7, "nibble-dependent mode was 0 or 1,"),
        (0xf3e9, 0xf3e9, "use category dependent mode instead."),
        (0xf3f8, 0xf3f8, "jump dependent on definitive mode."),
        (0xf441, 0xf441, "postbytes <0x80 have no extra operands."),
        (0xf44e, 0xf44e, "Display disassembled instruction after the invocation of disdecode. U points to mnemonic table entry."),
        (0xf452, 0xf452, "Display the mnemonic."),
        (0xf45f, 0xf45f, "Perform action dependent on mode."),
        (0xf4b2, 0xf4b2, "Walk through the register table."),
        (0xf4bc, 0xf4bc, "Is bit corresponding to reg set in postbyte"),
        (0xf4ca, 0xf4ca, "no u register in pshu pulu."),
        (0xf4da, 0xf4da, "no s register in pshs puls."),
        (0xf4df, 0xf4df, "remove the bits from postbyte."),
        (0xf4eb, 0xf4eb, "print comma after first register."),
        (0xf557, 0xf557, "Display ,Xreg and terminating ]"),
        (0xf55c, 0xf55c, "Display ] if indirect."),
        (0xf578, 0xf578, "Jump to routine for indexed mode"),
        (0xf634, 0xf634, "Display byte A in decimal (0<=A<20)"),
        (0xf644, 0xf644, "This is the code for the U command, unassemble instructions in memory. Syntax: U or Uaddr or Uaddr,length"),
        (0xf64a, 0xf64a, "Scan address,length parameters."),
        (0xf65c, 0xf65c, "Display instruction address"),
        (0xf679, 0xf679, "Display instruction bytes as hex."),
        (0xf683, 0xf683, "Fill out with spaces to width 11."),
        (0xf689, 0xf689, "Display disassembled instruction."),
        (0xf69b, 0xf69b, "Simple 'expression evaluator' for assembler."),
        (0xf6ac, 0xf6ac, "Was the minus sign there."),
        (0xf6b3, 0xf6b3, "Clear Z flag for valid result."),
        (0xf6bd, 0xf6bd, "Hex number if starting with dollar."),
        (0xf6c3, 0xf6c3, "char if starting with ' else decimal"),
        (0xf6cd, 0xf6cd, "Increment past final quote if it's there."),
        (0xf6d0, 0xf6d0, "Clear zero flag."),
        (0xf6f3, 0xf6f3, "Multiply number by 10."),
        (0xf6f7, 0xf6f7, "Add digit to 10."),
        (0xf6fb, 0xf6fb, "Get next character."),
        (0xf709, 0xf709, "Assemble the instruction pointed to by X. Fisrt stage: copy mnemonic to mnemonic buffer."),
        (0xf714, 0xf714, "Mnemonic ends at first space or null"),
        (0xf71e, 0xf71e, "Capitalize letters, but only letters."),
        (0xf722, 0xf722, "Copy to mnemonic buffer."),
        (0xf72f, 0xf72f, "Fill the rest of mnem buffer with spaces."),
        (0xf731, 0xf731, "Second stage: look mnemonic up using binary search."),
        (0xf733, 0xf733, "Low index=0"),
        (0xf737, 0xf737, "High index=mnemsize."),
        (0xf73d, 0xf73d, "lower limit -1?"),
        (0xf741, 0xf741, "hi index lower than low index?"),
        (0xf744, 0xf744, "Add indexes."),
        (0xf749, 0xf749, "Divide by 2 to get average"),
        (0xf751, 0xf751, "Multiply by 8 to get offset."),
        (0xf755, 0xf755, "Add offset to table base"),
        (0xf762, 0xf762, "Characters don't match?"),
        (0xf767, 0xf767, "We found the mnemonic."),
        (0xf76f, 0xf76f, "mnembuf<table, adjust high limit."),
        (0xf774, 0xf774, "mnembuf>table, adjust low limit."),
        (0xf77e, 0xf77e, "Stage 3: Perform routine depending on category code."),
        (0xf7b4, 0xf7b4, "Cat 0, one byte opcode w/o operands RTS"),
        (0xf7b8, 0xf7b8, "Cat 1, two byte opcode w/o operands SWI2"),
        (0xf7bc, 0xf7bc, "Cat 2, opcode w/ immdiate operand ANDCC"),
        (0xf7d1, 0xf7d1, "Cat 3, LEA"),
        (0xf7dd, 0xf7dd, "No immediate w/ lea"),
        (0xf7f1, 0xf7f1, "Use 8F nn nn for direct mode."),
        (0xf7f7, 0xf7f7, "Cat 4, short branch instructions"),
        (0xf80a, 0xf80a, "Cat 5, long brach w/ two byte opcode"),
        (0xf81d, 0xf81d, "Cat 6, long branch w/ one byte opcode."),
        (0xf824, 0xf824, "Cat 7, 8-bit two operand instructions ADDA"),
        (0xf835, 0xf835, "Cat 8, 16-bit 2operand insns 1byte opc LDX"),
        (0xf846, 0xf846, "Cat 9, 16-bit 2operand insns 2byte opc LDY"),
        (0xf859, 0xf859, "Cat 10, one-operand insns NEG..CLR"),
        (0xf863, 0xf863, "No immediate mode"),
        (0xf869, 0xf869, "indexed etc"),
        (0xf871, 0xf871, "Add 0x70 for extended direct."),
        (0xf873, 0xf873, "And 0x60 for indexed etc."),
        (0xf875, 0xf875, "And nothing for direct8."),
        (0xf87b, 0xf87b, "Cat 11, TFR and EXG"),
        (0xf8a4, 0xf8a4, "Cat 12, PSH and PUL"),
        (0xf8ca, 0xf8ca, "Cat 13, pseudo oeprations"),
        (0xf8cb, 0xf8cb, "Adjust opcdoe depending on mode (in 0x80-0xFF range)"),
        (0xf8d2, 0xf8d2, "Is it direct?"),
        (0xf8d6, 0xf8d6, "Indexed etc?"),
        (0xf8d8, 0xf8d8, "Not, then immediate, no adjust."),
        (0xf8d9, 0xf8d9, "Add 0x20 to opcode for indexed etc modes."),
        (0xf8dc, 0xf8dc, "Add 0x10 to opcode for direct8"),
        (0xf8e2, 0xf8e2, "If opsize=2, add another 0x20 for extended16"),
        (0xf8e5, 0xf8e5, "Start scanning of operands."),
        (0xf8ed, 0xf8ed, "This subroutine scans the assembler operands."),
        (0xf8ed, 0xf8ed, "amode settings in assembler: 1=immediate, 2=direct/extended, 3=indexed etc. 4=pc relative, 5=indirect, 6=pcrelative and indirect."),
        (0xf8f3, 0xf8f3, "operand starts with [, then indirect."),
        (0xf906, 0xf906, "Convert to uppercase."),
        (0xf91a, 0xf91a, "Could it be A,X B,X or D,X"),
        (0xf930, 0xf930, "Point to the start of the operand"),
        (0xf93f, 0xf93f, "Go for extended if operand unknown."),
        (0xf944, 0xf944, "Can we use 8-bit operand?"),
        (0xf94c, 0xf94c, "Set opsize depending on magnitude of op."),
        (0xf954, 0xf954, "Or was it indirect."),
        (0xf956, 0xf956, "Then we have postbyte and opsize=2"),
        (0xf964, 0xf964, "Assume direct or absolute addressing"),
        (0xf96b, 0xf96b, "If followed by, then indexed."),
        (0xf974, 0xf974, "Was it an indirect mode?"),
        (0xf979, 0xf979, "Set indirect bit."),
        (0xf980, 0xf980, "Check for the other ]"),
        (0xf987, 0xf987, "Immediate addressing."),
        (0xf996, 0xf996, "Inirect mode w/ imm is illegal."),
        (0xf9ad, 0xf9ad, "Count the - signs for autodecrement."),
        (0xf9c9, 0xf9c9, "Count the + signs for autoincrement."),
        (0xf9fd, 0xf9fd, "Convert to uppercase."),
        (0xfa01, 0xfa01, "Check for PC relative."),
        (0xfa12, 0xfa12, "Go for long index if operand unknown."),
        (0xfa25, 0xfa25, "Indirect may not be 5-bit index"),
        (0xfa27, 0xfa27, "It's a five-bit index."),
        (0xfa5e, 0xfa5e, "Convert to uppercase"),
        (0xfa68, 0xfa68, "Scan past the ,PCR"),
        (0xfa6e, 0xfa6e, "Set postbyte"),
        (0xfa74, 0xfa74, "Set addr mode to PCR"),
        (0xfa7a, 0xfa7a, "Scan for one of the 4 index registers and adjust postbyte."),
        (0xfa7c, 0xfa7c, "Convert to uppercase."),
        (0xfa8c, 0xfa8c, "Index register not found where expected."),
        (0xfa92, 0xfa92, "Set index reg bits in postbyte."),
        (0xfa98, 0xfa98, "This routine sets amode to 3, if it was less."),
        (0xfaa5, 0xfaa5, "This subroutine lays down the address."),
        (0xfab7, 0xfab7, "pc rel modes."),
        (0xfb0e, 0xfb0e, "This routine checks and lays down short relative address."),
        (0xfb32, 0xfb32, "This routine lays down long relative address."),
        (0xfb6e, 0xfb6e, "Find register for TFR and PSH instruction"),
        (0xfba4, 0xfba4, "This is the code for the A command, assemble instructions. Syntax: Aaddr"),
        (0xfbb5, 0xfbb5, "Print address and space."),
        (0xfbbc, 0xfbbc, "Get new line"),
        (0xfbbf, 0xfbbf, "Exit on empty line."),
        (0xfbc4, 0xfbc4, "Make line zero terminated."),
        (0xfbce, 0xfbce, "Jump table for monitor routines that are usable by other programs."),
        (0xffd2, 0xffd2, "Interrupt vector addresses at top of ROM. Most are vectored through jumps in RAM."),

        (0xfff2, 0xfff2, 'SWI3'),
        (0xfff4, 0xfff4, 'SWI2'),
        (0xfff6, 0xfff6, 'FIRQ'),
        (0xfff8, 0xfff8, 'IRQ'),
        (0xfffa, 0xfffa, 'SWI'),
        (0xfffc, 0xfffc, 'NMI'),
        (0xfffe, 0xfffe, 'RESET'),

        # manually inserted:

        # Memory map of SBC
        (0x0, 0x40, "Zero page variables reserved by monitor and O.S."),
        (0x40, 0xFF , "Zero page portion for user programs."),
        (0x100, 0x17F , "Xmodem buffer 0, terminal input buffer"),
        (0x180, 0x1FF , "Xmodem buffer 1, terminal output buffer"),
        (0x200, 0x27F , "Terminal input line"),
        (0x280, 0x2FF , "Variables reserved by monitor and O.S."),
        (0x300, 0x400 , "System stack"),
        (0x400, 0x7FFF , "RAM for user programs and data"),
        (0x8000, 0xDFFF , "PROM for user programs"),
        (0xE000, 0xE1FF , "I/O addresses"),
        (0xE200, 0xE3FF , "Reserved"),
        (0xE400, 0xFFFF , "Monitor ROM"),

        (0xe000, 0xe000, "Control/status port of ACIA"),
        (0xe001, 0xe001, "Data port of ACIA"),
        
        
    )


def print_out(txt):
    print txt


def get_sbc09_meminfo():
    return SBC09MemInfo(log.debug)



if __name__ == "__main__":
    mem_info = SBC09MemInfo(print_out)

    mem_info(0xe000) # SERIAL INTERFACE
