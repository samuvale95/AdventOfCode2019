from dataclasses import dataclass

@dataclass
class Program_executor:
    program:list
    operations:dict(int, callable)=None

    def add_operator(self, opcode:int, f:callable) -> None:
        self.operations[opcode] = f

    def run(self) -> list:
        for i in range(0, len(self.program), 4):
            if(int(self.program[i])==99): break

            a = int(self.program[i+1])
            b = int(self.program[i+2])
            res = int(self.program[i+3])
            self.program[res]=self.operations[int(self.program[i])](int(self.program[a]), int(self.program[b]))